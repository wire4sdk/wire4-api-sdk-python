# wire4_client.CuentasDeBeneficiariosSPEIApi

All URIs are relative to *https://sandbox-api.wire4.mx/wire4/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_account_using_delete**](CuentasDeBeneficiariosSPEIApi.md#delete_account_using_delete) | **DELETE** /subscriptions/{subscription}/beneficiaries/spei/{account} | Elimina la cuenta del beneficiario
[**get_available_relationships_monex_using_get**](CuentasDeBeneficiariosSPEIApi.md#get_available_relationships_monex_using_get) | **GET** /subscriptions/{subscription}/beneficiaries/relationships | Consulta de relaciones
[**get_beneficiaries_for_account_using_get**](CuentasDeBeneficiariosSPEIApi.md#get_beneficiaries_for_account_using_get) | **GET** /subscriptions/{subscription}/beneficiaries/spei | Consulta los beneficiarios registrados
[**pre_register_accounts_using_post**](CuentasDeBeneficiariosSPEIApi.md#pre_register_accounts_using_post) | **POST** /subscriptions/{subscription}/beneficiaries/spei | Pre-registro de cuentas de beneficiarios.
[**remove_beneficiaries_pending_using_delete**](CuentasDeBeneficiariosSPEIApi.md#remove_beneficiaries_pending_using_delete) | **DELETE** /subscriptions/{subscription}/beneficiaries/spei/request/{requestId} | Eliminación de beneficiarios SPEI® sin confirmar
[**update_amount_limit_account_using_put**](CuentasDeBeneficiariosSPEIApi.md#update_amount_limit_account_using_put) | **PUT** /subscriptions/{subscription}/beneficiaries/spei/{account} | Actualiza el monto límite

# **delete_account_using_delete**
> delete_account_using_delete(authorization, account, subscription)

Elimina la cuenta del beneficiario

Borra la cuenta de beneficiario proporcionada relacionada al contrato perteneciente a la subscripción. La cuenta a borrar debe ser una cuenta que opere con SPEI.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.CuentasDeBeneficiariosSPEIApi()
authorization = 'authorization_example' # str | Header para token
account = 'account_example' # str | La cuenta del beneciario que será eliminada
subscription = 'subscription_example' # str | El identificador de la suscripción a esta API

try:
    # Elimina la cuenta del beneficiario
    api_instance.delete_account_using_delete(authorization, account, subscription)
except ApiException as e:
    print("Exception when calling CuentasDeBeneficiariosSPEIApi->delete_account_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Header para token | 
 **account** | **str**| La cuenta del beneciario que será eliminada | 
 **subscription** | **str**| El identificador de la suscripción a esta API | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_relationships_monex_using_get**
> RelationshipsResponse get_available_relationships_monex_using_get(authorization, subscription)

Consulta de relaciones

Obtiene las posibles relaciones existentes para registrar beneficiarios en Monex. Se debe invocar este recurso antes de pre-registrar una cuenta de beneficiario.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.CuentasDeBeneficiariosSPEIApi()
authorization = 'authorization_example' # str | Header para token
subscription = 'subscription_example' # str | Identificador de la suscripción a esta API

try:
    # Consulta de relaciones
    api_response = api_instance.get_available_relationships_monex_using_get(authorization, subscription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CuentasDeBeneficiariosSPEIApi->get_available_relationships_monex_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Header para token | 
 **subscription** | **str**| Identificador de la suscripción a esta API | 

### Return type

[**RelationshipsResponse**](RelationshipsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_beneficiaries_for_account_using_get**
> BeneficiariesResponse get_beneficiaries_for_account_using_get(authorization, subscription, account=account, rfc=rfc)

Consulta los beneficiarios registrados

Obtiene los beneficiarios registrados al contrato relacionado con la suscripción, Los beneficiarios son los que actualmente se encuentran registrados en banca Monex.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.CuentasDeBeneficiariosSPEIApi()
authorization = 'authorization_example' # str | Header para token
subscription = 'subscription_example' # str | El identificador de la suscripción a esta API
account = 'account_example' # str | Cuenta del beneficiario, puede ser Clabe, TDD o Celular (optional)
rfc = 'rfc_example' # str | RFC del beneficiario (optional)

try:
    # Consulta los beneficiarios registrados
    api_response = api_instance.get_beneficiaries_for_account_using_get(authorization, subscription, account=account, rfc=rfc)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CuentasDeBeneficiariosSPEIApi->get_beneficiaries_for_account_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Header para token | 
 **subscription** | **str**| El identificador de la suscripción a esta API | 
 **account** | **str**| Cuenta del beneficiario, puede ser Clabe, TDD o Celular | [optional] 
 **rfc** | **str**| RFC del beneficiario | [optional] 

### Return type

[**BeneficiariesResponse**](BeneficiariesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pre_register_accounts_using_post**
> TokenRequiredResponse pre_register_accounts_using_post(body, authorization, subscription)

Pre-registro de cuentas de beneficiarios.

Pre-registra una o más cuentas de beneficiario en la plataforma, proporcionando una URL donde el cuentahabiente Monex debe ingresar un valor de su llave digital para confirmar el alta de las cuentas de beneficiarios.<br/>Los posibles valores de <i>relationship</i> y <i>kind_of_relationship</i> se deben  obtener de /subscriptions/{subscription}/beneficiaries/relationships.<br/><br/>La confirmación de registro en Monex se realiza a través de una llamada a los webhooks registrados con el evento ACCOUNT.CREATED.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.CuentasDeBeneficiariosSPEIApi()
body = wire4_client.AccountRequest() # AccountRequest | Información de la cuenta del beneficiario
authorization = 'authorization_example' # str | Header para token
subscription = 'subscription_example' # str | El identificador de la suscripción a esta API

try:
    # Pre-registro de cuentas de beneficiarios.
    api_response = api_instance.pre_register_accounts_using_post(body, authorization, subscription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CuentasDeBeneficiariosSPEIApi->pre_register_accounts_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountRequest**](AccountRequest.md)| Información de la cuenta del beneficiario | 
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

# **remove_beneficiaries_pending_using_delete**
> remove_beneficiaries_pending_using_delete(authorization, request_id, subscription)

Eliminación de beneficiarios SPEI® sin confirmar

Elimina un conjunto de beneficiarios a registrar en la cuenta del cliente Monex relacionada a la suscripción, los beneficiarios no deben haber sido confirmados por el cliente.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.CuentasDeBeneficiariosSPEIApi()
authorization = 'authorization_example' # str | Header para token
request_id = 'request_id_example' # str | Identificador de los beneficiarios a eliminar
subscription = 'subscription_example' # str | El identificador de la suscripción a esta API

try:
    # Eliminación de beneficiarios SPEI® sin confirmar
    api_instance.remove_beneficiaries_pending_using_delete(authorization, request_id, subscription)
except ApiException as e:
    print("Exception when calling CuentasDeBeneficiariosSPEIApi->remove_beneficiaries_pending_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Header para token | 
 **request_id** | **str**| Identificador de los beneficiarios a eliminar | 
 **subscription** | **str**| El identificador de la suscripción a esta API | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_amount_limit_account_using_put**
> update_amount_limit_account_using_put(body, authorization, account, subscription)

Actualiza el monto límite

Actualiza el monto límite a la cuenta de beneficiario proporcionada relacionada al contrato perteneciente a la subscripción.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.CuentasDeBeneficiariosSPEIApi()
body = wire4_client.AmountRequest() # AmountRequest | Información de la cuenta y el monto límite a actualizar
authorization = 'authorization_example' # str | Header para token
account = 'account_example' # str | Cuenta a actualizar
subscription = 'subscription_example' # str | El identificador de la suscripción a esta API

try:
    # Actualiza el monto límite
    api_instance.update_amount_limit_account_using_put(body, authorization, account, subscription)
except ApiException as e:
    print("Exception when calling CuentasDeBeneficiariosSPEIApi->update_amount_limit_account_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AmountRequest**](AmountRequest.md)| Información de la cuenta y el monto límite a actualizar | 
 **authorization** | **str**| Header para token | 
 **account** | **str**| Cuenta a actualizar | 
 **subscription** | **str**| El identificador de la suscripción a esta API | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

