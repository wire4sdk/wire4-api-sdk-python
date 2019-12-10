# wire4_client.ComprobanteElectrnicoDePagoCEPApi

All URIs are relative to *https://sandbox-api.wire4.mx/wire4/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**obtain_transaction_cep_using_post**](ComprobanteElectrnicoDePagoCEPApi.md#obtain_transaction_cep_using_post) | **POST** /ceps | Consulta de CEP

# **obtain_transaction_cep_using_post**
> CepResponse obtain_transaction_cep_using_post(body)

Consulta de CEP

Consulta el CEP de un pago realizado a través del SPEI, si es que este se encuentra disponible en BANXICO.

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
api_instance = wire4_client.ComprobanteElectrnicoDePagoCEPApi(wire4_client.ApiClient(configuration))
body = wire4_client.CepSearchBanxico() # CepSearchBanxico | Información para buscar un CEP

try:
    # Consulta de CEP
    api_response = api_instance.obtain_transaction_cep_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComprobanteElectrnicoDePagoCEPApi->obtain_transaction_cep_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CepSearchBanxico**](CepSearchBanxico.md)| Información para buscar un CEP | 

### Return type

[**CepResponse**](CepResponse.md)

### Authorization

[wire4_aut_app](../README.md#wire4_aut_app)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

