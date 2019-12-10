#    COPYRIGHT © 2017. TCPIP.
#    PATENT PENDING. ALL RIGHTS RESERVED.
#    SPEI GATEWAY IS REGISTERED TRADEMARKS OF TCPIP.
#
#    This software is confidential and proprietary information of TCPIP.
#    You shall not disclose such Confidential Information and shall use it only
#    in accordance with the company policy.

# coding: utf-8

"""
     <i>Fecha de creación: 5 de diciembre, 2019</i>

     author: Saintiago García
     version: 1.0
"""

import os
from collections import OrderedDict
from datetime import datetime, timedelta

from oauthlib.oauth2 import BackendApplicationClient, LegacyApplicationClient
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth
from wire4_client import ApiClient
from wire4_client.configuration import Configuration
from wire4_client.rest import ApiException

from authenticator.wire4_auth.core import CachedToken
from authenticator.wire4_auth.core import EnvironmentEnum


class OAuthWire4:

    MAX_APP_USER_SIZE_CACHED: int = 100

    environment: EnvironmentEnum = EnvironmentEnum.SANDBOX

    def __init__(self, client_id: str, client_secret: str, environment: EnvironmentEnum):
        os.environ["OAUTHLIB_RELAX_TOKEN_SCOPE"] = "True"
        self._client_id = client_id
        self._client_secret = client_secret
        OAuthWire4.environment = environment

        # noinspection PyTypeChecker
        self._token_cached_app = CachedToken(None, None, None)
        self._tokens_cached_app_user = OrderedDict()

    @property
    def client_id(self) -> str:
        return self._client_id

    @property
    def client_secret(self) -> str:
        return self.client_secret

    @property
    def token_cached_app(self) -> CachedToken:
        return self._token_cached_app

    @property
    def tokens_cached_app_user(self) -> dict:
        return self._tokens_cached_app_user

    def is_expired(self, expires_at: float) -> bool:

        return expires_at is not None and datetime.fromtimestamp(expires_at) > (datetime.now() - timedelta(minutes=5))

    def obtain_access_token_app(self, scope="general") -> str:

        if self.token_cached_app.token is not None and scope in self.token_cached_app.token.get("scope") and \
            self.is_expired(self.token_cached_app.token.get("expires_at")) and \
                self.token_cached_app.token.get("access_token") is not None:

            return self.token_cached_app.token.get("access_token")

        try:
            auth = HTTPBasicAuth(self._client_id, self._client_secret)
            scopes = [scope]
            client = BackendApplicationClient(client_id=self._client_id, scope=scopes)

            oauth = OAuth2Session(client=client)
            token = oauth.fetch_token(token_url=OAuthWire4.environment.token_url, auth=auth)
            self.token_cached_app.token = token

            return token.get("access_token")
        except Exception as ex:
            raise ApiException(reason="error to obtain token app: {0}".format(ex))

    def obtain_access_token_app_user(self, user_key: str, secret_key: str, scope="spei_admin") -> str:

        key_search = user_key + scope
        token_cached = self.tokens_cached_app_user.get(key_search)
        if token_cached is not None and scope in token_cached.token.get("scope") and \
            self.is_expired(token_cached.token.get("expires_at")) and\
                token_cached.token.get("access_token") is not None:

            return token_cached.token.get("access_token")

        try:
            auth = HTTPBasicAuth(self._client_id, self._client_secret)
            scopes = [scope]
            client = LegacyApplicationClient(client_id=self._client_id)

            oauth = OAuth2Session(client=client)
            token = oauth.fetch_token(token_url=OAuthWire4.environment.token_url, username=user_key,
                                      password=secret_key, auth=auth, scope=scopes)

            if len(self.tokens_cached_app_user) + 1 > self.MAX_APP_USER_SIZE_CACHED:
                for key in self.tokens_cached_app_user:
                    self.tokens_cached_app_user.pop(key)
                    break

            self.tokens_cached_app_user[key_search] = CachedToken(user_key, secret_key, token)

            return token.get("access_token")
        except Exception as ex:
            raise ApiException(reason="error to obtain token app user: {0}".format(ex))

    @staticmethod
    def get_default_api_client(token: str) -> ApiClient:
        # Configure OAuth2 access token for authorization
        configuration = Configuration()
        configuration.access_token = token
        configuration.host = OAuthWire4.environment.service_url

        return ApiClient(configuration)
