# wire4_client.WebhooksApi

All URIs are relative to *https://sandbox-api.wire4.mx/wire4/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_webhook**](WebhooksApi.md#get_webhook) | **GET** /webhooks/{id} | Consulta de Webhook
[**get_webhooks**](WebhooksApi.md#get_webhooks) | **GET** /webhooks | Consulta de Webhooks
[**register_webhook**](WebhooksApi.md#register_webhook) | **POST** /webhooks | Alta de Webhook

# **get_webhook**
> WebhookResponse get_webhook(id)

Consulta de Webhook

Obtiene un webhook registrado en la plataforma mediante su identificador.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: wire4_aut_app
configuration = wire4_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = wire4_client.WebhooksApi(wire4_client.ApiClient(configuration))
id = 'id_example' # str | Identificador del webhook

try:
    # Consulta de Webhook
    api_response = api_instance.get_webhook(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->get_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identificador del webhook | 

### Return type

[**WebhookResponse**](WebhookResponse.md)

### Authorization

[wire4_aut_app](../README.md#wire4_aut_app)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhooks**
> WebhooksList get_webhooks()

Consulta de Webhooks

Obtiene los webhooks registrados en la plataforma que tengan estatus 'ACTIVE' e 'INACTIVE'.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: wire4_aut_app
configuration = wire4_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = wire4_client.WebhooksApi(wire4_client.ApiClient(configuration))

try:
    # Consulta de Webhooks
    api_response = api_instance.get_webhooks()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->get_webhooks: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WebhooksList**](WebhooksList.md)

### Authorization

[wire4_aut_app](../README.md#wire4_aut_app)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_webhook**
> WebhookResponse register_webhook(body)

Alta de Webhook

Registra un webhook en la plataforma para su uso como notificador de eventos cuando estos ocurran.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: wire4_aut_app
configuration = wire4_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = wire4_client.WebhooksApi(wire4_client.ApiClient(configuration))
body = wire4_client.WebhookRequest() # WebhookRequest | Información para registrar un Webhook

try:
    # Alta de Webhook
    api_response = api_instance.register_webhook(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->register_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebhookRequest**](WebhookRequest.md)| Información para registrar un Webhook | 

### Return type

[**WebhookResponse**](WebhookResponse.md)

### Authorization

[wire4_aut_app](../README.md#wire4_aut_app)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

