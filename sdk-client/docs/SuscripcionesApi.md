# wire4_client.SuscripcionesApi

All URIs are relative to *https://sandbox-api.wire4.mx/wire4/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pre_enrollment_monex_user_using_post**](SuscripcionesApi.md#pre_enrollment_monex_user_using_post) | **POST** /subscriptions/pre-subscription | registra una pre-suscripción
[**remove_enrollment_user_using_delete**](SuscripcionesApi.md#remove_enrollment_user_using_delete) | **DELETE** /subscriptions/{subscription} | Elimna una suscripción por id
[**remove_subscription_pending_status_using_delete**](SuscripcionesApi.md#remove_subscription_pending_status_using_delete) | **DELETE** /subscriptions/pre-subscription/{subscription} | Elimna una pre-suscripción

# **pre_enrollment_monex_user_using_post**
> PreEnrollmentResponse pre_enrollment_monex_user_using_post(body, authorization)

registra una pre-suscripción

Pre-registra una suscripción para operar un contrato a través de un aplicación socio de la plataforma, proporcionando una URL donde el cliente Monex debe autorizar el acceso a los datos de su cuenta a el socio.<br/>Una vez que el cuentahabiente autorice el acceso, se envia un webhook con el evento ENROLLMENT.CREATED, el cual contiene los datos de acceso.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.SuscripcionesApi()
body = wire4_client.PreEnrollmentData() # PreEnrollmentData | Información para el enrolamiento
authorization = 'authorization_example' # str | Header para token

try:
    # registra una pre-suscripción
    api_response = api_instance.pre_enrollment_monex_user_using_post(body, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuscripcionesApi->pre_enrollment_monex_user_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PreEnrollmentData**](PreEnrollmentData.md)| Información para el enrolamiento | 
 **authorization** | **str**| Header para token | 

### Return type

[**PreEnrollmentResponse**](PreEnrollmentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_enrollment_user_using_delete**
> remove_enrollment_user_using_delete(authorization, subscription)

Elimna una suscripción por id

Elimina una suscripción, una ves eliminada la suscripcion ya no se podran realizar operacions en el API uilizando esta suscripción

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.SuscripcionesApi()
authorization = 'authorization_example' # str | Header para token
subscription = 'subscription_example' # str | El identificador de la suscripción a esta API

try:
    # Elimna una suscripción por id
    api_instance.remove_enrollment_user_using_delete(authorization, subscription)
except ApiException as e:
    print("Exception when calling SuscripcionesApi->remove_enrollment_user_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Header para token | 
 **subscription** | **str**| El identificador de la suscripción a esta API | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_subscription_pending_status_using_delete**
> remove_subscription_pending_status_using_delete(authorization, subscription)

Elimna una pre-suscripción

Se elimina una pre-suscripción, sólo se elimina en caso de que cliente monex no haya concedio su autorización de acceso, es decir que la pre-suscripcion este pendiente.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.SuscripcionesApi()
authorization = 'authorization_example' # str | Header para token
subscription = 'subscription_example' # str | El identificador de la suscripción a esta API

try:
    # Elimna una pre-suscripción
    api_instance.remove_subscription_pending_status_using_delete(authorization, subscription)
except ApiException as e:
    print("Exception when calling SuscripcionesApi->remove_subscription_pending_status_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Header para token | 
 **subscription** | **str**| El identificador de la suscripción a esta API | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

