import pytest
import json

def test_importable():
    from aws_marketplace_catalog_shapes_audience_1_0_entitytype.models.audience_entity_detail import AudienceEntityDetail # noqa: F401

    assert True

def test_audience_1_0_entity_detail_deserialization():
    from aws_marketplace_catalog_shapes_audience_1_0_entitytype.models.audience_entity_detail import AudienceEntityDetail

    expected_json = {
        "Name": "Audience for Experience exp-123ab4567",
        "Description": "This Audience is used for a test.",
        "Principals": ["o-orgidfortesting", "ou-123abc-12345abcde"],
        "ExperienceId": "exp-123ab4567"
    }

    actual_detail = AudienceEntityDetail.from_json(json.dumps(expected_json))
    expected_detail = AudienceEntityDetail(
        name="Audience for Experience exp-123ab4567",
        description="This Audience is used for a test.",
        principals=["o-orgidfortesting", "ou-123abc-12345abcde"],
        experience_id="exp-123ab4567"
    )

    assert actual_detail == expected_detail, "Deserialized object does not match expected object"
