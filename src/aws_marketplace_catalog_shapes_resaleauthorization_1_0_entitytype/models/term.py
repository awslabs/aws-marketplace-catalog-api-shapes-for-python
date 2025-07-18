# coding: utf-8

"""
    ResaleAuthorization_1_0_EntityType

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
from aws_marketplace_catalog_shapes_resaleauthorization_1_0_entitytype.models.document import Document
from aws_marketplace_catalog_shapes_resaleauthorization_1_0_entitytype.models.grant import Grant
from aws_marketplace_catalog_shapes_resaleauthorization_1_0_entitytype.models.positive_targeting import PositiveTargeting
from aws_marketplace_catalog_shapes_resaleauthorization_1_0_entitytype.models.rate_cards import RateCards
from aws_marketplace_catalog_shapes_resaleauthorization_1_0_entitytype.models.schedule import Schedule
from typing import Optional, Set
from typing_extensions import Self

class Term(BaseModel):
    """
    Term
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, alias="Type")
    id: Optional[StrictStr] = Field(default=None, alias="Id")
    positive_targeting: Optional[PositiveTargeting] = Field(default=None, alias="PositiveTargeting")
    documents: Optional[List[Document]] = Field(default=None, alias="Documents")
    maximum_agreement_start_date: Optional[StrictStr] = Field(default=None, alias="MaximumAgreementStartDate")
    currency_code: Optional[StrictStr] = Field(default=None, alias="CurrencyCode")
    rate_cards: Optional[List[RateCards]] = Field(default=None, alias="RateCards")
    duration: Optional[StrictStr] = Field(default=None, alias="Duration")
    price: Optional[StrictStr] = Field(default=None, alias="Price")
    grants: Optional[List[Grant]] = Field(default=None, alias="Grants")
    schedule: Optional[List[Schedule]] = Field(default=None, alias="Schedule")
    __properties: ClassVar[List[str]] = ["Type", "Id", "PositiveTargeting", "Documents", "MaximumAgreementStartDate", "CurrencyCode", "RateCards", "Duration", "Price", "Grants", "Schedule"]

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
        """Create an instance of Term from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of positive_targeting
        if self.positive_targeting:
            _dict['PositiveTargeting'] = self.positive_targeting.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in documents (list)
        _items = []
        if self.documents:
            for _item_documents in self.documents:
                if _item_documents:
                    _items.append(_item_documents.to_dict())
            _dict['Documents'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in rate_cards (list)
        _items = []
        if self.rate_cards:
            for _item_rate_cards in self.rate_cards:
                if _item_rate_cards:
                    _items.append(_item_rate_cards.to_dict())
            _dict['RateCards'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in grants (list)
        _items = []
        if self.grants:
            for _item_grants in self.grants:
                if _item_grants:
                    _items.append(_item_grants.to_dict())
            _dict['Grants'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in schedule (list)
        _items = []
        if self.schedule:
            for _item_schedule in self.schedule:
                if _item_schedule:
                    _items.append(_item_schedule.to_dict())
            _dict['Schedule'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Term from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Type": obj.get("Type"),
            "Id": obj.get("Id"),
            "PositiveTargeting": PositiveTargeting.from_dict(obj["PositiveTargeting"]) if obj.get("PositiveTargeting") is not None else None,
            "Documents": [Document.from_dict(_item) for _item in obj["Documents"]] if obj.get("Documents") is not None else None,
            "MaximumAgreementStartDate": obj.get("MaximumAgreementStartDate"),
            "CurrencyCode": obj.get("CurrencyCode"),
            "RateCards": [RateCards.from_dict(_item) for _item in obj["RateCards"]] if obj.get("RateCards") is not None else None,
            "Duration": obj.get("Duration"),
            "Price": obj.get("Price"),
            "Grants": [Grant.from_dict(_item) for _item in obj["Grants"]] if obj.get("Grants") is not None else None,
            "Schedule": [Schedule.from_dict(_item) for _item in obj["Schedule"]] if obj.get("Schedule") is not None else None
        })
        return _obj


