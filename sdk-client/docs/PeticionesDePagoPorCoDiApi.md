# wire4_client.PeticionesDePagoPorCoDiApi

All URIs are relative to *https://sandbox-api.wire4.mx/wire4/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**consult_codi_request_by_order_id**](PeticionesDePagoPorCoDiApi.md#consult_codi_request_by_order_id) | **GET** /codi/sales-point/charges | Consulta información de petición por orderId
[**generate_codi_code_qr**](PeticionesDePagoPorCoDiApi.md#generate_codi_code_qr) | **POST** /codi/sales-point/charges | Genera código QR

# **consult_codi_request_by_order_id**
> PaymentRequestCodiResponseDTO consult_codi_request_by_order_id(authorization, order_id, sales_point_id)

Consulta información de petición por orderId

Obtiene la información de una petición de pago CODI® por orderId para un punto de venta.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.PeticionesDePagoPorCoDiApi()
authorization = 'authorization_example' # str | Header para token
order_id = 'order_id_example' # str | Identificador del pago CODI®
sales_point_id = 'sales_point_id_example' # str | Identificador del punto de venta

try:
    # Consulta información de petición por orderId
    api_response = api_instance.consult_codi_request_by_order_id(authorization, order_id, sales_point_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeticionesDePagoPorCoDiApi->consult_codi_request_by_order_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Header para token | 
 **order_id** | **str**| Identificador del pago CODI® | 
 **sales_point_id** | **str**| Identificador del punto de venta | 

### Return type

[**PaymentRequestCodiResponseDTO**](PaymentRequestCodiResponseDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_codi_code_qr**
> CodiCodeQrResponseDTO generate_codi_code_qr(body, authorization, sales_point_id)

Genera código QR

Genera un código QR solicitado por un punto de venta para un pago mediante CODI®

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.PeticionesDePagoPorCoDiApi()
body = wire4_client.CodiCodeRequestDTO() # CodiCodeRequestDTO | Información del pago CODI®
authorization = 'authorization_example' # str | Header para token
sales_point_id = 'sales_point_id_example' # str | Identificador del punto de venta

try:
    # Genera código QR
    api_response = api_instance.generate_codi_code_qr(body, authorization, sales_point_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeticionesDePagoPorCoDiApi->generate_codi_code_qr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CodiCodeRequestDTO**](CodiCodeRequestDTO.md)| Información del pago CODI® | 
 **authorization** | **str**| Header para token | 
 **sales_point_id** | **str**| Identificador del punto de venta | 

### Return type

[**CodiCodeQrResponseDTO**](CodiCodeQrResponseDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

