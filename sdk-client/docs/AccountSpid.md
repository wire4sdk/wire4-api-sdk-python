# AccountSpid

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_limit** | **float** | Monto límite permitido para la cuenta | 
**bank_code_banxico** | **str** | Código banxico con una longitud de 5 dígitos, es requerido en caso de que la cuenta del beneficiario sea un número de celular | [optional] 
**beneficiary_account** | **str** | Cuenta del beneficiario debe ser una cuenta CLABE | 
**cancel_return_url** | **str** | Url a la que se redirigira en caso no exitoso | [optional] 
**email** | **list[str]** | Lista de email&#x27;s, este dato es opcional | [optional] 
**institution** | [**BeneficiaryInstitution**](BeneficiaryInstitution.md) |  | 
**kind_of_relationship** | **str** | Tipo de relación de la cuentaobtained of endpoint relationships | 
**numeric_reference** | **str** | Referencia numérica | [optional] 
**payment_concept** | **str** | Concepto de pago | [optional] 
**relationship** | **str** | Código de relación de la cuenta, este valor debe ser igual a un valor obtenido del endpoint relationship | 
**return_url** | **str** | Url a la que se redireccionara en caso exitoso | [optional] 
**rfc** | **str** | Registro federal de contribuyentes | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

