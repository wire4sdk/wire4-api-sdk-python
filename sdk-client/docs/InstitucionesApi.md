# wire4_client.InstitucionesApi

All URIs are relative to *https://sandbox-api.wire4.mx/wire4/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_institutions_using_get**](InstitucionesApi.md#get_all_institutions_using_get) | **GET** /institutions | Información de instituciones bancarias.

# **get_all_institutions_using_get**
> InstitutionsList get_all_institutions_using_get(authorization)

Información de instituciones bancarias.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.InstitucionesApi()
authorization = 'authorization_example' # str | Header para token

try:
    # Información de instituciones bancarias.
    api_response = api_instance.get_all_institutions_using_get(authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstitucionesApi->get_all_institutions_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Header para token | 

### Return type

[**InstitutionsList**](InstitutionsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

