# MessagePayment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | Cuenta del ordenante | [optional] 
**amount** | **float** | Monto de la transferencia | [optional] 
**beneficiary_account** | **str** | Cuenta del beneficiario | [optional] 
**beneficiary_bank** | [**MessageInstitution**](MessageInstitution.md) |  | [optional] 
**beneficiary_name** | **str** | Nombre del beneficiario | [optional] 
**cep** | [**MessageCEP**](MessageCEP.md) |  | [optional] 
**clave_rastreo** | **str** | Clave de rastreo de la transferencia | [optional] 
**concept** | **str** | Concepto de la transferencia de salida | [optional] 
**confirm_date** | **datetime** | Fecha de confirmación de la transferencia de salida | [optional] 
**currency_code** | **str** | Código de la moneda de la transferencia de salida | [optional] 
**detention_message** | **str** | Mensaje de detención de Monex de la transferencia de salida | [optional] 
**error_message** | **str** | Mensaje de error | [optional] 
**monex_description** | **str** | La descripción de Monex de la transferencia de salida | [optional] 
**order_id** | **str** | El identificador de la transferencia de salida | [optional] 
**payment_order_id** | **int** | El identificador de la orden de pago de Monex de la transferencia de salida | [optional] 
**pending_reason** | **str** | Razón de porque está pendiente aún cuando se autorizó la transferencia | [optional] 
**reference** | **int** | Referecia de la transferencia | [optional] 
**request_id** | **str** | El identificador, en esta API, de la petición de envío de la transferencia de salida | [optional] 
**status_code** | **str** | El estado de la transferencia de salida | [optional] 
**transaction_id** | **int** | El identificador de Monex de la transferencia de salida | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

