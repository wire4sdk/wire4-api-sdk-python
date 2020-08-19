# wire4_client.CuentasDeBeneficiariosSPIDApi

All URIs are relative to *https://sandbox-api.wire4.mx/wire4/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_spid_beneficiaries_for_account**](CuentasDeBeneficiariosSPIDApi.md#get_spid_beneficiaries_for_account) | **GET** /subscriptions/{subscription}/beneficiaries/spid | Consulta los beneficiarios SPID registrados
[**pre_register_accounts_using_post1**](CuentasDeBeneficiariosSPIDApi.md#pre_register_accounts_using_post1) | **POST** /subscriptions/{subscription}/beneficiaries/spid | Pre-registro de cuentas de beneficiarios SPID

# **get_spid_beneficiaries_for_account**
> SpidBeneficiariesResponse get_spid_beneficiaries_for_account(authorization, subscription, account=account, beneficiary_bank=beneficiary_bank, beneficiary_name=beneficiary_name, end_date=end_date, init_date=init_date, rfc=rfc, status=status)

Consulta los beneficiarios SPID registrados

Obtiene los beneficiarios SPID registrados al contrato relacionado con la suscripción, Los beneficiarios son los que actualmente se encuentran registrados en banca Monex.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.CuentasDeBeneficiariosSPIDApi()
authorization = 'authorization_example' # str | Header para token
subscription = 'subscription_example' # str | El identificador de la suscripción a esta API
account = 'account_example' # str | Cuenta del beneficiario, puede ser Clabe, TDD o Celular (optional)
beneficiary_bank = 'beneficiary_bank_example' # str | Clave del banco beneficiario (optional)
beneficiary_name = 'beneficiary_name_example' # str | Nombre del beneficiario (optional)
end_date = 'end_date_example' # str | Fecha de inicio del perido a filtrar en formato dd-mm-yyyy (optional)
init_date = 'init_date_example' # str | Fecha de inicio del perido a filtrar en formato dd-mm-yyyy (optional)
rfc = 'rfc_example' # str | RFC del beneficiario (optional)
status = 'status_example' # str | Estatus de la cuenta (optional)

try:
    # Consulta los beneficiarios SPID registrados
    api_response = api_instance.get_spid_beneficiaries_for_account(authorization, subscription, account=account, beneficiary_bank=beneficiary_bank, beneficiary_name=beneficiary_name, end_date=end_date, init_date=init_date, rfc=rfc, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CuentasDeBeneficiariosSPIDApi->get_spid_beneficiaries_for_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Header para token | 
 **subscription** | **str**| El identificador de la suscripción a esta API | 
 **account** | **str**| Cuenta del beneficiario, puede ser Clabe, TDD o Celular | [optional] 
 **beneficiary_bank** | **str**| Clave del banco beneficiario | [optional] 
 **beneficiary_name** | **str**| Nombre del beneficiario | [optional] 
 **end_date** | **str**| Fecha de inicio del perido a filtrar en formato dd-mm-yyyy | [optional] 
 **init_date** | **str**| Fecha de inicio del perido a filtrar en formato dd-mm-yyyy | [optional] 
 **rfc** | **str**| RFC del beneficiario | [optional] 
 **status** | **str**| Estatus de la cuenta | [optional] 

### Return type

[**SpidBeneficiariesResponse**](SpidBeneficiariesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pre_register_accounts_using_post1**
> TokenRequiredResponse pre_register_accounts_using_post1(body, authorization, subscription)

Pre-registro de cuentas de beneficiarios SPID

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.CuentasDeBeneficiariosSPIDApi()
body = wire4_client.AccountSpid() # AccountSpid | Información de la cuenta del beneficiario
authorization = 'authorization_example' # str | Header para token
subscription = 'subscription_example' # str | El identificador de la suscripción a esta API

try:
    # Pre-registro de cuentas de beneficiarios SPID
    api_response = api_instance.pre_register_accounts_using_post1(body, authorization, subscription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CuentasDeBeneficiariosSPIDApi->pre_register_accounts_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountSpid**](AccountSpid.md)| Información de la cuenta del beneficiario | 
 **authorization** | **str**| Header para token | 
 **subscription** | **str**| El identificador de la suscripción a esta API | 

### Return type

[**TokenRequiredResponse**](TokenRequiredResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

