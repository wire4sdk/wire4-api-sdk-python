# wire4_client.WebhooksApi

All URIs are relative to *https://sandbox-api.wire4.mx/wire4/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_webhook**](WebhooksApi.md#get_webhook) | **GET** /webhooks/{id} | Consulta de Webhook
[**get_webhooks**](WebhooksApi.md#get_webhooks) | **GET** /webhooks | Consulta de Webhooks
[**register_webhook**](WebhooksApi.md#register_webhook) | **POST** /webhooks | Alta de Webhook

# **get_webhook**
> WebhookResponse get_webhook(authorization, id)

Consulta de Webhook

Obtiene un webhook registrado en la plataforma mediante su identificador.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.WebhooksApi()
authorization = 'authorization_example' # str | Header para token
id = 'id_example' # str | Identificador del webhook

try:
    # Consulta de Webhook
    api_response = api_instance.get_webhook(authorization, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->get_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Header para token | 
 **id** | **str**| Identificador del webhook | 

### Return type

[**WebhookResponse**](WebhookResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhooks**
> WebhooksList get_webhooks(authorization)

Consulta de Webhooks

Obtiene los webhooks registrados en la plataforma que tengan estatus 'ACTIVE' e 'INACTIVE'.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.WebhooksApi()
authorization = 'authorization_example' # str | Header para token

try:
    # Consulta de Webhooks
    api_response = api_instance.get_webhooks(authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->get_webhooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Header para token | 

### Return type

[**WebhooksList**](WebhooksList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_webhook**
> WebhookResponse register_webhook(body, authorization)

Alta de Webhook

Registra un webhook en la plataforma para su uso como notificador de eventos cuando estos ocurran.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.WebhooksApi()
body = wire4_client.WebhookRequest() # WebhookRequest | Información para registrar un Webhook
authorization = 'authorization_example' # str | Header para token

try:
    # Alta de Webhook
    api_response = api_instance.register_webhook(body, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->register_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebhookRequest**](WebhookRequest.md)| Información para registrar un Webhook | 
 **authorization** | **str**| Header para token | 

### Return type

[**WebhookResponse**](WebhookResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

