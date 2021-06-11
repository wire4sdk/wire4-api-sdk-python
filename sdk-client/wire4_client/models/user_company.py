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


class UserCompany(object):
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
        'emails': 'list[str]',
        'legal_representative': 'bool',
        'masked_name': 'str',
        'masked_user_name': 'str',
        'name': 'str',
        'phone_numbers': 'list[str]',
        'surname_father': 'str',
        'surname_mother': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'emails': 'emails',
        'legal_representative': 'legal_representative',
        'masked_name': 'masked_name',
        'masked_user_name': 'masked_user_name',
        'name': 'name',
        'phone_numbers': 'phone_numbers',
        'surname_father': 'surname_father',
        'surname_mother': 'surname_mother',
        'user_name': 'user_name'
    }

    def __init__(self, emails=None, legal_representative=None, masked_name=None, masked_user_name=None, name=None, phone_numbers=None, surname_father=None, surname_mother=None, user_name=None):  # noqa: E501
        """UserCompany - a model defined in Swagger"""  # noqa: E501
        self._emails = None
        self._legal_representative = None
        self._masked_name = None
        self._masked_user_name = None
        self._name = None
        self._phone_numbers = None
        self._surname_father = None
        self._surname_mother = None
        self._user_name = None
        self.discriminator = None
        if emails is not None:
            self.emails = emails
        if legal_representative is not None:
            self.legal_representative = legal_representative
        if masked_name is not None:
            self.masked_name = masked_name
        if masked_user_name is not None:
            self.masked_user_name = masked_user_name
        if name is not None:
            self.name = name
        if phone_numbers is not None:
            self.phone_numbers = phone_numbers
        if surname_father is not None:
            self.surname_father = surname_father
        if surname_mother is not None:
            self.surname_mother = surname_mother
        if user_name is not None:
            self.user_name = user_name

    @property
    def emails(self):
        """Gets the emails of this UserCompany.  # noqa: E501

        Una lista de los correos del usuario  # noqa: E501

        :return: The emails of this UserCompany.  # noqa: E501
        :rtype: list[str]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """Sets the emails of this UserCompany.

        Una lista de los correos del usuario  # noqa: E501

        :param emails: The emails of this UserCompany.  # noqa: E501
        :type: list[str]
        """

        self._emails = emails

    @property
    def legal_representative(self):
        """Gets the legal_representative of this UserCompany.  # noqa: E501

        Indica sí es representate legal  # noqa: E501

        :return: The legal_representative of this UserCompany.  # noqa: E501
        :rtype: bool
        """
        return self._legal_representative

    @legal_representative.setter
    def legal_representative(self, legal_representative):
        """Sets the legal_representative of this UserCompany.

        Indica sí es representate legal  # noqa: E501

        :param legal_representative: The legal_representative of this UserCompany.  # noqa: E501
        :type: bool
        """

        self._legal_representative = legal_representative

    @property
    def masked_name(self):
        """Gets the masked_name of this UserCompany.  # noqa: E501

        El nombre del usuario enmascarado  # noqa: E501

        :return: The masked_name of this UserCompany.  # noqa: E501
        :rtype: str
        """
        return self._masked_name

    @masked_name.setter
    def masked_name(self, masked_name):
        """Sets the masked_name of this UserCompany.

        El nombre del usuario enmascarado  # noqa: E501

        :param masked_name: The masked_name of this UserCompany.  # noqa: E501
        :type: str
        """

        self._masked_name = masked_name

    @property
    def masked_user_name(self):
        """Gets the masked_user_name of this UserCompany.  # noqa: E501

        El nombre del usuario de acceso enmascarado  # noqa: E501

        :return: The masked_user_name of this UserCompany.  # noqa: E501
        :rtype: str
        """
        return self._masked_user_name

    @masked_user_name.setter
    def masked_user_name(self, masked_user_name):
        """Sets the masked_user_name of this UserCompany.

        El nombre del usuario de acceso enmascarado  # noqa: E501

        :param masked_user_name: The masked_user_name of this UserCompany.  # noqa: E501
        :type: str
        """

        self._masked_user_name = masked_user_name

    @property
    def name(self):
        """Gets the name of this UserCompany.  # noqa: E501

        El nombre del usuario  # noqa: E501

        :return: The name of this UserCompany.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserCompany.

        El nombre del usuario  # noqa: E501

        :param name: The name of this UserCompany.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def phone_numbers(self):
        """Gets the phone_numbers of this UserCompany.  # noqa: E501

        Una lista de los teléfonos del usuario  # noqa: E501

        :return: The phone_numbers of this UserCompany.  # noqa: E501
        :rtype: list[str]
        """
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, phone_numbers):
        """Sets the phone_numbers of this UserCompany.

        Una lista de los teléfonos del usuario  # noqa: E501

        :param phone_numbers: The phone_numbers of this UserCompany.  # noqa: E501
        :type: list[str]
        """

        self._phone_numbers = phone_numbers

    @property
    def surname_father(self):
        """Gets the surname_father of this UserCompany.  # noqa: E501

        El apellido paterno del usuario  # noqa: E501

        :return: The surname_father of this UserCompany.  # noqa: E501
        :rtype: str
        """
        return self._surname_father

    @surname_father.setter
    def surname_father(self, surname_father):
        """Sets the surname_father of this UserCompany.

        El apellido paterno del usuario  # noqa: E501

        :param surname_father: The surname_father of this UserCompany.  # noqa: E501
        :type: str
        """

        self._surname_father = surname_father

    @property
    def surname_mother(self):
        """Gets the surname_mother of this UserCompany.  # noqa: E501

        El apellido materno del usuario  # noqa: E501

        :return: The surname_mother of this UserCompany.  # noqa: E501
        :rtype: str
        """
        return self._surname_mother

    @surname_mother.setter
    def surname_mother(self, surname_mother):
        """Sets the surname_mother of this UserCompany.

        El apellido materno del usuario  # noqa: E501

        :param surname_mother: The surname_mother of this UserCompany.  # noqa: E501
        :type: str
        """

        self._surname_mother = surname_mother

    @property
    def user_name(self):
        """Gets the user_name of this UserCompany.  # noqa: E501

        El nombre del usuario de acceso  # noqa: E501

        :return: The user_name of this UserCompany.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this UserCompany.

        El nombre del usuario de acceso  # noqa: E501

        :param user_name: The user_name of this UserCompany.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

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
        if issubclass(UserCompany, dict):
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
        if not isinstance(other, UserCompany):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
