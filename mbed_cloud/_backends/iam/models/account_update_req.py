# coding: utf-8

"""
    IAM Identities REST API

    REST API to manage accounts, groups, users and API keys

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class AccountUpdateReq(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, address_line2=None, city=None, address_line1=None, display_name=None, country=None, company=None, status=None, state=None, contact=None, postal_code=None, is_provisioning_allowed=False, tier=None, phone_number=None, email=None, aliases=None):
        """
        AccountUpdateReq - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'address_line2': 'str',
            'city': 'str',
            'address_line1': 'str',
            'display_name': 'str',
            'country': 'str',
            'company': 'str',
            'status': 'str',
            'state': 'str',
            'contact': 'str',
            'postal_code': 'str',
            'is_provisioning_allowed': 'bool',
            'tier': 'str',
            'phone_number': 'str',
            'email': 'str',
            'aliases': 'list[str]'
        }

        self.attribute_map = {
            'address_line2': 'address_line2',
            'city': 'city',
            'address_line1': 'address_line1',
            'display_name': 'display_name',
            'country': 'country',
            'company': 'company',
            'status': 'status',
            'state': 'state',
            'contact': 'contact',
            'postal_code': 'postal_code',
            'is_provisioning_allowed': 'is_provisioning_allowed',
            'tier': 'tier',
            'phone_number': 'phone_number',
            'email': 'email',
            'aliases': 'aliases'
        }

        self._address_line2 = address_line2
        self._city = city
        self._address_line1 = address_line1
        self._display_name = display_name
        self._country = country
        self._company = company
        self._status = status
        self._state = state
        self._contact = contact
        self._postal_code = postal_code
        self._is_provisioning_allowed = is_provisioning_allowed
        self._tier = tier
        self._phone_number = phone_number
        self._email = email
        self._aliases = aliases

    @property
    def address_line2(self):
        """
        Gets the address_line2 of this AccountUpdateReq.
        Postal address line 2.

        :return: The address_line2 of this AccountUpdateReq.
        :rtype: str
        """
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        """
        Sets the address_line2 of this AccountUpdateReq.
        Postal address line 2.

        :param address_line2: The address_line2 of this AccountUpdateReq.
        :type: str
        """

        self._address_line2 = address_line2

    @property
    def city(self):
        """
        Gets the city of this AccountUpdateReq.
        The city part of the postal address.

        :return: The city of this AccountUpdateReq.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this AccountUpdateReq.
        The city part of the postal address.

        :param city: The city of this AccountUpdateReq.
        :type: str
        """

        self._city = city

    @property
    def address_line1(self):
        """
        Gets the address_line1 of this AccountUpdateReq.
        Postal address line 1.

        :return: The address_line1 of this AccountUpdateReq.
        :rtype: str
        """
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        """
        Sets the address_line1 of this AccountUpdateReq.
        Postal address line 1.

        :param address_line1: The address_line1 of this AccountUpdateReq.
        :type: str
        """

        self._address_line1 = address_line1

    @property
    def display_name(self):
        """
        Gets the display_name of this AccountUpdateReq.
        The display name for the account.

        :return: The display_name of this AccountUpdateReq.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AccountUpdateReq.
        The display name for the account.

        :param display_name: The display_name of this AccountUpdateReq.
        :type: str
        """

        self._display_name = display_name

    @property
    def country(self):
        """
        Gets the country of this AccountUpdateReq.
        The country part of the postal address.

        :return: The country of this AccountUpdateReq.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this AccountUpdateReq.
        The country part of the postal address.

        :param country: The country of this AccountUpdateReq.
        :type: str
        """

        self._country = country

    @property
    def company(self):
        """
        Gets the company of this AccountUpdateReq.
        The name of the company.

        :return: The company of this AccountUpdateReq.
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """
        Sets the company of this AccountUpdateReq.
        The name of the company.

        :param company: The company of this AccountUpdateReq.
        :type: str
        """

        self._company = company

    @property
    def status(self):
        """
        Gets the status of this AccountUpdateReq.
        The status of the account. Manageable by the root admin only.

        :return: The status of this AccountUpdateReq.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this AccountUpdateReq.
        The status of the account. Manageable by the root admin only.

        :param status: The status of this AccountUpdateReq.
        :type: str
        """

        self._status = status

    @property
    def state(self):
        """
        Gets the state of this AccountUpdateReq.
        The state part of the postal address.

        :return: The state of this AccountUpdateReq.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this AccountUpdateReq.
        The state part of the postal address.

        :param state: The state of this AccountUpdateReq.
        :type: str
        """

        self._state = state

    @property
    def contact(self):
        """
        Gets the contact of this AccountUpdateReq.
        The name of the contact person for this account.

        :return: The contact of this AccountUpdateReq.
        :rtype: str
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """
        Sets the contact of this AccountUpdateReq.
        The name of the contact person for this account.

        :param contact: The contact of this AccountUpdateReq.
        :type: str
        """

        self._contact = contact

    @property
    def postal_code(self):
        """
        Gets the postal_code of this AccountUpdateReq.
        The postal code part of the postal address.

        :return: The postal_code of this AccountUpdateReq.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this AccountUpdateReq.
        The postal code part of the postal address.

        :param postal_code: The postal_code of this AccountUpdateReq.
        :type: str
        """

        self._postal_code = postal_code

    @property
    def is_provisioning_allowed(self):
        """
        Gets the is_provisioning_allowed of this AccountUpdateReq.
        Flag (true/false) indicating whether Factory Tool is allowed to download or not. Manageable by the root admin only.

        :return: The is_provisioning_allowed of this AccountUpdateReq.
        :rtype: bool
        """
        return self._is_provisioning_allowed

    @is_provisioning_allowed.setter
    def is_provisioning_allowed(self, is_provisioning_allowed):
        """
        Sets the is_provisioning_allowed of this AccountUpdateReq.
        Flag (true/false) indicating whether Factory Tool is allowed to download or not. Manageable by the root admin only.

        :param is_provisioning_allowed: The is_provisioning_allowed of this AccountUpdateReq.
        :type: bool
        """

        self._is_provisioning_allowed = is_provisioning_allowed

    @property
    def tier(self):
        """
        Gets the tier of this AccountUpdateReq.
        The tier level of the account; '0': free tier, '1': commercial account. Other values are reserved for the future. Manageable by the root admin only.

        :return: The tier of this AccountUpdateReq.
        :rtype: str
        """
        return self._tier

    @tier.setter
    def tier(self, tier):
        """
        Sets the tier of this AccountUpdateReq.
        The tier level of the account; '0': free tier, '1': commercial account. Other values are reserved for the future. Manageable by the root admin only.

        :param tier: The tier of this AccountUpdateReq.
        :type: str
        """

        self._tier = tier

    @property
    def phone_number(self):
        """
        Gets the phone_number of this AccountUpdateReq.
        The phone number of the company.

        :return: The phone_number of this AccountUpdateReq.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this AccountUpdateReq.
        The phone number of the company.

        :param phone_number: The phone_number of this AccountUpdateReq.
        :type: str
        """

        self._phone_number = phone_number

    @property
    def email(self):
        """
        Gets the email of this AccountUpdateReq.
        The company email address for this account.

        :return: The email of this AccountUpdateReq.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this AccountUpdateReq.
        The company email address for this account.

        :param email: The email of this AccountUpdateReq.
        :type: str
        """

        self._email = email

    @property
    def aliases(self):
        """
        Gets the aliases of this AccountUpdateReq.
        An array of aliases.

        :return: The aliases of this AccountUpdateReq.
        :rtype: list[str]
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """
        Sets the aliases of this AccountUpdateReq.
        An array of aliases.

        :param aliases: The aliases of this AccountUpdateReq.
        :type: list[str]
        """

        self._aliases = aliases

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
