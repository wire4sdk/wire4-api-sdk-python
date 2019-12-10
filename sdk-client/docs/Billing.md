# Billing

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Monto total de la factura | [optional] 
**emission_at** | **datetime** | Fecha y hora en que se emitió de la factura | [optional] 
**end_date** | **datetime** | Fecha en que finaliza el periodo que se factura | [optional] 
**id** | **str** | Identificador de la factura | [optional] 
**start_date** | **datetime** | Fecha de inicio del periodo que se factura | [optional] 
**status** | **str** | Estatus de la factura | [optional] 
**transactions** | [**list[BillingTransaction]**](BillingTransaction.md) |  | [optional] 
**url_pdf** | **str** | Url de la representación impresa en pdf de la factura | [optional] 
**url_xml** | **str** | Url del archivo xml de la factura | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

