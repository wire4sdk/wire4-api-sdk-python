# wire4_client.ContactoApi

All URIs are relative to *https://sandbox-api.wire4.mx/wire4/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_contact_using_post**](ContactoApi.md#send_contact_using_post) | **POST** /contact | Solicitud de contacto

# **send_contact_using_post**
> send_contact_using_post(body, authorization)

Solicitud de contacto

Notifica a un asesor Monex para que se ponga en contacto con un posible cliente.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.ContactoApi()
body = wire4_client.ContactRequest() # ContactRequest | Información del contacto
authorization = 'authorization_example' # str | Header para token

try:
    # Solicitud de contacto
    api_instance.send_contact_using_post(body, authorization)
except ApiException as e:
    print("Exception when calling ContactoApi->send_contact_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ContactRequest**](ContactRequest.md)| Información del contacto | 
 **authorization** | **str**| Header para token | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

