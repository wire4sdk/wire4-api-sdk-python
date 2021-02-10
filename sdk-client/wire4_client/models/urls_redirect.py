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


class UrlsRedirect(object):
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
        'cancel_return_url': 'str',
        'return_url': 'str'
    }

    attribute_map = {
        'cancel_return_url': 'cancel_return_url',
        'return_url': 'return_url'
    }

    def __init__(self, cancel_return_url=None, return_url=None):  # noqa: E501
        """UrlsRedirect - a model defined in Swagger"""  # noqa: E501
        self._cancel_return_url = None
        self._return_url = None
        self.discriminator = None
        self.cancel_return_url = cancel_return_url
        self.return_url = return_url

    @property
    def cancel_return_url(self):
        """Gets the cancel_return_url of this UrlsRedirect.  # noqa: E501

        Es la dirección URL a la que se redirigirá en caso de que el cliente cancele el registro. Se valida hasta 512 caracteres.  # noqa: E501

        :return: The cancel_return_url of this UrlsRedirect.  # noqa: E501
        :rtype: str
        """
        return self._cancel_return_url

    @cancel_return_url.setter
    def cancel_return_url(self, cancel_return_url):
        """Sets the cancel_return_url of this UrlsRedirect.

        Es la dirección URL a la que se redirigirá en caso de que el cliente cancele el registro. Se valida hasta 512 caracteres.  # noqa: E501

        :param cancel_return_url: The cancel_return_url of this UrlsRedirect.  # noqa: E501
        :type: str
        """
        if cancel_return_url is None:
            raise ValueError("Invalid value for `cancel_return_url`, must not be `None`")  # noqa: E501

        self._cancel_return_url = cancel_return_url

    @property
    def return_url(self):
        """Gets the return_url of this UrlsRedirect.  # noqa: E501

        Es la dirección URL a la que se redirigirá en caso exitoso. Se valida hasta 512 caracteres.  # noqa: E501

        :return: The return_url of this UrlsRedirect.  # noqa: E501
        :rtype: str
        """
        return self._return_url

    @return_url.setter
    def return_url(self, return_url):
        """Sets the return_url of this UrlsRedirect.

        Es la dirección URL a la que se redirigirá en caso exitoso. Se valida hasta 512 caracteres.  # noqa: E501

        :param return_url: The return_url of this UrlsRedirect.  # noqa: E501
        :type: str
        """
        if return_url is None:
            raise ValueError("Invalid value for `return_url`, must not be `None`")  # noqa: E501

        self._return_url = return_url

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
        if issubclass(UrlsRedirect, dict):
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
        if not isinstance(other, UrlsRedirect):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
