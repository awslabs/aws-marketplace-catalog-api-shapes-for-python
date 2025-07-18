# coding: utf-8

"""
    Offer_1_0_Appendix

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
from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.currency_code import CurrencyCode
from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.fixed_upfront_pricing_term_type import FixedUpfrontPricingTermType
from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.grant_item import GrantItem
from typing import Optional, Set
from typing_extensions import Self

class FixedUpfrontPricingTerm(BaseModel):
    """
    FixedUpfrontPricingTerm
    """ # noqa: E501
    type: FixedUpfrontPricingTermType = Field(alias="Type")
    currency_code: CurrencyCode = Field(alias="CurrencyCode")
    price: Annotated[str, Field(strict=True)] = Field(alias="Price")
    grants: Annotated[List[GrantItem], Field(min_length=1, max_length=800)] = Field(description="MaxQuantity is required", alias="Grants")
    duration: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, alias="Duration")
    __properties: ClassVar[List[str]] = ["Type", "CurrencyCode", "Price", "Grants", "Duration"]

    @field_validator('price')
    def price_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^((100000000(\.0{0,3})?)|(\d{1,8}(\.\d{0,3})?))$", value):
            raise ValueError(r"must validate the regular expression /^((100000000(\.0{0,3})?)|(\d{1,8}(\.\d{0,3})?))$/")
        return value

    @field_validator('duration')
    def duration_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^P(?=.)(\d+Y)?(\d+M)?(\d+D)?$", value):
            raise ValueError(r"must validate the regular expression /^P(?=.)(\d+Y)?(\d+M)?(\d+D)?$/")
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
        """Create an instance of FixedUpfrontPricingTerm from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in grants (list)
        _items = []
        if self.grants:
            for _item_grants in self.grants:
                if _item_grants:
                    _items.append(_item_grants.to_dict())
            _dict['Grants'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FixedUpfrontPricingTerm from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Type": obj.get("Type"),
            "CurrencyCode": obj.get("CurrencyCode"),
            "Price": obj.get("Price"),
            "Grants": [GrantItem.from_dict(_item) for _item in obj["Grants"]] if obj.get("Grants") is not None else None,
            "Duration": obj.get("Duration")
        })
        return _obj


