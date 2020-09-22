# wire4_client.PuntosDeVentaCoDiApi

All URIs are relative to *https://sandbox-api.wire4.mx/wire4/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sales_point**](PuntosDeVentaCoDiApi.md#create_sales_point) | **POST** /codi/companies/salespoint | Registra un punto de venta asociado a una empresa
[**obtain_sale_points**](PuntosDeVentaCoDiApi.md#obtain_sale_points) | **GET** /codi/companies/salespoint | Obtiene los puntos de venta asociados a una empresa

# **create_sales_point**
> SalesPointRespose create_sales_point(body, authorization, company_id)

Registra un punto de venta asociado a una empresa

Registra un punto de venta desde donde se emitaran los cobros CODI®, el punto de venta se debe asociar a un cuenta cableregistrada previamente ante Banxico para realizar cobros con CODI®

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.PuntosDeVentaCoDiApi()
body = wire4_client.SalesPointRequest() # SalesPointRequest | Información del punto de venta CODI®
authorization = 'authorization_example' # str | Header para token
company_id = 'company_id_example' # str | El identificador de la empresa

try:
    # Registra un punto de venta asociado a una empresa
    api_response = api_instance.create_sales_point(body, authorization, company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PuntosDeVentaCoDiApi->create_sales_point: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SalesPointRequest**](SalesPointRequest.md)| Información del punto de venta CODI® | 
 **authorization** | **str**| Header para token | 
 **company_id** | **str**| El identificador de la empresa | 

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

Obtiene los puntos de venta asociados a una empresa

Obtiene los puntos de venta asociados a una empresa en las cuales se hacen operaciones CODI®

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
company_id = 'company_id_example' # str | El identificador de la empresa

try:
    # Obtiene los puntos de venta asociados a una empresa
    api_response = api_instance.obtain_sale_points(authorization, company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PuntosDeVentaCoDiApi->obtain_sale_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Header para token | 
 **company_id** | **str**| El identificador de la empresa | 

### Return type

[**list[SalesPointFound]**](SalesPointFound.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

