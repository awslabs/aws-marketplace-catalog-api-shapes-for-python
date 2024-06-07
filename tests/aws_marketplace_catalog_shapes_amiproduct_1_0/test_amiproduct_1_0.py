import pytest
import json

def test_importable():
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.create_product_change_detail import CreateProductChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.update_delivery_options_change_detail import UpdateDeliveryOptionsChangeDetail # noqa: F401
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.add_delivery_options_change_detail import AddDeliveryOptionsChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.restrict_delivery_options_change_detail import RestrictDeliveryOptionsChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.update_information_change_detail import UpdateInformationChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.add_instance_types_change_detail import AddInstanceTypesChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.restrict_instance_types_change_detail import RestrictInstanceTypesChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.add_dimension_change_detail import AddDimensionChangeDetail   # noqa: F401
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.restrict_dimension_change_detail import RestrictDimensionChangeDetail   # noqa: F401
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.update_future_region_support_change_detail import UpdateFutureRegionSupportChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.update_targeting_change_detail import UpdateTargetingChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.update_visibility_change_detail import UpdateVisibilityChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.add_regions_change_detail import AddRegionsChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.restrict_regions_change_detail import RestrictRegionsChangeDetail  # noqa: F401

    assert True

def test_amiproduct_1_0_entity_detail_deserialization():
    from aws_marketplace_catalog_shapes_amiproduct_1_0_entitytype.models.ami_product_entity_detail import AmiProductEntityDetail
    from aws_marketplace_catalog_shapes_amiproduct_1_0_entitytype.models.version import Version
    from aws_marketplace_catalog_shapes_amiproduct_1_0_entitytype.models.delivery_option import DeliveryOption
    from aws_marketplace_catalog_shapes_amiproduct_1_0_entitytype.models.instructions import Instructions
    from aws_marketplace_catalog_shapes_amiproduct_1_0_entitytype.models.access import Access
    from aws_marketplace_catalog_shapes_amiproduct_1_0_entitytype.models.recommendations import Recommendations
    from aws_marketplace_catalog_shapes_amiproduct_1_0_entitytype.models.security_group import SecurityGroup
    from aws_marketplace_catalog_shapes_amiproduct_1_0_entitytype.models.source import Source
    from aws_marketplace_catalog_shapes_amiproduct_1_0_entitytype.models.compatibility import Compatibility
    from aws_marketplace_catalog_shapes_amiproduct_1_0_entitytype.models.operating_system import OperatingSystem
    from aws_marketplace_catalog_shapes_amiproduct_1_0_entitytype.models.description import Description
    from aws_marketplace_catalog_shapes_amiproduct_1_0_entitytype.models.promotional_resources import PromotionalResources
    from aws_marketplace_catalog_shapes_amiproduct_1_0_entitytype.models.additional_resource import AdditionalResource
    from aws_marketplace_catalog_shapes_amiproduct_1_0_entitytype.models.region_availability import RegionAvailability
    from aws_marketplace_catalog_shapes_amiproduct_1_0_entitytype.models.support_information import SupportInformation
    from aws_marketplace_catalog_shapes_amiproduct_1_0_entitytype.models.dimension import Dimension
    from aws_marketplace_catalog_shapes_amiproduct_1_0_entitytype.models.targeting import Targeting
    from aws_marketplace_catalog_shapes_amiproduct_1_0_entitytype.models.positive_targeting import PositiveTargeting

    expected_json = {
        "Versions": [{
            "Id": "123abc02-0480-43b2-910e-6903901b9abc",
            "ReleaseNotes": "Initial Release",
            "UpgradeInstructions": "NA",
            "VersionTitle": "1",
            "CreationDate": "2023-03-12T00:00:00.000Z",
            "DeliveryOptions": [{
                "Id": "cf01e606-1c1b-3310-9315-a123456bcd99",
                "Type": "CloudFormationTemplate",
                "SourceId": "cf012b3c-6dce-32dc-84f5-12z0d56b1239",
                "Title": "Cloud Formation Template",
                "ShortDescription": "CloudFormation delivery option example",
                "LongDescription": "CloudFormation delivery option example long description",
                "Visibility": "Public",
                "Instructions": {
                    "Usage": "Usage instructions"
                }
            }, {
                "Id": "ami1e606-1c1b-3310-9315-a123456bcd99",
                "Type": "AmazonMachineImage",
                "SourceId": "ami12b3c-6dce-32dc-84f5-12z0d56b1239",
                "ShortDescription": "AMI delivery option example",
                "Visibility": "Public",
                "Instructions": {
                    "Usage": "Usage instructions",
                    "Access": {
                        "Type": "Endpoint",
                        "Port": 8443,
                        "Protocol": "https",
                        "RelativePath": "index.html"
                    }
                },
                "Recommendations": {
                    "SecurityGroups": [{
                        "Protocol": "tcp",
                        "FromPort": 22,
                        "ToPort": 22,
                        "CidrIps": ["0.0.0.0/0"]
                    }],
                    "InstanceType": "t2.large"
                },
                "Title": "(x86_64) Amazon Machine Image",
                "AmiAlias": "/aws/service/marketplace/prod-testid/2"
            }],
            "Sources": [{
                "Id": "cft85b1c-1c1b-3310-9315-a123456bcd99",
                "Type": "CloudFormationTemplate",
                "Template": "https://awsmp-ingestion-cf-templates.s3.amazonaws.com/Template",
                "NestedDocuments": ["Document"],
                "ConsumedSources": ["abcd123c-4aff-328b-85b3-0ccf1019c6e3"],
                "ArchitectureDiagram": "https://awsmp-ingestion-cf-templates.s3.amazonaws.com/ArchitectureDiagram",
                "AWSDependentServices": ["Amazon EC2", "Amazon EBS"]
            }, {
                "Id": "ami85b1c-1c1b-3310-9315-a123456bcd99",
                "Type": "AmazonMachineImage",
                "Image": "ami-0123449f427774b03a",
                "Architecture": "x86_64",
                "VirtualizationType": "hvm",
                "Compatibility": {
                    "AvailableInstanceTypes": ["t2.medium"],
                    "RestrictedInstanceTypes": ["t2.large"]
                },
                "OperatingSystem": {
                    "Name": "AMAZONLINUX",
                    "Version": "2.0",
                    "Username": "Administrator",
                    "ScanningPort": 22
                }
            }]
        }],
        "Description": {
            "ProductTitle": "AMI Test Product",
            "ProductCode": "9abcdefg9bw4k0zssg7thx123",
            "ShortDescription": "Product description",
            "Manufacturer": "AWS-Tester",
            "LongDescription": "Long product description",
            "Sku": "SKU",
            "Highlights": ["Test product"],
            "AssociatedProducts": None,
            "SearchKeywords": ["AWS"],
            "Visibility": "Limited",
            "ProductState": "Active",
            "Categories": ["Operating Systems"]
        },
        "Targeting": {
            "PositiveTargeting": {
                "BuyerAccounts": ["123456789123"]
            }
        },
        "Compatibility": {
            "AvailableInstanceTypes": ["t2.medium"],
            "RestrictedInstanceTypes": ["t2.large"]
        },
        "PromotionalResources": {
            "LogoUrl": "https://s3.amazonaws.com/awsmp-logos/logo.png",
            "Videos": [],
            "AdditionalResources": [{
                "Type": "Link",
                "Text": "Additional Resource",
                "Url": "amazon.com"
            }],
            "PromotionalMedia": None
        },
        "Dimensions": [{
            "Name": "t2.2xlarge",
            "Description": "description",
            "Key": "t2.2xlarge",
            "Unit": "Hrs",
            "Types": ["Metered"]
        }],
        "SupportInformation": {
            "Description": "Product support information"
        },
        "RegionAvailability": {
            "FutureRegionSupport": None,
            "Restrict": [],
            "Regions": ["us-east-1"]
        }
    }

    actual_detail = AmiProductEntityDetail.from_json(json.dumps(expected_json))
    expected_detail = AmiProductEntityDetail(
        versions=[Version(
            id="123abc02-0480-43b2-910e-6903901b9abc",
            release_notes="Initial Release",
            upgrade_instructions="NA",
            version_title="1",
            creation_date="2023-03-12T00:00:00.000Z",
            delivery_options=[
                DeliveryOption(
                    id="cf01e606-1c1b-3310-9315-a123456bcd99",
                    type="CloudFormationTemplate",
                    source_id="cf012b3c-6dce-32dc-84f5-12z0d56b1239",
                    title="Cloud Formation Template",
                    short_description="CloudFormation delivery option example",
                    long_description="CloudFormation delivery option example long description",
                    visibility="Public",
                    instructions=Instructions(
                        usage="Usage instructions"
                    )
                ),
                DeliveryOption(
                    id="ami1e606-1c1b-3310-9315-a123456bcd99",
                    type="AmazonMachineImage",
                    source_id="ami12b3c-6dce-32dc-84f5-12z0d56b1239",
                    title="(x86_64) Amazon Machine Image",
                    short_description="AMI delivery option example",
                    visibility="Public",
                    instructions=Instructions(
                        usage="Usage instructions",
                        access=Access(
                            type="Endpoint",
                            port=8443,
                            protocol="https",
                            relative_path="index.html"
                        )
                    ),
                    recommendations=Recommendations(
                        security_groups=[SecurityGroup(
                            protocol="tcp",
                            from_port=22,
                            to_port=22,
                            cidr_ips=["0.0.0.0/0"]
                        )],
                        instance_type="t2.large"
                    ),
                    ami_alias="/aws/service/marketplace/prod-testid/2"
                )
            ],
            sources=[
                Source(
                    id="cft85b1c-1c1b-3310-9315-a123456bcd99",
                    type="CloudFormationTemplate",
                    Template="https://awsmp-ingestion-cf-templates.s3.amazonaws.com/Template",
                    NestedDocuments=["Document"],
                    ConsumedSources=["abcd123c-4aff-328b-85b3-0ccf1019c6e3"],
                    ArchitectureDiagram="https://awsmp-ingestion-cf-templates.s3.amazonaws.com/ArchitectureDiagram",
                    AWSDependentServices=["Amazon EC2", "Amazon EBS"]
                ),
                Source(
                    id="ami85b1c-1c1b-3310-9315-a123456bcd99",
                    type="AmazonMachineImage",
                    resource="Resource",
                    image="ami-0123449f427774b03a",
                    architecture="x86_64",
                    virtualization_type="hvm",
                    compatibility=Compatibility(
                        available_instance_types=["t2.medium"],
                        restricted_instance_types=["t2.large"]
                    ),
                    operating_system=OperatingSystem(
                        name="AMAZONLINUX",
                        version="2.0",
                        username="Administrator",
                        scanning_port=22
                    )
                )
            ]
        )],
        description=Description(
            product_title="AMI Test Product",
            product_code="9abcdefg9bw4k0zssg7thx123",
            short_description="Product description",
            manufacturer="AWS-Tester",
            long_description="Long product description",
            sku="SKU",
            highlights=["Test product"],
            search_keywords=["AWS"],
            visibility="Limited",
            categories=["Operating Systems"],
            product_state="Active"
        ),
        promotional_resources=PromotionalResources(
            logo_url="https://s3.amazonaws.com/awsmp-logos/logo.png",
            videos=[],
            additional_resources=[AdditionalResource(
                type="Link",
                text="Additional Resource",
                url="amazon.com"
            )]
        ),
        region_availability=RegionAvailability(
            restrict=[],
            regions=["us-east-1"]
        ),
        support_information=SupportInformation(
            description="Product support information"
        ),
        dimensions=[Dimension(
            name="t2.2xlarge",
            description="description",
            key="t2.2xlarge",
            unit="Hrs",
            types=["Metered"]
        )],
        targeting=Targeting(
            positive_targeting=PositiveTargeting(
                buyer_accounts=["123456789123"]
            )
        ),
        compatibility=Compatibility(
            available_instance_types=["t2.medium"],
            restricted_instance_types=["t2.large"]
        )
    )

    assert actual_detail == expected_detail, "Deserialized object does not match expected object"

def test_create_product_change_detail_serialization():
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.create_product_change_detail import CreateProductChangeDetail

    create_product_change_detail = CreateProductChangeDetail(product_title="MyProductTitle")
    actual_json = create_product_change_detail.to_json()
    expected_json = {
        "ProductTitle": "MyProductTitle"
    }

    assert actual_json == json.dumps(expected_json), "Generated CreateProductChangeDetail does not match expected json"

def test_update_delivery_options_change_detail_serialization():
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.update_delivery_options_change_detail import UpdateDeliveryOptionsChangeDetail
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.update_version import UpdateVersion
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.update_delivery_option import UpdateDeliveryOption
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.update_details import UpdateDetails
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.update_ami_delivery_option_details import UpdateAmiDeliveryOptionDetails
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.access_endpoint_url import AccessEndpointUrl
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.security_group import SecurityGroup

    update_delivery_options_change_detail = UpdateDeliveryOptionsChangeDetail(
        version=UpdateVersion(release_notes="Release notes"),
        delivery_options=[UpdateDeliveryOption(
            id="00000000-0000-0000-0000-000000000000",
            details=UpdateDetails(
                ami_delivery_option_details=UpdateAmiDeliveryOptionDetails(
                    usage_instructions="instructions",
                    recommended_instance_type="m4.2xlarge",
                    access_endpoint_url=AccessEndpointUrl(
                        port=8443,
                        protocol="https",
                        relative_path="index.html"
                    ),
                    security_groups=[SecurityGroup(
                        ip_protocol="tcp",
                        from_port=443,
                        to_port=443,
                        ip_ranges=["0.0.0.0/0"]
                    )]
                )
            )
        )]
    )
    actual_json = update_delivery_options_change_detail.to_json()
    expected_json = {
        "Version": {
            "ReleaseNotes": "Release notes"
        },
        "DeliveryOptions": [{
            "Id": "00000000-0000-0000-0000-000000000000",
            "Details": {
                "AmiDeliveryOptionDetails": {
                    "UsageInstructions": "instructions",
                    "AccessEndpointUrl": {
                        "Port": 8443,
                        "Protocol": "https",
                        "RelativePath": "index.html"
                    },
                    "RecommendedInstanceType": "m4.2xlarge",
                    "SecurityGroups": [{
                        "FromPort": 443,
                        "IpProtocol": "tcp",
                        "IpRanges": ["0.0.0.0/0"],
                        "ToPort": 443
                    }]
                }
            }
        }]
    }

    assert actual_json == json.dumps(expected_json), "Generated UpdateDeliveryOptionsChangeDetail does not match expected json"

def test_add_delivery_options_change_detail_serialization():
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.add_delivery_options_change_detail import AddDeliveryOptionsChangeDetail
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.add_version import AddVersion
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.add_delivery_option import AddDeliveryOption
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.add_details import AddDetails
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.add_ami_delivery_option_details import AddAmiDeliveryOptionDetails
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.ami_source import AmiSource
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.access_endpoint_url import AccessEndpointUrl
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.security_group import SecurityGroup

    add_delivery_options_change_detail = AddDeliveryOptionsChangeDetail(
        version=AddVersion(
            version_title="Version title",
            release_notes="Release notes"
        ),
        delivery_options=[AddDeliveryOption(
            id="00000000-0000-0000-0000-000000000000",
            details=AddDetails(
                ami_delivery_option_details=AddAmiDeliveryOptionDetails(
                    ami_source=AmiSource(
                        ami_id="ami-086d874dcc2f96d24",
                        access_role_arn="arn:aws:iam::123456789012:role/myRole",
                        user_name="username",
                        operating_system_name="Windows",
                        operating_system_version="10.5",
                        scanning_port=22
                    ),
                    usage_instructions="instructions",
                    recommended_instance_type="m4.2xlarge",
                    access_endpoint_url=AccessEndpointUrl(
                        port=8443,
                        protocol="https",
                        relative_path="index.html"
                    ),
                    security_groups=[SecurityGroup(
                        ip_protocol="tcp",
                        from_port=443,
                        to_port=443,
                        ip_ranges=["0.0.0.0/0"]
                    )]
                )
            )
        )]
    )
    actual_json = add_delivery_options_change_detail.to_json()
    expected_json = {
        "Version": {
            "VersionTitle": "Version title",
            "ReleaseNotes": "Release notes"
        },
        "DeliveryOptions": [{
            "Details": {
                "AmiDeliveryOptionDetails": {
                    "AmiSource": {
                        "AmiId": "ami-086d874dcc2f96d24",
                        "AccessRoleArn": "arn:aws:iam::123456789012:role/myRole",
                        "UserName": "username",
                        "ScanningPort": 22,
                        "OperatingSystemName": "Windows",
                        "OperatingSystemVersion": "10.5"
                    },
                    "UsageInstructions": "instructions",
                    "AccessEndpointUrl": {
                        "Port": 8443,
                        "Protocol": "https",
                        "RelativePath": "index.html"
                    },
                    "RecommendedInstanceType": "m4.2xlarge",
                    "SecurityGroups": [{
                        "FromPort": 443,
                        "IpProtocol": "tcp",
                        "IpRanges": ["0.0.0.0/0"],
                        "ToPort": 443
                    }]
                }
            }
        }]
    }

    assert actual_json == json.dumps(expected_json), "Generated AddDeliveryOptionsChangeDetail does not match expected json"

def test_restrict_delivery_options_change_detail_serialization():
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.restrict_delivery_options_change_detail import RestrictDeliveryOptionsChangeDetail

    restrict_delivery_options_change_detail = RestrictDeliveryOptionsChangeDetail(
        delivery_option_ids=["00000000-0000-0000-0000-000000000000"]
    )
    actual_json = restrict_delivery_options_change_detail.to_json()
    expected_json = {
        "DeliveryOptionIds": ["00000000-0000-0000-0000-000000000000"]
    }

    assert actual_json == json.dumps(expected_json), "Generated RestrictDeliveryOptionsChangeDetail does not match expected json"

def test_update_information_change_detail_serialization():
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.update_information_change_detail import UpdateInformationChangeDetail
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.additional_resource import AdditionalResource

    update_information_change_detail = UpdateInformationChangeDetail(
        product_title="MyProductTitle",
        short_description="My Product",
        long_description="My Product long description",
        sku="SKU",
        logo_url="https://s3.amazonaws.com/awsmp-logos/logo.png",
        video_urls=["https://s3.amazonaws.com/awsmp-media/video.mp4"],
        highlights=["Highlight"],
        additional_resources=[AdditionalResource(text="url", url="https://amazon.com")],
        support_description="Support description",
        support_resources=["[Email: support@company.com](mailto:support@company.com)",
            "[AWS Infrastructure Support](https://aws.amazon.com/premiumsupport/)"],
        categories=["Operating Systems", "Network Infrastructure", "Application Development"],
        associated_products=["22509f00-8f07-4a19-aacb-53fe1acb1231"],
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
         "SupportResources": ["[Email: support@company.com](mailto:support@company.com)",
            "[AWS Infrastructure Support](https://aws.amazon.com/premiumsupport/)"],
         "Categories": ["Operating Systems", "Network Infrastructure", "Application Development"],
         "AssociatedProducts": ["22509f00-8f07-4a19-aacb-53fe1acb1231"],
         "SearchKeywords": ["example", "keywords"]
    }


    assert actual_json == json.dumps(expected_json), "Generated UpdateInformationChangeDetail does not match expected json"

def test_add_instance_types_change_detail_serialization():
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.add_instance_types_change_detail import AddInstanceTypesChangeDetail

    add_instance_types_change_detail = AddInstanceTypesChangeDetail(instance_types={"m1.medium"})
    actual_json = add_instance_types_change_detail.to_json()
    expected_json = {
        "InstanceTypes": ["m1.medium"]
    }

    assert actual_json == json.dumps(expected_json), "Generated AddInstanceTypesChangeDetail does not match expected json"

def test_restrict_instance_types_change_detail_serialization():
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.restrict_instance_types_change_detail import RestrictInstanceTypesChangeDetail

    restrict_instance_types_change_detail = RestrictInstanceTypesChangeDetail(instance_types={"m1.medium"})
    actual_json = restrict_instance_types_change_detail.to_json()
    expected_json = {
        "InstanceTypes": ["m1.medium"]
    }

    assert actual_json == json.dumps(expected_json), "Generated RestrictInstanceTypesChangeDetail does not match expected json"

def test_add_dimension_change_detail_serialization():
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.add_dimension_change_detail import AddDimensionChangeDetail
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.dimension_type import DimensionType

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

def test_restrict_dimension_change_detail_serialization():
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.restrict_dimension_change_detail import RestrictDimensionChangeDetail
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.dimension_type import DimensionType

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

def test_update_future_region_support_change_detail_serialization():
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.update_future_region_support_change_detail import UpdateFutureRegionSupportChangeDetail
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.future_region_support import FutureRegionSupport
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.supported_region import SupportedRegion

    update_future_region_support_change_detail = UpdateFutureRegionSupportChangeDetail(
        future_region_support=FutureRegionSupport(supported_regions=[SupportedRegion.ALL])
    )
    actual_json = update_future_region_support_change_detail.to_json()
    expected_json = {
        "FutureRegionSupport": {
            "SupportedRegions": ["All"]
        }
    }

    assert actual_json == json.dumps(expected_json), "Generated UpdateFutureRegionSupportChangeDetail does not match expected json"

def test_update_targeting_change_detail_serialization():
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.update_targeting_change_detail import UpdateTargetingChangeDetail
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.positive_targeting import PositiveTargeting

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
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.update_visibility_change_detail import UpdateVisibilityChangeDetail
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.target_visibility import TargetVisibility

    update_visibility_change_detail = UpdateVisibilityChangeDetail(
        target_visibility=TargetVisibility.PUBLIC,
        replacement_product_id="prod-1234567890123")
    actual_json = update_visibility_change_detail.to_json()
    expected_json = {
        "TargetVisibility": "Public",
        "ReplacementProductId": "prod-1234567890123"
    }

    assert actual_json == json.dumps(expected_json), "Generated UpdateVisibilityChangeDetail does not match expected json"

def test_add_regions_change_detail_serialization():
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.add_regions_change_detail import AddRegionsChangeDetail

    add_regions_change_detail = AddRegionsChangeDetail(regions=["us-east-1", "eu-west-2"])
    actual_json = add_regions_change_detail.to_json()
    expected_json = {
        "Regions": ["us-east-1", "eu-west-2"]
    }

    assert actual_json == json.dumps(expected_json), "Generated AddRegionsChangeDetail does not match expected json"

def test_restrict_regions_change_detail_serialization():
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.restrict_regions_change_detail import RestrictRegionsChangeDetail

    restrict_regions_change_detail = RestrictRegionsChangeDetail(regions=["us-east-1", "eu-west-2"])
    actual_json = restrict_regions_change_detail.to_json()
    expected_json = {
        "Regions": ["us-east-1", "eu-west-2"]
    }

    assert actual_json == json.dumps(expected_json), "Generated RestrictRegionsChangeDetail does not match expected json"

def test_release_product_change_detail_serialization():
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.release_product_change_detail import ReleaseProductChangeDetail

    release_product_change_detail = ReleaseProductChangeDetail()
    actual_json = release_product_change_detail.to_json()
    expected_json = {}

    assert actual_json == json.dumps(expected_json), "Generated ReleaseProductChangeDetail does not match expected json"
