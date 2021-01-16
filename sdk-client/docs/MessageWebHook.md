# MessageWebHook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | Es la versión de esta API. | [optional] 
**created** | **datetime** | Fecha de creación del mensaje. | [optional] 
**data** | **object** | Es el objeto que contiene la información del evento. | [optional] 
**id** | **str** | Es el identificador del mensaje. | [optional] 
**livemode** | **bool** | Indica si proviene de un entorno productivo. | [optional] 
**object** | **str** | Tipo de objeto  que contiene el mensaje en el atributo &#x27;data&#x27;. Los posibles valores son:  &lt;ul&gt;&lt;li&gt;subscription&lt;/li&gt;, &lt;li&gt;beneficiary&lt;/li&gt;, &lt;li&gt;spei_outgoing&lt;/li&gt;, &lt;li&gt;spei_incoming&lt;/li&gt;, &lt;li&gt;spid_outgoing&lt;/li&gt;, &lt;li&gt;request_outgoing&lt;/li&gt;&lt;ul&gt;  | [optional] 
**pending_webhooks** | **int** | Es el número de mensajes pendientes de enviar. | [optional] 
**request** | **str** | Es el identificador del recurso relacionado. | [optional] 
**type** | **str** | El tipo evento que se está enviando en la notificación. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

