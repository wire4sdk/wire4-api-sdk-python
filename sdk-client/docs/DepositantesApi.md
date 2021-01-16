# wire4_client.DepositantesApi

All URIs are relative to *https://sandbox-api.wire4.mx/wire4/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_depositants_using_get**](DepositantesApi.md#get_depositants_using_get) | **GET** /subscriptions/{subscription}/depositants | Consulta de cuentas de depositantes
[**register_depositants_using_post**](DepositantesApi.md#register_depositants_using_post) | **POST** /subscriptions/{subscription}/depositants | Registra un nuevo depositante

# **get_depositants_using_get**
> GetDepositants get_depositants_using_get(authorization, subscription)

Consulta de cuentas de depositantes

Obtiene una lista de depositantes asociados al contrato relacionado a la suscripción.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.DepositantesApi()
authorization = 'authorization_example' # str | Header para token
subscription = 'subscription_example' # str | Es el identificador de la suscripción a esta API.

try:
    # Consulta de cuentas de depositantes
    api_response = api_instance.get_depositants_using_get(authorization, subscription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DepositantesApi->get_depositants_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Header para token | 
 **subscription** | **str**| Es el identificador de la suscripción a esta API. | 

### Return type

[**GetDepositants**](GetDepositants.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_depositants_using_post**
> DepositantsResponse register_depositants_using_post(body, authorization, subscription)

Registra un nuevo depositante

Registra un nuevo depositante en el contrato asociado a la suscripción.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.DepositantesApi()
body = wire4_client.DepositantsRegister() # DepositantsRegister | Depositant info
authorization = 'authorization_example' # str | Header para token
subscription = 'subscription_example' # str | Es el identificador de la suscripción a esta API.

try:
    # Registra un nuevo depositante
    api_response = api_instance.register_depositants_using_post(body, authorization, subscription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DepositantesApi->register_depositants_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DepositantsRegister**](DepositantsRegister.md)| Depositant info | 
 **authorization** | **str**| Header para token | 
 **subscription** | **str**| Es el identificador de la suscripción a esta API. | 

### Return type

[**DepositantsResponse**](DepositantsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

