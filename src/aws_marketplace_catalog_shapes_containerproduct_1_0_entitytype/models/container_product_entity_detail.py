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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from pydantic import Field
from aws_marketplace_catalog_shapes_containerproduct_1_0_entitytype.models.description import Description
from aws_marketplace_catalog_shapes_containerproduct_1_0_entitytype.models.dimension import Dimension
from aws_marketplace_catalog_shapes_containerproduct_1_0_entitytype.models.promotional_resources import PromotionalResources
from aws_marketplace_catalog_shapes_containerproduct_1_0_entitytype.models.repository import Repository
from aws_marketplace_catalog_shapes_containerproduct_1_0_entitytype.models.signature_verification_key import SignatureVerificationKey
from aws_marketplace_catalog_shapes_containerproduct_1_0_entitytype.models.support_information import SupportInformation
from aws_marketplace_catalog_shapes_containerproduct_1_0_entitytype.models.targeting import Targeting
from aws_marketplace_catalog_shapes_containerproduct_1_0_entitytype.models.version import Version
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ContainerProductEntityDetail(BaseModel):
    """
    ContainerProductEntityDetail
    """ # noqa: E501
    versions: Optional[List[Version]] = Field(default=None, alias="Versions")
    repositories: Optional[List[Repository]] = Field(default=None, alias="Repositories")
    description: Optional[Description] = Field(default=None, alias="Description")
    promotional_resources: Optional[PromotionalResources] = Field(default=None, alias="PromotionalResources")
    support_information: Optional[SupportInformation] = Field(default=None, alias="SupportInformation")
    dimensions: Optional[List[Dimension]] = Field(default=None, alias="Dimensions")
    targeting: Optional[Targeting] = Field(default=None, alias="Targeting")
    signature_verification_keys: Optional[List[SignatureVerificationKey]] = Field(default=None, alias="SignatureVerificationKeys")
    __properties: ClassVar[List[str]] = ["Versions", "Repositories", "Description", "PromotionalResources", "SupportInformation", "Dimensions", "Targeting", "SignatureVerificationKeys"]

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
        """Create an instance of ContainerProductEntityDetail from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in versions (list)
        _items = []
        if self.versions:
            for _item in self.versions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Versions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in repositories (list)
        _items = []
        if self.repositories:
            for _item in self.repositories:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Repositories'] = _items
        # override the default output from pydantic by calling `to_dict()` of description
        if self.description:
            _dict['Description'] = self.description.to_dict()
        # override the default output from pydantic by calling `to_dict()` of promotional_resources
        if self.promotional_resources:
            _dict['PromotionalResources'] = self.promotional_resources.to_dict()
        # override the default output from pydantic by calling `to_dict()` of support_information
        if self.support_information:
            _dict['SupportInformation'] = self.support_information.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in dimensions (list)
        _items = []
        if self.dimensions:
            for _item in self.dimensions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Dimensions'] = _items
        # override the default output from pydantic by calling `to_dict()` of targeting
        if self.targeting:
            _dict['Targeting'] = self.targeting.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in signature_verification_keys (list)
        _items = []
        if self.signature_verification_keys:
            for _item in self.signature_verification_keys:
                if _item:
                    _items.append(_item.to_dict())
            _dict['SignatureVerificationKeys'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ContainerProductEntityDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Versions": [Version.from_dict(_item) for _item in obj.get("Versions")] if obj.get("Versions") is not None else None,
            "Repositories": [Repository.from_dict(_item) for _item in obj.get("Repositories")] if obj.get("Repositories") is not None else None,
            "Description": Description.from_dict(obj.get("Description")) if obj.get("Description") is not None else None,
            "PromotionalResources": PromotionalResources.from_dict(obj.get("PromotionalResources")) if obj.get("PromotionalResources") is not None else None,
            "SupportInformation": SupportInformation.from_dict(obj.get("SupportInformation")) if obj.get("SupportInformation") is not None else None,
            "Dimensions": [Dimension.from_dict(_item) for _item in obj.get("Dimensions")] if obj.get("Dimensions") is not None else None,
            "Targeting": Targeting.from_dict(obj.get("Targeting")) if obj.get("Targeting") is not None else None,
            "SignatureVerificationKeys": [SignatureVerificationKey.from_dict(_item) for _item in obj.get("SignatureVerificationKeys")] if obj.get("SignatureVerificationKeys") is not None else None
        })
        return _obj


