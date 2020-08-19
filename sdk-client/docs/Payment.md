# Payment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | Cuenta emisora | [optional] 
**amount** | **float** | Monto de la transferencia | [optional] 
**beneficiary_account** | **str** | Cuenta del beneficiario | [optional] 
**beneficiary_bank** | [**Institution**](Institution.md) |  | [optional] 
**beneficiary_name** | **str** | Nombre del Beneficiario | [optional] 
**cep** | [**MessageCEP**](MessageCEP.md) |  | [optional] 
**clave_rastreo** | **str** | Clave de rastreo de la transferencia | [optional] 
**concept** | **str** | Concepto de pago | [optional] 
**confirm_date** | **datetime** | Fecha de aplicación de la transferencia | [optional] 
**currency_code** | **str** | Código de moneda de la transferencia | [optional] 
**detention_message** | **str** | Mensaje proporcionado por Monex para la transferencia | [optional] 
**error_message** | **str** | Mensaje de error, en caso de algún error se informará aquí | [optional] 
**monex_description** | **str** | Descripción | [optional] 
**order_id** | **str** | Identificador asignado por la aplciación a la transferencia | [optional] 
**payment_order_id** | **int** | Identificador de la orden de pago en Monex | [optional] 
**pending_reason** | **str** | Razón de porque esta pendiente aun cuando se autorizó la transferencia | [optional] 
**reference** | **int** | Referencia numérica | [optional] 
**status_code** | **str** | Estado de la transferencia de la transferencia, los posibles valores son: PENDING, COMPLETED, FAILED, CANCELLED | [optional] 
**transaction_id** | **int** | Identificador de la transferencia asignado por Monex | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

