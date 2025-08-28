import pytest
import json

def test_importable():
    from aws_marketplace_catalog_shapes_saasproduct_1_0_entitytype.models.saa_s_product_entity_detail import SaaSProductEntityDetail # noqa: F401
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.update_information_change_detail import UpdateInformationChangeDetail # noqa: F401
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.add_delivery_options_change_detail import AddDeliveryOptionsChangeDetail # noqa: F401
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.update_delivery_options_change_detail import UpdateDeliveryOptionsChangeDetail # noqa: F401
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.update_delivery_options_visibility_change_detail import UpdateDeliveryOptionsVisibilityChangeDetail # noqa: F401
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.create_product_change_detail import CreateProductChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.add_dimension_change_detail import AddDimensionChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.update_dimension_change_detail import UpdateDimensionChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.update_targeting_change_detail import UpdateTargetingChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.update_visibility_change_detail import UpdateVisibilityChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.restrict_dimension_change_detail import RestrictDimensionChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.add_api_delivery_option_details import AddApiDeliveryOptionDetails  # noqa: F401
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.update_api_delivery_option_details import UpdateApiDeliveryOptionDetails  # noqa: F401

    assert True

def test_saas_product_1_0_entity_detail_deserialization():
    from aws_marketplace_catalog_shapes_saasproduct_1_0_entitytype.models.saa_s_product_entity_detail import SaaSProductEntityDetail
    from aws_marketplace_catalog_shapes_saasproduct_1_0_entitytype.models.description import Description
    from aws_marketplace_catalog_shapes_saasproduct_1_0_entitytype.models.promotional_resources import PromotionalResources
    from aws_marketplace_catalog_shapes_saasproduct_1_0_entitytype.models.video import Video
    from aws_marketplace_catalog_shapes_saasproduct_1_0_entitytype.models.additional_resource import AdditionalResource
    from aws_marketplace_catalog_shapes_saasproduct_1_0_entitytype.models.support_information import SupportInformation
    from aws_marketplace_catalog_shapes_saasproduct_1_0_entitytype.models.dimension import Dimension
    from aws_marketplace_catalog_shapes_saasproduct_1_0_entitytype.models.version import Version
    from aws_marketplace_catalog_shapes_saasproduct_1_0_entitytype.models.delivery_option import DeliveryOption
    from aws_marketplace_catalog_shapes_saasproduct_1_0_entitytype.models.targeting import Targeting
    from aws_marketplace_catalog_shapes_saasproduct_1_0_entitytype.models.positive_targeting import PositiveTargeting
    from aws_marketplace_catalog_shapes_saasproduct_1_0_entitytype.models.deployment_template import DeploymentTemplate

    expected_json = {
        "Description": {
            "ProductTitle": "Test Product",
            "ProductCode": "5cqs4jta6m2iuh6jak7s7bjsy",
            "ShortDescription": "Test Product",
            "LongDescription": "SaaS test product",
            "Sku": "SKU",
            "Highlights": ["Config adds no run-time overheads"],
            "SearchKeywords": ["example", "keywords"],
            "Visibility": "Restricted",
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
            "Name": "Free Forever Plan",
            "Description": "Free Forever Plan",
            "Key": "FreePlan",
            "Unit": "Units",
            "Types": ["ExternallyMetered"]
        }, {
            "Name": "Starter Plan",
            "Description": "Starter Plan",
            "Key": "StarterPlan",
            "Unit": "Units",
            "Types": ["ExternallyMetered"]
        }, {
            "Name": "Pro Plan",
            "Description": "Pro Plan",
            "Key": "ProPlan",
            "Unit": "Units",
            "Types": ["ExternallyMetered"]
        }, {
            "Name": "Business Plan",
            "Description": "Business Plan",
            "Key": "BusinessPlan",
            "Unit": "Units",
            "Types": ["ExternallyMetered"]
        }, {
            "Name": "Enterprise Plan",
            "Description": "Enterprise Plan",
            "Key": "EnterprisePlan",
            "Unit": "Units",
            "Types": ["ExternallyMetered"]
        }],
        "Versions": [{
            "Id": "version-57xgyhrofhrqm",
            "DeliveryOptions": [{
                "Id": "do-lgvhsajjzx7u6",
                "Type": "SoftwareRegistration",
                "FulfillmentUrl": "https://amazon.com"
            }, {
                "Id": "do-a5xyrbn3y2kzg",
                "Type": "SoftwareRegistration",
                "FulfillmentUrl": "https://amazon.com",
                "QuickLaunchEnabled": True,
                "LaunchUrl": "https://amazon.com",
                "DeploymentTemplates": [{
                    "Type": "CloudFormation@1.0",
                    "Title": "Title",
                    "Description": "Description",
                    "IamPolicy": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Action\":[\"s3:Get*\",\"s3:List*\"],\"Resource\":\\n[\"arn:aws:s3:::EXAMPLE-BUCKET\",\"arn:aws:s3:::EXAMPLE-BUCKET/*\"]}]}",
                    "DefaultStackName": "default-stack-name",
                    "TemplateUrl": "https://amazon.com"
                }],
                "UsageInstructions": "Instructions to configure the product.",
                "Visibility": "Limited",
                "Targeting": {
                    "PositiveTargeting": {
                        "BuyerAccounts": ["123456789123"]
                    }
                }
            }]
        }],
        "Targeting": {
            "PositiveTargeting": {
                "BuyerAccounts": ["123456789123"]
            }
        }
    }

    actual_detail = SaaSProductEntityDetail.from_json(json.dumps(expected_json))
    expected_detail = SaaSProductEntityDetail(
        description=Description(
            product_title="Test Product",
            product_code="5cqs4jta6m2iuh6jak7s7bjsy",
            short_description="Test Product",
            long_description="SaaS test product",
            highlights=["Config adds no run-time overheads"],
            search_keywords=["example", "keywords"],
            sku="SKU",
            visibility="Restricted",
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
            additional_resources=[
                AdditionalResource(
                    type="Link",
                    text="Sample Resource",
                    url="https://amazon.com"
                )
            ]
        ),
        support_information=SupportInformation(description="Product support information"),
        dimensions=[
            Dimension(
                name="Free Forever Plan",
                description="Free Forever Plan",
                key="FreePlan",
                unit="Units",
                types=["ExternallyMetered"]
            ),
            Dimension(
                name="Starter Plan",
                description="Starter Plan",
                key="StarterPlan",
                unit="Units",
                types=["ExternallyMetered"]
            ),
            Dimension(
                name="Pro Plan",
                description="Pro Plan",
                key="ProPlan",
                unit="Units",
                types=["ExternallyMetered"]
            ),
            Dimension(
                name="Business Plan",
                description="Business Plan",
                key="BusinessPlan",
                unit="Units",
                types=["ExternallyMetered"]
            ),
            Dimension(
                name="Enterprise Plan",
                description="Enterprise Plan",
                key="EnterprisePlan",
                unit="Units",
                types=["ExternallyMetered"]
            )
        ],
        versions=[
            Version(
                id="version-57xgyhrofhrqm",
                delivery_options=[
                    DeliveryOption(
                        id="do-lgvhsajjzx7u6",
                        type="SoftwareRegistration",
                        fulfillment_url="https://amazon.com"
                    ),
                    DeliveryOption(
                        id="do-a5xyrbn3y2kzg",
                        type="SoftwareRegistration",
                        fulfillment_url="https://amazon.com",
                        visibility="Limited",
                        targeting=Targeting(
                            positive_targeting=PositiveTargeting(
                                buyer_accounts=["123456789123"]
                            )
                        ),
                        quick_launch_enabled=True,
                        launch_url="https://amazon.com",
                        deployment_templates=[
                            DeploymentTemplate(
                                type="CloudFormation@1.0",
                                title="Title",
                                description="Description",
                                iam_policy="{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Action\":[\"s3:Get*\",\"s3:List*\"],\"Resource\":\\n[\"arn:aws:s3:::EXAMPLE-BUCKET\",\"arn:aws:s3:::EXAMPLE-BUCKET/*\"]}]}",
                                template_url="https://amazon.com",
                                default_stack_name="default-stack-name"
                            )
                        ],
                        usage_instructions="Instructions to configure the product."
                    )
                ]
            )
        ],
        targeting=Targeting(
            positive_targeting=PositiveTargeting(
                buyer_accounts=["123456789123"]
            )
        )
    )

    assert actual_detail == expected_detail, "Deserialized object does not match expected object"

def test_saas_product_1_0_api_delivery_option_entity_detail_deserialization():
    from aws_marketplace_catalog_shapes_saasproduct_1_0_entitytype.models.saa_s_product_entity_detail import SaaSProductEntityDetail
    from aws_marketplace_catalog_shapes_saasproduct_1_0_entitytype.models.description import Description
    from aws_marketplace_catalog_shapes_saasproduct_1_0_entitytype.models.promotional_resources import PromotionalResources
    from aws_marketplace_catalog_shapes_saasproduct_1_0_entitytype.models.support_information import SupportInformation
    from aws_marketplace_catalog_shapes_saasproduct_1_0_entitytype.models.dimension import Dimension
    from aws_marketplace_catalog_shapes_saasproduct_1_0_entitytype.models.version import Version
    from aws_marketplace_catalog_shapes_saasproduct_1_0_entitytype.models.delivery_option import DeliveryOption
    from aws_marketplace_catalog_shapes_saasproduct_1_0_entitytype.models.targeting import Targeting
    from aws_marketplace_catalog_shapes_saasproduct_1_0_entitytype.models.positive_targeting import PositiveTargeting
    from aws_marketplace_catalog_shapes_saasproduct_1_0_entitytype.models.endpoint import Endpoint
    from aws_marketplace_catalog_shapes_saasproduct_1_0_entitytype.models.integration_protocol import IntegrationProtocol

    expected_json = {
        "Description": {
            "ProductTitle": "API Test Product",
            "ProductCode": "5cqs4jta6m2iuh6jak7s7bjsy",
            "ShortDescription": "API test product",
            "LongDescription": "API-based SaaS test product",
            "Sku": "API-SKU",
            "Highlights": ["MCP Server integration"],
            "SearchKeywords": ["api", "mcp"],
            "Visibility": "Public",
            "ProductState": "Active",
            "Categories": ["AI Services"]
        },
        "PromotionalResources": {
            "LogoUrl": "https://s3.amazonaws.com/awsmp-logos/api-logo.png",
            "Videos": [],
            "AdditionalResources": []
        },
        "SupportInformation": {
            "Description": "API product support information"
        },
        "Dimensions": [{
            "Name": "API Calls",
            "Description": "Number of API calls",
            "Key": "ApiCalls",
            "Unit": "Requests",
            "Types": ["Metered"]
        }],
        "Versions": [{
            "Id": "version-api123",
            "DeliveryOptions": [{
                "Id": "do-api123",
                "Type": "ApiDelivery",
                "ApiType": "MCP_SERVER",
                "QuickLaunchEnabled": True,
                "CompatibleServices": ["Bedrock-AgentCore"],
                "FulfillmentUrl": "https://api.example.com/register",
                "UsageInstructions": "Connect to our MCP server endpoint",
                "Endpoints": [{
                    "Name": "MainEndpoint",
                    "EndpointUrl": "https://api.example.com/mcp",
                    "Description": "Main MCP server endpoint",
                    "AuthorizationTypes": ["API_KEY"],
                    "Schemas": [],
                    "IntegrationProtocols": [{
                        "Type": "MCP",
                        "UsageInstructions": "Use MCP protocol for integration"
                    }]
                }],
                "Visibility": "Public"
            }]
        }],
        "Targeting": {
            "PositiveTargeting": {
                "BuyerAccounts": ["123456789123"]
            }
        }
    }

    actual_detail = SaaSProductEntityDetail.from_json(json.dumps(expected_json))
    expected_detail = SaaSProductEntityDetail(
        description=Description(
            product_title="API Test Product",
            product_code="5cqs4jta6m2iuh6jak7s7bjsy",
            short_description="API test product",
            long_description="API-based SaaS test product",
            highlights=["MCP Server integration"],
            search_keywords=["api", "mcp"],
            sku="API-SKU",
            visibility="Public",
            product_state="Active",
            categories=["AI Services"]
        ),
        promotional_resources=PromotionalResources(
            logo_url="https://s3.amazonaws.com/awsmp-logos/api-logo.png",
            videos=[],
            additional_resources=[]
        ),
        support_information=SupportInformation(description="API product support information"),
        dimensions=[
            Dimension(
                name="API Calls",
                description="Number of API calls",
                key="ApiCalls",
                unit="Requests",
                types=["Metered"]
            )
        ],
        versions=[
            Version(
                id="version-api123",
                delivery_options=[
                    DeliveryOption(
                        id="do-api123",
                        type="ApiDelivery",
                        api_type="MCP_SERVER",
                        quick_launch_enabled=True,
                        compatible_services=["Bedrock-AgentCore"],
                        fulfillment_url="https://api.example.com/register",
                        usage_instructions="Connect to our MCP server endpoint",
                        endpoints=[
                            Endpoint(
                                name="MainEndpoint",
                                endpoint_url="https://api.example.com/mcp",
                                description="Main MCP server endpoint",
                                authorization_types=["API_KEY"],
                                schemas=[],
                                integration_protocols=[
                                    IntegrationProtocol(
                                        type="MCP",
                                        usage_instructions="Use MCP protocol for integration"
                                    )
                                ]
                            )
                        ],
                        visibility="Public"
                    )
                ]
            )
        ],
        targeting=Targeting(
            positive_targeting=PositiveTargeting(
                buyer_accounts=["123456789123"]
            )
        )
    )

    assert actual_detail == expected_detail, "API delivery option deserialized object does not match expected object"

def test_update_information_change_detail_serialization():
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.update_information_change_detail import UpdateInformationChangeDetail
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.additional_resource import AdditionalResource

    update_information_change_detail = UpdateInformationChangeDetail(
        product_title="MyProductTitle",
        short_description="My Product",
        long_description="My Product long description",
        sku="SKU",
        video_urls=["https://s3.amazonaws.com/awsmp-media/video.mp4"],
        logo_url="https://s3.amazonaws.com/awsmp-logos/logo.png",
        highlights=["Highlight"],
        additional_resources=[AdditionalResource(text="url", url="https://amazon.com")],
        support_description="Support description",
        categories=["Operating Systems", "Network Infrastructure", "Application Development"],
        search_keywords=["example", "keywords"]
    )

    actual_json = update_information_change_detail.to_json()
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

    assert actual_json == json.dumps(expected_json), "Generated UpdateInformationChangeDetail does not match expected json"

def test_add_delivery_options_change_detail_serialization():
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.add_delivery_options_change_detail import AddDeliveryOptionsChangeDetail
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.add_delivery_option import AddDeliveryOption
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.add_delivery_option_details import AddDeliveryOptionDetails
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.add_saa_s_url_delivery_option_details import AddSaaSUrlDeliveryOptionDetails
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.deployment_template import DeploymentTemplate
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.cloud_formation_details import CloudFormationDetails

    add_delivery_options_change_detail = AddDeliveryOptionsChangeDetail(
        delivery_options=[AddDeliveryOption(
            details=AddDeliveryOptionDetails(
                saa_s_url_delivery_option_details=AddSaaSUrlDeliveryOptionDetails(
                    fulfillment_url="https://amazon.com",
                    launch_url="https://amazon.com",
                    deployment_templates=[DeploymentTemplate(
                        title="title",
                        description="description",
                        iam_policy="iam policy",
                        cloud_formation_details=CloudFormationDetails(
                            default_stack_name="stack-name",
                            template_url="https://www.example.s3.amazonaws.com/example.txt"
                        )
                    )],
                    usage_instructions="instructions",
                    quick_launch_enabled=False
                )
            )
        )]
    )
    actual_json = add_delivery_options_change_detail.to_json()
    expected_json = {
        "DeliveryOptions": [{
            "Details": {
                "SaaSUrlDeliveryOptionDetails": {
                    "FulfillmentUrl": "https://amazon.com",
                    "LaunchUrl": "https://amazon.com",
                    "DeploymentTemplates": [{
                        "Title": "title",
                        "Description": "description",
                        "IamPolicy": "iam policy",
                        "CloudFormationDetails": {
                            "DefaultStackName": "stack-name",
                            "TemplateUrl": "https://www.example.s3.amazonaws.com/example.txt"
                        }
                    }],
                    "UsageInstructions": "instructions",
                    "QuickLaunchEnabled": False
                }
            }
        }]
    }

    assert actual_json == json.dumps(expected_json), "Generated AddDeliveryOptionsChangeDetail does not match expected json"

def test_add_api_delivery_options_change_detail_serialization():
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.add_delivery_options_change_detail import AddDeliveryOptionsChangeDetail
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.add_delivery_option import AddDeliveryOption
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.add_delivery_option_details import AddDeliveryOptionDetails
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.add_api_delivery_option_details import AddApiDeliveryOptionDetails
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.api_endpoint import ApiEndpoint
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.integration_protocol import IntegrationProtocol
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.api_type import ApiType
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.authorization_type import AuthorizationType
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.protocol_type import ProtocolType

    add_delivery_options_change_detail = AddDeliveryOptionsChangeDetail(
        delivery_options=[AddDeliveryOption(
            details=AddDeliveryOptionDetails(
                api_delivery_option_details=AddApiDeliveryOptionDetails(
                    api_type=ApiType.MCP_SERVER,
                    quick_launch_enabled=True,
                    compatible_services=["Bedrock-AgentCore"],
                    fulfillment_url="https://api.example.com/register",
                    usage_instructions="Connect to our MCP server endpoint",
                    endpoints=[ApiEndpoint(
                        name="MainEndpoint",
                        endpoint_url="https://api.example.com/mcp",
                        description="Main MCP server endpoint",
                        authorization_types=[AuthorizationType.API_KEY],
                        schemas=[],
                        integration_protocols=[IntegrationProtocol(
                            type=ProtocolType.MCP,
                            usage_instructions="Use MCP protocol for integration"
                        )]
                    )]
                )
            )
        )]
    )
    actual_json = add_delivery_options_change_detail.to_json()
    expected_json = {
        "DeliveryOptions": [{
            "Details": {
                "ApiDeliveryOptionDetails": {
                    "ApiType": "MCP_SERVER",
                    "QuickLaunchEnabled": True,
                    "CompatibleServices": ["Bedrock-AgentCore"],
                    "FulfillmentUrl": "https://api.example.com/register",
                    "UsageInstructions": "Connect to our MCP server endpoint",
                    "Endpoints": [{
                        "Name": "MainEndpoint",
                        "EndpointUrl": "https://api.example.com/mcp",
                        "Description": "Main MCP server endpoint",
                        "AuthorizationTypes": ["API_KEY"],
                        "Schemas": [],
                        "IntegrationProtocols": [{
                            "Type": "MCP",
                            "UsageInstructions": "Use MCP protocol for integration"
                        }]
                    }]
                }
            }
        }]
    }

    assert actual_json == json.dumps(expected_json), "Generated API AddDeliveryOptionsChangeDetail does not match expected json"

def test_update_delivery_options_change_detail_serialization():
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.update_delivery_options_change_detail import UpdateDeliveryOptionsChangeDetail
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.update_delivery_option import UpdateDeliveryOption
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.update_delivery_option_details import UpdateDeliveryOptionDetails
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.update_saa_s_url_delivery_option_details import UpdateSaaSUrlDeliveryOptionDetails
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.deployment_template import DeploymentTemplate
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.cloud_formation_details import CloudFormationDetails

    update_delivery_options_change_detail = UpdateDeliveryOptionsChangeDetail(
        delivery_options=[UpdateDeliveryOption(
            id="do-1234567891234567891234",
            details=UpdateDeliveryOptionDetails(
                saa_s_url_delivery_option_details=UpdateSaaSUrlDeliveryOptionDetails(
                    fulfillment_url="https://amazon.com",
                    launch_url="https://amazon.com",
                    deployment_templates=[DeploymentTemplate(
                        title="title",
                        description="description",
                        iam_policy="iam policy",
                        cloud_formation_details=CloudFormationDetails(
                            default_stack_name="stack-name",
                            template_url="https://www.example.s3.amazonaws.com/example.txt"
                        )
                    )],
                    usage_instructions="instructions"
                )
            )
        )]
    )
    actual_json = update_delivery_options_change_detail.to_json()
    expected_json = {
        "DeliveryOptions": [{
            "Id": "do-1234567891234567891234",
            "Details": {
                "SaaSUrlDeliveryOptionDetails": {
                    "FulfillmentUrl": "https://amazon.com",
                    "LaunchUrl": "https://amazon.com",
                    "DeploymentTemplates": [{
                        "Title": "title",
                        "Description": "description",
                        "IamPolicy": "iam policy",
                        "CloudFormationDetails": {
                            "DefaultStackName": "stack-name",
                            "TemplateUrl": "https://www.example.s3.amazonaws.com/example.txt"
                        }
                    }],
                    "UsageInstructions": "instructions"
                }
            }
        }]
    }

    assert actual_json == json.dumps(expected_json), "Generated UpdateDeliveryOptionsChangeDetail does not match expected json"

def test_update_api_delivery_options_change_detail_serialization():
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.update_delivery_options_change_detail import UpdateDeliveryOptionsChangeDetail
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.update_delivery_option import UpdateDeliveryOption
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.update_delivery_option_details import UpdateDeliveryOptionDetails
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.update_api_delivery_option_details import UpdateApiDeliveryOptionDetails
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.api_endpoint import ApiEndpoint
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.authorization_type import AuthorizationType

    update_delivery_options_change_detail = UpdateDeliveryOptionsChangeDetail(
        delivery_options=[UpdateDeliveryOption(
            id="do-api123456789",
            details=UpdateDeliveryOptionDetails(
                api_delivery_option_details=UpdateApiDeliveryOptionDetails(
                    usage_instructions="Updated MCP server instructions",
                    endpoints=[ApiEndpoint(
                        endpoint_url="https://api.example.com/mcp/v2",
                        authorization_types=[AuthorizationType.OAUTH2]
                    )]
                )
            )
        )]
    )
    actual_json = update_delivery_options_change_detail.to_json()
    expected_json = {
        "DeliveryOptions": [{
            "Id": "do-api123456789",
            "Details": {
                "ApiDeliveryOptionDetails": {
                    "UsageInstructions": "Updated MCP server instructions",
                    "Endpoints": [{
                        "EndpointUrl": "https://api.example.com/mcp/v2",
                        "AuthorizationTypes": ["OAUTH2"]
                    }]
                }
            }
        }]
    }

    assert actual_json == json.dumps(expected_json), "Generated API UpdateDeliveryOptionsChangeDetail does not match expected json"

def test_update_delivery_options_visibility_change_detail_serialization():
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.update_delivery_options_visibility_change_detail import UpdateDeliveryOptionsVisibilityChangeDetail
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.update_delivery_option_visibility import UpdateDeliveryOptionVisibility
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.update_delivery_options_target_visibility import UpdateDeliveryOptionsTargetVisibility
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.targeting import Targeting
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.positive_targeting import PositiveTargeting

    update_delivery_options_visibility_change_detail = UpdateDeliveryOptionsVisibilityChangeDetail(
        delivery_options=[
            UpdateDeliveryOptionVisibility(
                id="do-1234567891234567891234",
                target_visibility=UpdateDeliveryOptionsTargetVisibility.PUBLIC
            ),
            UpdateDeliveryOptionVisibility(
                id="do-43210987654321",
                    target_visibility=UpdateDeliveryOptionsTargetVisibility.LIMITED,
                    targeting=Targeting(
                        positive_targeting=PositiveTargeting(
                            buyer_accounts=["123456789012"]
                        )
                    )
            )
        ]
    )
    actual_json = update_delivery_options_visibility_change_detail.to_json()
    expected_json = {
        "DeliveryOptions": [{
            "Id": "do-1234567891234567891234",
            "TargetVisibility": "Public"
        }, {
            "Id": "do-43210987654321",
            "TargetVisibility": "Limited",
            "Targeting": {
                "PositiveTargeting": {
                    "BuyerAccounts": ["123456789012"]
                }
            }
        }]
    }

    assert actual_json == json.dumps(expected_json), "Generated UpdateDeliveryOptionsVisibilityChangeDetail does not match expected json"

def test_create_product_change_detail_serialization():
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.create_product_change_detail import CreateProductChangeDetail

    create_product_change_detail = CreateProductChangeDetail(product_title="ProductTitle")
    actual_json = create_product_change_detail.to_json()
    expected_json = {
        "ProductTitle": "ProductTitle"
    }

    assert actual_json == json.dumps(expected_json), "Generated CreateProductChangeDetail does not match expected json"

def test_add_dimension_change_detail_serialization():
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.add_dimension_change_detail import AddDimensionChangeDetail
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.dimension_type import DimensionType

    add_dimension_change_detail = AddDimensionChangeDetail(
        name="Course Fee",
        description="Course Fee Description",
        key="Premium",
        unit="UnitHrs",
        types=[DimensionType.ENTITLED]
    )
    actual_json = add_dimension_change_detail.to_json()
    expected_json = {
        "Name": "Course Fee",
        "Description": "Course Fee Description",
        "Key": "Premium",
        "Unit": "UnitHrs",
        "Types": ["Entitled"]
    }

    assert actual_json == json.dumps(expected_json), "Generated AddDimensionChangeDetail does not match expected json"

def test_update_dimension_change_detail_serialization():
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.update_dimension_change_detail import UpdateDimensionChangeDetail
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.dimension_type import DimensionType

    update_dimension_change_detail = UpdateDimensionChangeDetail(
        name="Updated Course Fee",
        description="Updated Course Fee Description",
        key="CourseFee",
        types=[DimensionType.EXTERNALLYMETERED]
    )
    actual_json = update_dimension_change_detail.to_json()
    expected_json = {
        "Name": "Updated Course Fee",
        "Description": "Updated Course Fee Description",
        "Key": "CourseFee",
        "Types": ["ExternallyMetered"]
    }

    assert actual_json == json.dumps(expected_json), "Generated UpdateDimensionChangeDetail does not match expected json"
    
def test_update_targeting_change_detail_serialization():
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.update_targeting_change_detail import UpdateTargetingChangeDetail
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.positive_targeting import PositiveTargeting

    update_targeting_change_detail = UpdateTargetingChangeDetail(
        positive_targeting=PositiveTargeting(buyer_accounts=["123456789012", "098765432112"])
    )
    actual_json = update_targeting_change_detail.to_json()
    expected_json = {
        "PositiveTargeting": {
            "BuyerAccounts": ["123456789012", "098765432112"]
        }
    }

    assert actual_json == json.dumps(expected_json), "Generated UpdateVisibilityChangeDetail does not match expected json"

def test_update_visibility_change_detail_serialization():
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.update_visibility_change_detail import UpdateVisibilityChangeDetail
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.target_visibility import TargetVisibility

    update_visibility_change_detail = UpdateVisibilityChangeDetail(
        target_visibility=TargetVisibility.PUBLIC,
        replacement_product_id="prod-1234567890123")
    actual_json = update_visibility_change_detail.to_json()
    expected_json = {
        "TargetVisibility": "Public",
        "ReplacementProductId": "prod-1234567890123"
    }

    assert actual_json == json.dumps(expected_json), "Generated UpdateVisibilityChangeDetail does not match expected json"

def test_restrict_dimension_change_detail_serialization():
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.restrict_dimension_change_detail import RestrictDimensionChangeDetail
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.dimension_type import DimensionType

    restrict_dimension_change_detail = RestrictDimensionChangeDetail(
        key="Basic",
        types=[DimensionType.EXTERNALLYMETERED, DimensionType.METERED]
    )
    actual_json = restrict_dimension_change_detail.to_json()
    expected_json = {
        "Key": "Basic",
        "Types": ["ExternallyMetered", "Metered"]
    }

    assert actual_json == json.dumps(expected_json), "Generated RestrictDimensionChangeDetail does not match expected json"

def test_release_product_change_detail_serialization():
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.release_product_change_detail import ReleaseProductChangeDetail

    release_product_change_detail = ReleaseProductChangeDetail()
    actual_json = release_product_change_detail.to_json()
    expected_json = {}

    assert actual_json == json.dumps(expected_json), "Generated ReleaseProductChangeDetail does not match expected json"

def test_add_api_delivery_options_with_schemas_change_detail_serialization():
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.add_delivery_options_change_detail import AddDeliveryOptionsChangeDetail
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.add_delivery_option import AddDeliveryOption
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.add_delivery_option_details import AddDeliveryOptionDetails
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.add_api_delivery_option_details import AddApiDeliveryOptionDetails
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.api_endpoint import ApiEndpoint
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.integration_protocol import IntegrationProtocol
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.api_schema import ApiSchema
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.api_type import ApiType
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.authorization_type import AuthorizationType
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.protocol_type import ProtocolType
    from aws_marketplace_catalog_shapes_saasproduct_1_0_changetypes.models.schema_type import SchemaType

    add_delivery_options_change_detail = AddDeliveryOptionsChangeDetail(
        delivery_options=[AddDeliveryOption(
            details=AddDeliveryOptionDetails(
                api_delivery_option_details=AddApiDeliveryOptionDetails(
                    api_type=ApiType.MCP_SERVER,
                    quick_launch_enabled=True,
                    compatible_services=["Bedrock-AgentCore"],
                    fulfillment_url="https://api.example.com/register",
                    usage_instructions="Connect to our MCP server endpoint",
                    endpoints=[ApiEndpoint(
                        name="MainEndpoint",
                        endpoint_url="https://api.example.com/mcp",
                        description="Main MCP server endpoint",
                        authorization_types=[AuthorizationType.API_KEY],
                        schemas=[ApiSchema(
                            type=SchemaType.OPEN_API,
                            schema_url="https://api.example.com/schema.json"
                        )],
                        integration_protocols=[IntegrationProtocol(
                            type=ProtocolType.MCP,
                            usage_instructions="Use MCP protocol for integration"
                        )]
                    )]
                )
            )
        )]
    )
    actual_json = add_delivery_options_change_detail.to_json()
    expected_json = {
        "DeliveryOptions": [{
            "Details": {
                "ApiDeliveryOptionDetails": {
                    "ApiType": "MCP_SERVER",
                    "QuickLaunchEnabled": True,
                    "CompatibleServices": ["Bedrock-AgentCore"],
                    "FulfillmentUrl": "https://api.example.com/register",
                    "UsageInstructions": "Connect to our MCP server endpoint",
                    "Endpoints": [{
                        "Name": "MainEndpoint",
                        "EndpointUrl": "https://api.example.com/mcp",
                        "Description": "Main MCP server endpoint",
                        "AuthorizationTypes": ["API_KEY"],
                        "Schemas": [{
                            "Type": "OPEN_API",
                            "SchemaUrl": "https://api.example.com/schema.json"
                        }],
                        "IntegrationProtocols": [{
                            "Type": "MCP",
                            "UsageInstructions": "Use MCP protocol for integration"
                        }]
                    }]
                }
            }
        }]
    }

    assert actual_json == json.dumps(expected_json), "Generated API AddDeliveryOptionsChangeDetail with schemas does not match expected json"
