# WebhookResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | **list[str]** | Tipos de eventos de los cuales Wire4 te enviará información. | [optional] 
**name** | **str** | Nombre del webhook. | [optional] 
**secret** | **str** | Llave con la cual se debe de identificar que el webhook fue enviado por Wire4, para mayor información revisar la guía de notificaciones (https://wire4.mx/#/guides/notificaciones), en la sección de  \&quot;Comprobación de firmas de Webhook\&quot;. | [optional] 
**status** | **str** | Estatus en el que se encuentra el webhook | [optional] 
**url** | **str** | URL a la cual Wire4 enviará las notificaciones cuando un evento ocurra. | [optional] 
**wh_uuid** | **str** | Identificador del webhook. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

