# wire4_client.TransferenciasSPIDApi

All URIs are relative to *https://sandbox-api.wire4.mx/wire4/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_spid_classifications_using_get**](TransferenciasSPIDApi.md#get_spid_classifications_using_get) | **GET** /subscriptions/{subscription}/beneficiaries/spid/classifications | Consulta de clasificaciones para operaciones SPID®
[**register_outgoing_spid_transaction_using_post**](TransferenciasSPIDApi.md#register_outgoing_spid_transaction_using_post) | **POST** /subscriptions/{subscription}/transactions/outcoming/spid | Registro de transferencias SPID®

# **get_spid_classifications_using_get**
> SpidClassificationsResponseDTO get_spid_classifications_using_get(authorization, subscription)

Consulta de clasificaciones para operaciones SPID®

Obtiene las clasificaciones para operaciones con dólares (SPID®) de Monex.<br/><br/>Este recurso se debe invocar previo al realizar una operación SPID.<br/><br/>

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.TransferenciasSPIDApi()
authorization = 'authorization_example' # str | Header para token
subscription = 'subscription_example' # str | Es el identificador de la suscripción a esta API.

try:
    # Consulta de clasificaciones para operaciones SPID®
    api_response = api_instance.get_spid_classifications_using_get(authorization, subscription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransferenciasSPIDApi->get_spid_classifications_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Header para token | 
 **subscription** | **str**| Es el identificador de la suscripción a esta API. | 

### Return type

[**SpidClassificationsResponseDTO**](SpidClassificationsResponseDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_outgoing_spid_transaction_using_post**
> TokenRequiredResponse register_outgoing_spid_transaction_using_post(body, authorization, subscription)

Registro de transferencias SPID®

Registra un conjunto de transferencias a realizar en la cuenta del cliente Monex relacionada a la suscripción. En la respuesta se proporcionará una dirección URL que lo llevará al centro de autorización para que las transferencias sean confirmadas (autorizadas) por el cliente para que se efectúen, para ello debe ingresar la llave electrónica (Token).

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.TransferenciasSPIDApi()
body = wire4_client.TransactionOutgoingSpid() # TransactionOutgoingSpid | Información de las transferencias SPID de salida
authorization = 'authorization_example' # str | Header para token
subscription = 'subscription_example' # str | Es el identificador de la suscripción a esta API.

try:
    # Registro de transferencias SPID®
    api_response = api_instance.register_outgoing_spid_transaction_using_post(body, authorization, subscription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransferenciasSPIDApi->register_outgoing_spid_transaction_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransactionOutgoingSpid**](TransactionOutgoingSpid.md)| Información de las transferencias SPID de salida | 
 **authorization** | **str**| Header para token | 
 **subscription** | **str**| Es el identificador de la suscripción a esta API. | 

### Return type

[**TokenRequiredResponse**](TokenRequiredResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

