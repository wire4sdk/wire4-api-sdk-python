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


class MessageRequestChanged(object):
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
        'request_id': 'str',
        'status': 'str'
    }

    attribute_map = {
        'request_id': 'request_id',
        'status': 'status'
    }

    def __init__(self, request_id=None, status=None):  # noqa: E501
        """MessageRequestChanged - a model defined in Swagger"""  # noqa: E501
        self._request_id = None
        self._status = None
        self.discriminator = None
        if request_id is not None:
            self.request_id = request_id
        if status is not None:
            self.status = status

    @property
    def request_id(self):
        """Gets the request_id of this MessageRequestChanged.  # noqa: E501

        Identificador de la petición realizada a esta API  # noqa: E501

        :return: The request_id of this MessageRequestChanged.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this MessageRequestChanged.

        Identificador de la petición realizada a esta API  # noqa: E501

        :param request_id: The request_id of this MessageRequestChanged.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

    @property
    def status(self):
        """Gets the status of this MessageRequestChanged.  # noqa: E501

        El cambio a informar en la procesamiento/estado de la petición  # noqa: E501

        :return: The status of this MessageRequestChanged.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MessageRequestChanged.

        El cambio a informar en la procesamiento/estado de la petición  # noqa: E501

        :param status: The status of this MessageRequestChanged.  # noqa: E501
        :type: str
        """
        allowed_values = ["AUTHORIZED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if issubclass(MessageRequestChanged, dict):
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
        if not isinstance(other, MessageRequestChanged):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
