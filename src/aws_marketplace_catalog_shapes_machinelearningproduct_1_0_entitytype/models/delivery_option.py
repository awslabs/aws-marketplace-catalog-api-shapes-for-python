# coding: utf-8

"""
    MachineLearningProduct_1_0_EntityType

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
from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.instructions import Instructions
from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.recommended_instance_types import RecommendedInstanceTypes
from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.supported_instance_types import SupportedInstanceTypes
from typing import Optional, Set
from typing_extensions import Self

class DeliveryOption(BaseModel):
    """
    DeliveryOption
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, alias="Id")
    type: Optional[StrictStr] = Field(default=None, alias="Type")
    source_id: Optional[StrictStr] = Field(default=None, alias="SourceId")
    title: Optional[StrictStr] = Field(default=None, alias="Title")
    short_description: Optional[StrictStr] = Field(default=None, alias="ShortDescription")
    instructions: Optional[Instructions] = Field(default=None, alias="Instructions")
    visibility: Optional[StrictStr] = Field(default=None, alias="Visibility")
    recommended_instance_types: Optional[RecommendedInstanceTypes] = Field(default=None, alias="RecommendedInstanceTypes")
    supported_instance_types: Optional[SupportedInstanceTypes] = Field(default=None, alias="SupportedInstanceTypes")
    __properties: ClassVar[List[str]] = ["Id", "Type", "SourceId", "Title", "ShortDescription", "Instructions", "Visibility", "RecommendedInstanceTypes", "SupportedInstanceTypes"]

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
        """Create an instance of DeliveryOption from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of instructions
        if self.instructions:
            _dict['Instructions'] = self.instructions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of recommended_instance_types
        if self.recommended_instance_types:
            _dict['RecommendedInstanceTypes'] = self.recommended_instance_types.to_dict()
        # override the default output from pydantic by calling `to_dict()` of supported_instance_types
        if self.supported_instance_types:
            _dict['SupportedInstanceTypes'] = self.supported_instance_types.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeliveryOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Id": obj.get("Id"),
            "Type": obj.get("Type"),
            "SourceId": obj.get("SourceId"),
            "Title": obj.get("Title"),
            "ShortDescription": obj.get("ShortDescription"),
            "Instructions": Instructions.from_dict(obj["Instructions"]) if obj.get("Instructions") is not None else None,
            "Visibility": obj.get("Visibility"),
            "RecommendedInstanceTypes": RecommendedInstanceTypes.from_dict(obj["RecommendedInstanceTypes"]) if obj.get("RecommendedInstanceTypes") is not None else None,
            "SupportedInstanceTypes": SupportedInstanceTypes.from_dict(obj["SupportedInstanceTypes"]) if obj.get("SupportedInstanceTypes") is not None else None
        })
        return _obj


