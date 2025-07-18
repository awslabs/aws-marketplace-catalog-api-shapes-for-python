# coding: utf-8

"""
    ContainerProduct_1_0_EntityType

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
from aws_marketplace_catalog_shapes_containerproduct_1_0_entitytype.models.delivery_option import DeliveryOption
from aws_marketplace_catalog_shapes_containerproduct_1_0_entitytype.models.source import Source
from typing import Optional, Set
from typing_extensions import Self

class Version(BaseModel):
    """
    Version
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, alias="Id")
    release_notes: Optional[StrictStr] = Field(default=None, alias="ReleaseNotes")
    upgrade_instructions: Optional[StrictStr] = Field(default=None, alias="UpgradeInstructions")
    version_title: Optional[StrictStr] = Field(default=None, alias="VersionTitle")
    creation_date: Optional[StrictStr] = Field(default=None, alias="CreationDate")
    sources: Optional[List[Source]] = Field(default=None, alias="Sources")
    delivery_options: Optional[List[DeliveryOption]] = Field(default=None, alias="DeliveryOptions")
    __properties: ClassVar[List[str]] = ["Id", "ReleaseNotes", "UpgradeInstructions", "VersionTitle", "CreationDate", "Sources", "DeliveryOptions"]

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
        """Create an instance of Version from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in sources (list)
        _items = []
        if self.sources:
            for _item_sources in self.sources:
                if _item_sources:
                    _items.append(_item_sources.to_dict())
            _dict['Sources'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in delivery_options (list)
        _items = []
        if self.delivery_options:
            for _item_delivery_options in self.delivery_options:
                if _item_delivery_options:
                    _items.append(_item_delivery_options.to_dict())
            _dict['DeliveryOptions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Version from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Id": obj.get("Id"),
            "ReleaseNotes": obj.get("ReleaseNotes"),
            "UpgradeInstructions": obj.get("UpgradeInstructions"),
            "VersionTitle": obj.get("VersionTitle"),
            "CreationDate": obj.get("CreationDate"),
            "Sources": [Source.from_dict(_item) for _item in obj["Sources"]] if obj.get("Sources") is not None else None,
            "DeliveryOptions": [DeliveryOption.from_dict(_item) for _item in obj["DeliveryOptions"]] if obj.get("DeliveryOptions") is not None else None
        })
        return _obj


