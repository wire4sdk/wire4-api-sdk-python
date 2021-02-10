# coding: utf-8

"""
    Wire4RestAPI

    Referencia de API. La API de Wire4 está organizada en torno a REST  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from wire4_client.models.urls_redirect import UrlsRedirect  # noqa: F401,E501


class AuthorizationTransactionGroup(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'redirect_urls': 'UrlsRedirect',
        'transactions': 'list[str]'
    }

    attribute_map = {
        'redirect_urls': 'redirect_urls',
        'transactions': 'transactions'
    }

    def __init__(self, redirect_urls=None, transactions=None):  # noqa: E501
        """AuthorizationTransactionGroup - a model defined in Swagger"""  # noqa: E501
        self._redirect_urls = None
        self._transactions = None
        self.discriminator = None
        self.redirect_urls = redirect_urls
        self.transactions = transactions

    @property
    def redirect_urls(self):
        """Gets the redirect_urls of this AuthorizationTransactionGroup.  # noqa: E501


        :return: The redirect_urls of this AuthorizationTransactionGroup.  # noqa: E501
        :rtype: UrlsRedirect
        """
        return self._redirect_urls

    @redirect_urls.setter
    def redirect_urls(self, redirect_urls):
        """Sets the redirect_urls of this AuthorizationTransactionGroup.


        :param redirect_urls: The redirect_urls of this AuthorizationTransactionGroup.  # noqa: E501
        :type: UrlsRedirect
        """
        if redirect_urls is None:
            raise ValueError("Invalid value for `redirect_urls`, must not be `None`")  # noqa: E501

        self._redirect_urls = redirect_urls

    @property
    def transactions(self):
        """Gets the transactions of this AuthorizationTransactionGroup.  # noqa: E501

        Listado de order_id de las transacciones a agrupar.  # noqa: E501

        :return: The transactions of this AuthorizationTransactionGroup.  # noqa: E501
        :rtype: list[str]
        """
        return self._transactions

    @transactions.setter
    def transactions(self, transactions):
        """Sets the transactions of this AuthorizationTransactionGroup.

        Listado de order_id de las transacciones a agrupar.  # noqa: E501

        :param transactions: The transactions of this AuthorizationTransactionGroup.  # noqa: E501
        :type: list[str]
        """
        if transactions is None:
            raise ValueError("Invalid value for `transactions`, must not be `None`")  # noqa: E501

        self._transactions = transactions

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AuthorizationTransactionGroup, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AuthorizationTransactionGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
