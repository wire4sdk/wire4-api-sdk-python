# coding: utf-8

"""
    Wire4RestAPI

    Referencia de API. La API de Wire4 está organizada en torno a REST  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import wire4_client
from api.facturas_api import FacturasApi  # noqa: E501
from wire4_client.rest import ApiException


class TestFacturasApi(unittest.TestCase):
    """FacturasApi unit test stubs"""

    def setUp(self):
        self.api = api.facturas_api.FacturasApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_billings_report_by_id_using_get(self):
        """Test case for billings_report_by_id_using_get

        Consulta de facturas por identificador  # noqa: E501
        """
        pass

    def test_billings_report_using_get(self):
        """Test case for billings_report_using_get

        Consulta de facturas  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
