# wire4_client.CuentasDeBeneficiariosSPIDApi

All URIs are relative to *https://sandbox-api.wire4.mx/wire4/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pre_register_accounts_using_post1**](CuentasDeBeneficiariosSPIDApi.md#pre_register_accounts_using_post1) | **POST** /subscriptions/{subscription}/beneficiaries/spid | Pre-registro de cuentas de beneficiarios SPID

# **pre_register_accounts_using_post1**
> TokenRequiredResponse pre_register_accounts_using_post1(body, subscription)

Pre-registro de cuentas de beneficiarios SPID

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: wire4_aut_app_user_spid
configuration = wire4_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = wire4_client.CuentasDeBeneficiariosSPIDApi(wire4_client.ApiClient(configuration))
body = wire4_client.AccountSpid() # AccountSpid | Información de la cuenta del beneficiario
subscription = 'subscription_example' # str | El identificador de la suscripción a esta API

try:
    # Pre-registro de cuentas de beneficiarios SPID
    api_response = api_instance.pre_register_accounts_using_post1(body, subscription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CuentasDeBeneficiariosSPIDApi->pre_register_accounts_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountSpid**](AccountSpid.md)| Información de la cuenta del beneficiario | 
 **subscription** | **str**| El identificador de la suscripción a esta API | 

### Return type

[**TokenRequiredResponse**](TokenRequiredResponse.md)

### Authorization

[wire4_aut_app_user_spid](../README.md#wire4_aut_app_user_spid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

