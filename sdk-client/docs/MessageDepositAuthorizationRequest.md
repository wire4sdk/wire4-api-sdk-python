# MessageDepositAuthorizationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Es el monto de la transferencia. | [optional] 
**beneficiary_account** | **str** | Es la cuenta del beneficiario. | [optional] 
**beneficiary_name** | **str** | Es el nombre del beneficiario. | [optional] 
**beneficiary_rfc** | **str** | Es el Registro Federal de Contribuyentes (RFC) del beneficiario. | [optional] 
**clave_rastreo** | **str** | Es la clave de rastreo de la transferencia. | [optional] 
**confirm_date** | **datetime** | Es la Fecha de confirmación de la transferencia. | [optional] 
**currency_code** | **str** | Es el código de divisa de la transferencia. Es en el formato estándar ISO 4217 y es de 3 dígitos. Puede ser \&quot;MXN\&quot; o \&quot;USD\&quot;. | [optional] 
**deposit_date** | **datetime** | Es la fecha de recepción de la transferencia. | [optional] 
**depositant** | **str** | Es el nombre del depositante en caso de que la transferencia se reciba en una cuenta de depositante. | [optional] 
**depositant_alias** | **str** | Es el alias de la cuenta CLABE del depositante en caso que la transferencia se reciba de una cuenta de depositante | [optional] 
**depositant_clabe** | **str** | Es la cuenta CLABE del depositante en caso que la transferencia se reciba en una cuenta de depositante | [optional] 
**depositant_email** | **str** | Es el Correo electrónico (email) del depositante en caso que la transferencia se reciba en una cuenta de depositante | [optional] 
**depositant_rfc** | **str** | Es el Registro Federal de Contribuyentes (RFC) del depositante, en caso que la transferencia se reciba en una cuenta de depositante. | [optional] 
**description** | **str** | Es el concepto de la transferencia. | [optional] 
**monex_description** | **str** | Es la descripción de Monex para la transferencia. | [optional] 
**monex_transaction_id** | **str** | Es el identificador asignado por Monex a la transferencia. | [optional] 
**reference** | **str** | Es la referecia de la transferencia. | [optional] 
**sender_account** | **str** | Es la cuenta del ordenante que podría ser un número celular (10 dígitos), una tarjeta de débito (TDD, de 16 dígitos) o Cuenta CLABE interbancaria (18 dígitos). | [optional] 
**sender_bank** | [**MessageInstitution**](MessageInstitution.md) |  | [optional] 
**sender_name** | **str** | Es el nombre del ordenante. | [optional] 
**sender_rfc** | **str** | Es el Registro Federal de Contribuyente (RFC) del ordenante. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

