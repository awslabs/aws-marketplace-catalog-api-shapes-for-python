# coding: utf-8

"""
    SaaSProduct_1_0_ChangeTypes

        Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved. 

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, field_validator
from pydantic import Field
from typing_extensions import Annotated
from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.dimension_type import DimensionType
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class RestrictDimensionChangeDetail(BaseModel):
    """
    Represents a single RestrictDimension object within the array of the RestrictDimesions change type
    """ # noqa: E501
    key: Annotated[str, Field(strict=True, max_length=100)] = Field(alias="Key")
    types: Annotated[List[DimensionType], Field(min_length=1, max_length=3)] = Field(alias="Types")
    __properties: ClassVar[List[str]] = ["Key", "Types"]

    @field_validator('key')
    def key_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[A-Za-z0-9_.-]+$", value):
            raise ValueError(r"must validate the regular expression /^[A-Za-z0-9_.-]+$/")
        return value

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
        """Create an instance of RestrictDimensionChangeDetail from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of RestrictDimensionChangeDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Key": obj.get("Key"),
            "Types": obj.get("Types")
        })
        return _obj


