# wire4_client.CuentasDeBeneficiariosSPEIApi

All URIs are relative to *https://sandbox-api.wire4.mx/wire4/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorize_accounts_pending_put**](CuentasDeBeneficiariosSPEIApi.md#authorize_accounts_pending_put) | **PUT** /subscriptions/{subscription}/beneficiaries/pending | Solicitud para agrupar cuentas de beneficiarios SPEI/SPID en estado pendiente.
[**delete_account_using_delete**](CuentasDeBeneficiariosSPEIApi.md#delete_account_using_delete) | **DELETE** /subscriptions/{subscription}/beneficiaries/spei/{account} | Elimina la cuenta del beneficiario
[**get_available_relationships_monex_using_get**](CuentasDeBeneficiariosSPEIApi.md#get_available_relationships_monex_using_get) | **GET** /subscriptions/{subscription}/beneficiaries/relationships | Consulta de relaciones
[**get_beneficiaries_by_request_id**](CuentasDeBeneficiariosSPEIApi.md#get_beneficiaries_by_request_id) | **GET** /subscriptions/{subscription}/beneficiaries/spei/{requestId} | Consulta los beneficiarios por el identificador de la petición de registro
[**get_beneficiaries_for_account_using_get**](CuentasDeBeneficiariosSPEIApi.md#get_beneficiaries_for_account_using_get) | **GET** /subscriptions/{subscription}/beneficiaries/spei | Consulta los beneficiarios registrados
[**pre_register_accounts_using_post**](CuentasDeBeneficiariosSPEIApi.md#pre_register_accounts_using_post) | **POST** /subscriptions/{subscription}/beneficiaries/spei | Pre-registro de cuentas de beneficiarios SPEI®.
[**remove_beneficiaries_pending_using_delete**](CuentasDeBeneficiariosSPEIApi.md#remove_beneficiaries_pending_using_delete) | **DELETE** /subscriptions/{subscription}/beneficiaries/spei/request/{requestId} | Eliminación de beneficiarios SPEI® sin confirmar
[**update_amount_limit_account_using_put**](CuentasDeBeneficiariosSPEIApi.md#update_amount_limit_account_using_put) | **PUT** /subscriptions/{subscription}/beneficiaries/spei/{account} | Solicitud para actualizar el monto límite de una cuenta

# **authorize_accounts_pending_put**
> AuthorizedBeneficiariesResponse authorize_accounts_pending_put(body, authorization, subscription)

Solicitud para agrupar cuentas de beneficiarios SPEI/SPID en estado pendiente.

Solicta la agrupación de las cuentas de beneficiarios en estado pendiente para que sean autorizadas,  para ello se crea un conjunto de éstas que puede incluir tanto de SPEI como de SPID. Además se debe indicar las urls de redirección en caso de error y éxito

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.CuentasDeBeneficiariosSPEIApi()
body = wire4_client.UrlsRedirect() # UrlsRedirect | Información de la cuenta del beneficiario
authorization = 'authorization_example' # str | Header para token
subscription = 'subscription_example' # str | Es el identificador de la suscripción a esta API.

try:
    # Solicitud para agrupar cuentas de beneficiarios SPEI/SPID en estado pendiente.
    api_response = api_instance.authorize_accounts_pending_put(body, authorization, subscription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CuentasDeBeneficiariosSPEIApi->authorize_accounts_pending_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UrlsRedirect**](UrlsRedirect.md)| Información de la cuenta del beneficiario | 
 **authorization** | **str**| Header para token | 
 **subscription** | **str**| Es el identificador de la suscripción a esta API. | 

### Return type

[**AuthorizedBeneficiariesResponse**](AuthorizedBeneficiariesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account_using_delete**
> delete_account_using_delete(authorization, account, subscription)

Elimina la cuenta del beneficiario

Elimina la cuenta de beneficiario proporcionada relacionada al contrato perteneciente a la suscripción. La cuenta a borrar debe ser una que opere con SPEI.

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
account = 'account_example' # str | Es la cuenta del beneficiario que será eliminada.
subscription = 'subscription_example' # str | Es el identificador de la suscripción a esta API.

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
 **account** | **str**| Es la cuenta del beneficiario que será eliminada. | 
 **subscription** | **str**| Es el identificador de la suscripción a esta API. | 

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
subscription = 'subscription_example' # str | Es el identificador de la suscripción a esta API.

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
 **subscription** | **str**| Es el identificador de la suscripción a esta API. | 

### Return type

[**RelationshipsResponse**](RelationshipsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_beneficiaries_by_request_id**
> BeneficiariesResponse get_beneficiaries_by_request_id(authorization, request_id, subscription)

Consulta los beneficiarios por el identificador de la petición de registro

Obtiene los beneficiarios enviados para registro en una petición al contrato relacionado con la suscripción, Los beneficiarios son los que actualmente se encuentran registrados en banca Monex, que pertenezcan a la petición que se solicita.

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
request_id = 'request_id_example' # str | El identificador de la petición del registro de beneficiarios a esta API.
subscription = 'subscription_example' # str | Es el identificador de la suscripción a esta API.

try:
    # Consulta los beneficiarios por el identificador de la petición de registro
    api_response = api_instance.get_beneficiaries_by_request_id(authorization, request_id, subscription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CuentasDeBeneficiariosSPEIApi->get_beneficiaries_by_request_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Header para token | 
 **request_id** | **str**| El identificador de la petición del registro de beneficiarios a esta API. | 
 **subscription** | **str**| Es el identificador de la suscripción a esta API. | 

### Return type

[**BeneficiariesResponse**](BeneficiariesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_beneficiaries_for_account_using_get**
> BeneficiariesResponse get_beneficiaries_for_account_using_get(authorization, subscription, account=account, beneficiary_bank=beneficiary_bank, beneficiary_name=beneficiary_name, end_date=end_date, init_date=init_date, page=page, rfc=rfc, size=size, status=status)

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
subscription = 'subscription_example' # str | Es el identificador de la suscripción a esta API.
account = 'account_example' # str | Es la cuenta del beneficiario, podría ser teléfono celular (es de 10 dígitos), Tarjeta de débito (TDD, es de 16 dígitos) o cuenta CLABE (es de 18 dígitos). <br/><br/>Por ejemplo Teléfono celular: 5525072600, TDD: 4323 1234 5678 9123, CLABE: 032180000118359719. (optional)
beneficiary_bank = 'beneficiary_bank_example' # str | Es la clave del banco beneficiario. Se puede obtener del recurso de las <a href=\"#operation/getAllInstitutionsUsingGET\">instituciones.</a> (optional)
beneficiary_name = 'beneficiary_name_example' # str | Es el nombre del beneficiario. (optional)
end_date = 'end_date_example' # str | Es la fecha de inicio del perido a filtrar en formato dd-mm-yyyy. (optional)
init_date = 'init_date_example' # str | Es la fºecha de inicio del perido a filtrar en formato dd-mm-yyyy. (optional)
page = '0' # str | Es el número de página. (optional) (default to 0)
rfc = 'rfc_example' # str | Es el Registro Federal de Controbuyentes (RFC) del beneficiario. (optional)
size = '20' # str | Es el tamaño de página. (optional) (default to 20)
status = 'status_example' # str | Es el estado (estatus) de la cuenta. Los valores pueden ser <b>PENDING</b> y <b>REGISTERED</b>. (optional)

try:
    # Consulta los beneficiarios registrados
    api_response = api_instance.get_beneficiaries_for_account_using_get(authorization, subscription, account=account, beneficiary_bank=beneficiary_bank, beneficiary_name=beneficiary_name, end_date=end_date, init_date=init_date, page=page, rfc=rfc, size=size, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CuentasDeBeneficiariosSPEIApi->get_beneficiaries_for_account_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Header para token | 
 **subscription** | **str**| Es el identificador de la suscripción a esta API. | 
 **account** | **str**| Es la cuenta del beneficiario, podría ser teléfono celular (es de 10 dígitos), Tarjeta de débito (TDD, es de 16 dígitos) o cuenta CLABE (es de 18 dígitos). &lt;br/&gt;&lt;br/&gt;Por ejemplo Teléfono celular: 5525072600, TDD: 4323 1234 5678 9123, CLABE: 032180000118359719. | [optional] 
 **beneficiary_bank** | **str**| Es la clave del banco beneficiario. Se puede obtener del recurso de las &lt;a href&#x3D;\&quot;#operation/getAllInstitutionsUsingGET\&quot;&gt;instituciones.&lt;/a&gt; | [optional] 
 **beneficiary_name** | **str**| Es el nombre del beneficiario. | [optional] 
 **end_date** | **str**| Es la fecha de inicio del perido a filtrar en formato dd-mm-yyyy. | [optional] 
 **init_date** | **str**| Es la fºecha de inicio del perido a filtrar en formato dd-mm-yyyy. | [optional] 
 **page** | **str**| Es el número de página. | [optional] [default to 0]
 **rfc** | **str**| Es el Registro Federal de Controbuyentes (RFC) del beneficiario. | [optional] 
 **size** | **str**| Es el tamaño de página. | [optional] [default to 20]
 **status** | **str**| Es el estado (estatus) de la cuenta. Los valores pueden ser &lt;b&gt;PENDING&lt;/b&gt; y &lt;b&gt;REGISTERED&lt;/b&gt;. | [optional] 

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

Pre-registro de cuentas de beneficiarios SPEI®.

Pre-registra una o más cuentas de beneficiario en la plataforma de Wire4, ésta le proporcionará una URL donde lo llevará al centro de autorización para que el cuentahabiente Monex ingrese su llave digital para confirmar el alta de las cuentas de beneficiarios.<br/> Los posibles valores de <em>relationship</em> y <em>kind_of_relationship</em> se deben  obtener de <a href=\"#operation/getAvailableRelationshipsMonexUsingGET\">/subscriptions/{subscription}/beneficiaries/relationships.</a><br/><br/>La confirmación de registro en Monex se realizará a través de una notificación a los webhooks registrados con el evento de tipo <a href=\"#section/Eventos/Tipos-de-Eventos\">ACCOUNT.CREATED.</a>

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
subscription = 'subscription_example' # str | Es el identificador de la suscripción a esta API.

try:
    # Pre-registro de cuentas de beneficiarios SPEI®.
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
 **subscription** | **str**| Es el identificador de la suscripción a esta API. | 

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

Elimina uno o más beneficiarios que se encuentran en estado pendiente de confirmar (autorizar) de la cuenta del cliente Monex relacionada a la suscripción.

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
request_id = 'request_id_example' # str | Es el identificador con el que se dió de alta a los beneficiarios (viene en el cuerpo de la respuesta del <a href=\"#operation/getAvailableRelationshipsMonexUsingGET\">pre-registro de beneficiarios</a>), los registros bajo éste campo van a ser eliminados.
subscription = 'subscription_example' # str | Es el identificador de la suscripción a esta API.

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
 **request_id** | **str**| Es el identificador con el que se dió de alta a los beneficiarios (viene en el cuerpo de la respuesta del &lt;a href&#x3D;\&quot;#operation/getAvailableRelationshipsMonexUsingGET\&quot;&gt;pre-registro de beneficiarios&lt;/a&gt;), los registros bajo éste campo van a ser eliminados. | 
 **subscription** | **str**| Es el identificador de la suscripción a esta API. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_amount_limit_account_using_put**
> TokenRequiredResponse update_amount_limit_account_using_put(body, authorization, account, subscription)

Solicitud para actualizar el monto límite de una cuenta

Se crea una solicitud para actualizar el monto límite a la cuenta de beneficiario proporcionada y relacionada al contrato perteneciente a la subscripción. Una vez enviada la solicitud se retornará una URl que lo llevará al centro de autorización para que el cuentahabiente Monex ingrese su llave digital para confirmar la actualización del monto límite. 

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.CuentasDeBeneficiariosSPEIApi()
body = wire4_client.AmountRequest() # AmountRequest | Información de la cuenta y el monto límite a actualizar.
authorization = 'authorization_example' # str | Header para token
account = 'account_example' # str | Es la cuenta que va a ser actualizada.
subscription = 'subscription_example' # str | Es el identificador de la suscripción a esta API.

try:
    # Solicitud para actualizar el monto límite de una cuenta
    api_response = api_instance.update_amount_limit_account_using_put(body, authorization, account, subscription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CuentasDeBeneficiariosSPEIApi->update_amount_limit_account_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AmountRequest**](AmountRequest.md)| Información de la cuenta y el monto límite a actualizar. | 
 **authorization** | **str**| Header para token | 
 **account** | **str**| Es la cuenta que va a ser actualizada. | 
 **subscription** | **str**| Es el identificador de la suscripción a esta API. | 

### Return type

[**TokenRequiredResponse**](TokenRequiredResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

