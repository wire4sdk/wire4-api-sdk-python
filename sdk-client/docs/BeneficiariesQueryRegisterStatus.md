# BeneficiariesQueryRegisterStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_date** | **datetime** | Fecha en que el usuario propietario del token autorizo el registro de beneficiarios | [optional] 
**beneficiaries** | [**list[AccountResponse]**](AccountResponse.md) | Lista de beneficiarios obtenidos | [optional] 
**request_date** | **datetime** | Fecha en que se realizó la petición de registro de beneficiarios | [optional] 
**request_id** | **str** | Identificador de la petición del registro de beneficiarios | [optional] 
**status_request** | **str** | Indica sí la petición ya fue autorizada usando el token del usuario | [optional] 
**total_beneficiaries** | **int** | Total de beneficiarios enviados en la petición | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

