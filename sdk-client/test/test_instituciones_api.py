# coding: utf-8

"""
    Wire4RestAPI

    Referencia de la API de Wire4  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import wire4_client
from api.instituciones_api import InstitucionesApi  # noqa: E501
from wire4_client.rest import ApiException


class TestInstitucionesApi(unittest.TestCase):
    """InstitucionesApi unit test stubs"""

    def setUp(self):
        self.api = api.instituciones_api.InstitucionesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_all_institutions_using_get(self):
        """Test case for get_all_institutions_using_get

        Consulta de instituciones bancarias  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
