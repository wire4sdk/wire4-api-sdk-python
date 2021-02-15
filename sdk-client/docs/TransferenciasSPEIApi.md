# wire4_client.TransferenciasSPEIApi

All URIs are relative to *https://sandbox-api.wire4.mx/wire4/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_authorization_transactions_group**](TransferenciasSPEIApi.md#create_authorization_transactions_group) | **POST** /subscriptions/{subscription}/transactions/group | Agrupa transacciones bajo un request_id 
[**drop_transactions_pending_using_delete**](TransferenciasSPEIApi.md#drop_transactions_pending_using_delete) | **DELETE** /subscriptions/{subscription}/transactions/outcoming/spei/request/{requestId} | Eliminación de transferencias SPEI® pendientes
[**incoming_spei_transactions_report_using_get**](TransferenciasSPEIApi.md#incoming_spei_transactions_report_using_get) | **GET** /subscriptions/{subscription}/transactions/incoming/spei | Consulta de transferencias recibidas
[**out_comming_spei_request_id_transactions_report_using_get**](TransferenciasSPEIApi.md#out_comming_spei_request_id_transactions_report_using_get) | **GET** /subscriptions/{subscription}/transactions/outcoming/spei/{requestId} | Consulta de transferencias de salida por identificador de petición
[**outgoing_spei_transactions_report_using_get**](TransferenciasSPEIApi.md#outgoing_spei_transactions_report_using_get) | **GET** /subscriptions/{subscription}/transactions/outcoming/spei | Consulta de transferencias realizadas
[**register_outgoing_spei_transaction_using_post**](TransferenciasSPEIApi.md#register_outgoing_spei_transaction_using_post) | **POST** /subscriptions/{subscription}/transactions/outcoming/spei | Registro de transferencias

# **create_authorization_transactions_group**
> TokenRequiredResponse create_authorization_transactions_group(body, authorization, subscription)

Agrupa transacciones bajo un request_id 

Agrupa transacciones SPEI/SPID en un mismo transaction_id, posteriormente genera la dirección URL del centro de autorización para la confirmación de las transacciones. <br><br>Las transacciones deben estar en estatus PENDING y pertenecer a un mismo contrato.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.TransferenciasSPEIApi()
body = wire4_client.AuthorizationTransactionGroup() # AuthorizationTransactionGroup | Objeto con la información para agrupar transacciones existentes y autorizarlas de forma conjunta.
authorization = 'authorization_example' # str | Header para token
subscription = 'subscription_example' # str | Es el Identificador de la suscripción.

try:
    # Agrupa transacciones bajo un request_id 
    api_response = api_instance.create_authorization_transactions_group(body, authorization, subscription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransferenciasSPEIApi->create_authorization_transactions_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthorizationTransactionGroup**](AuthorizationTransactionGroup.md)| Objeto con la información para agrupar transacciones existentes y autorizarlas de forma conjunta. | 
 **authorization** | **str**| Header para token | 
 **subscription** | **str**| Es el Identificador de la suscripción. | 

### Return type

[**TokenRequiredResponse**](TokenRequiredResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **drop_transactions_pending_using_delete**
> drop_transactions_pending_using_delete(authorization, request_id, subscription, order_id=order_id)

Eliminación de transferencias SPEI® pendientes

Elimina un conjunto de transferencias en estado pendiente de confirmar o autorizar, en la cuenta del cliente Monex relacionada a la suscripción.<br><br><b>Nota:</b> Las transferencias no deben haber sido confirmadas o autorizadas por el cliente.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.TransferenciasSPEIApi()
authorization = 'authorization_example' # str | Header para token
request_id = 'request_id_example' # str | Identificador de las transferencias a eliminar.
subscription = 'subscription_example' # str | Es el identificador de la suscripción a esta API.
order_id = 'order_id_example' # str | Listado de identificadores dentro del request_id para eliminar. (optional)

try:
    # Eliminación de transferencias SPEI® pendientes
    api_instance.drop_transactions_pending_using_delete(authorization, request_id, subscription, order_id=order_id)
except ApiException as e:
    print("Exception when calling TransferenciasSPEIApi->drop_transactions_pending_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Header para token | 
 **request_id** | **str**| Identificador de las transferencias a eliminar. | 
 **subscription** | **str**| Es el identificador de la suscripción a esta API. | 
 **order_id** | **str**| Listado de identificadores dentro del request_id para eliminar. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **incoming_spei_transactions_report_using_get**
> list[Deposit] incoming_spei_transactions_report_using_get(authorization, subscription)

Consulta de transferencias recibidas

Realiza una consulta de las transferencias recibidas (depósitos) en la cuenta del cliente Monex relacionada a la suscripción, las transferencias que regresa este recuso son únicamente las transferencias  recibidas durante el día en el que se realiza la consulta.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.TransferenciasSPEIApi()
authorization = 'authorization_example' # str | Header para token
subscription = 'subscription_example' # str | Es el identificador de la suscripción a esta API.

try:
    # Consulta de transferencias recibidas
    api_response = api_instance.incoming_spei_transactions_report_using_get(authorization, subscription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransferenciasSPEIApi->incoming_spei_transactions_report_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Header para token | 
 **subscription** | **str**| Es el identificador de la suscripción a esta API. | 

### Return type

[**list[Deposit]**](Deposit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **out_comming_spei_request_id_transactions_report_using_get**
> PaymentsRequestId out_comming_spei_request_id_transactions_report_using_get(authorization, request_id, subscription)

Consulta de transferencias de salida por identificador de petición

Consulta las transferencias de salida registradas en una petición, las transferencias que regresa este recuso son únicamente las transferencias de salida agrupadas al identificador de la petición que se generó al hacer el registro de las transacciones el cuál se debe especificar como parte del path de este endpoint.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.TransferenciasSPEIApi()
authorization = 'authorization_example' # str | Header para token
request_id = 'request_id_example' # str | Identificador de la petición a buscar.
subscription = 'subscription_example' # str | Es el identificador de la suscripción a esta API.

try:
    # Consulta de transferencias de salida por identificador de petición
    api_response = api_instance.out_comming_spei_request_id_transactions_report_using_get(authorization, request_id, subscription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransferenciasSPEIApi->out_comming_spei_request_id_transactions_report_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Header para token | 
 **request_id** | **str**| Identificador de la petición a buscar. | 
 **subscription** | **str**| Es el identificador de la suscripción a esta API. | 

### Return type

[**PaymentsRequestId**](PaymentsRequestId.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outgoing_spei_transactions_report_using_get**
> list[Payment] outgoing_spei_transactions_report_using_get(authorization, subscription, order_id=order_id)

Consulta de transferencias realizadas

Consulta las transferencias realizadas en la cuenta del cliente Monex relacionada a la suscripción, las transferencias que regresa este recuso son únicamente las transferencias recibidas en el día en el que se realiza la consulta.<br>Se pueden realizar consultas por <strong>order_id</strong> al realizar este tipo de consultas no importa el día en el que se realizó la transferencia

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.TransferenciasSPEIApi()
authorization = 'authorization_example' # str | Header para token
subscription = 'subscription_example' # str | Es el identificador de la suscripción a esta API.
order_id = 'order_id_example' # str | Es el identificador de la orden a buscar. (optional)

try:
    # Consulta de transferencias realizadas
    api_response = api_instance.outgoing_spei_transactions_report_using_get(authorization, subscription, order_id=order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransferenciasSPEIApi->outgoing_spei_transactions_report_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Header para token | 
 **subscription** | **str**| Es el identificador de la suscripción a esta API. | 
 **order_id** | **str**| Es el identificador de la orden a buscar. | [optional] 

### Return type

[**list[Payment]**](Payment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_outgoing_spei_transaction_using_post**
> TokenRequiredResponse register_outgoing_spei_transaction_using_post(body, authorization, subscription)

Registro de transferencias

Se registra un conjunto de transferencias (una o más) a realizar en la cuenta del cliente Monex relacionada a la suscripción. En la respuesta se proporcionará una dirección URL que lo llevará al centro de autorización para que las transferencias sean confirmadas (autorizadas) por el cliente para que se efectúen, para ello debe ingresar la llave electrónica (Token).<br>  Nota: Debe considerar que el concepto de cada una de las transacciones solo debe contener caracteres alfanuméricos por lo que en caso de que se reciban caracteres como ñ o acentos serán sustituidos por n o en su caso por la letra sin acento. Los caracteres no alfanuméricos como pueden ser caracteres especiales serán eliminados.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.TransferenciasSPEIApi()
body = wire4_client.TransactionsOutgoingRegister() # TransactionsOutgoingRegister | Información de las transferencias SPEI de salida
authorization = 'authorization_example' # str | Header para token
subscription = 'subscription_example' # str | Es el identificador de la suscripción a esta API.

try:
    # Registro de transferencias
    api_response = api_instance.register_outgoing_spei_transaction_using_post(body, authorization, subscription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransferenciasSPEIApi->register_outgoing_spei_transaction_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransactionsOutgoingRegister**](TransactionsOutgoingRegister.md)| Información de las transferencias SPEI de salida | 
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

