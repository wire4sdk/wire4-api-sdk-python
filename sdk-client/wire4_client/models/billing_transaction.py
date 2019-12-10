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
from wire4_client.models.timestamp import Timestamp  # noqa: F401,E501


class BillingTransaction(object):
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
        'clave_rastreo': 'str',
        'monex_id': 'int',
        'operation_date': 'Timestamp',
        'order_id': 'str',
        'payment_order_id': 'str',
        'transaction_id': 'int',
        'type': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'clave_rastreo': 'clave_rastreo',
        'monex_id': 'monex_id',
        'operation_date': 'operation_date',
        'order_id': 'order_id',
        'payment_order_id': 'payment_order_id',
        'transaction_id': 'transaction_id',
        'type': 'type'
    }

    def __init__(self, amount=None, clave_rastreo=None, monex_id=None, operation_date=None, order_id=None, payment_order_id=None, transaction_id=None, type=None):  # noqa: E501
        """BillingTransaction - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._clave_rastreo = None
        self._monex_id = None
        self._operation_date = None
        self._order_id = None
        self._payment_order_id = None
        self._transaction_id = None
        self._type = None
        self.discriminator = None
        if amount is not None:
            self.amount = amount
        if clave_rastreo is not None:
            self.clave_rastreo = clave_rastreo
        if monex_id is not None:
            self.monex_id = monex_id
        if operation_date is not None:
            self.operation_date = operation_date
        if order_id is not None:
            self.order_id = order_id
        if payment_order_id is not None:
            self.payment_order_id = payment_order_id
        if transaction_id is not None:
            self.transaction_id = transaction_id
        if type is not None:
            self.type = type

    @property
    def amount(self):
        """Gets the amount of this BillingTransaction.  # noqa: E501

        Monto de la transacción  # noqa: E501

        :return: The amount of this BillingTransaction.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this BillingTransaction.

        Monto de la transacción  # noqa: E501

        :param amount: The amount of this BillingTransaction.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def clave_rastreo(self):
        """Gets the clave_rastreo of this BillingTransaction.  # noqa: E501

        Clave de rastreo que se asignó a la transacción  # noqa: E501

        :return: The clave_rastreo of this BillingTransaction.  # noqa: E501
        :rtype: str
        """
        return self._clave_rastreo

    @clave_rastreo.setter
    def clave_rastreo(self, clave_rastreo):
        """Sets the clave_rastreo of this BillingTransaction.

        Clave de rastreo que se asignó a la transacción  # noqa: E501

        :param clave_rastreo: The clave_rastreo of this BillingTransaction.  # noqa: E501
        :type: str
        """

        self._clave_rastreo = clave_rastreo

    @property
    def monex_id(self):
        """Gets the monex_id of this BillingTransaction.  # noqa: E501

        Identificador de transaccion en banco monex  # noqa: E501

        :return: The monex_id of this BillingTransaction.  # noqa: E501
        :rtype: int
        """
        return self._monex_id

    @monex_id.setter
    def monex_id(self, monex_id):
        """Sets the monex_id of this BillingTransaction.

        Identificador de transaccion en banco monex  # noqa: E501

        :param monex_id: The monex_id of this BillingTransaction.  # noqa: E501
        :type: int
        """

        self._monex_id = monex_id

    @property
    def operation_date(self):
        """Gets the operation_date of this BillingTransaction.  # noqa: E501


        :return: The operation_date of this BillingTransaction.  # noqa: E501
        :rtype: Timestamp
        """
        return self._operation_date

    @operation_date.setter
    def operation_date(self, operation_date):
        """Sets the operation_date of this BillingTransaction.


        :param operation_date: The operation_date of this BillingTransaction.  # noqa: E501
        :type: Timestamp
        """

        self._operation_date = operation_date

    @property
    def order_id(self):
        """Gets the order_id of this BillingTransaction.  # noqa: E501

        Identificador de la orden  # noqa: E501

        :return: The order_id of this BillingTransaction.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this BillingTransaction.

        Identificador de la orden  # noqa: E501

        :param order_id: The order_id of this BillingTransaction.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def payment_order_id(self):
        """Gets the payment_order_id of this BillingTransaction.  # noqa: E501

        Identificador de la orden de pago  # noqa: E501

        :return: The payment_order_id of this BillingTransaction.  # noqa: E501
        :rtype: str
        """
        return self._payment_order_id

    @payment_order_id.setter
    def payment_order_id(self, payment_order_id):
        """Sets the payment_order_id of this BillingTransaction.

        Identificador de la orden de pago  # noqa: E501

        :param payment_order_id: The payment_order_id of this BillingTransaction.  # noqa: E501
        :type: str
        """

        self._payment_order_id = payment_order_id

    @property
    def transaction_id(self):
        """Gets the transaction_id of this BillingTransaction.  # noqa: E501

        Identificador de la transacción  # noqa: E501

        :return: The transaction_id of this BillingTransaction.  # noqa: E501
        :rtype: int
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this BillingTransaction.

        Identificador de la transacción  # noqa: E501

        :param transaction_id: The transaction_id of this BillingTransaction.  # noqa: E501
        :type: int
        """

        self._transaction_id = transaction_id

    @property
    def type(self):
        """Gets the type of this BillingTransaction.  # noqa: E501

        Tipo de transaccion IN | OUT  # noqa: E501

        :return: The type of this BillingTransaction.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BillingTransaction.

        Tipo de transaccion IN | OUT  # noqa: E501

        :param type: The type of this BillingTransaction.  # noqa: E501
        :type: str
        """
        allowed_values = ["IN", "OUT"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(BillingTransaction, dict):
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
        if not isinstance(other, BillingTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other