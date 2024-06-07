# coding: utf-8

"""
    ResaleAuthorization_1_0_ChangeTypes

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
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CreateResaleAuthorizationChangeDetail(BaseModel):
    """
    CreateResaleAuthorizationChangeDetail
    """ # noqa: E501
    name: Annotated[str, Field(min_length=1, strict=True, max_length=100)] = Field(alias="Name")
    description: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = Field(default=None, alias="Description")
    product_id: Annotated[str, Field(min_length=1, strict=True, max_length=50)] = Field(alias="ProductId")
    reseller_account_id: Annotated[str, Field(strict=True)] = Field(alias="ResellerAccountId")
    __properties: ClassVar[List[str]] = ["Name", "Description", "ProductId", "ResellerAccountId"]

    @field_validator('name')
    def name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^\S+[\S\s]*$", value):
            raise ValueError(r"must validate the regular expression /^\S+[\S\s]*$/")
        return value

    @field_validator('description')
    def description_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[\S\s]*$", value):
            raise ValueError(r"must validate the regular expression /^[\S\s]*$/")
        return value

    @field_validator('reseller_account_id')
    def reseller_account_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^\d{12}$", value):
            raise ValueError(r"must validate the regular expression /^\d{12}$/")
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
        """Create an instance of CreateResaleAuthorizationChangeDetail from a JSON string"""
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
        """Create an instance of CreateResaleAuthorizationChangeDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Name": obj.get("Name"),
            "Description": obj.get("Description"),
            "ProductId": obj.get("ProductId"),
            "ResellerAccountId": obj.get("ResellerAccountId")
        })
        return _obj


