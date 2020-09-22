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
from api.suscripciones_api import SuscripcionesApi  # noqa: E501
from wire4_client.rest import ApiException


class TestSuscripcionesApi(unittest.TestCase):
    """SuscripcionesApi unit test stubs"""

    def setUp(self):
        self.api = api.suscripciones_api.SuscripcionesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_pre_enrollment_monex_user_using_post(self):
        """Test case for pre_enrollment_monex_user_using_post

        Registra una pre-suscripción  # noqa: E501
        """
        pass

    def test_remove_enrollment_user_using_delete(self):
        """Test case for remove_enrollment_user_using_delete

        Elimina una suscripción por el identificador de la suscripción  # noqa: E501
        """
        pass

    def test_remove_subscription_pending_status_using_delete(self):
        """Test case for remove_subscription_pending_status_using_delete

        Elimina una pre-suscripción  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
