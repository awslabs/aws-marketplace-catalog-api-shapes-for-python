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
from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.validity_term_type import ValidityTermType
from typing import Optional, Set
from typing_extensions import Self

class ValidityTerm(BaseModel):
    """
    ValidityTerm
    """ # noqa: E501
    type: ValidityTermType = Field(alias="Type")
    agreement_duration: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, alias="AgreementDuration")
    agreement_start_date: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, alias="AgreementStartDate")
    agreement_end_date: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, alias="AgreementEndDate")
    __properties: ClassVar[List[str]] = ["Type", "AgreementDuration", "AgreementStartDate", "AgreementEndDate"]

    @field_validator('agreement_duration')
    def agreement_duration_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^P(?=.)(\d+Y)?(\d+M)?(\d+D)?$", value):
            raise ValueError(r"must validate the regular expression /^P(?=.)(\d+Y)?(\d+M)?(\d+D)?$/")
        return value

    @field_validator('agreement_start_date')
    def agreement_start_date_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^([1-9]\d{3}-((0[1-9]|1[0-2])-(0[1-9]|1\d|2[0-8])|(0[13-9]|1[0-2])-(29|30)|(0[13578]|1[02])-31)|([1-9]\d(0[48]|[2468][048]|[13579][26])|([2468][048]|[13579][26])00)-02-29)$", value):
            raise ValueError(r"must validate the regular expression /^([1-9]\d{3}-((0[1-9]|1[0-2])-(0[1-9]|1\d|2[0-8])|(0[13-9]|1[0-2])-(29|30)|(0[13578]|1[02])-31)|([1-9]\d(0[48]|[2468][048]|[13579][26])|([2468][048]|[13579][26])00)-02-29)$/")
        return value

    @field_validator('agreement_end_date')
    def agreement_end_date_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^([1-9]\d{3}-((0[1-9]|1[0-2])-(0[1-9]|1\d|2[0-8])|(0[13-9]|1[0-2])-(29|30)|(0[13578]|1[02])-31)|([1-9]\d(0[48]|[2468][048]|[13579][26])|([2468][048]|[13579][26])00)-02-29)$", value):
            raise ValueError(r"must validate the regular expression /^([1-9]\d{3}-((0[1-9]|1[0-2])-(0[1-9]|1\d|2[0-8])|(0[13-9]|1[0-2])-(29|30)|(0[13578]|1[02])-31)|([1-9]\d(0[48]|[2468][048]|[13579][26])|([2468][048]|[13579][26])00)-02-29)$/")
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
        """Create an instance of ValidityTerm from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ValidityTerm from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Type": obj.get("Type"),
            "AgreementDuration": obj.get("AgreementDuration"),
            "AgreementStartDate": obj.get("AgreementStartDate"),
            "AgreementEndDate": obj.get("AgreementEndDate")
        })
        return _obj


