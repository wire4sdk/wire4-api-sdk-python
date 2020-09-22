# coding: utf-8

"""
    Wire4RestAPI

    Referencia de la API de Wire4  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class MessageSalesPoint(object):
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
        'account': 'str',
        'ip': 'str',
        'name': 'str'
    }

    attribute_map = {
        'account': 'account',
        'ip': 'ip',
        'name': 'name'
    }

    def __init__(self, account=None, ip=None, name=None):  # noqa: E501
        """MessageSalesPoint - a model defined in Swagger"""  # noqa: E501
        self._account = None
        self._ip = None
        self._name = None
        self.discriminator = None
        if account is not None:
            self.account = account
        if ip is not None:
            self.ip = ip
        if name is not None:
            self.name = name

    @property
    def account(self):
        """Gets the account of this MessageSalesPoint.  # noqa: E501

        Cuenta donde se realziaran los pagos  # noqa: E501

        :return: The account of this MessageSalesPoint.  # noqa: E501
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this MessageSalesPoint.

        Cuenta donde se realziaran los pagos  # noqa: E501

        :param account: The account of this MessageSalesPoint.  # noqa: E501
        :type: str
        """

        self._account = account

    @property
    def ip(self):
        """Gets the ip of this MessageSalesPoint.  # noqa: E501

        Ip desde la cual se accedera al API  # noqa: E501

        :return: The ip of this MessageSalesPoint.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this MessageSalesPoint.

        Ip desde la cual se accedera al API  # noqa: E501

        :param ip: The ip of this MessageSalesPoint.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def name(self):
        """Gets the name of this MessageSalesPoint.  # noqa: E501

        Nombre del punto de venta  # noqa: E501

        :return: The name of this MessageSalesPoint.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MessageSalesPoint.

        Nombre del punto de venta  # noqa: E501

        :param name: The name of this MessageSalesPoint.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(MessageSalesPoint, dict):
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
        if not isinstance(other, MessageSalesPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other