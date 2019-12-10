# Account

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_limit** | **float** | Monto límite permitido registrado para la cuenta | 
**bank_key** | **str** | Clave del banco, es requerido en caso de que la cuenta del beneficiario sea un número de celular | [optional] 
**beneficiary_account** | **str** | Cuenta del beneficiario, podría ser teléfono celular, TDD o cuenta CLABE | 
**email** | **list[str]** | Lista de email&#x27;s, este dato es opcional | [optional] 
**institution** | [**BeneficiaryInstitution**](BeneficiaryInstitution.md) |  | [optional] 
**kind_of_relationship** | **str** | Tipo de relación con el propietario de la cuenta, para registrar una cuenta este valor se debe obtener  del recurso relationships | 
**numeric_reference_spei** | **str** | Referencia numérica a utilizar cuando se realice una transferencia y no se especifique una referencia | [optional] 
**payment_concept_spei** | **str** | Concepto de pago a utilizar cuando se realice una transferencia y no se especifique un concepto | [optional] 
**person** | [**Person**](Person.md) |  | [optional] 
**relationship** | **str** | Relación con el propietario de la cuenta, para registrar una cuenta este valor se debe obtener  del recurso relationships | 
**rfc** | **str** | Registro federal de contribuyentes de la persona o institución propietaria de la cuenta | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

