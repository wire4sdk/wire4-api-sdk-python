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
from wire4_client.models.spid_classification_dto import SpidClassificationDTO  # noqa: F401,E501


class SpidClassificationsResponseDTO(object):
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
        'classifications': 'list[SpidClassificationDTO]'
    }

    attribute_map = {
        'classifications': 'classifications'
    }

    def __init__(self, classifications=None):  # noqa: E501
        """SpidClassificationsResponseDTO - a model defined in Swagger"""  # noqa: E501
        self._classifications = None
        self.discriminator = None
        if classifications is not None:
            self.classifications = classifications

    @property
    def classifications(self):
        """Gets the classifications of this SpidClassificationsResponseDTO.  # noqa: E501

        Lista de clasificaciones para operaciones con dólares (SPID)  # noqa: E501

        :return: The classifications of this SpidClassificationsResponseDTO.  # noqa: E501
        :rtype: list[SpidClassificationDTO]
        """
        return self._classifications

    @classifications.setter
    def classifications(self, classifications):
        """Sets the classifications of this SpidClassificationsResponseDTO.

        Lista de clasificaciones para operaciones con dólares (SPID)  # noqa: E501

        :param classifications: The classifications of this SpidClassificationsResponseDTO.  # noqa: E501
        :type: list[SpidClassificationDTO]
        """

        self._classifications = classifications

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
        if issubclass(SpidClassificationsResponseDTO, dict):
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
        if not isinstance(other, SpidClassificationsResponseDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
