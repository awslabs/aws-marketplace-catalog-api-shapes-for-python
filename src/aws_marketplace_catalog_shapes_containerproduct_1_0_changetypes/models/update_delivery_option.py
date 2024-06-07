# coding: utf-8

"""
    ContainerProduct_1_0_ChangeTypes

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
from pydantic import BaseModel, field_validator
from pydantic import Field
from typing_extensions import Annotated
from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.update_delivery_options_details import UpdateDeliveryOptionsDetails
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class UpdateDeliveryOption(BaseModel):
    """
    UpdateDeliveryOption
    """ # noqa: E501
    id: Annotated[str, Field(strict=True, max_length=36)] = Field(alias="Id")
    details: Optional[UpdateDeliveryOptionsDetails] = Field(default=None, alias="Details")
    __properties: ClassVar[List[str]] = ["Id", "Details"]

    @field_validator('id')
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"([a-f0-9]{8}(-[a-f0-9]{4}){4}[a-f0-9]{8})", value):
            raise ValueError(r"must validate the regular expression /([a-f0-9]{8}(-[a-f0-9]{4}){4}[a-f0-9]{8})/")
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
        """Create an instance of UpdateDeliveryOption from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of details
        if self.details:
            _dict['Details'] = self.details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of UpdateDeliveryOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Id": obj.get("Id"),
            "Details": UpdateDeliveryOptionsDetails.from_dict(obj.get("Details")) if obj.get("Details") is not None else None
        })
        return _obj


