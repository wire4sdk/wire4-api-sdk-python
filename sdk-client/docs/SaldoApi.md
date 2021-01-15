# wire4_client.SaldoApi

All URIs are relative to *https://sandbox-api.wire4.mx/wire4/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_balance_using_get**](SaldoApi.md#get_balance_using_get) | **GET** /subscriptions/{subscription}/balance | Consulta los saldo de una cuenta

# **get_balance_using_get**
> BalanceListResponse get_balance_using_get(authorization, subscription)

Consulta los saldo de una cuenta

Obtiene el saldo de un contrato, según las divisas que se manejen en dicho contrato, ya sea peso mexicano (MXP) o dólar estadounidense (USD).

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.SaldoApi()
authorization = 'authorization_example' # str | Header para token
subscription = 'subscription_example' # str | Es el identificador de la suscripción a esta API.

try:
    # Consulta los saldo de una cuenta
    api_response = api_instance.get_balance_using_get(authorization, subscription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SaldoApi->get_balance_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Header para token | 
 **subscription** | **str**| Es el identificador de la suscripción a esta API. | 

### Return type

[**BalanceListResponse**](BalanceListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

