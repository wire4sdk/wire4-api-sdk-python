# MessageCEP

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_beneficiary** | **str** | Es la cuenta del beneficiario. | [optional] 
**account_sender** | **str** | Es la cuenta que envía la operación. | [optional] 
**amount** | **float** | Es el monto de la operación. | [optional] 
**available** | **bool** | Indica sí el CEP está disponible. | [optional] 
**bank_beneficiary** | **str** | Es la clave del banco beneficiario. | [optional] 
**bank_sender** | **str** | Es la clave del banco que envía la operación. | [optional] 
**beneficiary_name** | **str** | Es el nombre del beneficiario. | [optional] 
**beneficiary_rfc** | **str** | Es el Registro Federal de Contribuyentes (RFC) del beneficiario. | [optional] 
**cadena_original** | **str** | Es la cadena original emitida por el Servicio de Administración Tributaria (SAT). | [optional] 
**capture_date** | **datetime** | Es la fecha de captura. | [optional] 
**certificate_serial_number** | **str** | Es el número de serie emitido por el SAT | [optional] 
**clave_rastreo** | **str** | Es la clave de rastreo de la operación. | [optional] 
**description** | **str** | Es la descripción de la operación. | [optional] 
**iva** | **float** | Es el Impuesto al Valor Agregado (IVA) de la operación. | [optional] 
**operation_date** | **datetime** | Es la fecha en la que se realizó la operación. | [optional] 
**operation_date_cep** | **datetime** | Es la fecha en la que se genera el CEP. | [optional] 
**reference** | **str** | Es la Referencia de la operación | [optional] 
**sender_name** | **str** | Es el nombre de quién envía la operación. | [optional] 
**sender_rfc** | **str** | Es el Registro Federal de Contrinuyentes (RFC) de quién envía la operación. | [optional] 
**signature** | **str** | Firma del CEP | [optional] 
**url_zip** | **str** | Dirección URL de descarga del archivo ZIP que contiene el PDF y XML del CEP proporcionado por BANXICO | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

