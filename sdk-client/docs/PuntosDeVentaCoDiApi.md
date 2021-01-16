# wire4_client.PuntosDeVentaCoDiApi

All URIs are relative to *https://sandbox-api.wire4.mx/wire4/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sales_point**](PuntosDeVentaCoDiApi.md#create_sales_point) | **POST** /codi/companies/salespoint | Registro de punto de venta.
[**obtain_sale_points**](PuntosDeVentaCoDiApi.md#obtain_sale_points) | **GET** /codi/companies/salespoint | Consulta de puntos de venta

# **create_sales_point**
> SalesPointRespose create_sales_point(body, authorization, company_id)

Registro de punto de venta.

Se registra un punto de venta (TPV) desde donde se emitarán los cobros CODI®. El punto de venta se debe asociar a un cuenta CLABE registrada previamente ante Banxico para realizar cobros con CODI®.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.PuntosDeVentaCoDiApi()
body = wire4_client.SalesPointRequest() # SalesPointRequest | Es el objeto que contiene información del punto de venta CODI®.
authorization = 'authorization_example' # str | Header para token
company_id = 'company_id_example' # str | Es el identificador de la empresa.

try:
    # Registro de punto de venta.
    api_response = api_instance.create_sales_point(body, authorization, company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PuntosDeVentaCoDiApi->create_sales_point: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SalesPointRequest**](SalesPointRequest.md)| Es el objeto que contiene información del punto de venta CODI®. | 
 **authorization** | **str**| Header para token | 
 **company_id** | **str**| Es el identificador de la empresa. | 

### Return type

[**SalesPointRespose**](SalesPointRespose.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **obtain_sale_points**
> list[SalesPointFound] obtain_sale_points(authorization, company_id)

Consulta de puntos de venta

Obtiene los puntos de venta asociados a una empresa en las cuales se hacen operaciones CODI®.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.PuntosDeVentaCoDiApi()
authorization = 'authorization_example' # str | Header para token
company_id = 'company_id_example' # str | Es el identificador de la empresa. Ejemplo: 8838d513-5916-4662-bb30-2448f0f543ed

try:
    # Consulta de puntos de venta
    api_response = api_instance.obtain_sale_points(authorization, company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PuntosDeVentaCoDiApi->obtain_sale_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Header para token | 
 **company_id** | **str**| Es el identificador de la empresa. Ejemplo: 8838d513-5916-4662-bb30-2448f0f543ed | 

### Return type

[**list[SalesPointFound]**](SalesPointFound.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

