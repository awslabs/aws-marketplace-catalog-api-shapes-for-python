# coding: utf-8

"""
    SaaSProduct_1_0_EntityType

        Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved. 

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from aws_marketplace_catalog_shapes_saasproduct_1_0_entitytype.models.resource import Resource
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class SupportInformation(BaseModel):
    """
    SupportInformation
    """ # noqa: E501
    description: Optional[StrictStr] = Field(default=None, alias="Description")
    resources: Optional[List[Resource]] = Field(default=None, alias="Resources")
    __properties: ClassVar[List[str]] = ["Description", "Resources"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SupportInformation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in resources (list)
        _items = []
        if self.resources:
            for _item in self.resources:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Resources'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of SupportInformation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Description": obj.get("Description"),
            "Resources": [Resource.from_dict(_item) for _item in obj.get("Resources")] if obj.get("Resources") is not None else None
        })
        return _obj


