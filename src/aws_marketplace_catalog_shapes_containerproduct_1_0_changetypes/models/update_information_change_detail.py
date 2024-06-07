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
from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.additional_resource import AdditionalResource
from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.promotional_media import PromotionalMedia
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class UpdateInformationChangeDetail(BaseModel):
    """
    UpdateInformationChangeDetail
    """ # noqa: E501
    product_title: Optional[Annotated[str, Field(strict=True, max_length=72)]] = Field(default=None, alias="ProductTitle")
    short_description: Optional[Annotated[str, Field(strict=True, max_length=1000)]] = Field(default=None, alias="ShortDescription")
    long_description: Optional[Annotated[str, Field(strict=True, max_length=5000)]] = Field(default=None, alias="LongDescription")
    sku: Optional[Annotated[str, Field(strict=True, max_length=5000)]] = Field(default=None, alias="Sku")
    logo_url: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, alias="LogoUrl")
    video_urls: Optional[Annotated[List[Annotated[str, Field(strict=True)]], Field(min_length=0, max_length=1)]] = Field(default=None, alias="VideoUrls")
    promotional_media: Optional[Annotated[List[PromotionalMedia], Field(min_length=0, max_length=15)]] = Field(default=None, alias="PromotionalMedia")
    highlights: Optional[Annotated[List[Annotated[str, Field(min_length=0, strict=True, max_length=500)]], Field(min_length=1, max_length=3)]] = Field(default=None, alias="Highlights")
    additional_resources: Optional[Annotated[List[AdditionalResource], Field(min_length=0, max_length=3)]] = Field(default=None, alias="AdditionalResources")
    support_description: Optional[Annotated[str, Field(strict=True, max_length=2000)]] = Field(default=None, alias="SupportDescription")
    support_resources: Optional[Annotated[List[Annotated[str, Field(strict=True, max_length=2000)]], Field(min_length=0, max_length=3)]] = Field(default=None, alias="SupportResources")
    categories: Optional[Annotated[List[Annotated[str, Field(strict=True)]], Field(min_length=1, max_length=3)]] = Field(default=None, alias="Categories")
    associated_products: Optional[Annotated[List[Annotated[str, Field(strict=True)]], Field(min_length=1, max_length=10)]] = Field(default=None, alias="AssociatedProducts")
    search_keywords: Optional[Annotated[List[Annotated[str, Field(strict=True, max_length=250)]], Field(min_length=1, max_length=5)]] = Field(default=None, alias="SearchKeywords")
    __properties: ClassVar[List[str]] = ["ProductTitle", "ShortDescription", "LongDescription", "Sku", "LogoUrl", "VideoUrls", "PromotionalMedia", "Highlights", "AdditionalResources", "SupportDescription", "SupportResources", "Categories", "AssociatedProducts", "SearchKeywords"]

    @field_validator('product_title')
    def product_title_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\S+[\S\s]*", value):
            raise ValueError(r"must validate the regular expression /^\S+[\S\s]*/")
        return value

    @field_validator('short_description')
    def short_description_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\S+[\S\s]*", value):
            raise ValueError(r"must validate the regular expression /^\S+[\S\s]*/")
        return value

    @field_validator('long_description')
    def long_description_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\S+[\S\s]*", value):
            raise ValueError(r"must validate the regular expression /^\S+[\S\s]*/")
        return value

    @field_validator('sku')
    def sku_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\S+[\S\s]*", value):
            raise ValueError(r"must validate the regular expression /^\S+[\S\s]*/")
        return value

    @field_validator('logo_url')
    def logo_url_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^https:\/\/(www\.)?[-a-zA-Z0-9@._]{1,256}\.[a-zA-Z0-9()]{2,63}\b([-a-zA-Z0-9@_+.\/]*)", value):
            raise ValueError(r"must validate the regular expression /^https:\/\/(www\.)?[-a-zA-Z0-9@._]{1,256}\.[a-zA-Z0-9()]{2,63}\b([-a-zA-Z0-9@_+.\/]*)/")
        return value

    @field_validator('support_description')
    def support_description_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\S+[\S\s]*", value):
            raise ValueError(r"must validate the regular expression /^\S+[\S\s]*/")
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
        """Create an instance of UpdateInformationChangeDetail from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in promotional_media (list)
        _items = []
        if self.promotional_media:
            for _item in self.promotional_media:
                if _item:
                    _items.append(_item.to_dict())
            _dict['PromotionalMedia'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in additional_resources (list)
        _items = []
        if self.additional_resources:
            for _item in self.additional_resources:
                if _item:
                    _items.append(_item.to_dict())
            _dict['AdditionalResources'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of UpdateInformationChangeDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ProductTitle": obj.get("ProductTitle"),
            "ShortDescription": obj.get("ShortDescription"),
            "LongDescription": obj.get("LongDescription"),
            "Sku": obj.get("Sku"),
            "LogoUrl": obj.get("LogoUrl"),
            "VideoUrls": obj.get("VideoUrls"),
            "PromotionalMedia": [PromotionalMedia.from_dict(_item) for _item in obj.get("PromotionalMedia")] if obj.get("PromotionalMedia") is not None else None,
            "Highlights": obj.get("Highlights"),
            "AdditionalResources": [AdditionalResource.from_dict(_item) for _item in obj.get("AdditionalResources")] if obj.get("AdditionalResources") is not None else None,
            "SupportDescription": obj.get("SupportDescription"),
            "SupportResources": obj.get("SupportResources"),
            "Categories": obj.get("Categories"),
            "AssociatedProducts": obj.get("AssociatedProducts"),
            "SearchKeywords": obj.get("SearchKeywords")
        })
        return _obj

