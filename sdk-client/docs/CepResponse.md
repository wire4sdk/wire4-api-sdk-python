# CepResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_beneficiary** | **str** | Es la cuenta del beneficiario. | [optional] 
**account_sender** | **str** | Es la cuenta del ordenante. | [optional] 
**amount** | **float** | Es el monto de la transferencia. | [optional] 
**available** | **bool** | Indica si el CEP se encuentra disponible o no. | [optional] 
**beneficiary_bank_key** | **str** | Es la clave del banco beneficiario el cual se puede obtener del recurso de las &lt;a href&#x3D;\&quot;#operation/getAllInstitutionsUsingGET\&quot;&gt;instituciones.&lt;/a&gt; | [optional] 
**beneficiary_name** | **str** | Nombre del beneficiario. | [optional] 
**beneficiary_rfc** | **str** | Es el Registro Federal de Contribuyentes (RFC) del beneficiario. | [optional] 
**cadena_original** | **str** | Cadena original del CEP. | [optional] 
**capture_date** | **datetime** | Es la fecha de captura de la transferencia. Ésta fecha viene en formato ISO 8601 con zona horaria, ejemplo: &lt;strong&gt;2020-10-27T11:03:15.000-06:00&lt;/strong&gt;. | [optional] 
**certificate_serial_number** | **str** | Número de serie del certificado. | [optional] 
**clave_rastreo** | **str** | Es la clave de rastreo. | [optional] 
**description** | **str** | Es la descripción de la transferencia. | [optional] 
**iva** | **float** | IVA de la transferencia. | [optional] 
**operation_date** | **datetime** | Es la fecha de operación de la transferencia. Ésta fecha viene en formato ISO 8601 con zona horaria, ejemplo: &lt;strong&gt;2020-10-27T11:03:15.000-06:00&lt;/strong&gt;. | [optional] 
**operation_date_cep** | **datetime** | Es la fecha de abono registrada en el CEP.  Ésta fecha viene en formato ISO 8601 con zona horaria, ejemplo: &lt;strong&gt;2020-10-27T11:03:15.000-06:00&lt;/strong&gt;. | [optional] 
**reference** | **str** | Es la referencia numérica de la transferencia. | [optional] 
**sender_bank_key** | **str** | Es la clave del banco emisor el cual se puede obtener del recurso de las &lt;a href&#x3D;\&quot;#operation/getAllInstitutionsUsingGET\&quot;&gt;instituciones.&lt;/a&gt; | [optional] 
**sender_name** | **str** | Es el nombre del emisor. | [optional] 
**sender_rfc** | **str** | Es el Registro Federal de Contribuyentes (RFC) del emisor. | [optional] 
**signature** | **str** | Firma del CEP.. | [optional] 
**type** | **str** | Es el tiop de CEP, puede ser: &lt;strong&gt;SPEI&lt;/strong&gt; o &lt;strong&gt;SPID&lt;/strong&gt;. | [optional] 
**url_zip** | **str** | La url al archivo zip del CEP, el cual contiene el xml y pdf | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

