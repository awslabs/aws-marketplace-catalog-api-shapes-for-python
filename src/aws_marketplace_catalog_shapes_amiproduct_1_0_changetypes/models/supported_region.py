# coding: utf-8

"""
    AmiProduct_1_0_ChangeTypes

        Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved. 

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class SupportedRegion(str, Enum):
    """
    SupportedRegion
    """

    """
    allowed enum values
    """
    ALL = 'All'
    US = 'US'
    NONE = 'None'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SupportedRegion from a JSON string"""
        return cls(json.loads(json_str))

