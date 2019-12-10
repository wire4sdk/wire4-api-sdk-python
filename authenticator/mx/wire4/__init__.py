#    COPYRIGHT © 2017. TCPIP.
#    PATENT PENDING. ALL RIGHTS RESERVED.
#    SPEI GATEWAY IS REGISTERED TRADEMARKS OF TCPIP.
#
#    This software is confidential and proprietary information of TCPIP.
#    You shall not disclose such Confidential Information and shall use it only
#    in accordance with the company policy.

# coding: utf-8

"""
     <i>Fecha de creación: 9 de diciembre, 2019</i>

     author: Saintiago García
     version: 1.0
"""
# import oauth2 components
from authenticator.mx.wire4.auth.oauth_wire4 import OAuthWire4

# import core components
from authenticator.mx.wire4.core.environment_enum import  EnvironmentEnum
from authenticator.mx.wire4.core.cached_token import CachedToken

# import webHook verification signature components
from authenticator.mx.wire4.webhook_verification_signature.utils_compute import UtilsCompute