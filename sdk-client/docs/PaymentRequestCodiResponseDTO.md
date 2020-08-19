# PaymentRequestCodiResponseDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Monto del pago. | [optional] 
**barcode_base64** | **str** | Imagen QR en formato Base64 para el CODI®. | [optional] 
**barcode_url** | **str** | URL de la imagen QR para el CODI®. | [optional] 
**concept** | **str** | Concepto de pago. | [optional] 
**creation_date** | **datetime** | Fecha de creación. | [optional] 
**due_date** | **datetime** | Fecha de vencimiento. | [optional] 
**id** | **str** | Identificador de la operacion. | [optional] 
**operation_date** | **datetime** | Fecha de la operacion. | [optional] 
**operations** | [**list[PaymentRequestCodiResponseDTO]**](PaymentRequestCodiResponseDTO.md) | Listado de pagos realizados sobre la petición. | [optional] 
**order_id** | **str** | OrderId asignada a la solicitud. | [optional] 
**payment_type** | **str** | Tipo de pago. | [optional] 
**phone_number** | **str** | Numero de teléfono. | [optional] 
**status** | **str** | Estatus de la orden de pago. | [optional] 
**transaction_id** | **str** | Identificador de la transacción. | [optional] 
**type** | **str** | Tipo de petición. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

