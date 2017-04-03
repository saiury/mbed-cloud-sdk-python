# coding: utf-8

"""
    Firmware Catalog API

    This is the API Documentation for the mbed firmware catalog service which is part of the update service.

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class FirmwareImage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, datafile=None, description=None, created_at=None, object=None, updated_at=None, image_id=None, etag=None, datafile_checksum=None, id=None, name=None):
        """
        FirmwareImage - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'datafile': 'str',
            'description': 'str',
            'created_at': 'datetime',
            'object': 'str',
            'updated_at': 'datetime',
            'image_id': 'str',
            'etag': 'datetime',
            'datafile_checksum': 'str',
            'id': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'datafile': 'datafile',
            'description': 'description',
            'created_at': 'created_at',
            'object': 'object',
            'updated_at': 'updated_at',
            'image_id': 'image_id',
            'etag': 'etag',
            'datafile_checksum': 'datafile_checksum',
            'id': 'id',
            'name': 'name'
        }

        self._datafile = datafile
        self._description = description
        self._created_at = created_at
        self._object = object
        self._updated_at = updated_at
        self._image_id = image_id
        self._etag = etag
        self._datafile_checksum = datafile_checksum
        self._id = id
        self._name = name

    @property
    def datafile(self):
        """
        Gets the datafile of this FirmwareImage.
        The binary file of firmware image

        :return: The datafile of this FirmwareImage.
        :rtype: str
        """
        return self._datafile

    @datafile.setter
    def datafile(self, datafile):
        """
        Sets the datafile of this FirmwareImage.
        The binary file of firmware image

        :param datafile: The datafile of this FirmwareImage.
        :type: str
        """
        if datafile is None:
            raise ValueError("Invalid value for `datafile`, must not be `None`")

        self._datafile = datafile

    @property
    def description(self):
        """
        Gets the description of this FirmwareImage.
        The description of the object

        :return: The description of this FirmwareImage.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this FirmwareImage.
        The description of the object

        :param description: The description of this FirmwareImage.
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")

        self._description = description

    @property
    def created_at(self):
        """
        Gets the created_at of this FirmwareImage.
        The time the object was created

        :return: The created_at of this FirmwareImage.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this FirmwareImage.
        The time the object was created

        :param created_at: The created_at of this FirmwareImage.
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")

        self._created_at = created_at

    @property
    def object(self):
        """
        Gets the object of this FirmwareImage.
        The API resource entity

        :return: The object of this FirmwareImage.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this FirmwareImage.
        The API resource entity

        :param object: The object of this FirmwareImage.
        :type: str
        """
        if object is None:
            raise ValueError("Invalid value for `object`, must not be `None`")

        self._object = object

    @property
    def updated_at(self):
        """
        Gets the updated_at of this FirmwareImage.
        The time the object was updated

        :return: The updated_at of this FirmwareImage.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this FirmwareImage.
        The time the object was updated

        :param updated_at: The updated_at of this FirmwareImage.
        :type: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")

        self._updated_at = updated_at

    @property
    def image_id(self):
        """
        Gets the image_id of this FirmwareImage.
        DEPRECATED: The ID of the firmware image

        :return: The image_id of this FirmwareImage.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """
        Sets the image_id of this FirmwareImage.
        DEPRECATED: The ID of the firmware image

        :param image_id: The image_id of this FirmwareImage.
        :type: str
        """
        if image_id is None:
            raise ValueError("Invalid value for `image_id`, must not be `None`")

        self._image_id = image_id

    @property
    def etag(self):
        """
        Gets the etag of this FirmwareImage.
        The entity instance signature

        :return: The etag of this FirmwareImage.
        :rtype: datetime
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this FirmwareImage.
        The entity instance signature

        :param etag: The etag of this FirmwareImage.
        :type: datetime
        """
        if etag is None:
            raise ValueError("Invalid value for `etag`, must not be `None`")

        self._etag = etag

    @property
    def datafile_checksum(self):
        """
        Gets the datafile_checksum of this FirmwareImage.
        Checksum generated for the datafile

        :return: The datafile_checksum of this FirmwareImage.
        :rtype: str
        """
        return self._datafile_checksum

    @datafile_checksum.setter
    def datafile_checksum(self, datafile_checksum):
        """
        Sets the datafile_checksum of this FirmwareImage.
        Checksum generated for the datafile

        :param datafile_checksum: The datafile_checksum of this FirmwareImage.
        :type: str
        """
        if datafile_checksum is None:
            raise ValueError("Invalid value for `datafile_checksum`, must not be `None`")

        self._datafile_checksum = datafile_checksum

    @property
    def id(self):
        """
        Gets the id of this FirmwareImage.
        The ID of the firmware image

        :return: The id of this FirmwareImage.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FirmwareImage.
        The ID of the firmware image

        :param id: The id of this FirmwareImage.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this FirmwareImage.
        The name of the object

        :return: The name of this FirmwareImage.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FirmwareImage.
        The name of the object

        :param name: The name of this FirmwareImage.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

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
        if not isinstance(other, FirmwareImage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other