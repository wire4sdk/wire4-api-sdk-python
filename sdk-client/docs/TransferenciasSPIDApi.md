# wire4_client.TransferenciasSPIDApi

All URIs are relative to *https://sandbox-api.wire4.mx/wire4/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_spid_classifications_using_get**](TransferenciasSPIDApi.md#get_spid_classifications_using_get) | **GET** /subscriptions/{subscription}/beneficiaries/spid/classifications | Consulta las clasificaciones para operaciones con SPID
[**register_outgoing_spid_transaction_using_post**](TransferenciasSPIDApi.md#register_outgoing_spid_transaction_using_post) | **POST** /subscriptions/{subscription}/transactions/outcoming/spid | Registro de transferencias SPID

# **get_spid_classifications_using_get**
> SpidClassificationsResponseDTO get_spid_classifications_using_get(subscription)

Consulta las clasificaciones para operaciones con SPID

Obtiene las clasificaciones para operaciones con dólares (SPID) de Monex.<br/>Este recurso se debe invocar previo al realizar una operación SPID.<br/>Se requiere que el token de autenticación se genere con scope spid_admin.

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
api_instance = wire4_client.TransferenciasSPIDApi(wire4_client.ApiClient(configuration))
subscription = 'subscription_example' # str | El identificador de la suscripción a esta API

try:
    # Consulta las clasificaciones para operaciones con SPID
    api_response = api_instance.get_spid_classifications_using_get(subscription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransferenciasSPIDApi->get_spid_classifications_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription** | **str**| El identificador de la suscripción a esta API | 

### Return type

[**SpidClassificationsResponseDTO**](SpidClassificationsResponseDTO.md)

### Authorization

[wire4_aut_app_user_spid](../README.md#wire4_aut_app_user_spid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_outgoing_spid_transaction_using_post**
> TokenRequiredResponse register_outgoing_spid_transaction_using_post(body, subscription)

Registro de transferencias SPID

Registra un conjunto de transferencias a realizar en la cuenta del cliente Monex relacionada a la suscripción, las transferencias deben ser confirmadas por el cliente para que se efectuen.

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
api_instance = wire4_client.TransferenciasSPIDApi(wire4_client.ApiClient(configuration))
body = wire4_client.TransactionOutgoingSpid() # TransactionOutgoingSpid | Información de las transferencias SPID de salida
subscription = 'subscription_example' # str | El identificador de la suscripción a esta API

try:
    # Registro de transferencias SPID
    api_response = api_instance.register_outgoing_spid_transaction_using_post(body, subscription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransferenciasSPIDApi->register_outgoing_spid_transaction_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransactionOutgoingSpid**](TransactionOutgoingSpid.md)| Información de las transferencias SPID de salida | 
 **subscription** | **str**| El identificador de la suscripción a esta API | 

### Return type

[**TokenRequiredResponse**](TokenRequiredResponse.md)

### Authorization

[wire4_aut_app_user_spid](../README.md#wire4_aut_app_user_spid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

