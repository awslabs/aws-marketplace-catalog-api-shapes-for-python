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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from aws_marketplace_catalog_shapes_resaleauthorization_1_0_entitytype.models.dimension import Dimension
from aws_marketplace_catalog_shapes_resaleauthorization_1_0_entitytype.models.offer_details import OfferDetails
from aws_marketplace_catalog_shapes_resaleauthorization_1_0_entitytype.models.pre_existing_buyer_agreement import PreExistingBuyerAgreement
from aws_marketplace_catalog_shapes_resaleauthorization_1_0_entitytype.models.rule import Rule
from aws_marketplace_catalog_shapes_resaleauthorization_1_0_entitytype.models.term import Term
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ResaleAuthorizationEntityDetail(BaseModel):
    """
    ResaleAuthorizationEntityDetail
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, alias="Name")
    description: Optional[StrictStr] = Field(default=None, alias="Description")
    product_id: Optional[StrictStr] = Field(default=None, alias="ProductId")
    product_name: Optional[StrictStr] = Field(default=None, alias="ProductName")
    status: Optional[StrictStr] = Field(default=None, alias="Status")
    pre_existing_buyer_agreement: Optional[PreExistingBuyerAgreement] = Field(default=None, alias="PreExistingBuyerAgreement")
    dimensions: Optional[List[Dimension]] = Field(default=None, alias="Dimensions")
    offer_details: Optional[OfferDetails] = Field(default=None, alias="OfferDetails")
    terms: Optional[List[Term]] = Field(default=None, alias="Terms")
    rules: Optional[List[Rule]] = Field(default=None, alias="Rules")
    created_date: Optional[StrictStr] = Field(default=None, alias="CreatedDate")
    manufacturer_legal_name: Optional[StrictStr] = Field(default=None, alias="ManufacturerLegalName")
    manufacturer_account_id: Optional[StrictStr] = Field(default=None, alias="ManufacturerAccountId")
    __properties: ClassVar[List[str]] = ["Name", "Description", "ProductId", "ProductName", "Status", "PreExistingBuyerAgreement", "Dimensions", "OfferDetails", "Terms", "Rules", "CreatedDate", "ManufacturerLegalName", "ManufacturerAccountId"]

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
        """Create an instance of ResaleAuthorizationEntityDetail from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of pre_existing_buyer_agreement
        if self.pre_existing_buyer_agreement:
            _dict['PreExistingBuyerAgreement'] = self.pre_existing_buyer_agreement.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in dimensions (list)
        _items = []
        if self.dimensions:
            for _item in self.dimensions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Dimensions'] = _items
        # override the default output from pydantic by calling `to_dict()` of offer_details
        if self.offer_details:
            _dict['OfferDetails'] = self.offer_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in terms (list)
        _items = []
        if self.terms:
            for _item in self.terms:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Terms'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in rules (list)
        _items = []
        if self.rules:
            for _item in self.rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Rules'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ResaleAuthorizationEntityDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Name": obj.get("Name"),
            "Description": obj.get("Description"),
            "ProductId": obj.get("ProductId"),
            "ProductName": obj.get("ProductName"),
            "Status": obj.get("Status"),
            "PreExistingBuyerAgreement": PreExistingBuyerAgreement.from_dict(obj.get("PreExistingBuyerAgreement")) if obj.get("PreExistingBuyerAgreement") is not None else None,
            "Dimensions": [Dimension.from_dict(_item) for _item in obj.get("Dimensions")] if obj.get("Dimensions") is not None else None,
            "OfferDetails": OfferDetails.from_dict(obj.get("OfferDetails")) if obj.get("OfferDetails") is not None else None,
            "Terms": [Term.from_dict(_item) for _item in obj.get("Terms")] if obj.get("Terms") is not None else None,
            "Rules": [Rule.from_dict(_item) for _item in obj.get("Rules")] if obj.get("Rules") is not None else None,
            "CreatedDate": obj.get("CreatedDate"),
            "ManufacturerLegalName": obj.get("ManufacturerLegalName"),
            "ManufacturerAccountId": obj.get("ManufacturerAccountId")
        })
        return _obj


