# AccountReassigned

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_limit** | **float** | Monto límite permitido registrado para la cuenta | 
**bank** | [**Institution**](Institution.md) |  | [optional] 
**beneficiary_account** | **str** | Cuenta del beneficiario, podría ser teléfono celular, TDD o cuenta CLABE | 
**currency_code** | **str** | Código de moneda, este dato es opcional, al registrar una cuenta si no se cuenta con este valor se asignara MXP | [optional] 
**email** | **list[str]** | Lista de email&#x27;s, este dato es opcional | [optional] 
**institution** | [**BeneficiaryInstitution**](BeneficiaryInstitution.md) |  | [optional] 
**kind_of_relationship** | **str** | Tipo de relación con el propietario de la cuenta, para registrar una cuenta este valor se debe obtener  del recurso relationships. &lt;br&gt; Nota: Si en la respuesta de Monex esta propiedad es nula, tampoco estará presente en esta respuesta. | 
**numeric_reference_spei** | **str** | Referencia numérica a utilizar cuando se realice una transferencia y no se especifique una referencia | [optional] 
**payment_concept_spei** | **str** | Concepto de pago a utilizar cuando se realice una transferencia y no se especifique un concepto | [optional] 
**person** | [**Person**](Person.md) |  | [optional] 
**register_date** | **datetime** | La fecha en la que se registro el beneficiario | [optional] 
**relationship** | **str** | Relación con el propietario de la cuenta, para registrar una cuenta este valor se debe obtener  del recurso relationships. &lt;br&gt; Nota: Si en la respuesta de Monex esta propiedad es nula, tampoco estará presente en esta respuesta. | 
**rfc** | **str** | Registro federal de contribuyentes de la persona o institución propietaria de la cuenta. &lt;br&gt; Nota: Si en la respuesta de Monex esta propiedad es nula, tampoco estará presente en esta respuesta. | 
**status** | **str** | El estado (status) en el que se encuentra el registro del beneficiario | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

