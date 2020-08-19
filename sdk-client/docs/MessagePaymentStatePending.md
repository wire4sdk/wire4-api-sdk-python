# MessagePaymentStatePending

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | Cuenta del ordenante | [optional] 
**amount** | **float** | Monto de la transferencia | [optional] 
**beneficiary_account** | **str** | Cuenta del beneficiario | [optional] 
**beneficiary_bank** | [**MessageInstitution**](MessageInstitution.md) |  | [optional] 
**beneficiary_name** | **str** | Nombre del beneficiario | [optional] 
**concept** | **str** | Concepto de la transferencia de salida | [optional] 
**currency_code** | **str** | Código de la moneda de la transferencia de salida | [optional] 
**detention_message** | **str** | Mensaje de detención de Monex, indica la causa por la cuál esta detenida la operación en Monex | [optional] 
**error_message** | **str** | Mensaje de error | [optional] 
**order_id** | **str** | El identificador de la transferencia de salida | [optional] 
**payment_order_id** | **int** | El identificador de la orden de pago de Monex de la transferencia de salida | [optional] 
**pending_reason** | **str** | Estatus que identifica la causa por la que la transferencia esta en pendiente, los posibles estatus son: FI&#x3D;Fondos Insuficientes | FM&#x3D;Firma mancomunada, en espera de ingreso de segundo token de autorización | DP&#x3D;Se detecto una transferencia duplicada que esta en espera de confirmación o de eliminación | [optional] 
**reference** | **int** | Referecia de la transferencia | [optional] 
**request_id** | **str** | El identificador, en esta API, de la petición de envío de la transferencia de salida | [optional] 
**status_code** | **str** | El estado de la transferencia de salida, deberá ser PENDING | [optional] 
**transaction_id** | **int** | El identificador de Monex de la transferencia de salida, podría no estar presente por lo que Usted debería hacer referencias mediate el paymentOrderID | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

