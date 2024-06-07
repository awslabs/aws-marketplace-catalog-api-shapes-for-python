import pytest
import json

def test_importable():
    from aws_marketplace_catalog_shapes_brandingsettings_1_0_entitytype.models.branding_settings_entity_detail import BrandingSettingsEntityDetail  # noqa: F401
    assert True

def test_brandingsettings_1_0_entity_detail_deserialization():
    from aws_marketplace_catalog_shapes_brandingsettings_1_0_entitytype.models.branding_settings_entity_detail import BrandingSettingsEntityDetail
    from aws_marketplace_catalog_shapes_brandingsettings_1_0_entitytype.models.configuration import Configuration

    expected_json = {
        "Name": "SampleBranding",
        "Description": "Sample Branding Description",
        "Configuration": {
            "Title": "My Company",
            "Information": "Custom branding welcome message",
            "ThemeColor": "#232f3e",
            "LogoUrl": "https://mybucket.s3.us-east-1.amazonaws.com/test.jpg"
        }
    }

    actual_detail = BrandingSettingsEntityDetail.from_json(json.dumps(expected_json))
    expected_detail = BrandingSettingsEntityDetail(
        name="SampleBranding",
        description="Sample Branding Description",
        configuration=Configuration(
            title="My Company",
            information="Custom branding welcome message",
            theme_color="#232f3e",
            logo_url="https://mybucket.s3.us-east-1.amazonaws.com/test.jpg"
        )
    )

    assert actual_detail == expected_detail, "Deserialized object does not match expected object"
