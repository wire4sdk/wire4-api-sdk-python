# wire4_client.EmpresasCoDiApi

All URIs are relative to *https://sandbox-api.wire4.mx/wire4/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**obtain_companies**](EmpresasCoDiApi.md#obtain_companies) | **GET** /codi/companies | Consulta de empresas CODI®
[**register_company_using_post**](EmpresasCoDiApi.md#register_company_using_post) | **POST** /codi/companies | Registro de empresas CODI®

# **obtain_companies**
> list[CompanyRegistered] obtain_companies(authorization)

Consulta de empresas CODI®

Consulta de empresas CODI® registradas para la aplicación.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.EmpresasCoDiApi()
authorization = 'authorization_example' # str | Header para token

try:
    # Consulta de empresas CODI®
    api_response = api_instance.obtain_companies(authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmpresasCoDiApi->obtain_companies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Header para token | 

### Return type

[**list[CompanyRegistered]**](CompanyRegistered.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_company_using_post**
> CompanyRegistered register_company_using_post(body, authorization)

Registro de empresas CODI®

Registra una empresa para hacer uso de operaciones CODI®.<br><br> <b>Nota:<b> Es requerido tener el certificado emitido por BANXICO® asi como el Nombre de la empresa, Nombre comercial y el Registro Federal de Contribuyentes (RFC) de la empresa.<br/>

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.EmpresasCoDiApi()
body = wire4_client.CompanyRequested() # CompanyRequested | Información de la cuenta del beneficiario
authorization = 'authorization_example' # str | Header para token

try:
    # Registro de empresas CODI®
    api_response = api_instance.register_company_using_post(body, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmpresasCoDiApi->register_company_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CompanyRequested**](CompanyRequested.md)| Información de la cuenta del beneficiario | 
 **authorization** | **str**| Header para token | 

### Return type

[**CompanyRegistered**](CompanyRegistered.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

