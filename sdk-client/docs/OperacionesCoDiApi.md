# wire4_client.OperacionesCoDiApi

All URIs are relative to *https://sandbox-api.wire4.mx/wire4/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**consult_codi_operations**](OperacionesCoDiApi.md#consult_codi_operations) | **POST** /codi/charges | Consulta de operaciones

# **consult_codi_operations**
> PagerResponseDto consult_codi_operations(authorization, body=body, company_id=company_id, page=page, sales_point_id=sales_point_id, size=size)

Consulta de operaciones

Obtiene las operaciones generadas a partir de peticiones de pago CODI® de forma paginada, pudiendo aplicar filtros.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.OperacionesCoDiApi()
authorization = 'authorization_example' # str | Header para token
body = wire4_client.CodiOperationsFiltersRequestDTO() # CodiOperationsFiltersRequestDTO | Filtros de busqueda (optional)
company_id = 'company_id_example' # str | Es el identificador de empresa CODI®. (optional)
page = 'page_example' # str | Es el número de pago. (optional)
sales_point_id = 'sales_point_id_example' # str | Es el identificador del punto de venta. (optional)
size = 'size_example' # str | Es el tamaño de página. (optional)

try:
    # Consulta de operaciones
    api_response = api_instance.consult_codi_operations(authorization, body=body, company_id=company_id, page=page, sales_point_id=sales_point_id, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperacionesCoDiApi->consult_codi_operations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Header para token | 
 **body** | [**CodiOperationsFiltersRequestDTO**](CodiOperationsFiltersRequestDTO.md)| Filtros de busqueda | [optional] 
 **company_id** | **str**| Es el identificador de empresa CODI®. | [optional] 
 **page** | **str**| Es el número de pago. | [optional] 
 **sales_point_id** | **str**| Es el identificador del punto de venta. | [optional] 
 **size** | **str**| Es el tamaño de página. | [optional] 

### Return type

[**PagerResponseDto**](PagerResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

