# coding: utf-8

"""
    Wire4RestAPI

    Referencia de la API de Wire4  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from wire4_client.api_client import ApiClient


class FacturasApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def billings_report_by_id_using_get(self, authorization, id, **kwargs):  # noqa: E501
        """Consulta de facturas por identificador  # noqa: E501

        Consulta las facturas emitidas por conceptos de uso de la plataforma y operaciones realizadas tanto de entrada como de salida. Se debe especificar el identificador de la factura  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.billings_report_by_id_using_get(authorization, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Header para token (required)
        :param str id: Identificador de la factura (required)
        :return: Billing
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.billings_report_by_id_using_get_with_http_info(authorization, id, **kwargs)  # noqa: E501
        else:
            (data) = self.billings_report_by_id_using_get_with_http_info(authorization, id, **kwargs)  # noqa: E501
            return data

    def billings_report_by_id_using_get_with_http_info(self, authorization, id, **kwargs):  # noqa: E501
        """Consulta de facturas por identificador  # noqa: E501

        Consulta las facturas emitidas por conceptos de uso de la plataforma y operaciones realizadas tanto de entrada como de salida. Se debe especificar el identificador de la factura  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.billings_report_by_id_using_get_with_http_info(authorization, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Header para token (required)
        :param str id: Identificador de la factura (required)
        :return: Billing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method billings_report_by_id_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `billings_report_by_id_using_get`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `billings_report_by_id_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/billings/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Billing',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def billings_report_using_get(self, authorization, **kwargs):  # noqa: E501
        """Consulta de facturas  # noqa: E501

        Consulta las facturas emitidas por conceptos de uso de la plataforma y operaciones realizadas tanto de entrada como de salida. Es posible filtrar por periodo de fecha yyyy-MM, por ejemplo 2019-11  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.billings_report_using_get(authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Header para token (required)
        :param str period: Filtro de fecha yyyy-MM
        :return: list[Billing]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.billings_report_using_get_with_http_info(authorization, **kwargs)  # noqa: E501
        else:
            (data) = self.billings_report_using_get_with_http_info(authorization, **kwargs)  # noqa: E501
            return data

    def billings_report_using_get_with_http_info(self, authorization, **kwargs):  # noqa: E501
        """Consulta de facturas  # noqa: E501

        Consulta las facturas emitidas por conceptos de uso de la plataforma y operaciones realizadas tanto de entrada como de salida. Es posible filtrar por periodo de fecha yyyy-MM, por ejemplo 2019-11  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.billings_report_using_get_with_http_info(authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Header para token (required)
        :param str period: Filtro de fecha yyyy-MM
        :return: list[Billing]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'period']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method billings_report_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `billings_report_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'period' in params:
            query_params.append(('period', params['period']))  # noqa: E501

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/billings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Billing]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
