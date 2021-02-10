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


class SalesPointFound(object):
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
        'access_ip': 'str',
        'account': 'str',
        'created_at': 'datetime',
        'name': 'str',
        'public_id': 'str',
        'status': 'str',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'access_ip': 'access_ip',
        'account': 'account',
        'created_at': 'created_at',
        'name': 'name',
        'public_id': 'public_id',
        'status': 'status',
        'updated_at': 'updated_at'
    }

    def __init__(self, access_ip=None, account=None, created_at=None, name=None, public_id=None, status=None, updated_at=None):  # noqa: E501
        """SalesPointFound - a model defined in Swagger"""  # noqa: E501
        self._access_ip = None
        self._account = None
        self._created_at = None
        self._name = None
        self._public_id = None
        self._status = None
        self._updated_at = None
        self.discriminator = None
        if access_ip is not None:
            self.access_ip = access_ip
        if account is not None:
            self.account = account
        if created_at is not None:
            self.created_at = created_at
        if name is not None:
            self.name = name
        if public_id is not None:
            self.public_id = public_id
        if status is not None:
            self.status = status
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def access_ip(self):
        """Gets the access_ip of this SalesPointFound.  # noqa: E501

        Es la dirección IP desde la que accede el punto de venta a wire4 y a la que se devuelven las notificaciones.  # noqa: E501

        :return: The access_ip of this SalesPointFound.  # noqa: E501
        :rtype: str
        """
        return self._access_ip

    @access_ip.setter
    def access_ip(self, access_ip):
        """Sets the access_ip of this SalesPointFound.

        Es la dirección IP desde la que accede el punto de venta a wire4 y a la que se devuelven las notificaciones.  # noqa: E501

        :param access_ip: The access_ip of this SalesPointFound.  # noqa: E501
        :type: str
        """

        self._access_ip = access_ip

    @property
    def account(self):
        """Gets the account of this SalesPointFound.  # noqa: E501

        Es la cuenta registra para el punto de venta.  # noqa: E501

        :return: The account of this SalesPointFound.  # noqa: E501
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this SalesPointFound.

        Es la cuenta registra para el punto de venta.  # noqa: E501

        :param account: The account of this SalesPointFound.  # noqa: E501
        :type: str
        """

        self._account = account

    @property
    def created_at(self):
        """Gets the created_at of this SalesPointFound.  # noqa: E501

        Es la fecha en la que se creó el punto de venta. Ésta fecha viene en formato ISO 8601 con zona horaria, ejemplo: <strong>2020-10-27T11:03:15.000-06:00</strong>.  # noqa: E501

        :return: The created_at of this SalesPointFound.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SalesPointFound.

        Es la fecha en la que se creó el punto de venta. Ésta fecha viene en formato ISO 8601 con zona horaria, ejemplo: <strong>2020-10-27T11:03:15.000-06:00</strong>.  # noqa: E501

        :param created_at: The created_at of this SalesPointFound.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def name(self):
        """Gets the name of this SalesPointFound.  # noqa: E501

        Es el nombre del punto de venta.  # noqa: E501

        :return: The name of this SalesPointFound.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SalesPointFound.

        Es el nombre del punto de venta.  # noqa: E501

        :param name: The name of this SalesPointFound.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def public_id(self):
        """Gets the public_id of this SalesPointFound.  # noqa: E501

        Es el identificador del punto de venta.  # noqa: E501

        :return: The public_id of this SalesPointFound.  # noqa: E501
        :rtype: str
        """
        return self._public_id

    @public_id.setter
    def public_id(self, public_id):
        """Sets the public_id of this SalesPointFound.

        Es el identificador del punto de venta.  # noqa: E501

        :param public_id: The public_id of this SalesPointFound.  # noqa: E501
        :type: str
        """

        self._public_id = public_id

    @property
    def status(self):
        """Gets the status of this SalesPointFound.  # noqa: E501

        Es el estado (estatus) del punto de venta. Puede ser \"ACTIVE\" o \"INACTIVO\".  # noqa: E501

        :return: The status of this SalesPointFound.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SalesPointFound.

        Es el estado (estatus) del punto de venta. Puede ser \"ACTIVE\" o \"INACTIVO\".  # noqa: E501

        :param status: The status of this SalesPointFound.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def updated_at(self):
        """Gets the updated_at of this SalesPointFound.  # noqa: E501

        Es la fecha en la que se actualizó el punto de venta. Ésta fecha viene en formato ISO 8601 con zona horaria, ejemplo: <strong>2020-10-27T11:03:15.000-06:00</strong>.  # noqa: E501

        :return: The updated_at of this SalesPointFound.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this SalesPointFound.

        Es la fecha en la que se actualizó el punto de venta. Ésta fecha viene en formato ISO 8601 con zona horaria, ejemplo: <strong>2020-10-27T11:03:15.000-06:00</strong>.  # noqa: E501

        :param updated_at: The updated_at of this SalesPointFound.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if issubclass(SalesPointFound, dict):
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
        if not isinstance(other, SalesPointFound):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
