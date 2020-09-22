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


class CodiOperationResponseDTO(object):
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
        'amount': 'float',
        'concept': 'str',
        'id': 'str',
        'operation_date': 'datetime',
        'payment_type': 'str',
        'status': 'str',
        'transaction_id': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'concept': 'concept',
        'id': 'id',
        'operation_date': 'operation_date',
        'payment_type': 'payment_type',
        'status': 'status',
        'transaction_id': 'transaction_id'
    }

    def __init__(self, amount=None, concept=None, id=None, operation_date=None, payment_type=None, status=None, transaction_id=None):  # noqa: E501
        """CodiOperationResponseDTO - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._concept = None
        self._id = None
        self._operation_date = None
        self._payment_type = None
        self._status = None
        self._transaction_id = None
        self.discriminator = None
        if amount is not None:
            self.amount = amount
        if concept is not None:
            self.concept = concept
        if id is not None:
            self.id = id
        if operation_date is not None:
            self.operation_date = operation_date
        if payment_type is not None:
            self.payment_type = payment_type
        if status is not None:
            self.status = status
        if transaction_id is not None:
            self.transaction_id = transaction_id

    @property
    def amount(self):
        """Gets the amount of this CodiOperationResponseDTO.  # noqa: E501

        Monto de la operacion.  # noqa: E501

        :return: The amount of this CodiOperationResponseDTO.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CodiOperationResponseDTO.

        Monto de la operacion.  # noqa: E501

        :param amount: The amount of this CodiOperationResponseDTO.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def concept(self):
        """Gets the concept of this CodiOperationResponseDTO.  # noqa: E501

        Concepto del pago.  # noqa: E501

        :return: The concept of this CodiOperationResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._concept

    @concept.setter
    def concept(self, concept):
        """Sets the concept of this CodiOperationResponseDTO.

        Concepto del pago.  # noqa: E501

        :param concept: The concept of this CodiOperationResponseDTO.  # noqa: E501
        :type: str
        """

        self._concept = concept

    @property
    def id(self):
        """Gets the id of this CodiOperationResponseDTO.  # noqa: E501

        Identificador de la operacion.  # noqa: E501

        :return: The id of this CodiOperationResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CodiOperationResponseDTO.

        Identificador de la operacion.  # noqa: E501

        :param id: The id of this CodiOperationResponseDTO.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def operation_date(self):
        """Gets the operation_date of this CodiOperationResponseDTO.  # noqa: E501

        Fecha de la operacion.  # noqa: E501

        :return: The operation_date of this CodiOperationResponseDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._operation_date

    @operation_date.setter
    def operation_date(self, operation_date):
        """Sets the operation_date of this CodiOperationResponseDTO.

        Fecha de la operacion.  # noqa: E501

        :param operation_date: The operation_date of this CodiOperationResponseDTO.  # noqa: E501
        :type: datetime
        """

        self._operation_date = operation_date

    @property
    def payment_type(self):
        """Gets the payment_type of this CodiOperationResponseDTO.  # noqa: E501

        Tipo de pago.  # noqa: E501

        :return: The payment_type of this CodiOperationResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._payment_type

    @payment_type.setter
    def payment_type(self, payment_type):
        """Sets the payment_type of this CodiOperationResponseDTO.

        Tipo de pago.  # noqa: E501

        :param payment_type: The payment_type of this CodiOperationResponseDTO.  # noqa: E501
        :type: str
        """

        self._payment_type = payment_type

    @property
    def status(self):
        """Gets the status of this CodiOperationResponseDTO.  # noqa: E501

        Estatus.  # noqa: E501

        :return: The status of this CodiOperationResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CodiOperationResponseDTO.

        Estatus.  # noqa: E501

        :param status: The status of this CodiOperationResponseDTO.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def transaction_id(self):
        """Gets the transaction_id of this CodiOperationResponseDTO.  # noqa: E501

        Identificador de la transacción.  # noqa: E501

        :return: The transaction_id of this CodiOperationResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this CodiOperationResponseDTO.

        Identificador de la transacción.  # noqa: E501

        :param transaction_id: The transaction_id of this CodiOperationResponseDTO.  # noqa: E501
        :type: str
        """

        self._transaction_id = transaction_id

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
        if issubclass(CodiOperationResponseDTO, dict):
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
        if not isinstance(other, CodiOperationResponseDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
