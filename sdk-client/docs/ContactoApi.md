# wire4_client.ContactoApi

All URIs are relative to *https://sandbox-api.wire4.mx/wire4/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_contact_using_post**](ContactoApi.md#send_contact_using_post) | **POST** /contact | Solicitud de contacto

# **send_contact_using_post**
> send_contact_using_post(body)

Solicitud de contacto

Notifica a un asesor Monex para que se ponga en contacto con un posible cliente.

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
api_instance = wire4_client.ContactoApi(wire4_client.ApiClient(configuration))
body = wire4_client.ContactRequest() # ContactRequest | Información del contacto

try:
    # Solicitud de contacto
    api_instance.send_contact_using_post(body)
except ApiException as e:
    print("Exception when calling ContactoApi->send_contact_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ContactRequest**](ContactRequest.md)| Información del contacto | 

### Return type

void (empty response body)

### Authorization

[wire4_aut_app](../README.md#wire4_aut_app)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

