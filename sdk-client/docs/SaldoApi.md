# wire4_client.SaldoApi

All URIs are relative to *https://sandbox-api.wire4.mx/wire4/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_balance_using_get**](SaldoApi.md#get_balance_using_get) | **GET** /subscriptions/{subscription}/balance | Consulta los saldo de una cuenta

# **get_balance_using_get**
> BalanceListResponse get_balance_using_get(subscription)

Consulta los saldo de una cuenta

Obtiene el de las divisas que se manejen en el contrato.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: wire4_aut_app_user_spei
configuration = wire4_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = wire4_client.SaldoApi(wire4_client.ApiClient(configuration))
subscription = 'subscription_example' # str | El identificador de la suscripción a esta API

try:
    # Consulta los saldo de una cuenta
    api_response = api_instance.get_balance_using_get(subscription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SaldoApi->get_balance_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription** | **str**| El identificador de la suscripción a esta API | 

### Return type

[**BalanceListResponse**](BalanceListResponse.md)

### Authorization

[wire4_aut_app_user_spei](../README.md#wire4_aut_app_user_spei)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

