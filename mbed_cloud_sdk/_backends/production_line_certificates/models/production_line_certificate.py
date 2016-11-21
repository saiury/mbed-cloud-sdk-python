# coding: utf-8

"""
    Provisioning endpoints - production line certificates.

    A producton line certificate is used to associate a specific installation of the Factory Tool with an mbed Cloud account.  The production line certificate is generated by the Factory Tool, and needs to be uploaded using these APIs. 

    OpenAPI spec version: 0.8
    
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


class ProductionLineCertificate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, comment=None, created_at=None, object=None, etag=None, public_signing_key_hash=None, active=None, production_line_certificate=None, id=None):
        """
        ProductionLineCertificate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'comment': 'str',
            'created_at': 'str',
            'object': 'str',
            'etag': 'str',
            'public_signing_key_hash': 'str',
            'active': 'bool',
            'production_line_certificate': 'str',
            'id': 'str'
        }

        self.attribute_map = {
            'comment': 'comment',
            'created_at': 'created_at',
            'object': 'object',
            'etag': 'etag',
            'public_signing_key_hash': 'publicSigningKeyHash',
            'active': 'active',
            'production_line_certificate': 'production-line-certificate',
            'id': 'id'
        }

        self._comment = comment
        self._created_at = created_at
        self._object = object
        self._etag = etag
        self._public_signing_key_hash = public_signing_key_hash
        self._active = active
        self._production_line_certificate = production_line_certificate
        self._id = id

    @property
    def comment(self):
        """
        Gets the comment of this ProductionLineCertificate.
        Comment of the production line certificate.

        :return: The comment of this ProductionLineCertificate.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this ProductionLineCertificate.
        Comment of the production line certificate.

        :param comment: The comment of this ProductionLineCertificate.
        :type: str
        """

        self._comment = comment

    @property
    def created_at(self):
        """
        Gets the created_at of this ProductionLineCertificate.
        UTC time of the entity creation.

        :return: The created_at of this ProductionLineCertificate.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this ProductionLineCertificate.
        UTC time of the entity creation.

        :param created_at: The created_at of this ProductionLineCertificate.
        :type: str
        """

        self._created_at = created_at

    @property
    def object(self):
        """
        Gets the object of this ProductionLineCertificate.
        Entity name = \"production-line-certificate\"

        :return: The object of this ProductionLineCertificate.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this ProductionLineCertificate.
        Entity name = \"production-line-certificate\"

        :param object: The object of this ProductionLineCertificate.
        :type: str
        """

        self._object = object

    @property
    def etag(self):
        """
        Gets the etag of this ProductionLineCertificate.
        Currently not used.

        :return: The etag of this ProductionLineCertificate.
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this ProductionLineCertificate.
        Currently not used.

        :param etag: The etag of this ProductionLineCertificate.
        :type: str
        """

        self._etag = etag

    @property
    def public_signing_key_hash(self):
        """
        Gets the public_signing_key_hash of this ProductionLineCertificate.
        SHA256 hash of the production line certificate (public signing key).

        :return: The public_signing_key_hash of this ProductionLineCertificate.
        :rtype: str
        """
        return self._public_signing_key_hash

    @public_signing_key_hash.setter
    def public_signing_key_hash(self, public_signing_key_hash):
        """
        Sets the public_signing_key_hash of this ProductionLineCertificate.
        SHA256 hash of the production line certificate (public signing key).

        :param public_signing_key_hash: The public_signing_key_hash of this ProductionLineCertificate.
        :type: str
        """

        self._public_signing_key_hash = public_signing_key_hash

    @property
    def active(self):
        """
        Gets the active of this ProductionLineCertificate.
        Production line certificate active.

        :return: The active of this ProductionLineCertificate.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this ProductionLineCertificate.
        Production line certificate active.

        :param active: The active of this ProductionLineCertificate.
        :type: bool
        """

        self._active = active

    @property
    def production_line_certificate(self):
        """
        Gets the production_line_certificate of this ProductionLineCertificate.
        Production line certificate (public signing key).

        :return: The production_line_certificate of this ProductionLineCertificate.
        :rtype: str
        """
        return self._production_line_certificate

    @production_line_certificate.setter
    def production_line_certificate(self, production_line_certificate):
        """
        Sets the production_line_certificate of this ProductionLineCertificate.
        Production line certificate (public signing key).

        :param production_line_certificate: The production_line_certificate of this ProductionLineCertificate.
        :type: str
        """

        self._production_line_certificate = production_line_certificate

    @property
    def id(self):
        """
        Gets the id of this ProductionLineCertificate.
        Entity ID.

        :return: The id of this ProductionLineCertificate.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProductionLineCertificate.
        Entity ID.

        :param id: The id of this ProductionLineCertificate.
        :type: str
        """

        self._id = id

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