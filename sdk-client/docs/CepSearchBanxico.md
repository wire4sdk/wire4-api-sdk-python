# CepSearchBanxico

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Monto de la transferencia | 
**beneficiary_account** | **str** | Cuenta de beneficiario | 
**beneficiary_bank_key** | **str** | Clave del banco beneficiario, se puede obtener este valor del listado de institucines &#x27;/institutions&#x27;. Si este valor no esta presente se obtiene de la cuenta del beneficiario, si la cuenta de beneficiario es un número celular este campo es requerido | [optional] 
**clave_rastreo** | **str** | Clave de rastreo de la transferencia | 
**operation_date** | **str** | Fecha de operación de la transferencia, formato: dd-MM-yyyy | 
**reference** | **str** | Referencia numérica de la transferencia | [optional] 
**sender_account** | **str** | Cuenta ordenante, es requerida cuando se no se envía la clave del banco ordenante  | [optional] 
**sender_bank_key** | **str** | Clave del banco ordenante, se puede obtener este valor del listado de institucines &#x27;/institutions&#x27;. Es requerida cuando no se envía la cuenta ordenante | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

