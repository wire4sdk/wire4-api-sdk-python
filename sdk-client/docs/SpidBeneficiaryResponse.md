# SpidBeneficiaryResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_limit** | **float** | Monto límite permitido para la cuenta | 
**bank** | [**Institution**](Institution.md) |  | [optional] 
**beneficiary_account** | **str** | Cuenta del beneficiario debe ser una cuenta CLABE | 
**email** | **list[str]** | Lista de email&#x27;s, este dato es opcional | [optional] 
**institution** | [**BeneficiaryInstitution**](BeneficiaryInstitution.md) |  | 
**kind_of_relationship** | **str** | Tipo de relación de la cuenta, este valor debe ser igual a uno de los obtenidos del recurso de consulta de relationships | 
**numeric_reference_spid** | **str** | Referencia numérica | [optional] 
**payment_concept_spid** | **str** | Concepto de pago | [optional] 
**register_date** | **datetime** | La fecha en la que se registro el beneficiario | [optional] 
**relationship** | **str** | Código de relación de la cuenta, este valor debe ser igual a uno de los obtenidos del recurso de consulta de  relationship | 
**rfc** | **str** | Registro federal de contribuyentes | [optional] 
**status** | **str** | El estado en el que se encuentra el registo del beneficiario | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

