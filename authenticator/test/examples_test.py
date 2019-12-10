#    COPYRIGHT © 2017. TCPIP.
#    PATENT PENDING. ALL RIGHTS RESERVED.
#    SPEI GATEWAY IS REGISTERED TRADEMARKS OF TCPIP.
#
#    This software is confidential and proprietary information of TCPIP.
#    You shall not disclose such Confidential Information and shall use it only
#    in accordance with the company policy.

# coding: utf-8

"""
     <i>Fecha de creación: 6 de diciembre, 2019</i>

     author: Saintiago García
     version: 1.0
"""
import sys
import unittest
import warnings

from wire4_client import ContactoApi, ContactRequest, CepSearchBanxico, ComprobanteElectrnicoDePagoCEPApi, \
    CepResponse, SuscripcionesApi, PreEnrollmentData, PreEnrollmentResponse, CuentasDeBeneficiariosSPEIApi, \
    RelationshipsResponse, AccountRequest, Account, Person, TokenRequiredResponse, BeneficiariesResponse, AmountRequest, \
    InstitucionesApi, InstitutionsList, SaldoApi, BalanceListResponse, CuentasDeBeneficiariosSPIDApi, \
    SpidClassificationsResponseDTO, TransferenciasSPIDApi, AccountSpid, BeneficiaryInstitution, DepositantesApi, \
    DepositantsRegister, DepositantsResponse, TransferenciasSPEIApi, WebhooksApi, WebhooksList, WebhookResponse, \
    Billing, FacturasApi, WebhookRequest, TransactionOutgoingSpid, TransactionsOutgoingRegister, TransactionOutgoing
from wire4_client.rest import ApiException

from wire4_auth.auth.oauth_wire4 import OAuthWire4
from wire4_auth.core.environment_enum import EnvironmentEnum


class TestAccount(unittest.TestCase):
    # OAuthWire4("kIinyEIYWUIF3pflFxhRdKft2_ga", "gca6FwUE_9Dk23UhWoM81pZkNgEa", EnvironmentEnum.DEVELOPMENT)

    CLIENT_ID: str = "FxUWmqYGZuv8O1qjxstvIyJothMa"

    CLIENT_SECRET: str = "kjwbkrPVgXsnaUGzthj55dsFhx4a"

    SUBSCRIPTION: str = "f1504fea-3a8f-475a-a50a-90d3c40efc59"

    USER_KEY: str = "071e2b59b354186b3a0158de493536@sandbox.wire4.mx"

    SECRET_KEY: str = "0d1e33e94604f01b4e00d2fcb6b48f"

    AMBIENT: EnvironmentEnum = EnvironmentEnum.SANDBOX

    def setUp(self):
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
        pass

    def testSendContact(self):
        # Create the authenticator to obtain access token
        # The token URL and Service URL are defined for this environment enum value.
        oauth_wire = OAuthWire4(self.CLIENT_ID, self.CLIENT_SECRET, self.AMBIENT)

        try:
            # Obtain an access token use application flow and scope "general"
            oauth_token_app: str = oauth_wire.obtain_access_token_app("general")
        except ApiException as ex:
            print("Exception to obtain access token %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        # create an instance of the API class and add the bearer token to request
        api_instance = ContactoApi(OAuthWire4.get_default_api_client(oauth_token_app))

        # build body with info (check references for more info: types, required fields, etc.)
        body = ContactRequest(address="Calle Falsa 123, Col Fantasía", company="Compu Mundo Hiper Mega Red",
                              contact_person="Homer J Simpson", email="homer.simpson@compumundohipermegared.com",
                              phone_number="4422102030")

        try:
            response = api_instance.send_contact_using_post_with_http_info(body)
            print(response)
        except ApiException as ex:
            print("Exception when calling the API %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        pass

    def testObtainCep(self):
        # Create the authenticator to obtain access token
        # The token URL and Service URL are defined for this environment enum value.
        oauth_wire = OAuthWire4(self.CLIENT_ID, self.CLIENT_SECRET, self.AMBIENT)

        try:
            # Obtain an access token use application flow and scope "general"
            oauth_token_app: str = oauth_wire.obtain_access_token_app("general")
        except ApiException as ex:
            print("Exception to obtain access token %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        # create an instance of the API class and add the bearer token to request
        api_instance = ComprobanteElectrnicoDePagoCEPApi(OAuthWire4.get_default_api_client(oauth_token_app))

        # build body with info (check references for more info: types, required fields, etc.)
        body = CepSearchBanxico(amount="8963.25", beneficiary_account="072680004657656853",
                                beneficiary_bank_key="40072", clave_rastreo="58735618", operation_date="05-12-2018",
                                reference="1122334", sender_account="112680000156896531", sender_bank_key="40112")

        try:
            response: CepResponse = api_instance.obtain_transaction_cep_using_post(body)
            print(response)
        except ApiException as ex:
            print("Exception when calling the API %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        pass

    def testMakePreSubscription(self):
        # Create the authenticator to obtain access token
        # The token URL and Service URL are defined for this environment enum value.
        oauth_wire = OAuthWire4(self.CLIENT_ID, self.CLIENT_SECRET, self.AMBIENT)

        try:
            # Obtain an access token use application flow and scope "general"
            oauth_token_app: str = oauth_wire.obtain_access_token_app("general")
        except ApiException as ex:
            print("Exception to obtain access token %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        # create an instance of the API class and add the bearer token to request
        api_instance = SuscripcionesApi(OAuthWire4.get_default_api_client(oauth_token_app))

        # build body with info (check references for more info: types, required fields, etc.)
        body = PreEnrollmentData(cancel_return_url="https://your-app-url.mx/return",
                                 return_url="https://your-app-url.mx/cancel")

        try:
            response: PreEnrollmentResponse = api_instance.pre_enrollment_monex_user_using_post(body)
            print(response)
        except ApiException as ex:
            print("Exception when calling the API %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        pass

    def testDeletePreSubscription(self):
        # Create the authenticator to obtain access token
        # The token URL and Service URL are defined for this environment enum value.
        oauth_wire = OAuthWire4(self.CLIENT_ID, self.CLIENT_SECRET, self.AMBIENT)

        try:
            # Obtain an access token use application flow and scope "general"
            oauth_token_app: str = oauth_wire.obtain_access_token_app("general")
        except ApiException as ex:
            print("Exception to obtain access token %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        # create an instance of the API class and add the bearer token to request
        api_instance = SuscripcionesApi(OAuthWire4.get_default_api_client(oauth_token_app))

        # build body with info (check references for more info, types, required fields)
        subscription: str = "ddae20c5-58c7-46b5-b988-73d55ca1c528"

        try:
            response = api_instance.remove_subscription_pending_status_using_delete_with_http_info(subscription)
            print(response)
        except ApiException as ex:
            print("Exception when calling the API %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        pass

    def testDeleteSubscription(self):

        subscription_to_remove_user_key = "86b348442874908861098f03ed9ffa@sandbox.wire4.mx"
        subscription_to_remove_user_secret = "9ee9ae9a86446c289656ff40934370"

        # Create the authenticator to obtain access token
        # The token URL and Service URL are defined for this environment enum value.
        oauth_wire = OAuthWire4(self.CLIENT_ID, self.CLIENT_SECRET, self.AMBIENT)

        try:
            # Obtain an access token use password flow and scope "spei_admin"
            # The user_key and user_secret belongs to the subscription to delete
            oauth_token_user = oauth_wire.obtain_access_token_app_user(subscription_to_remove_user_key,
                                                                       subscription_to_remove_user_secret, "spei_admin")
        except ApiException as ex:
            print("Exception to obtain access token %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        # create an instance of the API class and add the bearer token to request
        api_instance = SuscripcionesApi(OAuthWire4.get_default_api_client(oauth_token_user))

        # build body with info (check references for more info, types, required fields)
        subscription: str = "81b282bb-9056-4412-82de-ab066eae08a4"

        try:
            response = api_instance.remove_enrollment_user_using_delete_with_http_info(subscription)
            print(response)
        except ApiException as ex:
            print("Exception when calling the API %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        pass

    def testObtainRelationships(self):
        # Create the authenticator to obtain access token
        # The token URL and Service URL are defined for this environment enum value.
        oauth_wire = OAuthWire4(self.CLIENT_ID, self.CLIENT_SECRET, self.AMBIENT)

        try:
            # Obtain an access token use password flow and scope "spei_admin"
            oauth_token_user = oauth_wire.obtain_access_token_app_user(self.USER_KEY, self.SECRET_KEY, "spei_admin")
        except ApiException as ex:
            print("Exception to obtain access token %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        # create an instance of the API class and add the bearer token to request
        api_instance = CuentasDeBeneficiariosSPEIApi(OAuthWire4.get_default_api_client(oauth_token_user))

        # build body with info (check references for more info, types, required fields)
        subscription: str = self.SUBSCRIPTION

        try:
            response: RelationshipsResponse = api_instance.get_available_relationships_monex_using_get(subscription)
            print(response)
        except ApiException as ex:
            print("Exception when calling the API %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        pass

    def testPreRegisterBeneficiaries(self):
        # Create the authenticator to obtain access token
        # The token URL and Service URL are defined for this environment enum value.
        oauth_wire = OAuthWire4(self.CLIENT_ID, self.CLIENT_SECRET, self.AMBIENT)

        try:
            # Obtain an access token use password flow and scope "spei_admin"
            oauth_token_user = oauth_wire.obtain_access_token_app_user(self.USER_KEY, self.SECRET_KEY, "spei_admin")
        except ApiException as ex:
            print("Exception to obtain access token %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        # create an instance of the API class and add the bearer token to request
        api_instance = CuentasDeBeneficiariosSPEIApi(OAuthWire4.get_default_api_client(oauth_token_user))

        # build body with info (check references for more info, types, required fields)
        subscription: str = self.SUBSCRIPTION
        body: AccountRequest = AccountRequest(return_url="https://your-app-url.mx/return",
                                              cancel_return_url="https://your-app-url.mx/cancel",
                                              accounts=[Account(amount_limit=10000.00,
                                                                beneficiary_account="112680000156896531",
                                                                email=["beneficiary@wire4.mx"],
                                                                kind_of_relationship="RECURRENTE",
                                                                numeric_reference_spei="1234567",
                                                                payment_concept_spei="concept spei",
                                                                person=Person(last_name="Simpson",
                                                                              middle_name="Jay",
                                                                              name="Bartolomeo"),
                                                                relationship="ACREEDOR",
                                                                rfc="SJBA920125AB1")])

        try:
            response: TokenRequiredResponse = api_instance.pre_register_accounts_using_post(body, subscription)
            print(response)
        except ApiException as ex:
            print("Exception when calling the API %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        pass

    def testRemoveBeneficiariesPending(self):
        # Create the authenticator to obtain access token
        # The token URL and Service URL are defined for this environment enum value.
        oauth_wire = OAuthWire4(self.CLIENT_ID, self.CLIENT_SECRET, self.AMBIENT)

        try:
            # Obtain an access token use password flow and scope "spei_admin"
            oauth_token_user = oauth_wire.obtain_access_token_app_user(self.USER_KEY, self.SECRET_KEY, "spei_admin")
        except ApiException as ex:
            print("Exception to obtain access token %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        # create an instance of the API class and add the bearer token to request
        api_instance = CuentasDeBeneficiariosSPEIApi(OAuthWire4.get_default_api_client(oauth_token_user))

        # build body with info (check references for more info, types, required fields)
        subscription: str = self.SUBSCRIPTION
        request_id: str = "b3551c06-06ba-4476-9939-779db1649268"

        try:
            response = api_instance.remove_beneficiaries_pending_using_delete_with_http_info(request_id, subscription)
            print(response)
        except ApiException as ex:
            print("Exception when calling the API %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        pass

    def testObtainBeneficiaries(self):
        # Create the authenticator to obtain access token
        # The token URL and Service URL are defined for this environment enum value.
        oauth_wire = OAuthWire4(self.CLIENT_ID, self.CLIENT_SECRET, self.AMBIENT)

        try:
            # Obtain an access token use password flow and scope "spei_admin"
            oauth_token_user = oauth_wire.obtain_access_token_app_user(self.USER_KEY, self.SECRET_KEY, "spei_admin")
        except ApiException as ex:
            print("Exception to obtain access token %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        # create an instance of the API class and add the bearer token to request
        api_instance = CuentasDeBeneficiariosSPEIApi(OAuthWire4.get_default_api_client(oauth_token_user))

        # build body with info (check references for more info, types, required fields)
        subscription: str = self.SUBSCRIPTION

        try:
            # for filter by RFC: api_instance.get_beneficiaries_for_account_using_get(subscription, rfc="RFCE010980AR3")
            response: BeneficiariesResponse = api_instance.get_beneficiaries_for_account_using_get(subscription)
            print(response)
        except ApiException as ex:
            print("Exception when calling the API %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        pass

    def testChangeAmountLimitBeneficiary(self):
        # Create the authenticator to obtain access token
        # The token URL and Service URL are defined for this environment enum value.
        oauth_wire = OAuthWire4(self.CLIENT_ID, self.CLIENT_SECRET, self.AMBIENT)

        try:
            # Obtain an access token use password flow and scope "spei_admin"
            oauth_token_user = oauth_wire.obtain_access_token_app_user(self.USER_KEY, self.SECRET_KEY, "spei_admin")
        except ApiException as ex:
            print("Exception to obtain access token %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        # create an instance of the API class and add the bearer token to request
        api_instance = CuentasDeBeneficiariosSPEIApi(OAuthWire4.get_default_api_client(oauth_token_user))

        # build body with info (check references for more info, types, required fields)
        subscription: str = self.SUBSCRIPTION
        account: str = "112680000156896531"
        body: AmountRequest = AmountRequest(amount_limit=10000.00, currency_code="MXP",
                                            previous_amount_limit=20000.00)

        try:
            response = api_instance.update_amount_limit_account_using_put_with_http_info(body, account, subscription)
            print(response)
        except ApiException as ex:
            print("Exception when calling the API %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        pass

    def testDeleteBeneficiary(self):
        # Create the authenticator to obtain access token
        # The token URL and Service URL are defined for this environment enum value.
        oauth_wire = OAuthWire4(self.CLIENT_ID, self.CLIENT_SECRET, self.AMBIENT)

        try:
            # Obtain an access token use password flow and scope "spei_admin"
            oauth_token_user = oauth_wire.obtain_access_token_app_user(self.USER_KEY, self.SECRET_KEY, "spei_admin")
        except ApiException as ex:
            print("Exception to obtain access token %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        # create an instance of the API class and add the bearer token to request
        api_instance = CuentasDeBeneficiariosSPEIApi(OAuthWire4.get_default_api_client(oauth_token_user))

        # build body with info (check references for more info, types, required fields)
        subscription: str = self.SUBSCRIPTION
        account: str = "044680035044988526"

        try:
            response = api_instance.delete_account_using_delete_with_http_info(account, subscription)
            print(response)
        except ApiException as ex:
            print("Exception when calling the API %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        pass

    def testObtainInstitutions(self):
        # Create the authenticator to obtain access token
        # The token URL and Service URL are defined for this environment enum value.
        oauth_wire = OAuthWire4(self.CLIENT_ID, self.CLIENT_SECRET, self.AMBIENT)

        try:
            # Obtain an access token use application flow and scope "general"
            oauth_token_app: str = oauth_wire.obtain_access_token_app("general")
        except ApiException as ex:
            print("Exception to obtain access token %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        # create an instance of the API class and add the bearer token to request
        api_instance = InstitucionesApi(OAuthWire4.get_default_api_client(oauth_token_app))

        try:
            response: InstitutionsList = api_instance.get_all_institutions_using_get()
            print(response)
        except ApiException as ex:
            print("Exception when calling the API %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        pass

    def testObtainBalance(self):
        # Create the authenticator to obtain access token
        # The token URL and Service URL are defined for this environment enum value.
        oauth_wire = OAuthWire4(self.CLIENT_ID, self.CLIENT_SECRET, self.AMBIENT)

        try:
            # Obtain an access token use password flow and scope "spei_admin"
            oauth_token_user = oauth_wire.obtain_access_token_app_user(self.USER_KEY, self.SECRET_KEY, "spei_admin")
        except ApiException as ex:
            print("Exception to obtain access token %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        # create an instance of the API class and add the bearer token to request
        api_instance = SaldoApi(OAuthWire4.get_default_api_client(oauth_token_user))

        # build body with info (check references for more info, types, required fields)
        subscription: str = self.SUBSCRIPTION

        try:
            response: BalanceListResponse = api_instance.get_balance_using_get(subscription)
            print(response)
        except ApiException as ex:
            print("Exception when calling the API %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        pass

    def testObtainSPIDClassifications(self):
        # Create the authenticator to obtain access token
        # The token URL and Service URL are defined for this environment enum value.
        oauth_wire = OAuthWire4(self.CLIENT_ID, self.CLIENT_SECRET, self.AMBIENT)

        try:
            # Obtain an access token use password flow and scope "spid_admin"
            oauth_token_user = oauth_wire.obtain_access_token_app_user(self.USER_KEY, self.SECRET_KEY, "spid_admin")
        except ApiException as ex:
            print("Exception to obtain access token %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        # create an instance of the API class and add the bearer token to request
        api_instance = TransferenciasSPIDApi(OAuthWire4.get_default_api_client(oauth_token_user))

        # build body with info (check references for more info, types, required fields)
        subscription: str = self.SUBSCRIPTION

        try:
            response: SpidClassificationsResponseDTO = api_instance.get_spid_classifications_using_get(subscription)
            print(response)
        except ApiException as ex:
            print("Exception when calling the API %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        pass

    def testPreRegisterBeneficiariesSPID(self):
        # Create the authenticator to obtain access token
        # The token URL and Service URL are defined for this environment enum value.
        oauth_wire = OAuthWire4(self.CLIENT_ID, self.CLIENT_SECRET, self.AMBIENT)

        try:
            # Obtain an access token use password flow and scope "spid_admin"
            oauth_token_user = oauth_wire.obtain_access_token_app_user(self.USER_KEY, self.SECRET_KEY, "spid_admin")
        except ApiException as ex:
            print("Exception to obtain access token %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        # create an instance of the API class and add the bearer token to request
        api_instance = CuentasDeBeneficiariosSPIDApi(OAuthWire4.get_default_api_client(oauth_token_user))

        # build body with info (check references for more info, types, required fields)
        subscription: str = self.SUBSCRIPTION
        body: AccountSpid = AccountSpid(return_url="https://your-app-url.mx/return",
                                        cancel_return_url="https://your-app-url.mx/cancel",
                                        amount_limit=1000.00,
                                        beneficiary_account="112680000156896531",
                                        email=["beneficiary.spid@wire4.mx"],
                                        institution=BeneficiaryInstitution(name="BMONEX"),
                                        kind_of_relationship="RECURRENTE",
                                        numeric_reference="1234567",
                                        payment_concept="concept spid",
                                        relationship="ACREEDOR",
                                        rfc="SJBA920125AB1")

        try:
            response: TokenRequiredResponse = api_instance.pre_register_accounts_using_post1(body=body,
                                                                                             subscription=subscription)
            print(response)
        except ApiException as ex:
            print("Exception when calling the API %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        pass

    def testGetDepositants(self):
        # Create the authenticator to obtain access token
        # The token URL and Service URL are defined for this environment enum value.
        oauth_wire = OAuthWire4(self.CLIENT_ID, self.CLIENT_SECRET, self.AMBIENT)

        try:
            # Obtain an access token use password flow and scope "spei_admin"
            oauth_token_user = oauth_wire.obtain_access_token_app_user(self.USER_KEY, self.SECRET_KEY, "spei_admin")
        except ApiException as ex:
            print("Exception to obtain access token %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        # create an instance of the API class and add the bearer token to request
        api_instance = DepositantesApi(OAuthWire4.get_default_api_client(oauth_token_user))

        # build body with info (check references for more info, types, required fields)
        subscription: str = self.SUBSCRIPTION

        try:
            response: BalanceListResponse = api_instance.get_depositants_using_get(subscription)
            print(response)
        except ApiException as ex:
            print("Exception when calling the API %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        pass

    def testRegisterDepositants(self):
        # Create the authenticator to obtain access token
        # The token URL and Service URL are defined for this environment enum value.
        oauth_wire = OAuthWire4(self.CLIENT_ID, self.CLIENT_SECRET, self.AMBIENT)

        try:
            # Obtain an access token use password flow and scope "spei_admin"
            oauth_token_user = oauth_wire.obtain_access_token_app_user(self.USER_KEY, self.SECRET_KEY, "spei_admin")
        except ApiException as ex:
            print("Exception to obtain access token %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        # create an instance of the API class and add the bearer token to request
        api_instance = DepositantesApi(OAuthWire4.get_default_api_client(oauth_token_user))

        # build body with info (check references for more info, types, required fields)
        subscription: str = self.SUBSCRIPTION
        body: DepositantsRegister = DepositantsRegister(alias="Depositant 0292921",
                                                        currency_code="MXP",
                                                        email=["depositant@wire4.mx"],
                                                        name="Marge Bouvier")

        try:
            response: DepositantsResponse = api_instance.register_depositants_using_post(body, subscription)
            print(response)
        except ApiException as ex:
            print("Exception when calling the API %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        pass

    def testIncomingSpeiTransactionsReport(self):
        # Create the authenticator to obtain access token
        # The token URL and Service URL are defined for this environment enum value.
        oauth_wire = OAuthWire4(self.CLIENT_ID, self.CLIENT_SECRET, self.AMBIENT)

        try:
            # Obtain an access token use password flow and scope "spei_admin"
            oauth_token_user = oauth_wire.obtain_access_token_app_user(self.USER_KEY, self.SECRET_KEY, "spei_admin")
        except ApiException as ex:
            print("Exception to obtain access token %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        # create an instance of the API class and add the bearer token to request
        api_instance = TransferenciasSPEIApi(OAuthWire4.get_default_api_client(oauth_token_user))

        # build body with info (check references for more info, types, required fields)
        subscription: str = self.SUBSCRIPTION

        try:
            response: list = api_instance.incoming_spei_transactions_report_using_get(subscription)
            print(response)
        except ApiException as ex:
            print("Exception when calling the API %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        pass

    def testOutgoingSpeiTransactionsReport(self):
        # Create the authenticator to obtain access token
        # The token URL and Service URL are defined for this environment enum value.
        oauth_wire = OAuthWire4(self.CLIENT_ID, self.CLIENT_SECRET, self.AMBIENT)

        try:
            # Obtain an access token use password flow and scope "spei_admin"
            oauth_token_user = oauth_wire.obtain_access_token_app_user(self.USER_KEY, self.SECRET_KEY, "spei_admin")
        except ApiException as ex:
            print("Exception to obtain access token %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        # create an instance of the API class and add the bearer token to request
        api_instance = TransferenciasSPEIApi(OAuthWire4.get_default_api_client(oauth_token_user))

        # build body with info (check references for more info, types, required fields)
        subscription: str = self.SUBSCRIPTION

        try:
            response: list = api_instance.outgoing_spei_transactions_report_using_get(subscription)
            print(response)
        except ApiException as ex:
            print("Exception when calling the API %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        pass

    def testRegisterOutgoingSpeiTransaction(self):
        # Create the authenticator to obtain access token
        # The token URL and Service URL are defined for this environment enum value.
        oauth_wire = OAuthWire4(self.CLIENT_ID, self.CLIENT_SECRET, self.AMBIENT)

        try:
            # Obtain an access token use password flow and scope "spei_admin"
            oauth_token_user = oauth_wire.obtain_access_token_app_user(self.USER_KEY, self.SECRET_KEY, "spei_admin")
        except ApiException as ex:
            print("Exception to obtain access token %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        # create an instance of the API class and add the bearer token to request
        api_instance = TransferenciasSPEIApi(OAuthWire4.get_default_api_client(oauth_token_user))

        # build body with info (check references for more info, types, required fields)
        subscription: str = self.SUBSCRIPTION
        body: TransactionsOutgoingRegister = TransactionsOutgoingRegister(return_url="https://your-app-url.mx/return",
                                                                          cancel_return_url=
                                                                          "https://your-app-url.mx/cancel",
                                                                          transactions=[TransactionOutgoing(
                                                                              order_id=
                                                                              "137f14a4-9e12-4a98-bbd1-ab347753e68a",
                                                                              amount=1259.69,
                                                                              beneficiary_account="112680000156896531",
                                                                              currency_code="MXP",
                                                                              email=["notificar@wire4.mx"],
                                                                              reference=1234567,
                                                                              concept="Transfer out test 1")])

        try:
            response: TokenRequiredResponse = api_instance.register_outgoing_spei_transaction_using_post(body,
                                                                                                         subscription)
            print(response)
        except ApiException as ex:
            print("Exception when calling the API %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        pass

    def testDeleteOutgoingPendingSpeiTransaction(self):
        # Create the authenticator to obtain access token
        # The token URL and Service URL are defined for this environment enum value.
        oauth_wire = OAuthWire4(self.CLIENT_ID, self.CLIENT_SECRET, self.AMBIENT)

        try:
            # Obtain an access token use password flow and scope "spei_admin"
            oauth_token_user = oauth_wire.obtain_access_token_app_user(self.USER_KEY, self.SECRET_KEY, "spei_admin")
        except ApiException as ex:
            print("Exception to obtain access token %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        # create an instance of the API class and add the bearer token to request
        api_instance = TransferenciasSPEIApi(OAuthWire4.get_default_api_client(oauth_token_user))

        # build body with info (check references for more info, types, required fields)
        subscription: str = self.SUBSCRIPTION
        request_id: str = "8abc184f-c3ac-4abd-9045-a9b4a501f007"

        try:
            response: TokenRequiredResponse = api_instance.drop_transactions_pending_using_delete_with_http_info(
                request_id, subscription)
            print(response)
        except ApiException as ex:
            print("Exception when calling the API %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        pass

    def testRegisterOutgoingSpidTransaction(self):
        # Create the authenticator to obtain access token
        # The token URL and Service URL are defined for this environment enum value.
        oauth_wire = OAuthWire4(self.CLIENT_ID, self.CLIENT_SECRET, self.AMBIENT)

        try:
            # Obtain an access token use password flow and scope "spid_admin"
            oauth_token_user = oauth_wire.obtain_access_token_app_user(self.USER_KEY, self.SECRET_KEY, "spid_admin")
        except ApiException as ex:
            print("Exception to obtain access token %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        # create an instance of the API class and add the bearer token to request
        api_instance = TransferenciasSPIDApi(OAuthWire4.get_default_api_client(oauth_token_user))

        # build body with info (check references for more info, types, required fields)
        subscription: str = self.SUBSCRIPTION
        body: TransactionOutgoingSpid = TransactionOutgoingSpid(return_url="https://your-app-url.mx/return",
                                                                cancel_return_url="https://your-app-url.mx/cancel",
                                                                amount=1259.69,
                                                                beneficiary_account="112680000156896531",
                                                                classification_id="01",
                                                                currency_code="USD",
                                                                email=["notificar@wire4.mx"],
                                                                numeric_reference_spid=1234567,
                                                                order_id="d56d261b-c8e5-4cd5-9085-68c8074fea3a",
                                                                payment_concept_spid="Transfer out test 1")

        try:
            response: TokenRequiredResponse = api_instance.register_outgoing_spid_transaction_using_post(body,
                                                                                                         subscription)
            print(response)
        except ApiException as ex:
            print("Exception when calling the API %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        pass

    def testRegisterWebHook(self):
        # Create the authenticator to obtain access token
        # The token URL and Service URL are defined for this environment enum value.
        oauth_wire = OAuthWire4(self.CLIENT_ID, self.CLIENT_SECRET, self.AMBIENT)

        try:
            # Obtain an access token use application flow and scope "general"
            oauth_token_app: str = oauth_wire.obtain_access_token_app("general")
        except ApiException as ex:
            print("Exception to obtain access token %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        # create an instance of the API class and add the bearer token to request
        api_instance = WebhooksApi(OAuthWire4.get_default_api_client(oauth_token_app))
        body: WebhookRequest = WebhookRequest(events=["ACCOUNT.CREATED",
                                                      "TRANSACTION.OUTGOING.RECEIVED",
                                                      "ENROLLMENT.CREATED"],
                                              name="SDK-WEBHOOK-REGISTER",
                                              url="https://www.webhook.site/39034a03-8faf-424e-bb4a-7c3fee2bbfd3")

        try:
            response: WebhookResponse = api_instance.register_webhook(body)
            print(response)
        except ApiException as ex:
            print("Exception when calling the API %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        pass

    def testGetWebHooks(self):
        # Create the authenticator to obtain access token
        # The token URL and Service URL are defined for this environment enum value.
        oauth_wire = OAuthWire4(self.CLIENT_ID, self.CLIENT_SECRET, self.AMBIENT)

        try:
            # Obtain an access token use application flow and scope "general"
            oauth_token_app: str = oauth_wire.obtain_access_token_app("general")
        except ApiException as ex:
            print("Exception to obtain access token %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        # create an instance of the API class and add the bearer token to request
        api_instance = WebhooksApi(OAuthWire4.get_default_api_client(oauth_token_app))

        try:
            response: WebhooksList = api_instance.get_webhooks()
            print(response)
        except ApiException as ex:
            print("Exception when calling the API %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        pass

    def testGetWebHookById(self):
        # Create the authenticator to obtain access token
        # The token URL and Service URL are defined for this environment enum value.
        oauth_wire = OAuthWire4(self.CLIENT_ID, self.CLIENT_SECRET, self.AMBIENT)

        try:
            # Obtain an access token use application flow and scope "general"
            oauth_token_app: str = oauth_wire.obtain_access_token_app("general")
        except ApiException as ex:
            print("Exception to obtain access token %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        # create an instance of the API class and add the bearer token to request
        api_instance = WebhooksApi(OAuthWire4.get_default_api_client(oauth_token_app))

        try:
            response: WebhookResponse = api_instance.get_webhook(id="wh_3fe3e5f4849f4cabb147804fd55c86fc")
            print(response)
        except ApiException as ex:
            print("Exception when calling the API %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        pass

    def testGetFacturas(self):
        # Create the authenticator to obtain access token
        # The token URL and Service URL are defined for this environment enum value.
        oauth_wire = OAuthWire4(self.CLIENT_ID, self.CLIENT_SECRET, self.AMBIENT)

        try:
            # Obtain an access token use application flow and scope "general"
            oauth_token_app: str = oauth_wire.obtain_access_token_app("general")
        except ApiException as ex:
            print("Exception to obtain access token %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        # create an instance of the API class and add the bearer token to request
        api_instance = FacturasApi(OAuthWire4.get_default_api_client(oauth_token_app))

        try:
            response: list = api_instance.billings_report_using_get(period="2019-10")
            print(response)
        except ApiException as ex:
            print("Exception when calling the API %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        pass

    def testGetFacturasById(self):
        # Create the authenticator to obtain access token
        # The token URL and Service URL are defined for this environment enum value.
        oauth_wire = OAuthWire4(self.CLIENT_ID, self.CLIENT_SECRET, self.AMBIENT)

        try:
            # Obtain an access token use application flow and scope "general"
            oauth_token_app: str = oauth_wire.obtain_access_token_app("general")
        except ApiException as ex:
            print("Exception to obtain access token %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        # create an instance of the API class and add the bearer token to request
        api_instance = FacturasApi(OAuthWire4.get_default_api_client(oauth_token_app))

        try:
            response: Billing = api_instance.billings_report_by_id_using_get(id="834BA74A-BBBB-43C4-8400-A4528153C2BD")
            print(response)
        except ApiException as ex:
            print("Exception when calling the API %s\n" % ex, file=sys.stderr)
            # Optional manage exception in access token flow
            return

        pass


if __name__ == '__main__':
    unittest.main()
