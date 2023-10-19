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

class Account(object):
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
        'amount_limit': 'float',
        'bank_key': 'str',
        'beneficiary_account': 'str',
        'email': 'list[str]',
        'institution': 'BeneficiaryInstitution',
        'kind_of_relationship': 'str',
        'numeric_reference_spei': 'str',
        'payment_concept_spei': 'str',
        'person': 'Person',
        'relationship': 'str',
        'rfc': 'str'
    }

    attribute_map = {
        'amount_limit': 'amount_limit',
        'bank_key': 'bank_key',
        'beneficiary_account': 'beneficiary_account',
        'email': 'email',
        'institution': 'institution',
        'kind_of_relationship': 'kind_of_relationship',
        'numeric_reference_spei': 'numeric_reference_spei',
        'payment_concept_spei': 'payment_concept_spei',
        'person': 'person',
        'relationship': 'relationship',
        'rfc': 'rfc'
    }

    def __init__(self, amount_limit=None, bank_key=None, beneficiary_account=None, email=None, institution=None, kind_of_relationship=None, numeric_reference_spei=None, payment_concept_spei=None, person=None, relationship=None, rfc=None):  # noqa: E501
        """Account - a model defined in Swagger"""  # noqa: E501
        self._amount_limit = None
        self._bank_key = None
        self._beneficiary_account = None
        self._email = None
        self._institution = None
        self._kind_of_relationship = None
        self._numeric_reference_spei = None
        self._payment_concept_spei = None
        self._person = None
        self._relationship = None
        self._rfc = None
        self.discriminator = None
        self.amount_limit = amount_limit
        if bank_key is not None:
            self.bank_key = bank_key
        self.beneficiary_account = beneficiary_account
        if email is not None:
            self.email = email
        if institution is not None:
            self.institution = institution
        self.kind_of_relationship = kind_of_relationship
        if numeric_reference_spei is not None:
            self.numeric_reference_spei = numeric_reference_spei
        if payment_concept_spei is not None:
            self.payment_concept_spei = payment_concept_spei
        if person is not None:
            self.person = person
        self.relationship = relationship
        self.rfc = rfc

    @property
    def amount_limit(self):
        """Gets the amount_limit of this Account.  # noqa: E501

        Es el monto límite permitido que se registra para la cuenta. Por ejemplo 1000.00.  # noqa: E501

        :return: The amount_limit of this Account.  # noqa: E501
        :rtype: float
        """
        return self._amount_limit

    @amount_limit.setter
    def amount_limit(self, amount_limit):
        """Sets the amount_limit of this Account.

        Es el monto límite permitido que se registra para la cuenta. Por ejemplo 1000.00.  # noqa: E501

        :param amount_limit: The amount_limit of this Account.  # noqa: E501
        :type: float
        """
        if amount_limit is None:
            raise ValueError("Invalid value for `amount_limit`, must not be `None`")  # noqa: E501

        self._amount_limit = amount_limit

    @property
    def bank_key(self):
        """Gets the bank_key of this Account.  # noqa: E501

        Es la clave del banco, es requerido en caso de que la cuenta del beneficiario sea un número de celular.  # noqa: E501

        :return: The bank_key of this Account.  # noqa: E501
        :rtype: str
        """
        return self._bank_key

    @bank_key.setter
    def bank_key(self, bank_key):
        """Sets the bank_key of this Account.

        Es la clave del banco, es requerido en caso de que la cuenta del beneficiario sea un número de celular.  # noqa: E501

        :param bank_key: The bank_key of this Account.  # noqa: E501
        :type: str
        """

        self._bank_key = bank_key

    @property
    def beneficiary_account(self):
        """Gets the beneficiary_account of this Account.  # noqa: E501

        Es la cuenta del beneficiario, podría ser teléfono celular (se valida que sea de 10 dígitos), Tarjeta de débito (TDD, se valida que sea de 16 dígitos) o cuenta CLABE (se valida que sea de 18 dígitos). <br/><br/>Por ejemplo Teléfono celular: 5525072600, TDD: 4323 1234 5678 9123, CLABE: 032180000118359719.  # noqa: E501

        :return: The beneficiary_account of this Account.  # noqa: E501
        :rtype: str
        """
        return self._beneficiary_account

    @beneficiary_account.setter
    def beneficiary_account(self, beneficiary_account):
        """Sets the beneficiary_account of this Account.

        Es la cuenta del beneficiario, podría ser teléfono celular (se valida que sea de 10 dígitos), Tarjeta de débito (TDD, se valida que sea de 16 dígitos) o cuenta CLABE (se valida que sea de 18 dígitos). <br/><br/>Por ejemplo Teléfono celular: 5525072600, TDD: 4323 1234 5678 9123, CLABE: 032180000118359719.  # noqa: E501

        :param beneficiary_account: The beneficiary_account of this Account.  # noqa: E501
        :type: str
        """
        if beneficiary_account is None:
            raise ValueError("Invalid value for `beneficiary_account`, must not be `None`")  # noqa: E501

        self._beneficiary_account = beneficiary_account

    @property
    def email(self):
        """Gets the email of this Account.  # noqa: E501

        Es una lista de correos electrónicos (emails). Se valida el formato de email. Este campo es opcional.  # noqa: E501

        :return: The email of this Account.  # noqa: E501
        :rtype: list[str]
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Account.

        Es una lista de correos electrónicos (emails). Se valida el formato de email. Este campo es opcional.  # noqa: E501

        :param email: The email of this Account.  # noqa: E501
        :type: list[str]
        """

        self._email = email

    @property
    def institution(self):
        """Gets the institution of this Account.  # noqa: E501


        :return: The institution of this Account.  # noqa: E501
        :rtype: BeneficiaryInstitution
        """
        return self._institution

    @institution.setter
    def institution(self, institution):
        """Sets the institution of this Account.


        :param institution: The institution of this Account.  # noqa: E501
        :type: BeneficiaryInstitution
        """

        self._institution = institution

    @property
    def kind_of_relationship(self):
        """Gets the kind_of_relationship of this Account.  # noqa: E501

        Es el tipo de relación que se tiene con el propietario de la cuenta. Para registrar una cuenta, este valor se debe obtener del recurso <a href=\"#operation/getAvailableRelationshipsMonexUsingGET\">relationships.</a> <br /><br /><b>Nota:</b> <em>Si en la respuesta de Monex esta propiedad es nula, tampoco estará presente en esta respuesta.</em>  # noqa: E501

        :return: The kind_of_relationship of this Account.  # noqa: E501
        :rtype: str
        """
        return self._kind_of_relationship

    @kind_of_relationship.setter
    def kind_of_relationship(self, kind_of_relationship):
        """Sets the kind_of_relationship of this Account.

        Es el tipo de relación que se tiene con el propietario de la cuenta. Para registrar una cuenta, este valor se debe obtener del recurso <a href=\"#operation/getAvailableRelationshipsMonexUsingGET\">relationships.</a> <br /><br /><b>Nota:</b> <em>Si en la respuesta de Monex esta propiedad es nula, tampoco estará presente en esta respuesta.</em>  # noqa: E501

        :param kind_of_relationship: The kind_of_relationship of this Account.  # noqa: E501
        :type: str
        """
        if kind_of_relationship is None:
            raise ValueError("Invalid value for `kind_of_relationship`, must not be `None`")  # noqa: E501

        self._kind_of_relationship = kind_of_relationship

    @property
    def numeric_reference_spei(self):
        """Gets the numeric_reference_spei of this Account.  # noqa: E501

        Es la referencia numérica a utilizar cuando se realice una transferencia y no se especifique una referencia.  # noqa: E501

        :return: The numeric_reference_spei of this Account.  # noqa: E501
        :rtype: str
        """
        return self._numeric_reference_spei

    @numeric_reference_spei.setter
    def numeric_reference_spei(self, numeric_reference_spei):
        """Sets the numeric_reference_spei of this Account.

        Es la referencia numérica a utilizar cuando se realice una transferencia y no se especifique una referencia.  # noqa: E501

        :param numeric_reference_spei: The numeric_reference_spei of this Account.  # noqa: E501
        :type: str
        """

        self._numeric_reference_spei = numeric_reference_spei

    @property
    def payment_concept_spei(self):
        """Gets the payment_concept_spei of this Account.  # noqa: E501

        Es el concepto de pago a utilizar cuando se realice una transferencia y no se especifique un concepto  # noqa: E501

        :return: The payment_concept_spei of this Account.  # noqa: E501
        :rtype: str
        """
        return self._payment_concept_spei

    @payment_concept_spei.setter
    def payment_concept_spei(self, payment_concept_spei):
        """Sets the payment_concept_spei of this Account.

        Es el concepto de pago a utilizar cuando se realice una transferencia y no se especifique un concepto  # noqa: E501

        :param payment_concept_spei: The payment_concept_spei of this Account.  # noqa: E501
        :type: str
        """

        self._payment_concept_spei = payment_concept_spei

    @property
    def person(self):
        """Gets the person of this Account.  # noqa: E501


        :return: The person of this Account.  # noqa: E501
        :rtype: Person
        """
        return self._person

    @person.setter
    def person(self, person):
        """Sets the person of this Account.


        :param person: The person of this Account.  # noqa: E501
        :type: Person
        """

        self._person = person

    @property
    def relationship(self):
        """Gets the relationship of this Account.  # noqa: E501

        Es la relación con el propietario de la cuenta, para registrar este valor se debe obtener del recurso <a href=\"#operation/getAvailableRelationshipsMonexUsingGET\">relationships.</a> <br/> <br/> <b>Nota:</b> Si en la respuesta de Monex, sta propiedad es nula, tampoco estará presente en esta respuesta.  # noqa: E501

        :return: The relationship of this Account.  # noqa: E501
        :rtype: str
        """
        return self._relationship

    @relationship.setter
    def relationship(self, relationship):
        """Sets the relationship of this Account.

        Es la relación con el propietario de la cuenta, para registrar este valor se debe obtener del recurso <a href=\"#operation/getAvailableRelationshipsMonexUsingGET\">relationships.</a> <br/> <br/> <b>Nota:</b> Si en la respuesta de Monex, sta propiedad es nula, tampoco estará presente en esta respuesta.  # noqa: E501

        :param relationship: The relationship of this Account.  # noqa: E501
        :type: str
        """
        if relationship is None:
            raise ValueError("Invalid value for `relationship`, must not be `None`")  # noqa: E501

        self._relationship = relationship

    @property
    def rfc(self):
        """Gets the rfc of this Account.  # noqa: E501

        Es el Registro Federal de Contribuyentes (RFC) de la persona o institución propietaria dela cuenta. <br/> <br/><b>Nota:</b> Si en la respuesta de Monex esta propiedad es nula, tampoco estará presente en esta respuesta.  # noqa: E501

        :return: The rfc of this Account.  # noqa: E501
        :rtype: str
        """
        return self._rfc

    @rfc.setter
    def rfc(self, rfc):
        """Sets the rfc of this Account.

        Es el Registro Federal de Contribuyentes (RFC) de la persona o institución propietaria dela cuenta. <br/> <br/><b>Nota:</b> Si en la respuesta de Monex esta propiedad es nula, tampoco estará presente en esta respuesta.  # noqa: E501

        :param rfc: The rfc of this Account.  # noqa: E501
        :type: str
        """
        if rfc is None:
            raise ValueError("Invalid value for `rfc`, must not be `None`")  # noqa: E501

        self._rfc = rfc

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
        if issubclass(Account, dict):
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
        if not isinstance(other, Account):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
