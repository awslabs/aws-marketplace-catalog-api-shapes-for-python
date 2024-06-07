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
from pydantic import BaseModel
from pydantic import Field
from typing_extensions import Annotated
from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.update_delivery_option_visibility import UpdateDeliveryOptionVisibility
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class UpdateDeliveryOptionsVisibilityChangeDetail(BaseModel):
    """
    UpdateDeliveryOptionsVisibilityChangeDetail
    """ # noqa: E501
    delivery_options: Annotated[List[UpdateDeliveryOptionVisibility], Field(max_length=2)] = Field(alias="DeliveryOptions")
    __properties: ClassVar[List[str]] = ["DeliveryOptions"]

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
        """Create an instance of UpdateDeliveryOptionsVisibilityChangeDetail from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in delivery_options (list)
        _items = []
        if self.delivery_options:
            for _item in self.delivery_options:
                if _item:
                    _items.append(_item.to_dict())
            _dict['DeliveryOptions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of UpdateDeliveryOptionsVisibilityChangeDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "DeliveryOptions": [UpdateDeliveryOptionVisibility.from_dict(_item) for _item in obj.get("DeliveryOptions")] if obj.get("DeliveryOptions") is not None else None
        })
        return _obj


