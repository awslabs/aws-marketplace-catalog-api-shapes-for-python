import pytest
import json

def test_importable():
    from aws_marketplace_catalog_shapes_experience_1_0_entitytype.models.experience_entity_detail import ExperienceEntityDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_experience_1_0_changetypes.models.create_experience_change_detail import CreateExperienceChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_experience_1_0_changetypes.models.update_experience_change_detail import UpdateExperienceChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_experience_1_0_changetypes.models.allow_product_procurement_change_detail import AllowProductProcurementChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_experience_1_0_changetypes.models.deny_product_procurement_change_detail import DenyProductProcurementChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_experience_1_0_changetypes.models.create_procurement_policy_change_detail import CreateProcurementPolicyChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_experience_1_0_changetypes.models.update_procurement_policy_change_detail import UpdateProcurementPolicyChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_experience_1_0_changetypes.models.create_branding_settings_change_detail import CreateBrandingSettingsChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_experience_1_0_changetypes.models.update_branding_settings_change_detail import UpdateBrandingSettingsChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_experience_1_0_changetypes.models.associate_audience_change_detail import AssociateAudienceChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_experience_1_0_changetypes.models.disassociate_audience_change_detail import DisassociateAudienceChangeDetail  # noqa: F401

    assert True

def test_experience_1_0_entity_detail_deserialization():
    from aws_marketplace_catalog_shapes_experience_1_0_entitytype.models.experience_entity_detail import ExperienceEntityDetail

    expected_json = {
        "Name": "SampleExperience",
        "Description": "Sample Experience",
        "Status": "Enabled",
        "AdminStatus": "Editable",
        "ProcurementPolicies": ["procpolicy-abcdef12345"],
        "DiscoveryPolicies": ["discopolicy-abcdef12345"],
        "BrandingSettings": ["brandsettings-abcdef12345"],
        "Integration": "integ-abcdefgh12345"
    }

    actual_detail = ExperienceEntityDetail.from_json(json.dumps(expected_json))
    expected_detail = ExperienceEntityDetail(
        name="SampleExperience",
        description="Sample Experience",
        status="Enabled",
        admin_status="Editable",
        procurement_policies=["procpolicy-abcdef12345"],
        discovery_policies=["discopolicy-abcdef12345"],
        branding_settings=["brandsettings-abcdef12345"],
        integration="integ-abcdefgh12345"
    )

    assert actual_detail == expected_detail, "Deserialized object does not match expected object"

def test_create_experience_change_detail_serialization():
    from aws_marketplace_catalog_shapes_experience_1_0_changetypes.models.create_experience_change_detail import CreateExperienceChangeDetail

    create_experience_change_detail = CreateExperienceChangeDetail(
        name="MyExperience",
        description="Creating a new experience",
        catalog="aws-mp-commercial-prod"
    )
    actual_json = create_experience_change_detail.to_json()
    expected_json = {
        "Name": "MyExperience",
        "Description": "Creating a new experience",
        "Catalog": "aws-mp-commercial-prod"
    }

    assert actual_json == json.dumps(expected_json), "Generated CreateExperienceChangeDetail does not match expected json"

def test_update_experience_change_detail_serialization():
    from aws_marketplace_catalog_shapes_experience_1_0_changetypes.models.update_experience_change_detail import UpdateExperienceChangeDetail
    from aws_marketplace_catalog_shapes_experience_1_0_changetypes.models.status import Status

    update_experience_change_detail = UpdateExperienceChangeDetail(
        name="MyExperience",
        description="Creating a new experience",
        status=Status.ENABLED
    )
    actual_json = update_experience_change_detail.to_json()
    expected_json = {
        "Name": "MyExperience",
        "Description": "Creating a new experience",
        "Status": "Enabled"
    }

    assert actual_json == json.dumps(expected_json), "Generated UpdateExperienceChangeDetail does not match expected json"

def test_restrict_experience_change_detail_serialization():
    from aws_marketplace_catalog_shapes_experience_1_0_changetypes.models.restrict_experience_change_detail import RestrictExperienceChangeDetail

    restrict_experience_change_detail = RestrictExperienceChangeDetail()
    actual_json = restrict_experience_change_detail.to_json()
    expected_json = {}

    assert actual_json == json.dumps(expected_json), "Generated RestrictExperienceChangeDetail does not match expected json"

def test_revive_experience_change_detail_serialization():
    from aws_marketplace_catalog_shapes_experience_1_0_changetypes.models.revive_experience_change_detail import ReviveExperienceChangeDetail

    revive_experience_change_detail = ReviveExperienceChangeDetail()
    actual_json = revive_experience_change_detail.to_json()
    expected_json = {}

    assert actual_json == json.dumps(expected_json), "Generated ReviveExperienceChangeDetail does not match expected json"

def test_allow_product_procurement_change_detail_serialization():
    from aws_marketplace_catalog_shapes_experience_1_0_changetypes.models.allow_product_procurement_change_detail import AllowProductProcurementChangeDetail
    from aws_marketplace_catalog_shapes_experience_1_0_changetypes.models.product import Product

    allow_product_procurement_change_detail = AllowProductProcurementChangeDetail(
        products=[
            Product(
                ids=["example-1234-abcd-5678-90abcded1234", "example-1234-abcd-5678-90abcded4321"],
                notes="Useful product"
            ),
            Product(
                ids=["example-1234-abcd-5678-90abcded9876"],
            )
        ]
    )
    actual_json = allow_product_procurement_change_detail.to_json()
    expected_json = {
        "Products": [{
            "Ids": ["example-1234-abcd-5678-90abcded1234", "example-1234-abcd-5678-90abcded4321"],
            "Notes": "Useful product"
        }, {
            "Ids": ["example-1234-abcd-5678-90abcded9876"]
        }]
    }

    assert actual_json == json.dumps(expected_json), "Generated AllowProductProcurementChangeDetail does not match expected json"

def test_deny_product_procurement_change_detail_serialization():
    from aws_marketplace_catalog_shapes_experience_1_0_changetypes.models.deny_product_procurement_change_detail import DenyProductProcurementChangeDetail
    from aws_marketplace_catalog_shapes_experience_1_0_changetypes.models.product import Product

    deny_product_procurement_change_detail = DenyProductProcurementChangeDetail(
        products=[
            Product(
                ids=["example-1234-abcd-5678-90abcded1234", "example-1234-abcd-5678-90abcded4321"],
                notes="Useful product"
            ),
            Product(
                ids=["example-1234-abcd-5678-90abcded9876"],
            )
        ]
    )
    actual_json = deny_product_procurement_change_detail.to_json()
    expected_json = {
        "Products": [{
            "Ids": ["example-1234-abcd-5678-90abcded1234", "example-1234-abcd-5678-90abcded4321"],
            "Notes": "Useful product"
        }, {
            "Ids": ["example-1234-abcd-5678-90abcded9876"]
        }]
    }

    assert actual_json == json.dumps(expected_json), "Generated DenyProductProcurementChangeDetail does not match expected json"

def test_create_procurement_policy_change_detail_serialization():
    from aws_marketplace_catalog_shapes_experience_1_0_changetypes.models.create_procurement_policy_change_detail import CreateProcurementPolicyChangeDetail
    from aws_marketplace_catalog_shapes_experience_1_0_changetypes.models.procurement_policy_configuration import ProcurementPolicyConfiguration
    from aws_marketplace_catalog_shapes_experience_1_0_changetypes.models.policy_resource_requests import PolicyResourceRequests

    create_procurement_policy_change_detail = CreateProcurementPolicyChangeDetail(
        name="Developer Policy",
        description="Procurement policy used for developers",
        configuration=ProcurementPolicyConfiguration(policy_resource_requests=PolicyResourceRequests.ALLOW)
    )
    actual_json = create_procurement_policy_change_detail.to_json()
    expected_json = {
        "Name": "Developer Policy",
        "Description": "Procurement policy used for developers",
        "Configuration": {
            "PolicyResourceRequests": "Allow"
        }
    }

    assert actual_json == json.dumps(expected_json), "Generated CreateProcurementPolicyChangeDetail does not match expected json"

def test_update_procurement_policy_change_detail_serialization():
    from aws_marketplace_catalog_shapes_experience_1_0_changetypes.models.update_procurement_policy_change_detail import UpdateProcurementPolicyChangeDetail
    from aws_marketplace_catalog_shapes_experience_1_0_changetypes.models.procurement_policy_configuration import ProcurementPolicyConfiguration
    from aws_marketplace_catalog_shapes_experience_1_0_changetypes.models.policy_resource_requests import PolicyResourceRequests

    update_procurement_policy_change_detail = UpdateProcurementPolicyChangeDetail(
        name="Developer Policy",
        description="Procurement policy used for developers",
        configuration=ProcurementPolicyConfiguration(policy_resource_requests=PolicyResourceRequests.ALLOW)
    )
    actual_json = update_procurement_policy_change_detail.to_json()
    expected_json = {
        "Name": "Developer Policy",
        "Description": "Procurement policy used for developers",
        "Configuration": {
            "PolicyResourceRequests": "Allow"
        }
    }

    assert actual_json == json.dumps(expected_json), "Generated UpdateProcurementPolicyChangeDetail does not match expected json"

def test_create_branding_settings_change_detail_serialization():
    from aws_marketplace_catalog_shapes_experience_1_0_changetypes.models.create_branding_settings_change_detail import CreateBrandingSettingsChangeDetail
    from aws_marketplace_catalog_shapes_experience_1_0_changetypes.models.branding_configuration import BrandingConfiguration

    create_branding_settings_change_detail = CreateBrandingSettingsChangeDetail(
        name="SampleBranding",
        description="Sample Branding Description",
        configuration=BrandingConfiguration(
            title="Company Title",
            information="Information",
            theme_color="#232f3e",
            logo_url="https://mybucket.s3.us-east-1.amazonaws.com/test.jpg"
        )
    )
    actual_json = create_branding_settings_change_detail.to_json()
    expected_json = {
        "Name": "SampleBranding",
        "Description": "Sample Branding Description",
        "Configuration": {
            "Title": "Company Title",
            "Information": "Information",
            "ThemeColor": "#232f3e",
            "LogoUrl": "https://mybucket.s3.us-east-1.amazonaws.com/test.jpg"
        }
    }

    assert actual_json == json.dumps(expected_json), "Generated CreateBrandingSettingsChangeDetail does not match expected json"

def test_update_branding_settings_change_detail_serialization():
    from aws_marketplace_catalog_shapes_experience_1_0_changetypes.models.update_branding_settings_change_detail import UpdateBrandingSettingsChangeDetail
    from aws_marketplace_catalog_shapes_experience_1_0_changetypes.models.branding_configuration import BrandingConfiguration

    update_branding_settings_change_detail = UpdateBrandingSettingsChangeDetail(
        name="SampleBranding",
        description="Sample Branding Description",
        configuration=BrandingConfiguration(
            title="Company Title",
            information="Information",
            theme_color="#232f3e",
            logo_url="https://mybucket.s3.us-east-1.amazonaws.com/test.jpg"
        )
    )
    actual_json = update_branding_settings_change_detail.to_json()
    expected_json = {
        "Name": "SampleBranding",
        "Description": "Sample Branding Description",
        "Configuration": {
            "Title": "Company Title",
            "Information": "Information",
            "ThemeColor": "#232f3e",
            "LogoUrl": "https://mybucket.s3.us-east-1.amazonaws.com/test.jpg"
        }
    }

    assert actual_json == json.dumps(expected_json), "Generated UpdateBrandingSettingsChangeDetail does not match expected json"

def test_associate_audience_change_detail_serialization():
    from aws_marketplace_catalog_shapes_experience_1_0_changetypes.models.associate_audience_change_detail import AssociateAudienceChangeDetail

    associate_audience_change_detail = AssociateAudienceChangeDetail(
        name="Name for Audience",
        description="This Audience is used for a test.",
        principals={"123456789012"}
    )
    actual_json = associate_audience_change_detail.to_json()
    expected_json = {
        "Name": "Name for Audience",
        "Description": "This Audience is used for a test.",
        "Principals": ["123456789012"]
    }

    assert actual_json == json.dumps(expected_json), "Generated AssociateAudienceChangeDetail does not match expected json"

def test_disassociate_audience_change_detail_serialization():
    from aws_marketplace_catalog_shapes_experience_1_0_changetypes.models.disassociate_audience_change_detail import DisassociateAudienceChangeDetail

    disassociate_audience_change_detail = DisassociateAudienceChangeDetail(principals={"123456789012"})
    actual_json = disassociate_audience_change_detail.to_json()
    expected_json = {
        "Principals": ["123456789012"]
    }

    assert actual_json == json.dumps(expected_json), "Generated DisassociateAudienceChangeDetail does not match expected json"
