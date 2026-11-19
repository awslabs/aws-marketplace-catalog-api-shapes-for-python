import json


def test_importable():
    from aws_marketplace_catalog_shapes_product_1_0_entitytype.models.product_entity_detail import ProductEntityDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.create_product_change_detail import CreateProductChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.release_product_change_detail import ReleaseProductChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.update_information_change_detail import UpdateInformationChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.update_visibility_change_detail import UpdateVisibilityChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.update_targeting_change_detail import UpdateTargetingChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.add_dimension_change_detail import AddDimensionChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.update_dimension_change_detail import UpdateDimensionChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.restrict_dimension_change_detail import RestrictDimensionChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.update_buyer_engagement_option_change_detail import UpdateBuyerEngagementOptionChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.add_delivery_option_change_detail import AddDeliveryOptionChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.update_delivery_option_change_detail import UpdateDeliveryOptionChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.update_hosting_architecture_change_detail import UpdateHostingArchitectureChangeDetail  # noqa: F401

    assert True


def test_product_1_0_entity_detail_deserialization():
    from aws_marketplace_catalog_shapes_product_1_0_entitytype.models.product_entity_detail import ProductEntityDetail
    from aws_marketplace_catalog_shapes_product_1_0_entitytype.models.description import Description
    from aws_marketplace_catalog_shapes_product_1_0_entitytype.models.promotional_resources import PromotionalResources
    from aws_marketplace_catalog_shapes_product_1_0_entitytype.models.video import Video
    from aws_marketplace_catalog_shapes_product_1_0_entitytype.models.additional_resource import AdditionalResource
    from aws_marketplace_catalog_shapes_product_1_0_entitytype.models.support_information import SupportInformation
    from aws_marketplace_catalog_shapes_product_1_0_entitytype.models.dimension import Dimension
    from aws_marketplace_catalog_shapes_product_1_0_entitytype.models.targeting import Targeting
    from aws_marketplace_catalog_shapes_product_1_0_entitytype.models.positive_targeting import PositiveTargeting
    from aws_marketplace_catalog_shapes_product_1_0_entitytype.models.buyer_engagement_option import BuyerEngagementOption
    from aws_marketplace_catalog_shapes_product_1_0_entitytype.models.version import Version
    from aws_marketplace_catalog_shapes_product_1_0_entitytype.models.delivery_option import DeliveryOption
    from aws_marketplace_catalog_shapes_product_1_0_entitytype.models.delivery_option_details import DeliveryOptionDetails
    from aws_marketplace_catalog_shapes_product_1_0_entitytype.models.delivery_option_detail import DeliveryOptionDetail
    from aws_marketplace_catalog_shapes_product_1_0_entitytype.models.hosting_architecture import HostingArchitecture
    from aws_marketplace_catalog_shapes_product_1_0_entitytype.models.platform import Platform

    entity_json = {
        "Description": {
            "ProductTitle": "Test Product",
            "ProductCode": "5cqs4jta6m2iuh6jak7s7bjsy",
            "ShortDescription": "Test Product",
            "LongDescription": "Test product long description",
            "Sku": "SKU",
            "Highlights": ["Highlight"],
            "SearchKeywords": ["example", "keywords"],
            "Visibility": "Limited",
            "ReplacementProductId": "prod-1234567890123",
            "ProductState": "Active",
            "Categories": ["Source Control"]
        },
        "PromotionalResources": {
            "LogoUrl": "https://s3.amazonaws.com/awsmp-logos/logo.png",
            "Videos": [{
                "Type": "Link",
                "Title": "Product Video",
                "Url": "https://s3.amazonaws.com/awsmp-media/video.mp4"
            }],
            "AdditionalResources": [{
                "Type": "Link",
                "Text": "Sample Resource",
                "Url": "https://amazon.com"
            }]
        },
        "SupportInformation": {
            "Description": "Product support information"
        },
        "Dimensions": [{
            "Name": "Premium Tier",
            "Description": "Premium tier access",
            "Key": "PremiumTier",
            "Unit": "Units",
            "Types": ["Entitled"]
        }, {
            "Name": "API Calls",
            "Description": "Number of API calls",
            "Key": "ApiCalls",
            "Unit": "Requests",
            "Types": ["Metered", "ExternallyMetered"]
        }],
        "Targeting": {
            "PositiveTargeting": {
                "BuyerAccounts": ["123456789012"]
            }
        },
        "BuyerEngagement": [
            {"EngagementOption": "RequestProductDemo"},
            {"EngagementOption": "RequestPrivateOffer"}
        ],
        "Versions": [{
            "Id": "version-57xgyhrofhrqm",
            "DeliveryOptions": [{
                "Id": "do-abcdefghijklm",
                "Type": "example-delivery-option-type",
                "Details": {
                    "DeliveryOptionDetails": {
                        "UsageInstructions": "Instructions to configure the product.",
                        "CreationDate": "2026-01-15T10:30:00.000Z"
                    }
                },
                "HostingArchitecture": {
                    "ArchitectureDiagramUrl": "https://s3.amazonaws.com/example-bucket/architecture.png",
                    "Platforms": [{
                        "Provider": "AWS",
                        "Component": "CONTROL_PLANE",
                        "EnvironmentOwner": "PARTNER"
                    }, {
                        "Provider": "AWS",
                        "Component": "APPLICATION_PLANE",
                        "EnvironmentOwner": "BUYER"
                    }]
                }
            }]
        }]
    }

    actual_detail = ProductEntityDetail.from_json(json.dumps(entity_json))
    expected_detail = ProductEntityDetail(
        description=Description(
            product_title="Test Product",
            product_code="5cqs4jta6m2iuh6jak7s7bjsy",
            short_description="Test Product",
            long_description="Test product long description",
            sku="SKU",
            highlights=["Highlight"],
            search_keywords=["example", "keywords"],
            visibility="Limited",
            replacement_product_id="prod-1234567890123",
            product_state="Active",
            categories=["Source Control"]
        ),
        promotional_resources=PromotionalResources(
            logo_url="https://s3.amazonaws.com/awsmp-logos/logo.png",
            videos=[Video(
                type="Link",
                title="Product Video",
                url="https://s3.amazonaws.com/awsmp-media/video.mp4"
            )],
            additional_resources=[AdditionalResource(
                type="Link",
                text="Sample Resource",
                url="https://amazon.com"
            )]
        ),
        support_information=SupportInformation(description="Product support information"),
        dimensions=[
            Dimension(
                name="Premium Tier",
                description="Premium tier access",
                key="PremiumTier",
                unit="Units",
                types=["Entitled"]
            ),
            Dimension(
                name="API Calls",
                description="Number of API calls",
                key="ApiCalls",
                unit="Requests",
                types=["Metered", "ExternallyMetered"]
            )
        ],
        targeting=Targeting(
            positive_targeting=PositiveTargeting(buyer_accounts=["123456789012"])
        ),
        buyer_engagement=[
            BuyerEngagementOption(engagement_option="RequestProductDemo"),
            BuyerEngagementOption(engagement_option="RequestPrivateOffer")
        ],
        versions=[
            Version(
                id="version-57xgyhrofhrqm",
                delivery_options=[
                    DeliveryOption(
                        id="do-abcdefghijklm",
                        type="example-delivery-option-type",
                        details=DeliveryOptionDetails(
                            delivery_option_details=DeliveryOptionDetail(
                                usage_instructions="Instructions to configure the product.",
                                creation_date="2026-01-15T10:30:00.000Z"
                            )
                        ),
                        hosting_architecture=HostingArchitecture(
                            architecture_diagram_url="https://s3.amazonaws.com/example-bucket/architecture.png",
                            platforms=[
                                Platform(provider="AWS", component="CONTROL_PLANE", environment_owner="PARTNER"),
                                Platform(provider="AWS", component="APPLICATION_PLANE", environment_owner="BUYER")
                            ]
                        )
                    )
                ]
            )
        ]
    )

    assert actual_detail == expected_detail, "Deserialized object does not match expected object"


def test_create_product_change_detail_serialization():
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.create_product_change_detail import CreateProductChangeDetail

    detail = CreateProductChangeDetail(product_title="ProductTitle")
    expected_json = {
        "ProductTitle": "ProductTitle"
    }

    assert detail.to_json() == json.dumps(expected_json), "Generated CreateProductChangeDetail does not match expected json"


def test_release_product_change_detail_serialization():
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.release_product_change_detail import ReleaseProductChangeDetail

    detail = ReleaseProductChangeDetail()

    assert detail.to_json() == json.dumps({}), "Generated ReleaseProductChangeDetail does not match expected json"


def test_update_information_change_detail_serialization():
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.update_information_change_detail import UpdateInformationChangeDetail
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.additional_resource import AdditionalResource

    detail = UpdateInformationChangeDetail(
        product_title="MyProductTitle",
        short_description="My Product",
        long_description="My Product long description",
        sku="SKU",
        logo_url="https://s3.amazonaws.com/awsmp-logos/logo.png",
        video_urls=["https://s3.amazonaws.com/awsmp-media/video.mp4"],
        highlights=["Highlight"],
        additional_resources=[AdditionalResource(text="url", url="https://amazon.com")],
        support_description="Support description",
        categories=["Operating Systems", "Network Infrastructure", "Application Development"],
        search_keywords=["example", "keywords"]
    )
    expected_json = {
        "ProductTitle": "MyProductTitle",
        "ShortDescription": "My Product",
        "LongDescription": "My Product long description",
        "Sku": "SKU",
        "LogoUrl": "https://s3.amazonaws.com/awsmp-logos/logo.png",
        "VideoUrls": ["https://s3.amazonaws.com/awsmp-media/video.mp4"],
        "Highlights": ["Highlight"],
        "AdditionalResources": [{
            "Text": "url",
            "Url": "https://amazon.com"
        }],
        "SupportDescription": "Support description",
        "Categories": ["Operating Systems", "Network Infrastructure", "Application Development"],
        "SearchKeywords": ["example", "keywords"]
    }

    assert detail.to_json() == json.dumps(expected_json), "Generated UpdateInformationChangeDetail does not match expected json"


def test_update_visibility_change_detail_serialization():
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.update_visibility_change_detail import UpdateVisibilityChangeDetail
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.target_visibility import TargetVisibility

    detail = UpdateVisibilityChangeDetail(
        target_visibility=TargetVisibility.RESTRICTED,
        replacement_product_id="prod-1234567890123"
    )
    expected_json = {
        "TargetVisibility": "Restricted",
        "ReplacementProductId": "prod-1234567890123"
    }

    assert detail.to_json() == json.dumps(expected_json), "Generated UpdateVisibilityChangeDetail does not match expected json"


def test_update_targeting_change_detail_serialization():
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.update_targeting_change_detail import UpdateTargetingChangeDetail
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.positive_targeting import PositiveTargeting

    detail = UpdateTargetingChangeDetail(
        positive_targeting=PositiveTargeting(buyer_accounts=["123456789012", "098765432112"])
    )
    expected_json = {
        "PositiveTargeting": {
            "BuyerAccounts": ["123456789012", "098765432112"]
        }
    }

    assert detail.to_json() == json.dumps(expected_json), "Generated UpdateTargetingChangeDetail does not match expected json"


def test_add_dimension_change_detail_serialization():
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.add_dimension_change_detail import AddDimensionChangeDetail
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.dimension_type import DimensionType

    detail = AddDimensionChangeDetail(
        name="Premium Tier",
        description="Premium tier access",
        key="PremiumTier",
        unit="Units",
        types=[DimensionType.ENTITLED]
    )
    expected_json = {
        "Name": "Premium Tier",
        "Description": "Premium tier access",
        "Key": "PremiumTier",
        "Unit": "Units",
        "Types": ["Entitled"]
    }

    assert detail.to_json() == json.dumps(expected_json), "Generated AddDimensionChangeDetail does not match expected json"


def test_update_dimension_change_detail_serialization():
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.update_dimension_change_detail import UpdateDimensionChangeDetail
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.dimension_type import DimensionType

    detail = UpdateDimensionChangeDetail(
        name="Updated Premium Tier",
        description="Updated premium tier access",
        key="PremiumTier",
        types=[DimensionType.ENTITLED]
    )
    expected_json = {
        "Name": "Updated Premium Tier",
        "Description": "Updated premium tier access",
        "Key": "PremiumTier",
        "Types": ["Entitled"]
    }

    assert detail.to_json() == json.dumps(expected_json), "Generated UpdateDimensionChangeDetail does not match expected json"


def test_restrict_dimension_change_detail_serialization():
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.restrict_dimension_change_detail import RestrictDimensionChangeDetail
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.dimension_type import DimensionType

    detail = RestrictDimensionChangeDetail(
        key="ApiCalls",
        types=[DimensionType.METERED, DimensionType.EXTERNALLYMETERED]
    )
    expected_json = {
        "Key": "ApiCalls",
        "Types": ["Metered", "ExternallyMetered"]
    }

    assert detail.to_json() == json.dumps(expected_json), "Generated RestrictDimensionChangeDetail does not match expected json"


def test_update_buyer_engagement_options_change_detail_serialization():
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.update_buyer_engagement_option_change_detail import UpdateBuyerEngagementOptionChangeDetail
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.engagement_option import EngagementOption

    # The change type's root is a list, so callers build a list of items.
    details = [
        UpdateBuyerEngagementOptionChangeDetail(engagement_option=EngagementOption.REQUESTPRODUCTDEMO),
        UpdateBuyerEngagementOptionChangeDetail(engagement_option=EngagementOption.REQUESTPRIVATEOFFER)
    ]
    expected_json = [
        {"EngagementOption": "RequestProductDemo"},
        {"EngagementOption": "RequestPrivateOffer"}
    ]

    actual_json = json.dumps([json.loads(detail.to_json()) for detail in details])

    assert actual_json == json.dumps(expected_json), "Generated UpdateBuyerEngagementOptionChangeDetail list does not match expected json"


def test_add_delivery_option_change_detail_serialization():
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.add_delivery_option_change_detail import AddDeliveryOptionChangeDetail
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.add_delivery_option import AddDeliveryOption
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.add_delivery_option_details import AddDeliveryOptionDetails
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.add_delivery_option_detail import AddDeliveryOptionDetail

    detail = AddDeliveryOptionChangeDetail(
        delivery_options=[AddDeliveryOption(
            details=AddDeliveryOptionDetails(
                delivery_option_details=AddDeliveryOptionDetail(
                    type="example-delivery-option-type",
                    usage_instructions="Instructions to configure the product."
                )
            )
        )]
    )
    expected_json = {
        "DeliveryOptions": [{
            "Details": {
                "DeliveryOptionDetails": {
                    "Type": "example-delivery-option-type",
                    "UsageInstructions": "Instructions to configure the product."
                }
            }
        }]
    }

    assert detail.to_json() == json.dumps(expected_json), "Generated AddDeliveryOptionChangeDetail does not match expected json"


def test_update_delivery_option_change_detail_serialization():
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.update_delivery_option_change_detail import UpdateDeliveryOptionChangeDetail
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.update_delivery_option import UpdateDeliveryOption
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.update_delivery_option_details import UpdateDeliveryOptionDetails
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.update_delivery_option_detail import UpdateDeliveryOptionDetail

    detail = UpdateDeliveryOptionChangeDetail(
        delivery_options=[UpdateDeliveryOption(
            id="do-abcdefghijklm",
            details=UpdateDeliveryOptionDetails(
                delivery_option_details=UpdateDeliveryOptionDetail(
                    usage_instructions="Updated instructions to configure the product."
                )
            )
        )]
    )
    expected_json = {
        "DeliveryOptions": [{
            "Id": "do-abcdefghijklm",
            "Details": {
                "DeliveryOptionDetails": {
                    "UsageInstructions": "Updated instructions to configure the product."
                }
            }
        }]
    }

    assert detail.to_json() == json.dumps(expected_json), "Generated UpdateDeliveryOptionChangeDetail does not match expected json"


def test_update_hosting_architecture_change_detail_serialization():
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.update_hosting_architecture_change_detail import UpdateHostingArchitectureChangeDetail
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.hosting_architecture import HostingArchitecture
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.architectural_component import ArchitecturalComponent
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.provider import Provider
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.component import Component
    from aws_marketplace_catalog_shapes_product_1_0_changetypes.models.environment_owner import EnvironmentOwner

    detail = UpdateHostingArchitectureChangeDetail(
        delivery_option_id="do-abcdefghijklm",
        hosting_architecture=HostingArchitecture(
            architecture_diagram_url="https://s3.amazonaws.com/example-bucket/architecture.png",
            platforms=[
                ArchitecturalComponent(
                    provider=Provider.AWS,
                    component=Component.CONTROL_PLANE,
                    environment_owner=EnvironmentOwner.PARTNER
                ),
                ArchitecturalComponent(
                    provider=Provider.AWS,
                    component=Component.APPLICATION_PLANE,
                    environment_owner=EnvironmentOwner.BUYER
                )
            ]
        )
    )
    expected_json = {
        "DeliveryOptionId": "do-abcdefghijklm",
        "HostingArchitecture": {
            "ArchitectureDiagramUrl": "https://s3.amazonaws.com/example-bucket/architecture.png",
            "Platforms": [{
                "Provider": "AWS",
                "Component": "CONTROL_PLANE",
                "EnvironmentOwner": "PARTNER"
            }, {
                "Provider": "AWS",
                "Component": "APPLICATION_PLANE",
                "EnvironmentOwner": "BUYER"
            }]
        }
    }

    assert detail.to_json() == json.dumps(expected_json), "Generated UpdateHostingArchitectureChangeDetail does not match expected json"
