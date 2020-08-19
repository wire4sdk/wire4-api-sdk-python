# wire4_client.OperacionesCoDiApi

All URIs are relative to *https://sandbox-api.wire4.mx/wire4/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**consult_codi_operations**](OperacionesCoDiApi.md#consult_codi_operations) | **POST** /codi/charges | Obtiene las operaciones generadas a partir de peticiones de pago CoDi® de forma paginada, pudiendo aplicar filtros

# **consult_codi_operations**
> PagerResponseDto consult_codi_operations(authorization, body=body, company_id=company_id, page=page, sales_point_id=sales_point_id, size=size)

Obtiene las operaciones generadas a partir de peticiones de pago CoDi® de forma paginada, pudiendo aplicar filtros

Obtiene las operaciones generadas a partir de peticiones de pago CoDi® de forma paginada, pudiendo aplicar filtros

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
company_id = 'company_id_example' # str | Identificador de empresa CoDi (optional)
page = 'page_example' # str | Número de pago (optional)
sales_point_id = 'sales_point_id_example' # str | Identificador del punto de venta (optional)
size = 'size_example' # str | Tamaño de pagina (optional)

try:
    # Obtiene las operaciones generadas a partir de peticiones de pago CoDi® de forma paginada, pudiendo aplicar filtros
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
 **company_id** | **str**| Identificador de empresa CoDi | [optional] 
 **page** | **str**| Número de pago | [optional] 
 **sales_point_id** | **str**| Identificador del punto de venta | [optional] 
 **size** | **str**| Tamaño de pagina | [optional] 

### Return type

[**PagerResponseDto**](PagerResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

