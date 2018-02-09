# coding: utf-8

"""
    Device Directory API

    This is the API Documentation for the Mbed Device Directory service.

    OpenAPI spec version: 3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DeviceEventData(object):
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
        'date_time': 'datetime',
        'state_change': 'bool',
        'description': 'str',
        'changes': 'object',
        'event_type_description': 'str',
        'event_type': 'str',
        'data': 'object',
        'id': 'str',
        'device_id': 'str'
    }

    attribute_map = {
        'date_time': 'date_time',
        'state_change': 'state_change',
        'description': 'description',
        'changes': 'changes',
        'event_type_description': 'event_type_description',
        'event_type': 'event_type',
        'data': 'data',
        'id': 'id',
        'device_id': 'device_id'
    }

    def __init__(self, date_time=None, state_change=None, description=None, changes=None, event_type_description=None, event_type=None, data=None, id=None, device_id=None):
        """
        DeviceEventData - a model defined in Swagger
        """

        self._date_time = date_time
        self._state_change = state_change
        self._description = description
        self._changes = changes
        self._event_type_description = event_type_description
        self._event_type = event_type
        self._data = data
        self._id = id
        self._device_id = device_id
        self.discriminator = None

    @property
    def date_time(self):
        """
        Gets the date_time of this DeviceEventData.

        :return: The date_time of this DeviceEventData.
        :rtype: datetime
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """
        Sets the date_time of this DeviceEventData.

        :param date_time: The date_time of this DeviceEventData.
        :type: datetime
        """
        if date_time is None:
            raise ValueError("Invalid value for `date_time`, must not be `None`")

        self._date_time = date_time

    @property
    def state_change(self):
        """
        Gets the state_change of this DeviceEventData.

        :return: The state_change of this DeviceEventData.
        :rtype: bool
        """
        return self._state_change

    @state_change.setter
    def state_change(self, state_change):
        """
        Sets the state_change of this DeviceEventData.

        :param state_change: The state_change of this DeviceEventData.
        :type: bool
        """

        self._state_change = state_change

    @property
    def description(self):
        """
        Gets the description of this DeviceEventData.

        :return: The description of this DeviceEventData.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DeviceEventData.

        :param description: The description of this DeviceEventData.
        :type: str
        """

        self._description = description

    @property
    def changes(self):
        """
        Gets the changes of this DeviceEventData.

        :return: The changes of this DeviceEventData.
        :rtype: object
        """
        return self._changes

    @changes.setter
    def changes(self, changes):
        """
        Sets the changes of this DeviceEventData.

        :param changes: The changes of this DeviceEventData.
        :type: object
        """

        self._changes = changes

    @property
    def event_type_description(self):
        """
        Gets the event_type_description of this DeviceEventData.

        :return: The event_type_description of this DeviceEventData.
        :rtype: str
        """
        return self._event_type_description

    @event_type_description.setter
    def event_type_description(self, event_type_description):
        """
        Sets the event_type_description of this DeviceEventData.

        :param event_type_description: The event_type_description of this DeviceEventData.
        :type: str
        """

        self._event_type_description = event_type_description

    @property
    def event_type(self):
        """
        Gets the event_type of this DeviceEventData.

        :return: The event_type of this DeviceEventData.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """
        Sets the event_type of this DeviceEventData.

        :param event_type: The event_type of this DeviceEventData.
        :type: str
        """
        if event_type is not None and len(event_type) > 100:
            raise ValueError("Invalid value for `event_type`, length must be less than or equal to `100`")

        self._event_type = event_type

    @property
    def data(self):
        """
        Gets the data of this DeviceEventData.

        :return: The data of this DeviceEventData.
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this DeviceEventData.

        :param data: The data of this DeviceEventData.
        :type: object
        """

        self._data = data

    @property
    def id(self):
        """
        Gets the id of this DeviceEventData.

        :return: The id of this DeviceEventData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DeviceEventData.

        :param id: The id of this DeviceEventData.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def device_id(self):
        """
        Gets the device_id of this DeviceEventData.

        :return: The device_id of this DeviceEventData.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """
        Sets the device_id of this DeviceEventData.

        :param device_id: The device_id of this DeviceEventData.
        :type: str
        """

        self._device_id = device_id

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
        if not isinstance(other, DeviceEventData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
