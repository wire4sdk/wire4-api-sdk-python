# wire4_client.InstitucionesApi

All URIs are relative to *https://sandbox-api.wire4.mx/wire4/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_institutions_using_get**](InstitucionesApi.md#get_all_institutions_using_get) | **GET** /institutions | Información de instituciones bancarias.

# **get_all_institutions_using_get**
> InstitutionsList get_all_institutions_using_get()

Información de instituciones bancarias.

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
api_instance = wire4_client.InstitucionesApi(wire4_client.ApiClient(configuration))

try:
    # Información de instituciones bancarias.
    api_response = api_instance.get_all_institutions_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstitucionesApi->get_all_institutions_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InstitutionsList**](InstitutionsList.md)

### Authorization

[wire4_aut_app](../README.md#wire4_aut_app)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

