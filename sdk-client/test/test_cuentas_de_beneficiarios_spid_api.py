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
from api.cuentas_de_beneficiarios_spid_api import CuentasDeBeneficiariosSPIDApi  # noqa: E501
from wire4_client.rest import ApiException


class TestCuentasDeBeneficiariosSPIDApi(unittest.TestCase):
    """CuentasDeBeneficiariosSPIDApi unit test stubs"""

    def setUp(self):
        self.api = api.cuentas_de_beneficiarios_spid_api.CuentasDeBeneficiariosSPIDApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_spid_beneficiaries_for_account(self):
        """Test case for get_spid_beneficiaries_for_account

        Consulta los beneficiarios SPID registrados  # noqa: E501
        """
        pass

    def test_pre_register_accounts_using_post1(self):
        """Test case for pre_register_accounts_using_post1

        Pre-registro de cuentas de beneficiarios SPID®  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
