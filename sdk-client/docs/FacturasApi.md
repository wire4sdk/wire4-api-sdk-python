# wire4_client.FacturasApi

All URIs are relative to *https://sandbox-api.wire4.mx/wire4/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billings_report_by_id_using_get**](FacturasApi.md#billings_report_by_id_using_get) | **GET** /billings/{id} | Consulta de facturas por identificador
[**billings_report_using_get**](FacturasApi.md#billings_report_using_get) | **GET** /billings | Consulta de facturas

# **billings_report_by_id_using_get**
> Billing billings_report_by_id_using_get(authorization, id)

Consulta de facturas por identificador

Consulta las facturas emitidas por conceptos de uso de la plataforma y operaciones realizadas tanto de entrada como de salida. Se debe especificar el identificador de la factura

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.FacturasApi()
authorization = 'authorization_example' # str | Header para token
id = 'id_example' # str | Identificador de la factura

try:
    # Consulta de facturas por identificador
    api_response = api_instance.billings_report_by_id_using_get(authorization, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FacturasApi->billings_report_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Header para token | 
 **id** | **str**| Identificador de la factura | 

### Return type

[**Billing**](Billing.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **billings_report_using_get**
> list[Billing] billings_report_using_get(authorization, period=period)

Consulta de facturas

Consulta las facturas emitidas por conceptos de uso de la plataforma y operaciones realizadas tanto de entrada como de salida. Es posible filtrar por periodo de fecha yyyy-MM, por ejemplo 2019-11

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.FacturasApi()
authorization = 'authorization_example' # str | Header para token
period = 'period_example' # str | Filtro de fecha yyyy-MM (optional)

try:
    # Consulta de facturas
    api_response = api_instance.billings_report_using_get(authorization, period=period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FacturasApi->billings_report_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Header para token | 
 **period** | **str**| Filtro de fecha yyyy-MM | [optional] 

### Return type

[**list[Billing]**](Billing.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

