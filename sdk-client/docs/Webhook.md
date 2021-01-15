# Webhook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | **list[str]** | Tipo de evento manejado por el webhook. Para más referencia sobre los tipos de eventos soportados, revise la siguiente liga: &lt;a href&#x3D;\&quot;#section/Eventos\&quot;&gt;https://developers.wire4.mx/#section/Eventos.&lt;/a&gt; | [optional] 
**name** | **str** | Es el nombre del webhook. | [optional] 
**secret** | **str** | Es la llave con la que se debe de identificar que el webhook fue enviado por Wire4. Para mayor información revisar la guía de notificaciones en la sección de &lt;a href&#x3D;\&quot;https://wire4.mx/#/guides/notificaciones\&quot;&gt;\&quot;Comprobación de firmas de Webhook\&quot;.&lt;/a&gt; | [optional] 
**status** | **str** | Estado (estatus) en el que se encuentra el webhook. | [optional] 
**url** | **str** | Es la dirección URL a la que Wire4 enviará las notificaciones cuando un evento ocurra. | [optional] 
**wh_id** | **str** | Es el identificador del webhook. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

