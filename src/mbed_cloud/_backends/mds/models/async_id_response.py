# coding: utf-8

"""
    Connect API

    Mbed Cloud Connect API allows web applications to communicate with devices. You can subscribe to device resources and read/write values to them. mbed Cloud Connect makes connectivity to devices easy by queuing requests and caching resource values.

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AsyncIDResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'status': 'int',
        'payload': 'str',
        'max_age': 'str',
        'error': 'str',
        'id': 'str',
        'ct': 'str'
    }

    attribute_map = {
        'status': 'status',
        'payload': 'payload',
        'max_age': 'max-age',
        'error': 'error',
        'id': 'id',
        'ct': 'ct'
    }

    def __init__(self, status=None, payload=None, max_age=None, error=None, id=None, ct=None):
        """
        AsyncIDResponse - a model defined in Swagger
        """

        self._status = status
        self._payload = payload
        self._max_age = max_age
        self._error = error
        self._id = id
        self._ct = ct
        self.discriminator = None

    @property
    def status(self):
        """
        Gets the status of this AsyncIDResponse.
        The asynchronous response status code for a device operation related to a proxy request or manual subscription.

        :return: The status of this AsyncIDResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this AsyncIDResponse.
        The asynchronous response status code for a device operation related to a proxy request or manual subscription.

        :param status: The status of this AsyncIDResponse.
        :type: int
        """

        self._status = status

    @property
    def payload(self):
        """
        Gets the payload of this AsyncIDResponse.
        Requested data, base64 encoded.

        :return: The payload of this AsyncIDResponse.
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """
        Sets the payload of this AsyncIDResponse.
        Requested data, base64 encoded.

        :param payload: The payload of this AsyncIDResponse.
        :type: str
        """

        self._payload = payload

    @property
    def max_age(self):
        """
        Gets the max_age of this AsyncIDResponse.
        Determines how long this value stays valid in the cache, in seconds. 0 means that the value is not stored in the cache.

        :return: The max_age of this AsyncIDResponse.
        :rtype: str
        """
        return self._max_age

    @max_age.setter
    def max_age(self, max_age):
        """
        Sets the max_age of this AsyncIDResponse.
        Determines how long this value stays valid in the cache, in seconds. 0 means that the value is not stored in the cache.

        :param max_age: The max_age of this AsyncIDResponse.
        :type: str
        """

        self._max_age = max_age

    @property
    def error(self):
        """
        Gets the error of this AsyncIDResponse.
        An optional error message describing the error.

        :return: The error of this AsyncIDResponse.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this AsyncIDResponse.
        An optional error message describing the error.

        :param error: The error of this AsyncIDResponse.
        :type: str
        """

        self._error = error

    @property
    def id(self):
        """
        Gets the id of this AsyncIDResponse.
        The unique ID of the asynchronous response.

        :return: The id of this AsyncIDResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AsyncIDResponse.
        The unique ID of the asynchronous response.

        :param id: The id of this AsyncIDResponse.
        :type: str
        """

        self._id = id

    @property
    def ct(self):
        """
        Gets the ct of this AsyncIDResponse.
        The content type.

        :return: The ct of this AsyncIDResponse.
        :rtype: str
        """
        return self._ct

    @ct.setter
    def ct(self, ct):
        """
        Sets the ct of this AsyncIDResponse.
        The content type.

        :param ct: The ct of this AsyncIDResponse.
        :type: str
        """

        self._ct = ct

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
        if not isinstance(other, AsyncIDResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
