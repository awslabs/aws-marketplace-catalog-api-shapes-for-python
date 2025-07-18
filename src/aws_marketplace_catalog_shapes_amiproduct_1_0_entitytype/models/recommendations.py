# coding: utf-8

"""
    AmiProduct_1_0_EntityType

        Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved. 

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from aws_marketplace_catalog_shapes_amiproduct_1_0_entitytype.models.security_group import SecurityGroup
from typing import Optional, Set
from typing_extensions import Self

class Recommendations(BaseModel):
    """
    Recommendations
    """ # noqa: E501
    security_groups: Optional[List[SecurityGroup]] = Field(default=None, alias="SecurityGroups")
    instance_type: Optional[StrictStr] = Field(default=None, alias="InstanceType")
    __properties: ClassVar[List[str]] = ["SecurityGroups", "InstanceType"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Recommendations from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in security_groups (list)
        _items = []
        if self.security_groups:
            for _item_security_groups in self.security_groups:
                if _item_security_groups:
                    _items.append(_item_security_groups.to_dict())
            _dict['SecurityGroups'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Recommendations from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "SecurityGroups": [SecurityGroup.from_dict(_item) for _item in obj["SecurityGroups"]] if obj.get("SecurityGroups") is not None else None,
            "InstanceType": obj.get("InstanceType")
        })
        return _obj


