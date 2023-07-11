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

class RecurringChargeRequest(object):
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
        'charges': 'int',
        'customer': 'Customer',
        'first_charge_date': 'datetime',
        'order_id': 'str',
        'product': 'Product',
        'return_url': 'str'
    }

    attribute_map = {
        'cancel_return_url': 'cancel_return_url',
        'charges': 'charges',
        'customer': 'customer',
        'first_charge_date': 'first_charge_date',
        'order_id': 'order_id',
        'product': 'product',
        'return_url': 'return_url'
    }

    def __init__(self, cancel_return_url=None, charges=None, customer=None, first_charge_date=None, order_id=None, product=None, return_url=None):  # noqa: E501
        """RecurringChargeRequest - a model defined in Swagger"""  # noqa: E501
        self._cancel_return_url = None
        self._charges = None
        self._customer = None
        self._first_charge_date = None
        self._order_id = None
        self._product = None
        self._return_url = None
        self.discriminator = None
        self.cancel_return_url = cancel_return_url
        self.charges = charges
        self.customer = customer
        self.first_charge_date = first_charge_date
        self.order_id = order_id
        self.product = product
        self.return_url = return_url

    @property
    def cancel_return_url(self):
        """Gets the cancel_return_url of this RecurringChargeRequest.  # noqa: E501

        Es la dirección URL a la que se redirigirá en caso de que el usuario cancele.  # noqa: E501

        :return: The cancel_return_url of this RecurringChargeRequest.  # noqa: E501
        :rtype: str
        """
        return self._cancel_return_url

    @cancel_return_url.setter
    def cancel_return_url(self, cancel_return_url):
        """Sets the cancel_return_url of this RecurringChargeRequest.

        Es la dirección URL a la que se redirigirá en caso de que el usuario cancele.  # noqa: E501

        :param cancel_return_url: The cancel_return_url of this RecurringChargeRequest.  # noqa: E501
        :type: str
        """
        if cancel_return_url is None:
            raise ValueError("Invalid value for `cancel_return_url`, must not be `None`")  # noqa: E501

        self._cancel_return_url = cancel_return_url

    @property
    def charges(self):
        """Gets the charges of this RecurringChargeRequest.  # noqa: E501

        Número de cargos que se aplicarán a la tarjeta del cliente final a partir de la fecha del primer cargo  # noqa: E501

        :return: The charges of this RecurringChargeRequest.  # noqa: E501
        :rtype: int
        """
        return self._charges

    @charges.setter
    def charges(self, charges):
        """Sets the charges of this RecurringChargeRequest.

        Número de cargos que se aplicarán a la tarjeta del cliente final a partir de la fecha del primer cargo  # noqa: E501

        :param charges: The charges of this RecurringChargeRequest.  # noqa: E501
        :type: int
        """
        if charges is None:
            raise ValueError("Invalid value for `charges`, must not be `None`")  # noqa: E501

        self._charges = charges

    @property
    def customer(self):
        """Gets the customer of this RecurringChargeRequest.  # noqa: E501


        :return: The customer of this RecurringChargeRequest.  # noqa: E501
        :rtype: Customer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this RecurringChargeRequest.


        :param customer: The customer of this RecurringChargeRequest.  # noqa: E501
        :type: Customer
        """
        if customer is None:
            raise ValueError("Invalid value for `customer`, must not be `None`")  # noqa: E501

        self._customer = customer

    @property
    def first_charge_date(self):
        """Gets the first_charge_date of this RecurringChargeRequest.  # noqa: E501

        Fecha en la que se aplicará el primer cargo a la tarjeta del cliente final   # noqa: E501

        :return: The first_charge_date of this RecurringChargeRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._first_charge_date

    @first_charge_date.setter
    def first_charge_date(self, first_charge_date):
        """Sets the first_charge_date of this RecurringChargeRequest.

        Fecha en la que se aplicará el primer cargo a la tarjeta del cliente final   # noqa: E501

        :param first_charge_date: The first_charge_date of this RecurringChargeRequest.  # noqa: E501
        :type: datetime
        """
        if first_charge_date is None:
            raise ValueError("Invalid value for `first_charge_date`, must not be `None`")  # noqa: E501

        self._first_charge_date = first_charge_date

    @property
    def order_id(self):
        """Gets the order_id of this RecurringChargeRequest.  # noqa: E501

        Número de orden asignado por el cliente de Wire4  # noqa: E501

        :return: The order_id of this RecurringChargeRequest.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this RecurringChargeRequest.

        Número de orden asignado por el cliente de Wire4  # noqa: E501

        :param order_id: The order_id of this RecurringChargeRequest.  # noqa: E501
        :type: str
        """
        if order_id is None:
            raise ValueError("Invalid value for `order_id`, must not be `None`")  # noqa: E501

        self._order_id = order_id

    @property
    def product(self):
        """Gets the product of this RecurringChargeRequest.  # noqa: E501


        :return: The product of this RecurringChargeRequest.  # noqa: E501
        :rtype: Product
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this RecurringChargeRequest.


        :param product: The product of this RecurringChargeRequest.  # noqa: E501
        :type: Product
        """
        if product is None:
            raise ValueError("Invalid value for `product`, must not be `None`")  # noqa: E501

        self._product = product

    @property
    def return_url(self):
        """Gets the return_url of this RecurringChargeRequest.  # noqa: E501

        Es la dirección URL a la que se redirigirá en caso de éxito.  # noqa: E501

        :return: The return_url of this RecurringChargeRequest.  # noqa: E501
        :rtype: str
        """
        return self._return_url

    @return_url.setter
    def return_url(self, return_url):
        """Sets the return_url of this RecurringChargeRequest.

        Es la dirección URL a la que se redirigirá en caso de éxito.  # noqa: E501

        :param return_url: The return_url of this RecurringChargeRequest.  # noqa: E501
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
        if issubclass(RecurringChargeRequest, dict):
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
        if not isinstance(other, RecurringChargeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other