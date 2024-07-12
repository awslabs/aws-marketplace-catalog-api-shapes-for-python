import pytest
import json

def test_importable():
    from aws_marketplace_catalog_shapes_containerproduct_1_0_entitytype.models.container_product_entity_detail import ContainerProductEntityDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.create_product_change_detail import CreateProductChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.update_delivery_options_change_detail import UpdateDeliveryOptionsChangeDetail # noqa: F401
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.add_delivery_options_change_detail import AddDeliveryOptionsChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.restrict_delivery_options_change_detail import RestrictDeliveryOptionsChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.update_delivery_options_visibility_change_detail import UpdateDeliveryOptionsVisibilityChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.update_information_change_detail import UpdateInformationChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.add_repositories_change_detail import AddRepositoriesChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.add_dimension_change_detail import AddDimensionChangeDetail   # noqa: F401
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.update_dimension_change_detail import UpdateDimensionChangeDetail   # noqa: F401
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.update_targeting_change_detail import UpdateTargetingChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.update_visibility_change_detail import UpdateVisibilityChangeDetail  # noqa: F401

    assert True

def test_containerproduct_1_0_entity_detail_deserialization():
    from aws_marketplace_catalog_shapes_containerproduct_1_0_entitytype.models.container_product_entity_detail import ContainerProductEntityDetail
    from aws_marketplace_catalog_shapes_containerproduct_1_0_entitytype.models.version import Version
    from aws_marketplace_catalog_shapes_containerproduct_1_0_entitytype.models.source import Source
    from aws_marketplace_catalog_shapes_containerproduct_1_0_entitytype.models.source_compatibility import SourceCompatibility
    from aws_marketplace_catalog_shapes_containerproduct_1_0_entitytype.models.delivery_option import DeliveryOption
    from aws_marketplace_catalog_shapes_containerproduct_1_0_entitytype.models.delivery_option_compatibility import DeliveryOptionCompatibility
    from aws_marketplace_catalog_shapes_containerproduct_1_0_entitytype.models.instructions import Instructions
    from aws_marketplace_catalog_shapes_containerproduct_1_0_entitytype.models.recommendations import Recommendations
    from aws_marketplace_catalog_shapes_containerproduct_1_0_entitytype.models.deployment_resource import DeploymentResource
    from aws_marketplace_catalog_shapes_containerproduct_1_0_entitytype.models.override_parameter import OverrideParameter
    from aws_marketplace_catalog_shapes_containerproduct_1_0_entitytype.models.metadata import Metadata
    from aws_marketplace_catalog_shapes_containerproduct_1_0_entitytype.models.environment_override_parameter import EnvironmentOverrideParameter
    from aws_marketplace_catalog_shapes_containerproduct_1_0_entitytype.models.description import Description
    from aws_marketplace_catalog_shapes_containerproduct_1_0_entitytype.models.targeting import Targeting
    from aws_marketplace_catalog_shapes_containerproduct_1_0_entitytype.models.positive_targeting import PositiveTargeting
    from aws_marketplace_catalog_shapes_containerproduct_1_0_entitytype.models.promotional_resources import PromotionalResources
    from aws_marketplace_catalog_shapes_containerproduct_1_0_entitytype.models.video import Video
    from aws_marketplace_catalog_shapes_containerproduct_1_0_entitytype.models.additional_resource import AdditionalResource
    from aws_marketplace_catalog_shapes_containerproduct_1_0_entitytype.models.signature_verification_key import SignatureVerificationKey
    from aws_marketplace_catalog_shapes_containerproduct_1_0_entitytype.models.support_information import SupportInformation
    from aws_marketplace_catalog_shapes_containerproduct_1_0_entitytype.models.dimension import Dimension
    from aws_marketplace_catalog_shapes_containerproduct_1_0_entitytype.models.repository import Repository

    expected_json = {
        "Versions": [{
            "Id": "123abc02-0480-43b2-910e-6903901b9abc",
            "ReleaseNotes": "Initial Release",
            "UpgradeInstructions": "Upgrade instructions",
            "VersionTitle": "2.0.1",
            "CreationDate": "2023-03-12T00:00:00.000Z",
            "Sources": [{
                "Type": "DockerImages",
                "Id": "cft85b1c-1c1b-3310-9315-a123456bcd99",
                "Images": ["123456789123.dkr.ecr.us-east-1.amazonaws.com/placeholder:1.0"],
                "Compatibility": {
                    "Platform": "Linux"
                }
            }],
            "DeliveryOptions": [{
                "Id": "e28f7813-1c1b-3310-9315-a123456bcd99",
                "Type": "ElasticContainerRegistry",
                "SourceId": "a5c84c81-1c1b-3310-9315-a123456bcd99",
                "Title": "DockerImageSet",
                "ShortDescription": "Short description of product",
                "isRecommended": False,
                "Compatibility": {
                    "AWSServices": ["ECS", "EKS"]
                },
                "Instructions": {
                    "Usage": "Try this product on AWS ECS and AWS EKS"
                },
                "Recommendations": {
                    "DeploymentResources": [{
                        "Text": "ECS",
                        "Url": "https://amazon.com"
                    }]
                },
                "Visibility": "Limited"
            }]
        }, {
            "Id": "123abc02-0480-43b2-910e-6903901b9abc",
            "ReleaseNotes": "Initial Release",
            "UpgradeInstructions": "Upgrade instructions",
            "VersionTitle": "2.0.1",
            "CreationDate": "2023-03-12T00:00:00.000Z",
            "Sources": [{
                "Type": "DockerImages",
                "Id": "cft85b1c-1c1b-3310-9315-a123456bcd99",
                "Images": ["123456789123.dkr.ecr.us-east-1.amazonaws.com/placeholder:1.0"],
                "Compatibility": {
                    "Platform": "Linux"
                }
            }, {
                "Type": "HelmChart",
                "Id": "b01d60d7-1c1b-3310-9315-a123456bcd99",
                "HelmChartUri": "123456789123.dkr.ecr.us-east-1.amazonaws.com/container-seller/helm-test:my-helm"
            }],
            "DeliveryOptions": [{
                "Id": "9300f934-1c1b-3310-9315-a123456bcd99",
                "Type": "Helm",
                "SourceId": "a5c84c81-1c1b-3310-9315-331376cc34bc",
                "Title": "Helm delivery option title",
                "ShortDescription": "Short description of product",
                "isRecommended": False,
                "Compatibility": {
                    "AWSServices": ["EKS"]
                },
                "Instructions": {
                    "Usage": "Usage instructions"
                },
                "QuickLaunchEnabled": False,
                "ReleaseName": "Release Name",
                "MarketplaceServiceAccountName": "Service account name",
                "Namespace": "helm-namespace",
                "OverrideParameters": [{
                    "Key": "global.aws-region",
                    "Default": "us-east-1",
                    "Metadata": {
                        "Label": "test1",
                        "Description": "test parameter"
                    }
                }],
                "Visibility": "Limited"
            }]
        }, {
            "Id": "123abc02-0480-43b2-910e-6903901b9abc",
            "ReleaseNotes": "Initial Release",
            "UpgradeInstructions": "Upgrade instructions",
            "VersionTitle": "2.0.1",
            "CreationDate": "2023-03-12T00:00:00.000Z",
            "Sources": [{
                "Type": "DockerImages",
                "Id": "2ad85b1c-1c1b-3310-9315-a123456bcd99",
                "Images": ["123456789123.dkr.ecr.us-east-1.amazonaws.com/placeholder:1.0"],
                "Compatibility": {
                    "Platform": "Linux"
                }
            }, {
                "Type": "HelmChart",
                "Id": "b01d60d7-1c1b-3310-9315-a123456bcd99",
                "HelmChartUri": "123456789123.dkr.ecr.us-east-1.amazonaws.com/container-seller/helm-test:my-helm"
            }],
            "DeliveryOptions": [{
                "Id": "16182cde-1c1b-3310-9315-a123456bcd99",
                "Type": "EksAddOn",
                "SourceId": "a5c84c81-1c1b-3310-9315-331376cc34bc",
                "Title": "EKS AddOn title",
                "ShortDescription": "Short description of product",
                "Compatibility": {
                    "KubernetesVersions": ["1.22", "1.23"],
                    "Architectures": ["amd64", "arm64"]
                },
                "Instructions": {
                    "Usage": "Usage instructions"
                },
                "AddOnType": "gitops",
                "Visibility": "Limited",
                "Namespace": "eks-namespace",
                "EnvironmentOverrideParameters": [{
                    "Key": "global.aws-region",
                    "Value": "cluster_name"
                }],
                "DisplayAddOnName": "display-name",
                "AddOnName": "name",
                "DisplayAddOnVersion": "v1.2.1-eksbuild.1",
                "AddOnVersion": "1.2.1"
            }]
        }],
        "Description": {
            "ProductTitle": "Container Test Product",
            "ProductCode": "9abcdefg9bw4k0zssg7thx123",
            "ShortDescription": "Product description",
            "LongDescription": "Long product description",
            "Sku": "SKU",
            "Highlights": ["Test product"],
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
        "PromotionalResources": {
            "LogoUrl": "https://s3.amazonaws.com/awsmp-logos/logo.png",
            "Videos": [{
                "Type": "Link",
                "Title": "Product Video",
                "Url": "https://s3.amazonaws.com/media/video.mp4"
            }],
            "AdditionalResources": [{
                "Type": "Link",
                "Text": "Additional Resource",
                "Url": "amazon.com"
            }]
        },
        "SignatureVerificationKeys": [{
            "PublicKey": "-----BEGIN PUBLIC KEY-----\\nPublicKeyExample\\n-----END PUBLIC KEY-----\\n",
            "Status": "Active",
            "PublicKeyVersion": 1
        }],
        "SupportInformation": {
            "Description": "Product support information"
        },
        "Dimensions": [{
            "Name": "Dimension 1",
            "Description": "description",
            "Key": "dimension1",
            "Unit": "bit",
            "Types": ["Metered"]
        }],
        "Repositories": [{
            "Url": "123456789123.dkr.ecr.us-east-1.amazonaws.com/test-repository-1",
            "Type": "ECR"
        }, {
            "Url": "123456789123.dkr.ecr.us-east-1.amazonaws.com/test-repository-2",
            "Type": "ECR"
        }]
    }

    actual_detail = ContainerProductEntityDetail.from_json(json.dumps(expected_json))
    expected_detail = ContainerProductEntityDetail(
        versions=[
            Version(
                id="123abc02-0480-43b2-910e-6903901b9abc",
                release_notes="Initial Release",
                upgrade_instructions="Upgrade instructions",
                version_title="2.0.1",
                creation_date="2023-03-12T00:00:00.000Z",
                sources=[
                    Source(
                        type="DockerImages",
                        id="cft85b1c-1c1b-3310-9315-a123456bcd99",
                        images=["123456789123.dkr.ecr.us-east-1.amazonaws.com/placeholder:1.0"],
                        compatibility=SourceCompatibility(
                            platform="Linux"
                        )
                    )
                ],
                delivery_options=[
                    DeliveryOption(
                        id="e28f7813-1c1b-3310-9315-a123456bcd99",
                        type="ElasticContainerRegistry",
                        source_id="a5c84c81-1c1b-3310-9315-a123456bcd99",
                        title="DockerImageSet",
                        short_description="Short description of product",
                        is_recommended=False,
                        compatibility=DeliveryOptionCompatibility(
                            aws_services=["ECS", "EKS"]
                        ),
                        instructions=Instructions(
                            usage="Try this product on AWS ECS and AWS EKS"
                        ),
                        recommendations=Recommendations(
                            deployment_resources=[
                                DeploymentResource(
                                    text="ECS",
                                    url="https://amazon.com"
                                )
                            ]
                        ),
                        visibility="Limited"
                    )
                ]
            ),
            Version(
                id="123abc02-0480-43b2-910e-6903901b9abc",
                release_notes="Initial Release",
                upgrade_instructions="Upgrade instructions",
                version_title="2.0.1",
                creation_date="2023-03-12T00:00:00.000Z",
                sources=[
                    Source(
                        type="DockerImages",
                        id="cft85b1c-1c1b-3310-9315-a123456bcd99",
                        images=["123456789123.dkr.ecr.us-east-1.amazonaws.com/placeholder:1.0"],
                        compatibility=SourceCompatibility(
                            platform="Linux"
                        )
                    ),
                    Source(
                        type="HelmChart",
                        id="b01d60d7-1c1b-3310-9315-a123456bcd99",
                        helm_chart_uri="123456789123.dkr.ecr.us-east-1.amazonaws.com/container-seller/helm-test:my-helm"
                    )
                ],
                delivery_options=[
                    DeliveryOption(
                        id="9300f934-1c1b-3310-9315-a123456bcd99",
                        type="Helm",
                        source_id="a5c84c81-1c1b-3310-9315-331376cc34bc",
                        title="Helm delivery option title",
                        short_description="Short description of product",
                        is_recommended=False,
                        compatibility=DeliveryOptionCompatibility(
                            aws_services=["EKS"]
                        ),
                        instructions=Instructions(
                            usage="Usage instructions"
                        ),
                        quick_launch_enabled=False,
                        release_name="Release Name",
                        marketplace_service_account_name="Service account name",
                        namespace="helm-namespace",
                        override_parameters=[
                            OverrideParameter(
                                key="global.aws-region",
                                default="us-east-1",
                                metadata=Metadata(
                                    label="test1",
                                    description="test parameter"
                                )
                            )
                        ],
                        visibility="Limited"
                    )
                ]
            ),
            Version(
                id="123abc02-0480-43b2-910e-6903901b9abc",
                release_notes="Initial Release",
                upgrade_instructions="Upgrade instructions",
                version_title="2.0.1",
                creation_date="2023-03-12T00:00:00.000Z",
                sources=[
                    Source(
                        type="DockerImages",
                        id="2ad85b1c-1c1b-3310-9315-a123456bcd99",
                        images=["123456789123.dkr.ecr.us-east-1.amazonaws.com/placeholder:1.0"],
                        compatibility=SourceCompatibility(
                            platform="Linux"
                        )
                    ),
                    Source(
                        type="HelmChart",
                        id="b01d60d7-1c1b-3310-9315-a123456bcd99",
                        helm_chart_uri="123456789123.dkr.ecr.us-east-1.amazonaws.com/container-seller/helm-test:my-helm"
                    )
                ],
                delivery_options=[
                    DeliveryOption(
                        id="16182cde-1c1b-3310-9315-a123456bcd99",
                        type="EksAddOn",
                        source_id="a5c84c81-1c1b-3310-9315-331376cc34bc",
                        title="EKS AddOn title",
                        short_description="Short description of product",
                        compatibility=DeliveryOptionCompatibility(
                            kubernetes_versions=["1.22", "1.23"],
                            architectures=["amd64", "arm64"]
                        ),
                        instructions=Instructions(
                            usage="Usage instructions"
                        ),
                        add_on_type="gitops",
                        visibility="Limited",
                        namespace="eks-namespace",
                        environment_override_parameters=[
                            EnvironmentOverrideParameter(
                                key="global.aws-region",
                                value="cluster_name"
                            )
                        ],
                        display_add_on_name="display-name",
                        add_on_name="name",
                        display_add_on_version="v1.2.1-eksbuild.1",
                        add_on_version="1.2.1"
                    )
                ]
            )
        ],
        description=Description(
            product_title="Container Test Product",
            product_code="9abcdefg9bw4k0zssg7thx123",
            short_description="Product description",
            long_description="Long product description",
            sku="SKU",
            highlights=["Test product"],
            search_keywords=["AWS"],
            visibility="Limited",
            product_state="Active",
            categories=["Operating Systems"]
        ),
        targeting=Targeting(
            positive_targeting=PositiveTargeting(
                buyer_accounts=["123456789123"]
            )
        ),
        promotional_resources=PromotionalResources(
            logo_url="https://s3.amazonaws.com/awsmp-logos/logo.png",
            videos=[
                Video(
                    type="Link",
                    title="Product Video",
                    url="https://s3.amazonaws.com/media/video.mp4"
                )
            ],
            additional_resources=[
                AdditionalResource(
                    type="Link",
                    text="Additional Resource",
                    url="amazon.com"
                )
            ]
        ),
        signature_verification_keys=[
            SignatureVerificationKey(
                public_key="-----BEGIN PUBLIC KEY-----\\nPublicKeyExample\\n-----END PUBLIC KEY-----\\n",
                status="Active",
                public_key_version=1
            )
        ],
        support_information=SupportInformation(
            description="Product support information"
        ),
        dimensions=[
            Dimension(
                name="Dimension 1",
                description="description",
                key="dimension1",
                unit="bit",
                types=["Metered"]
            )
        ],
        repositories=[
            Repository(
                url="123456789123.dkr.ecr.us-east-1.amazonaws.com/test-repository-1",
                type="ECR"
            ),
            Repository(
                url="123456789123.dkr.ecr.us-east-1.amazonaws.com/test-repository-2",
                type="ECR"
            )
        ]
    )

    assert actual_detail == expected_detail, "Deserialized object does not match expected object"

def test_create_product_change_detail_serialization():
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.create_product_change_detail import CreateProductChangeDetail

    create_product_change_detail = CreateProductChangeDetail(product_title="MyProductTitle")
    actual_json = create_product_change_detail.to_json()
    expected_json = {
        "ProductTitle": "MyProductTitle"
    }

    assert actual_json == json.dumps(expected_json), "Generated CreateProductChangeDetail does not match expected json"

def test_update_delivery_options_change_detail_serialization():
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.update_delivery_options_change_detail import UpdateDeliveryOptionsChangeDetail
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.update_delivery_options_version import UpdateDeliveryOptionsVersion
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.update_delivery_option import UpdateDeliveryOption
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.update_delivery_options_details import UpdateDeliveryOptionsDetails
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.update_delivery_options_ecr_delivery_option_details import UpdateDeliveryOptionsEcrDeliveryOptionDetails
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.deployment_resource import DeploymentResource
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.update_delivery_options_helm_delivery_option_details import UpdateDeliveryOptionsHelmDeliveryOptionDetails
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.override_parameter import OverrideParameter
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.metadata import Metadata
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.update_delivery_options_eks_add_on_delivery_option_details import UpdateDeliveryOptionsEksAddOnDeliveryOptionDetails
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.environment_override_parameter import EnvironmentOverrideParameter

    update_information_change_detail = UpdateDeliveryOptionsChangeDetail(
        version=UpdateDeliveryOptionsVersion(
            version_title="1.1",
            release_notes="Release Notes"
        ),
        delivery_options=[
            UpdateDeliveryOption(
                id="00000000-0000-0000-0000-000000000000",
                details=UpdateDeliveryOptionsDetails(
                    ecr_delivery_option_details=UpdateDeliveryOptionsEcrDeliveryOptionDetails(
                        delivery_option_title="EKS Container image only delivery option",
                        container_images=["111122223333.dkr.ecr.us-east-1.amazonaws.com/some-seller-prefix/my-image:1.0"],
                        deployment_resources=[DeploymentResource(
                            name="HelmDeploymentTemplate",
                            url="111122223333.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame2:mychart1.1"
                        )],
                        compatible_services=["EKS"],
                        description="Sample Description",
                        usage_instructions="instructions"
                    )
                )
            ),
            UpdateDeliveryOption(
                id="00000000-0000-0000-0000-000000000000",
                details=UpdateDeliveryOptionsDetails(
                    helm_delivery_option_details=UpdateDeliveryOptionsHelmDeliveryOptionDetails(
                        delivery_option_title="my eks fulfillment option",
                        container_images=["111122223333.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame1:1.1"],
                        compatible_services=["EKS", "EKS-Anywhere"],
                        helm_chart_uri="111122223333.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame1:helmchart1.1",
                        description="Helm chart description",
                        usage_instructions="Usage instructions",
                        marketplace_service_account_name="service-account-name",
                        release_name="release-name",
                        namespace="cluster-namespace",
                        quick_launch_enabled=True,
                        override_parameters=[
                            OverrideParameter(
                                key="global.aws.region",
                                default_value="us-east-1",
                                metadata=Metadata(
                                    label="AWS region",
                                    description="Default region for launch",
                                    obfuscate=False
                                )
                            )
                        ]
                    )
                )
            ),
            UpdateDeliveryOption(
                id="00000000-0000-0000-0000-000000000000",
                details=UpdateDeliveryOptionsDetails(
                    eks_add_on_delivery_option_details=UpdateDeliveryOptionsEksAddOnDeliveryOptionDetails(
                        description="Description for delivery option provided by ISV",
                        usage_instructions="Usage instructions with launch instructions",
                        container_images=["111122223333.dkr.ecr.us-east-1.amazonaws.com/test-seller/canary-test-repo-product-6:mongo"],
                        compatible_kubernetes_versions=["1.25", "1.26"],
                        helm_chart_uri="111122223333.dkr.ecr.us-east-1.amazonaws.com/rocket/rocket-product-helm:1.0",
                        add_on_name="aws-mp-test",
                        add_on_version="1.2.1",
                        add_on_type="networking",
                        supported_architectures=["amd64", "arm64"],
                        namespace="my-test-namespace",
                        environment_override_parameters=[EnvironmentOverrideParameter(
                            key="my-field",
                            value="${AWS_EKS_CLUSTER_NAME}"
                        )],
                        delivery_option_title="AWS Marketplace Test AddOn"
                    )
                )

            )
        ]
    )

    actual_json = update_information_change_detail.to_json()
    expected_json = {
        "Version": {
            "VersionTitle": "1.1",
            "ReleaseNotes": "Release Notes"
        },
        "DeliveryOptions": [{
            "Id": "00000000-0000-0000-0000-000000000000",
            "Details": {
                "EcrDeliveryOptionDetails": {
                    "Description": "Sample Description",
                    "UsageInstructions": "instructions",
                    "ContainerImages": [
                        "111122223333.dkr.ecr.us-east-1.amazonaws.com/some-seller-prefix/my-image:1.0"
                    ],
                    "CompatibleServices": ["EKS"],
                    "DeploymentResources": [{
                        "Name": "HelmDeploymentTemplate",
                        "Url": "111122223333.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame2:mychart1.1"
                    }],
                    "DeliveryOptionTitle": "EKS Container image only delivery option"
                }
            }
        }, {
            "Id": "00000000-0000-0000-0000-000000000000",
            "Details": {
                "HelmDeliveryOptionDetails": {
                    "Description": "Helm chart description",
                    "UsageInstructions": "Usage instructions",
                    "ContainerImages": [
                        "111122223333.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame1:1.1"
                    ],
                    "CompatibleServices": ["EKS", "EKS-Anywhere"],
                    "HelmChartUri": "111122223333.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame1:helmchart1.1",
                    "QuickLaunchEnabled": True,
                    "ReleaseName": "release-name",
                    "Namespace": "cluster-namespace",
                    "MarketplaceServiceAccountName": "service-account-name",
                    "OverrideParameters": [{
                        "Key": "global.aws.region",
                        "DefaultValue": "us-east-1",
                        "Metadata": {
                            "Label": "AWS region",
                            "Description": "Default region for launch",
                            "Obfuscate": False
                        }
                    }],
                    "DeliveryOptionTitle": "my eks fulfillment option"
                }
            }
        }, {
            "Id": "00000000-0000-0000-0000-000000000000",
            "Details": {
                "EksAddOnDeliveryOptionDetails": {
                    "Description": "Description for delivery option provided by ISV",
                    "UsageInstructions": "Usage instructions with launch instructions",
                    "ContainerImages": [
                        "111122223333.dkr.ecr.us-east-1.amazonaws.com/test-seller/canary-test-repo-product-6:mongo"
                    ],
                    "HelmChartUri": "111122223333.dkr.ecr.us-east-1.amazonaws.com/rocket/rocket-product-helm:1.0",
                    "AddOnName": "aws-mp-test",
                    "AddOnVersion": "1.2.1",
                    "AddOnType": "networking",
                    "CompatibleKubernetesVersions": ["1.25", "1.26"],
                    "SupportedArchitectures": ["amd64", "arm64"],
                    "Namespace": "my-test-namespace",
                    "EnvironmentOverrideParameters": [{
                        "Key": "my-field",
                        "Value": "${AWS_EKS_CLUSTER_NAME}"
                    }],
                    "DeliveryOptionTitle": "AWS Marketplace Test AddOn"
                }
            }
        }]
    }

    assert actual_json == json.dumps(expected_json), "Generated UpdateDeliveryOptionsChangeDetail with ECR deliverydoes not match expected json"

def test_add_delivery_options_ecr_change_detail_serialization():
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.add_delivery_options_change_detail import AddDeliveryOptionsChangeDetail
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.add_version import AddVersion
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.add_delivery_option import AddDeliveryOption
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.add_delivery_option_details import AddDeliveryOptionDetails
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.add_delivery_option_details import AddDeliveryOptionsEcrDeliveryOptionDetails
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.deployment_resource import DeploymentResource

    add_delivery_options_change_detail = AddDeliveryOptionsChangeDetail(
        version=AddVersion(
            version_title="1.1",
            release_notes="Release notes"
        ),
        delivery_options=[AddDeliveryOption(
            delivery_option_title="EKS Container image only delivery option",
            details=AddDeliveryOptionDetails(
                ecr_delivery_option_details=AddDeliveryOptionsEcrDeliveryOptionDetails(
                    description="Sample Description",
                    usage_instructions="helm pull 111122223333.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame2:mychart1.1",
                    container_images=["111122223333.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame1:1.1"],
                    compatible_services=["EKS"],
                    deployment_resources=[DeploymentResource(
                        name="HelmDeploymentTemplate",
                        url="111122223333.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame2:mychart1.1"
                    )],
                    access_role_arn="arn:aws:iam::123456789012:role/myRole"
                )
            )
        )]
    )
    actual_json = add_delivery_options_change_detail.to_json()
    expected_json = {
        "Version": {
            "VersionTitle": "1.1",
            "ReleaseNotes": "Release notes"
        },
        "DeliveryOptions": [{
            "DeliveryOptionTitle": "EKS Container image only delivery option",
            "Details": {
                "EcrDeliveryOptionDetails": {
                    "Description": "Sample Description",
                    "UsageInstructions": "helm pull 111122223333.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame2:mychart1.1",
                    "ContainerImages": [
                        "111122223333.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame1:1.1"
                    ],
                    "CompatibleServices": ["EKS"],
                    "DeploymentResources": [{
                        "Name": "HelmDeploymentTemplate",
                        "Url": "111122223333.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame2:mychart1.1"
                    }],
                    "AccessRoleArn": "arn:aws:iam::123456789012:role/myRole"
                }
            }
        }]
    }

    assert actual_json == json.dumps(expected_json), "Generated AddDeliveryOptionsChangeDetail with ECR delivery does not match expected json"

def test_add_delivery_options_helm_change_detail_serialization():
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.add_delivery_options_change_detail import AddDeliveryOptionsChangeDetail
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.add_version import AddVersion
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.add_delivery_option import AddDeliveryOption
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.add_delivery_option_details import AddDeliveryOptionDetails
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.add_delivery_option_details import AddDeliveryOptionsHelmDeliveryOptionDetails
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.override_parameter import OverrideParameter
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.metadata import Metadata

    add_delivery_options_change_detail = AddDeliveryOptionsChangeDetail(
        version=AddVersion(
            version_title="1.1",
            release_notes="Release notes"
        ),
        delivery_options=[AddDeliveryOption(
            delivery_option_title="HelmChartDeliveryOption",
            details=AddDeliveryOptionDetails(
                helm_delivery_option_details=AddDeliveryOptionsHelmDeliveryOptionDetails(
                    description="Helm chart description",
                    usage_instructions="Usage instructions",
                    container_images=["111122223333.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame1:1.1"],
                    compatible_services=["EKS", "EKS-Anywhere"],
                    helm_chart_uri="111122223333.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame1:helmchart1.1",
                    quick_launch_enabled=True,
                    release_name="Optional release name",
                    namespace="Optional Kubernetes namespace",
                    marketplace_service_account_name="Service account name",
                    override_parameters=[
                        OverrideParameter(
                            key="HelmKeyName1",
                            default_value="${AWSMP_LICENSE_SECRET}",
                            metadata=Metadata(
                                label="AWS CloudFormation template field label",
                                description="AWS CloudFormation template field description",
                                obfuscate=False
                            )
                        ),
                        OverrideParameter(
                            key="HelmKeyName2",
                            default_value="${AWSMP_SERVICE_ACCOUNT}",
                            metadata=Metadata(
                                label="AWS CloudFormation template field label",
                                description="AWS CloudFormation template field description",
                                obfuscate=False
                            )
                        )
                    ]
                )
            )
        )]
    )
    actual_json = add_delivery_options_change_detail.to_json()
    expected_json = {
        "Version": {
            "VersionTitle": "1.1",
            "ReleaseNotes": "Release notes"
        },
        "DeliveryOptions": [{
            "DeliveryOptionTitle": "HelmChartDeliveryOption",
            "Details": {
                "HelmDeliveryOptionDetails": {
                    "Description": "Helm chart description",
                    "UsageInstructions": "Usage instructions",
                    "ContainerImages": [
                        "111122223333.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame1:1.1"
                    ],
                    "CompatibleServices": ["EKS", "EKS-Anywhere"],
                    "HelmChartUri": "111122223333.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame1:helmchart1.1",
                    "QuickLaunchEnabled": True,
                    "ReleaseName": "Optional release name",
                    "Namespace": "Optional Kubernetes namespace",
                    "MarketplaceServiceAccountName": "Service account name",
                    "OverrideParameters": [{
                        "Key": "HelmKeyName1",
                        "DefaultValue": "${AWSMP_LICENSE_SECRET}",
                        "Metadata": {
                            "Label": "AWS CloudFormation template field label",
                            "Description": "AWS CloudFormation template field description",
                            "Obfuscate": False
                        }
                    }, {
                        "Key": "HelmKeyName2",
                        "DefaultValue": "${AWSMP_SERVICE_ACCOUNT}",
                        "Metadata": {
                            "Label": "AWS CloudFormation template field label",
                            "Description": "AWS CloudFormation template field description",
                            "Obfuscate": False
                        }
                    }]
                }
            }
        }]
    }

    assert actual_json == json.dumps(expected_json), "Generated AddDeliveryOptionsChangeDetail with Helm delivery does not match expected json"

def test_add_delivery_options_eks_change_detail_serialization():
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.add_delivery_options_change_detail import AddDeliveryOptionsChangeDetail
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.add_version import AddVersion
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.add_delivery_option import AddDeliveryOption
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.add_delivery_option_details import AddDeliveryOptionDetails
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.add_delivery_option_details import AddDeliveryOptionsEksAddOnDeliveryOptionDetails
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.add_delivery_option_visibility import AddDeliveryOptionVisibility
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.environment_override_parameter import EnvironmentOverrideParameter

    add_delivery_options_change_detail = AddDeliveryOptionsChangeDetail(
        version=AddVersion(
            version_title="1.1",
            release_notes="Release notes"
        ),
        delivery_options=[AddDeliveryOption(
            delivery_option_title="AWS Marketplace Test AddOn",
            release=False,
            visibility=AddDeliveryOptionVisibility.LIMITED,
            details=AddDeliveryOptionDetails(
                eks_add_on_delivery_option_details=AddDeliveryOptionsEksAddOnDeliveryOptionDetails(
                    description="Description for delivery option provided by ISV",
                    usage_instructions="Usage instructions with launch instructions",
                    container_images=["111122223333.dkr.ecr.us-east-1.amazonaws.com/test-seller/canary-test-repo-product-6:mongo"],
                    compatible_kubernetes_versions=["1.25", "1.26"],
                    helm_chart_uri="111122223333.dkr.ecr.us-east-1.amazonaws.com/rocket/rocket-product-helm:1.0",
                    add_on_name="aws-mp-test",
                    add_on_version="1.2.1",
                    add_on_type="networking",
                    supported_architectures=["amd64", "arm64"],
                    namespace="my-test-namespace",
                    environment_override_parameters=[EnvironmentOverrideParameter(
                        key="my-field",
                        value="${AWS_EKS_CLUSTER_NAME}"
                    )]
                )
            )
        )]
    )
    actual_json = add_delivery_options_change_detail.to_json()
    expected_json = {
        "Version": {
            "VersionTitle":  "1.1",
            "ReleaseNotes":  "Release notes"
        },
        "DeliveryOptions": [{
            "DeliveryOptionTitle":  "AWS Marketplace Test AddOn",
            "Release":  False,
            "Visibility":  "Limited",
            "Details":  {
                "EksAddOnDeliveryOptionDetails":  {
                    "Description": "Description for delivery option provided by ISV",
                    "UsageInstructions": "Usage instructions with launch instructions",
                    "ContainerImages": [
                        "111122223333.dkr.ecr.us-east-1.amazonaws.com/test-seller/canary-test-repo-product-6:mongo"
                    ],
                    "HelmChartUri": "111122223333.dkr.ecr.us-east-1.amazonaws.com/rocket/rocket-product-helm:1.0",
                    "AddOnName": "aws-mp-test",
                    "AddOnVersion": "1.2.1",
                    "AddOnType": "networking",
                    "CompatibleKubernetesVersions": ["1.25", "1.26"],
                    "SupportedArchitectures": ["amd64", "arm64"],
                    "Namespace": "my-test-namespace",
                    "EnvironmentOverrideParameters": [{
                        "Key": "my-field",
                        "Value": "${AWS_EKS_CLUSTER_NAME}"
                    }]
                }
            }
        }]
    }

    assert actual_json == json.dumps(expected_json), "Generated AddDeliveryOptionsChangeDetail with ECR delivery does not match expected json"

def test_restrict_delivery_options_change_detail_serialization():
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.restrict_delivery_options_change_detail import RestrictDeliveryOptionsChangeDetail

    restrict_delivery_options_change_detail = RestrictDeliveryOptionsChangeDetail(
        delivery_option_ids=["00000000-0000-0000-0000-000000000000"]
    )
    actual_json = restrict_delivery_options_change_detail.to_json()
    expected_json = {
        "DeliveryOptionIds": ["00000000-0000-0000-0000-000000000000"]
    }

    assert actual_json == json.dumps(expected_json), "Generated RestrictDeliveryOptionsChangeDetail does not match expected json"

def test_update_delivery_options_visibility_change_detail_serialization():
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.update_delivery_options_visibility_change_detail import UpdateDeliveryOptionsVisibilityChangeDetail
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.update_delivery_option_visibility import UpdateDeliveryOptionVisibility
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.update_delivery_options_target_visibility import UpdateDeliveryOptionsTargetVisibility

    update_delivery_options_visibility_change_detail = UpdateDeliveryOptionsVisibilityChangeDetail(
        delivery_options=[UpdateDeliveryOptionVisibility(
            id="00000000-0000-0000-0000-000000000000",
            target_visibility=UpdateDeliveryOptionsTargetVisibility.PUBLIC
        )]
    )
    actual_json = update_delivery_options_visibility_change_detail.to_json()
    expected_json = {
        "DeliveryOptions": [{
            "Id": "00000000-0000-0000-0000-000000000000",
            "TargetVisibility": "Public"
        }]
    }

    assert actual_json == json.dumps(expected_json), "Generated UpdateDeliveryOptionsVisibilityChangeDetail does not match expected json"

def test_update_information_change_detail_serialization():
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.update_information_change_detail import UpdateInformationChangeDetail
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.additional_resource import AdditionalResource

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

def test_add_repositories_change_detail_serialization():
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.add_repositories_change_detail import AddRepositoriesChangeDetail
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.repository import Repository

    add_repositories_change_detail = AddRepositoriesChangeDetail(
        repositories=[Repository(
            repository_name="MyRepositoryName",
            repository_type="ECR"
        )]
    )
    actual_json = add_repositories_change_detail.to_json()
    expected_json = {
        "Repositories": [{
            "RepositoryName": "MyRepositoryName",
            "RepositoryType": "ECR"
        }]
    }

    assert actual_json == json.dumps(expected_json), "Generated AddRepositoriesChangeDetail does not match expected json"

def test_add_dimension_change_detail_serialization():
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.add_dimension_change_detail import AddDimensionChangeDetail
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.dimension_type import DimensionType

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
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.update_dimension_change_detail import UpdateDimensionChangeDetail
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.dimension_type import DimensionType

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
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.update_targeting_change_detail import UpdateTargetingChangeDetail
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.positive_targeting import PositiveTargeting

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
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.update_visibility_change_detail import UpdateVisibilityChangeDetail
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.target_visibility import TargetVisibility

    update_visibility_change_detail = UpdateVisibilityChangeDetail(
        target_visibility=TargetVisibility.PUBLIC,
        replacement_product_id="prod-1234567890123")
    actual_json = update_visibility_change_detail.to_json()
    expected_json = {
        "TargetVisibility": "Public",
        "ReplacementProductId": "prod-1234567890123"
    }

    assert actual_json == json.dumps(expected_json), "Generated UpdateVisibilityChangeDetail does not match expected json"

def test_release_product_change_detail_serialization():
    from aws_marketplace_catalog_shapes_containerproduct_1_0_changetypes.models.release_product_change_detail import ReleaseProductChangeDetail

    release_product_change_detail = ReleaseProductChangeDetail()
    actual_json = release_product_change_detail.to_json()
    expected_json = {}

    assert actual_json == json.dumps(expected_json), "Generated ReleaseProductChangeDetail does not match expected json"
