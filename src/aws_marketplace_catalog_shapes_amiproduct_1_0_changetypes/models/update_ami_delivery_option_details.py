# coding: utf-8

"""
    AmiProduct_1_0_ChangeTypes

        Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved. 

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.access_endpoint_url import AccessEndpointUrl
from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.security_group import SecurityGroup
from typing import Optional, Set
from typing_extensions import Self

class UpdateAmiDeliveryOptionDetails(BaseModel):
    """
    UpdateAmiDeliveryOptionDetails
    """ # noqa: E501
    usage_instructions: Optional[Annotated[str, Field(strict=True, max_length=4000)]] = Field(default=None, alias="UsageInstructions")
    access_endpoint_url: Optional[AccessEndpointUrl] = Field(default=None, alias="AccessEndpointUrl")
    recommended_instance_type: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, alias="RecommendedInstanceType")
    security_groups: Optional[Annotated[List[SecurityGroup], Field(min_length=1, max_length=25)]] = Field(default=None, alias="SecurityGroups")
    __properties: ClassVar[List[str]] = ["UsageInstructions", "AccessEndpointUrl", "RecommendedInstanceType", "SecurityGroups"]

    @field_validator('usage_instructions')
    def usage_instructions_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\S+[\S\s]*", value):
            raise ValueError(r"must validate the regular expression /^\S+[\S\s]*/")
        return value

    @field_validator('recommended_instance_type')
    def recommended_instance_type_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\S{1,24}$", value):
            raise ValueError(r"must validate the regular expression /^\S{1,24}$/")
        return value

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
        """Create an instance of UpdateAmiDeliveryOptionDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of access_endpoint_url
        if self.access_endpoint_url:
            _dict['AccessEndpointUrl'] = self.access_endpoint_url.to_dict()
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
        """Create an instance of UpdateAmiDeliveryOptionDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "UsageInstructions": obj.get("UsageInstructions"),
            "AccessEndpointUrl": AccessEndpointUrl.from_dict(obj["AccessEndpointUrl"]) if obj.get("AccessEndpointUrl") is not None else None,
            "RecommendedInstanceType": obj.get("RecommendedInstanceType"),
            "SecurityGroups": [SecurityGroup.from_dict(_item) for _item in obj["SecurityGroups"]] if obj.get("SecurityGroups") is not None else None
        })
        return _obj


