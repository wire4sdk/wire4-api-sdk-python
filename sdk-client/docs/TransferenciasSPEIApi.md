# wire4_client.TransferenciasSPEIApi

All URIs are relative to *https://sandbox-api.wire4.mx/wire4/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**drop_transactions_pending_using_delete**](TransferenciasSPEIApi.md#drop_transactions_pending_using_delete) | **DELETE** /subscriptions/{subscription}/transactions/outcoming/spei/request/{requestId} | Eliminación de transferencias SPEI® pendientes
[**incoming_spei_transactions_report_using_get**](TransferenciasSPEIApi.md#incoming_spei_transactions_report_using_get) | **GET** /subscriptions/{subscription}/transactions/incoming/spei | Consulta de transferencias recibidas
[**out_comming_spei_request_id_transactions_report_using_get**](TransferenciasSPEIApi.md#out_comming_spei_request_id_transactions_report_using_get) | **GET** /subscriptions/{subscription}/transactions/outcoming/spei/{requestId} | Consulta de transferencias de salida por identificador de petición
[**outgoing_spei_transactions_report_using_get**](TransferenciasSPEIApi.md#outgoing_spei_transactions_report_using_get) | **GET** /subscriptions/{subscription}/transactions/outcoming/spei | Consulta de transferencias realizadas
[**register_outgoing_spei_transaction_using_post**](TransferenciasSPEIApi.md#register_outgoing_spei_transaction_using_post) | **POST** /subscriptions/{subscription}/transactions/outcoming/spei | Registro de transferencias

# **drop_transactions_pending_using_delete**
> drop_transactions_pending_using_delete(request_id, subscription)

Eliminación de transferencias SPEI® pendientes

Elimina un conjunto de transferencias a realizar en la cuenta del cliente Monex relacionada a la suscripción, las transferencias no deben haber sido confirmadas por el cliente.

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
api_instance = wire4_client.TransferenciasSPEIApi(wire4_client.ApiClient(configuration))
request_id = 'request_id_example' # str | Identificador de las transferencias a eliminar
subscription = 'subscription_example' # str | El identificador de la suscripción a esta API

try:
    # Eliminación de transferencias SPEI® pendientes
    api_instance.drop_transactions_pending_using_delete(request_id, subscription)
except ApiException as e:
    print("Exception when calling TransferenciasSPEIApi->drop_transactions_pending_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| Identificador de las transferencias a eliminar | 
 **subscription** | **str**| El identificador de la suscripción a esta API | 

### Return type

void (empty response body)

### Authorization

[wire4_aut_app_user_spei](../README.md#wire4_aut_app_user_spei)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **incoming_spei_transactions_report_using_get**
> list[Deposit] incoming_spei_transactions_report_using_get(subscription)

Consulta de transferencias recibidas

Realiza una consulta de las transferencias recibidas (depósitos) en la cuenta del cliente Monex relacionada a la suscripción, las transferencias que regresa este recuso son únicamente las transferencias  recibidas durante el día en el que se realiza la consulta.

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
api_instance = wire4_client.TransferenciasSPEIApi(wire4_client.ApiClient(configuration))
subscription = 'subscription_example' # str | El identificador de la suscripción a esta API

try:
    # Consulta de transferencias recibidas
    api_response = api_instance.incoming_spei_transactions_report_using_get(subscription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransferenciasSPEIApi->incoming_spei_transactions_report_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription** | **str**| El identificador de la suscripción a esta API | 

### Return type

[**list[Deposit]**](Deposit.md)

### Authorization

[wire4_aut_app_user_spei](../README.md#wire4_aut_app_user_spei)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **out_comming_spei_request_id_transactions_report_using_get**
> PaymentsRequestId out_comming_spei_request_id_transactions_report_using_get(request_id, subscription)

Consulta de transferencias de salida por identificador de petición

Consulta las transferencias de salida registradas en una petición, las transferencias que regresa este recuso son únicamente las transferencias  de salida agrupadas al identificador de la petición que se generó al hacer el registro de las transacciones el cual se debe especificar como parte del path de este endpoint.

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
api_instance = wire4_client.TransferenciasSPEIApi(wire4_client.ApiClient(configuration))
request_id = 'request_id_example' # str | Identificador de la petición a buscar
subscription = 'subscription_example' # str | El identificador de la suscripción a esta API

try:
    # Consulta de transferencias de salida por identificador de petición
    api_response = api_instance.out_comming_spei_request_id_transactions_report_using_get(request_id, subscription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransferenciasSPEIApi->out_comming_spei_request_id_transactions_report_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| Identificador de la petición a buscar | 
 **subscription** | **str**| El identificador de la suscripción a esta API | 

### Return type

[**PaymentsRequestId**](PaymentsRequestId.md)

### Authorization

[wire4_aut_app_user_spei](../README.md#wire4_aut_app_user_spei)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outgoing_spei_transactions_report_using_get**
> list[Payment] outgoing_spei_transactions_report_using_get(subscription, order_id=order_id)

Consulta de transferencias realizadas

Consulta las transferencias realizadas en la cuenta del cliente Monex relacionada a la suscripción, las transferencias que regresa este recuso son únicamente las transferencias recibidas en el día en el que se realiza la consulta.<br>Se pueden realizar consultas por <strong>order_id</strong> al realizar este tipo de consultas no importa el día en el que se realizó la transferencia

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
api_instance = wire4_client.TransferenciasSPEIApi(wire4_client.ApiClient(configuration))
subscription = 'subscription_example' # str | El identificador de la suscripción a esta API
order_id = 'order_id_example' # str | Identificador de la orden a buscar (optional)

try:
    # Consulta de transferencias realizadas
    api_response = api_instance.outgoing_spei_transactions_report_using_get(subscription, order_id=order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransferenciasSPEIApi->outgoing_spei_transactions_report_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription** | **str**| El identificador de la suscripción a esta API | 
 **order_id** | **str**| Identificador de la orden a buscar | [optional] 

### Return type

[**list[Payment]**](Payment.md)

### Authorization

[wire4_aut_app_user_spei](../README.md#wire4_aut_app_user_spei)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_outgoing_spei_transaction_using_post**
> TokenRequiredResponse register_outgoing_spei_transaction_using_post(body, subscription)

Registro de transferencias

Registra un conjunto de transferencias a realizar en la cuenta del cliente Monex relacionada a la suscripción, las transferencias deben ser confirmadas por el cliente para que se efectuen.

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
api_instance = wire4_client.TransferenciasSPEIApi(wire4_client.ApiClient(configuration))
body = wire4_client.TransactionsOutgoingRegister() # TransactionsOutgoingRegister | Información de las transferencias SPEI de salida
subscription = 'subscription_example' # str | El identificador de la suscripción a esta API

try:
    # Registro de transferencias
    api_response = api_instance.register_outgoing_spei_transaction_using_post(body, subscription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransferenciasSPEIApi->register_outgoing_spei_transaction_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransactionsOutgoingRegister**](TransactionsOutgoingRegister.md)| Información de las transferencias SPEI de salida | 
 **subscription** | **str**| El identificador de la suscripción a esta API | 

### Return type

[**TokenRequiredResponse**](TokenRequiredResponse.md)

### Authorization

[wire4_aut_app_user_spei](../README.md#wire4_aut_app_user_spei)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

