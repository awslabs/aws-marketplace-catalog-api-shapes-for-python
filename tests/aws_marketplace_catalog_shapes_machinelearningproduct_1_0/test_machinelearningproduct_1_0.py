import pytest
import json

def test_importable():
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.machine_learning_product_entity_detail import MachineLearningProductEntityDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.create_product_change_detail import CreateProductChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.update_delivery_options_change_detail import UpdateDeliveryOptionsChangeDetail # noqa: F401
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.add_delivery_options_change_detail import AddDeliveryOptionsChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.restrict_delivery_options_change_detail import RestrictDeliveryOptionsChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.update_information_change_detail import UpdateInformationChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.update_targeting_change_detail import UpdateTargetingChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.update_visibility_change_detail import UpdateVisibilityChangeDetail  # noqa: F401

    assert True

def test_machinelearningproduct_1_0_model_package_entity_detail_deserialization():
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.machine_learning_product_entity_detail import MachineLearningProductEntityDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.version import Version
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.source import Source
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.delivery_option import DeliveryOption
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.instructions import Instructions
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.description import Description
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.targeting import Targeting
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.positive_targeting import PositiveTargeting
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.promotional_resources import PromotionalResources
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.video import Video
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.additional_resource import AdditionalResource
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.support_information import SupportInformation
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.dimension import Dimension
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.region_availability import RegionAvailability
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.input_properties import InputProperties
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.output_properties import OutputProperties
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.parameter import Parameter
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.output_parameter import OutputParameter
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.sample import Sample
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.supported_instance_types import SupportedInstanceTypes
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.recommended_instance_types import RecommendedInstanceTypes
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.region_availability import RegionAvailability

    expected_json = {
        "Versions": [{
            "Id": "00000000-0000-0000-0000-000000000000",
            "ReleaseNotes": "ML version test 1",
            "VersionTitle": "ML version test 1",
            "CreationDate": "2025-06-12T20:57:59.172Z",
            "Sources": [{
                "Type": "SageMakerModelPackage",
                "Id": "9784a25e-70d1-4cd2-b161-7f1cb207c886",
                "ModelPackageArn": "arn:aws:sagemaker:us-east-2:123456789123:model-package/ml-test-model"
            }],
            "DeliveryOptions": [{
                "Id": "00000000-0000-0000-0000-000000000000",
                "Type": "SageMakerModelPackage",
                "SourceId": "00000000-0000-0000-0000-000000000000",
                "Title": "SageMaker Model",
                "ShortDescription": "SageMaker ModelDelivery Option",
                "Instructions": {
                    "Usage": "This is how you use your model package",
                    "SampleNotebookUrl": "https://www.amazon.com",
                    "RepositoryUrl": "https://www.amazon.com",
                    "InputProperties": {
                        "Description": "Input should have all columns in the train/test file except for 'is_fraud' column.",
                        "Limitations": "Can predict on 1 input in the CSV only at a time",
                        "Parameters": [
                            {
                                "Name": "prompt1",
                                "Description": "Represents the instruct-style prompt for the model.",
                                "Constraints": "Max size=100",
                                "Required": True
                            },
                            {
                                "Name": "maxTokens1",
                                "Description": "Denotes the number of tokens to predict per generation.",
                                "Required": False
                            }
                        ],
                        "SageMakerCustomAttributes": [
                            {
                                "Name": "threshold1",
                                "Description": "Threshold of the confidence score of the detected object",
                                "Constraints": "MinValue : 0.0, MaxValue : 1.0, Required: true",
                                "Required": False
                            }
                        ],
                        "SampleInput": {
                            "RealtimeInferenceText": "text",
                            "BatchTransformUrl": "https://www.sampleData.com"
                        }
                    },
                    "OutputProperties": {
                        "Description": "The output is a JSON object that has the generated text along with likelihoods of tokens, if requested. See example json.",
                        "Parameters": [
                            {
                                "Name": "id",
                                "Description": "An identifier for response",
                                "AlwaysReturned": False
                            },
                            {
                                "Name": "generations",
                                "Description": "The generated text along with the likelihoods for tokens requested.",
                                "AlwaysReturned": False
                            }
                        ],
                        "SampleOutput": {
                            "RealtimeInferenceUrl": "https://www.sampledata.com",
                            "BatchTransformUrl": "https://www.amazon.com"
                        }
                    }
                },
                "RecommendedInstanceTypes": {
                    "BatchTransform": "ml.m5.large",
                    "RealtimeInference": "ml.m5.large"
                },
                "SupportedInstanceTypes": {
                    "BatchTransform": ["ml.m5.large"],
                    "RealtimeInference": ["ml.m5.large"]
                },
                "Visibility": "Public"
            }
            ]
        }],
        "Description": {
            "ProductTitle": "ML test product",
            "ProductCode": "a1cl2qqbjvpp7xurfh7oebrl8",
            "ShortDescription": "Brief description",
            "LongDescription": "Detailed description",
            "Sku": None,
            "Highlights": ["Sample highlight"],
            "SearchKeywords": ["Sample keyword"],
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
            "LogoUrl": "https://awsmp-logos.s3.amazonaws.com/0000000000000000",
            "Videos": [],
            "AdditionalResources": []
        },
        "SupportInformation": {
            "Description": "Need help? Contact our AWS security experts at aws.marketplace.com."
        },
        "Dimensions": [
            {
                "Name": "inference.count.m.i.c Inference Pricing",
                "Description": "inference.count.m.i.c Inference Pricing",
                "Key": "inference.count.m.i.c",
                "Unit": "Requests",
                "Types": ["Metered"]
            },
            {
                "Name": "ml.m5.large Inference (Batch)",
                "Description": "Model inference on the ml.m5.large instance type, batch mode",
                "Key": "ml.m5.large.m.i.b",
                "Unit": "HostHrs",
                "Types": ["Metered"]
            },
            {
                "Name": "ml.m5.large Inference (Real-Time)",
                "Description": "Model inference on the ml.m5.large instance type, real-time mode",
                "Key": "ml.m5.large.m.i.r",
                "Unit": "HostHrs",
                "Types": ["Metered"]
            }
        ],
        "RegionAvailability": {
            "FutureRegionSupport": None,
            "Restrict": [],
            "Regions": [
                "ap-south-1",
                "eu-north-1",
                "eu-west-3",
                "eu-west-2",
                "eu-west-1",
                "ap-northeast-2",
                "ap-northeast-1",
                "ca-central-1",
                "sa-east-1",
                "ap-southeast-1",
                "ap-southeast-2",
                "eu-central-1",
                "us-east-1",
                "us-east-2",
                "us-west-1",
                "us-west-2"
            ]
        }
    }

    actual_detail = MachineLearningProductEntityDetail.from_json(json.dumps(expected_json))
    expected_detail = MachineLearningProductEntityDetail(
        versions=[
            Version(
                id="00000000-0000-0000-0000-000000000000",
                release_notes="ML version test 1",
                version_title="ML version test 1",
                creation_date="2025-06-12T20:57:59.172Z",
                sources=[
                    Source(
                        type="SageMakerModelPackage",
                        id="9784a25e-70d1-4cd2-b161-7f1cb207c886",
                        model_package_arn="arn:aws:sagemaker:us-east-2:123456789123:model-package/ml-test-model"
                    )
                ],
                delivery_options=[
                    DeliveryOption(
                        id="00000000-0000-0000-0000-000000000000",
                        type="SageMakerModelPackage",
                        source_id="00000000-0000-0000-0000-000000000000",
                        title="SageMaker Model",
                        short_description="SageMaker ModelDelivery Option",
                        instructions=Instructions(
                            usage="This is how you use your model package",
                            sample_notebook_url="https://www.amazon.com",
                            repository_url="https://www.amazon.com",
                            input_properties=InputProperties(
                                description="Input should have all columns in the train/test file except for 'is_fraud' column.",
                                limitations="Can predict on 1 input in the CSV only at a time",
                                parameters=[
                                    Parameter(
                                        name="prompt1",
                                        description="Represents the instruct-style prompt for the model.",
                                        constraints="Max size=100",
                                        required=True
                                    ),
                                    Parameter(
                                        name="maxTokens1",
                                        description="Denotes the number of tokens to predict per generation.",
                                        required=False
                                    )
                                ],
                                sage_maker_custom_attributes=[
                                    Parameter(
                                        name="threshold1",
                                        description="Threshold of the confidence score of the detected object",
                                        constraints="MinValue : 0.0, MaxValue : 1.0, Required: true",
                                        required=False
                                    )
                                ],
                                sample_input=Sample(
                                    realtime_inference_text="text",
                                    batch_transform_url="https://www.sampleData.com"
                                )
                            ),
                            output_properties=OutputProperties(
                                description="The output is a JSON object that has the generated text along with likelihoods of tokens, if requested. See example json.",
                                parameters=[
                                    OutputParameter(
                                        name="id",
                                        description="An identifier for response",
                                        always_returned=False
                                    ),
                                    OutputParameter(
                                        name="generations",
                                        description="The generated text along with the likelihoods for tokens requested.",
                                        always_returned=False
                                    )
                                ],
                                sample_output=Sample(
                                    realtime_inference_url="https://www.sampledata.com",
                                    batch_transform_url="https://www.amazon.com"
                                )
                            )
                        ),
                        recommended_instance_types=RecommendedInstanceTypes(
                            batch_transform="ml.m5.large",
                            realtime_inference="ml.m5.large"
                        ),
                        supported_instance_types=SupportedInstanceTypes(
                            batch_transform=["ml.m5.large"],
                            realtime_inference=["ml.m5.large"]
                        ),
                        visibility="Public"
                    )
                ]
            )
        ],
        description=Description(
            product_title="ML test product",
            product_code="a1cl2qqbjvpp7xurfh7oebrl8",
            short_description="Brief description",
            long_description="Detailed description",
            sku=None,
            highlights=["Sample highlight"],
            search_keywords=["Sample keyword"],
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
            logo_url="https://awsmp-logos.s3.amazonaws.com/0000000000000000",
            videos=[],
            additional_resources=[]
        ),
        support_information=SupportInformation(
            description="Need help? Contact our AWS security experts at aws.marketplace.com."
        ),
        dimensions=[
            Dimension(
                name="inference.count.m.i.c Inference Pricing",
                description="inference.count.m.i.c Inference Pricing",
                key="inference.count.m.i.c",
                unit="Requests",
                types=["Metered"]
            ),
            Dimension(
                name="ml.m5.large Inference (Batch)",
                description="Model inference on the ml.m5.large instance type, batch mode",
                key="ml.m5.large.m.i.b",
                unit="HostHrs",
                types=["Metered"]
            ),
            Dimension(
                name="ml.m5.large Inference (Real-Time)",
                description="Model inference on the ml.m5.large instance type, real-time mode",
                key="ml.m5.large.m.i.r",
                unit="HostHrs",
                types=["Metered"]
            )
        ],
        region_availability=RegionAvailability(
            future_region_support=None,
            restrict=[],
            regions=[
                "ap-south-1",
                "eu-north-1",
                "eu-west-3",
                "eu-west-2",
                "eu-west-1",
                "ap-northeast-2",
                "ap-northeast-1",
                "ca-central-1",
                "sa-east-1",
                "ap-southeast-1",
                "ap-southeast-2",
                "eu-central-1",
                "us-east-1",
                "us-east-2",
                "us-west-1",
                "us-west-2"
            ]
        )
    )
    assert actual_detail == expected_detail, "Deserialized object does not match expected object"

def test_machinelearningproduct_1_0_algorithm_entity_detail_deserialization():
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.machine_learning_product_entity_detail import MachineLearningProductEntityDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.version import Version
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.source import Source
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.delivery_option import DeliveryOption
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.instructions import Instructions
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.description import Description
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.targeting import Targeting
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.positive_targeting import PositiveTargeting
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.promotional_resources import PromotionalResources
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.video import Video
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.additional_resource import AdditionalResource
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.support_information import SupportInformation
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.dimension import Dimension
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.region_availability import RegionAvailability
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.input_properties import InputProperties
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.output_properties import OutputProperties
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.parameter import Parameter
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.output_parameter import OutputParameter
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.sample import Sample
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.supported_instance_types import SupportedInstanceTypes
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.recommended_instance_types import RecommendedInstanceTypes
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_entitytype.models.region_availability import RegionAvailability

    expected_json = {
        "Versions": [{
            "Id": "00000000-0000-0000-0000-000000000000",
            "ReleaseNotes": "ML version test 1",
            "VersionTitle": "ML version test 1",
            "CreationDate": "2025-06-12T20:57:59.172Z",
            "Sources": [{
                "Type": "SageMakerAlgorithm",
                "Id": "00000000-0000-0000-0000-000000000000",
                "AlgorithmArn": "arn:aws:sagemaker:us-east-2:123456789123:algorithm/ml-test-algorithm"
            }],
            "DeliveryOptions": [{
                "Id": "00000000-0000-0000-0000-000000000000",
                "Type": "SageMakerAlgorithm",
                "SourceId": "00000000-0000-0000-0000-000000000000",
                "Title": "SageMaker Model",
                "ShortDescription": "SageMaker AlgorithmDelivery Option",
                "Instructions": {
                    "Usage": "This is how you use your model package",
                    "SampleNotebookUrl": "https://www.amazon.com",
                    "RepositoryUrl": "https://www.amazon.com",
                    "InputProperties": {
                        "Description": "Input should have all columns in the train/test file except for 'is_fraud' column.",
                        "Limitations": "Can predict on 1 input in the CSV only at a time",
                        "Parameters": [
                            {
                                "Name": "prompt1",
                                "Description": "Represents the instruct-style prompt for the model.",
                                "Constraints": "Max size=100",
                                "Required": True
                            },
                            {
                                "Name": "maxTokens1",
                                "Description": "Denotes the number of tokens to predict per generation.",
                                "Required": False
                            }
                        ],
                        "SageMakerCustomAttributes": [
                            {
                                "Name": "threshold1",
                                "Description": "Threshold of the confidence score of the detected object",
                                "Constraints": "MinValue : 0.0, MaxValue : 1.0, Required: true",
                                "Required": False
                            }
                        ],
                        "SampleInput": {
                            "RealtimeInferenceText": "text",
                            "BatchTransformUrl": "https://www.sampleData.com"
                        }
                    },
                    "OutputProperties": {
                        "Description": "The output is a JSON object that has the generated text along with likelihoods of tokens, if requested. See example json.",
                        "Parameters": [
                            {
                                "Name": "id",
                                "Description": "An identifier for response",
                                "AlwaysReturned": False
                            },
                            {
                                "Name": "generations",
                                "Description": "The generated text along with the likelihoods for tokens requested.",
                                "AlwaysReturned": False
                            }
                        ],
                        "SampleOutput": {
                            "RealtimeInferenceUrl": "https://www.sampledata.com",
                            "BatchTransformUrl": "https://www.amazon.com"
                        }
                    }
                },
                "RecommendedInstanceTypes": {
                    "BatchTransform": "ml.m5.large",
                    "RealtimeInference": "ml.m5.large",
                    "Training": "ml.m5.large"
                },
                "SupportedInstanceTypes": {
                    "BatchTransform": ["ml.m5.large"],
                    "RealtimeInference": ["ml.m5.large"],
                    "Training": ["ml.m5.large"]
                },
                "Visibility": "Public"
            }]
        }],
        "Description": {
            "ProductTitle": "ML test product",
            "ProductCode": "a1cl2qqbjvpp7xurfh7oebrl8",
            "ShortDescription": "Brief description",
            "LongDescription": "Detailed description",
            "Sku": None,
            "Highlights": ["Sample highlight"],
            "SearchKeywords": ["Sample keyword"],
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
            "LogoUrl": "https://awsmp-logos.s3.amazonaws.com/0000000000000000",
            "Videos": [],
            "AdditionalResources": []
        },
        "SupportInformation": {
            "Description": "Need help? Contact our AWS security experts at aws.marketplace.com."
        },
        "Dimensions": [
            {
                "Name": "inference.count.m.i.c Inference Pricing",
                "Description": "inference.count.m.i.c Inference Pricing",
                "Key": "inference.count.m.i.c",
                "Unit": "Requests",
                "Types": ["Metered"]
            },
            {
                "Name": "ml.m5.large Inference (Batch)",
                "Description": "Model inference on the ml.m5.large instance type, batch mode",
                "Key": "ml.m5.large.m.i.b",
                "Unit": "HostHrs",
                "Types": ["Metered"]
            },
            {
                "Name": "ml.m5.large Inference (Real-Time)",
                "Description": "Model inference on the ml.m5.large instance type, real-time mode",
                "Key": "ml.m5.large.m.i.r",
                "Unit": "HostHrs",
                "Types": ["Metered"]
            }
        ],
        "RegionAvailability": {
            "FutureRegionSupport": None,
            "Restrict": [],
            "Regions": [
                "ap-south-1",
                "eu-north-1",
                "eu-west-3",
                "eu-west-2",
                "eu-west-1",
                "ap-northeast-2",
                "ap-northeast-1",
                "ca-central-1",
                "sa-east-1",
                "ap-southeast-1",
                "ap-southeast-2",
                "eu-central-1",
                "us-east-1",
                "us-east-2",
                "us-west-1",
                "us-west-2"
            ]
        }
    }

    actual_detail = MachineLearningProductEntityDetail.from_json(json.dumps(expected_json))
    expected_detail = MachineLearningProductEntityDetail(
        versions=[
            Version(
                id="00000000-0000-0000-0000-000000000000",
                release_notes="ML version test 1",
                version_title="ML version test 1",
                creation_date="2025-06-12T20:57:59.172Z",
                sources=[
                    Source(
                        type="SageMakerAlgorithm",
                        id="00000000-0000-0000-0000-000000000000",
                        algorithm_arn="arn:aws:sagemaker:us-east-2:123456789123:algorithm/ml-test-algorithm"
                    )
                ],
                delivery_options=[
                    DeliveryOption(
                        id="00000000-0000-0000-0000-000000000000",
                        type="SageMakerAlgorithm",
                        source_id="00000000-0000-0000-0000-000000000000",
                        title="SageMaker Model",
                        short_description="SageMaker AlgorithmDelivery Option",
                        instructions=Instructions(
                            usage="This is how you use your model package",
                            sample_notebook_url="https://www.amazon.com",
                            repository_url="https://www.amazon.com",
                            input_properties=InputProperties(
                                description="Input should have all columns in the train/test file except for 'is_fraud' column.",
                                limitations="Can predict on 1 input in the CSV only at a time",
                                parameters=[
                                    Parameter(
                                        name="prompt1",
                                        description="Represents the instruct-style prompt for the model.",
                                        constraints="Max size=100",
                                        required=True
                                    ),
                                    Parameter(
                                        name="maxTokens1",
                                        description="Denotes the number of tokens to predict per generation.",
                                        required=False
                                    )
                                ],
                                sage_maker_custom_attributes=[
                                    Parameter(
                                        name="threshold1",
                                        description="Threshold of the confidence score of the detected object",
                                        constraints="MinValue : 0.0, MaxValue : 1.0, Required: true",
                                        required=False
                                    )
                                ],
                                sample_input=Sample(
                                    realtime_inference_text="text",
                                    batch_transform_url="https://www.sampleData.com"
                                )
                            ),
                            output_properties=OutputProperties(
                                description="The output is a JSON object that has the generated text along with likelihoods of tokens, if requested. See example json.",
                                parameters=[
                                    OutputParameter(
                                        name="id",
                                        description="An identifier for response",
                                        always_returned=False
                                    ),
                                    OutputParameter(
                                        name="generations",
                                        description="The generated text along with the likelihoods for tokens requested.",
                                        always_returned=False
                                    )
                                ],
                                sample_output=Sample(
                                    realtime_inference_url="https://www.sampledata.com",
                                    batch_transform_url="https://www.amazon.com"
                                )
                            )
                        ),
                        recommended_instance_types=RecommendedInstanceTypes(
                            batch_transform="ml.m5.large",
                            realtime_inference="ml.m5.large",
                            training="ml.m5.large"
                        ),
                        supported_instance_types=SupportedInstanceTypes(
                            batch_transform=["ml.m5.large"],
                            realtime_inference=["ml.m5.large"],
                            training=["ml.m5.large"]
                        ),
                        visibility="Public"
                    )
                ]
            )
        ],
        description=Description(
            product_title="ML test product",
            product_code="a1cl2qqbjvpp7xurfh7oebrl8",
            short_description="Brief description",
            long_description="Detailed description",
            sku=None,
            highlights=["Sample highlight"],
            search_keywords=["Sample keyword"],
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
            logo_url="https://awsmp-logos.s3.amazonaws.com/0000000000000000",
            videos=[],
            additional_resources=[]
        ),
        support_information=SupportInformation(
            description="Need help? Contact our AWS security experts at aws.marketplace.com."
        ),
        dimensions=[
            Dimension(
                name="inference.count.m.i.c Inference Pricing",
                description="inference.count.m.i.c Inference Pricing",
                key="inference.count.m.i.c",
                unit="Requests",
                types=["Metered"]
            ),
            Dimension(
                name="ml.m5.large Inference (Batch)",
                description="Model inference on the ml.m5.large instance type, batch mode",
                key="ml.m5.large.m.i.b",
                unit="HostHrs",
                types=["Metered"]
            ),
            Dimension(
                name="ml.m5.large Inference (Real-Time)",
                description="Model inference on the ml.m5.large instance type, real-time mode",
                key="ml.m5.large.m.i.r",
                unit="HostHrs",
                types=["Metered"]
            )
        ],
        region_availability=RegionAvailability(
            future_region_support=None,
            restrict=[],
            regions=[
                "ap-south-1",
                "eu-north-1",
                "eu-west-3",
                "eu-west-2",
                "eu-west-1",
                "ap-northeast-2",
                "ap-northeast-1",
                "ca-central-1",
                "sa-east-1",
                "ap-southeast-1",
                "ap-southeast-2",
                "eu-central-1",
                "us-east-1",
                "us-east-2",
                "us-west-1",
                "us-west-2"
            ]
        )
    )
    assert actual_detail == expected_detail, "Deserialized object does not match expected object"

def test_add_delivery_options_model_package_change_detail_serialization():
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.add_delivery_options_change_detail import AddDeliveryOptionsChangeDetail
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.add_version import AddVersion
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.add_delivery_option import AddDeliveryOption
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.add_delivery_options_details import AddDeliveryOptionsDetails
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.add_delivery_options_sage_maker_model_package_delivery_option_details import AddDeliveryOptionsSageMakerModelPackageDeliveryOptionDetails
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.input_properties import InputProperties
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.sample import Sample
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.parameter import Parameter
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.output_properties import OutputProperties
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.output_parameter import OutputParameter
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.sage_maker_model_package_recommended_instance_types import SageMakerModelPackageRecommendedInstanceTypes

    add_delivery_options_change_detail = AddDeliveryOptionsChangeDetail(
        version=AddVersion(
            version_title="1.1",
            release_notes="Release notes"
        ),
        delivery_options=[
            AddDeliveryOption(
                details=AddDeliveryOptionsDetails(
                    sage_maker_model_package_delivery_option_details=AddDeliveryOptionsSageMakerModelPackageDeliveryOptionDetails(
                        sage_maker_model_package_arn="arn:aws:sagemaker:us-east-2:123456789123:model-package/ml-test-model",
                        access_role_arn="arn:aws:iam::123456789012:role/myRole",
                        usage_instructions="Usage instructions",
                        sample_notebook_url="https://www.amazon.com",
                        repository_url="https://www.amazon.com",
                        input_properties=InputProperties(
                            description="Input should have all columns in the train/test file except for 'is_fraud' column.",
                            limitations="Can predict on 1 input in the CSV only at a time",
                            sample_input=Sample(
                                realtime_inference_text="text",
                                batch_transform_url="https://www.sampleData.com"
                            ),
                            parameters=[Parameter(
                                name="name1",
                                description="desc",
                                constraints="constraints",
                                required=False
                            )]
                        ),
                        output_properties=OutputProperties(
                            description="The output is a JSON object that has the generated text along with likelihoods of tokens, if requested. See example json.",
                            sample_output=Sample(
                                realtime_inference_url="https://www.sampledata.com",
                                batch_transform_url="https://www.amazon.com"
                            ),
                            parameters=[OutputParameter(
                                name="p1",
                                description="desc",
                                always_returned=False
                            )]
                        ),
                        recommended_instance_types=SageMakerModelPackageRecommendedInstanceTypes(
                            batch_transform="ml.m5.large",
                            realtime_inference="ml.m5.large"
                        )
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
            "Details": {
                "SageMakerModelPackageDeliveryOptionDetails": {
                    "UsageInstructions": "Usage instructions",
                    "SampleNotebookUrl": "https://www.amazon.com",
                    "RepositoryUrl": "https://www.amazon.com",
                    "InputProperties": {
                        "Description": "Input should have all columns in the train/test file except for 'is_fraud' column.",
                        "Limitations": "Can predict on 1 input in the CSV only at a time",
                        "SampleInput": {
                            "RealtimeInferenceText": "text",
                            "BatchTransformUrl": "https://www.sampleData.com"
                        },
                        "Parameters": [{
                            "Name": "name1",
                            "Description": "desc",
                            "Constraints": "constraints",
                            "Required": False
                        }]
                    },
                    "OutputProperties": {
                        "Description": "The output is a JSON object that has the generated text along with likelihoods of tokens, if requested. See example json.",
                        "SampleOutput": {
                            "RealtimeInferenceUrl": "https://www.sampledata.com",
                            "BatchTransformUrl": "https://www.amazon.com"
                        },
                        "Parameters": [{
                            "Name": "p1",
                            "Description": "desc",
                            "AlwaysReturned": False
                        }]
                    },
                    "RecommendedInstanceTypes": {
                        "BatchTransform": "ml.m5.large",
                        "RealtimeInference": "ml.m5.large"
                    },
                    "SageMakerModelPackageArn": "arn:aws:sagemaker:us-east-2:123456789123:model-package/ml-test-model",
                    "AccessRoleArn": "arn:aws:iam::123456789012:role/myRole"
                }
            }
        }]
    }

    assert actual_json == json.dumps(expected_json), "Generated AddDeliveryOptionsChangeDetail with model package delivery does not match expected json"

def test_add_delivery_options_algorithm_change_detail_serialization():
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.add_delivery_options_change_detail import AddDeliveryOptionsChangeDetail
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.add_version import AddVersion
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.add_delivery_option import AddDeliveryOption
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.add_delivery_options_details import AddDeliveryOptionsDetails
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.add_delivery_options_sage_maker_algorithm_delivery_option_details import AddDeliveryOptionsSageMakerAlgorithmDeliveryOptionDetails
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.input_properties import InputProperties
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.sample import Sample
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.parameter import Parameter
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.output_properties import OutputProperties
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.output_parameter import OutputParameter
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.sage_maker_algorithm_recommended_instance_types import SageMakerAlgorithmRecommendedInstanceTypes

    add_delivery_options_change_detail = AddDeliveryOptionsChangeDetail(
        version=AddVersion(
            version_title="1.1",
            release_notes="Release notes"
        ),
        delivery_options=[
            AddDeliveryOption(
                details=AddDeliveryOptionsDetails(
                    sage_maker_algorithm_delivery_option_details=AddDeliveryOptionsSageMakerAlgorithmDeliveryOptionDetails(
                        sage_maker_algorithm_arn="arn:aws:sagemaker:us-east-2:123456789123:algorithm/ml-test-algorithm",
                        access_role_arn="arn:aws:iam::123456789012:role/myRole",
                        usage_instructions="Usage instructions",
                        sample_notebook_url="https://www.amazon.com",
                        repository_url="https://www.amazon.com",
                        input_properties=InputProperties(
                            description="Input should have all columns in the train/test file except for 'is_fraud' column.",
                            limitations="Can predict on 1 input in the CSV only at a time",
                            sample_input=Sample(
                                realtime_inference_text="text",
                                batch_transform_url="https://www.sampleData.com"
                            ),
                            parameters=[Parameter(
                                name="name1",
                                description="desc",
                                constraints="constraints",
                                required=False
                            )]
                        ),
                        output_properties=OutputProperties(
                            description="The output is a JSON object that has the generated text along with likelihoods of tokens, if requested. See example json.",
                            sample_output=Sample(
                                realtime_inference_url="https://www.sampledata.com",
                                batch_transform_url="https://www.amazon.com"
                            ),
                            parameters=[OutputParameter(
                                name="p1",
                                description="desc",
                                always_returned=False
                            )]
                        ),
                        recommended_instance_types=SageMakerAlgorithmRecommendedInstanceTypes(
                            batch_transform="ml.m5.large",
                            realtime_inference="ml.m5.large",
                            training="ml.m5.large"
                        )
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
            "Details": {
                "SageMakerAlgorithmDeliveryOptionDetails": {
                    "UsageInstructions": "Usage instructions",
                    "SampleNotebookUrl": "https://www.amazon.com",
                    "RepositoryUrl": "https://www.amazon.com",
                    "InputProperties": {
                        "Description": "Input should have all columns in the train/test file except for 'is_fraud' column.",
                        "Limitations": "Can predict on 1 input in the CSV only at a time",
                        "SampleInput": {
                            "RealtimeInferenceText": "text",
                            "BatchTransformUrl": "https://www.sampleData.com"
                        },
                        "Parameters": [{
                            "Name": "name1",
                            "Description": "desc",
                            "Constraints": "constraints",
                            "Required": False
                        }]
                    },
                    "OutputProperties": {
                        "Description": "The output is a JSON object that has the generated text along with likelihoods of tokens, if requested. See example json.",
                        "SampleOutput": {
                            "RealtimeInferenceUrl": "https://www.sampledata.com",
                            "BatchTransformUrl": "https://www.amazon.com"
                        },
                        "Parameters": [{
                            "Name": "p1",
                            "Description": "desc",
                            "AlwaysReturned": False
                        }]
                    },
                    "RecommendedInstanceTypes": {
                        "BatchTransform": "ml.m5.large",
                        "RealtimeInference": "ml.m5.large",
                        "Training": "ml.m5.large"
                    },
                    "SageMakerAlgorithmArn": "arn:aws:sagemaker:us-east-2:123456789123:algorithm/ml-test-algorithm",
                    "AccessRoleArn": "arn:aws:iam::123456789012:role/myRole"
                }
            }
        }]
    }

    assert actual_json == json.dumps(expected_json), "Generated AddDeliveryOptionsChangeDetail with model package delivery does not match expected json"

def test_model_package_update_delivery_options_change_detail_serialization():
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.update_delivery_options_change_detail import UpdateDeliveryOptionsChangeDetail
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.update_delivery_options_version import UpdateDeliveryOptionsVersion
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.update_delivery_options_details import UpdateDeliveryOptionsDetails
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.update_delivery_option import UpdateDeliveryOption
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.update_delivery_options_sage_maker_model_package_delivery_option_details import UpdateDeliveryOptionsSageMakerModelPackageDeliveryOptionDetails
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.sage_maker_model_package_recommended_instance_types import SageMakerModelPackageRecommendedInstanceTypes

    update_information_change_details = UpdateDeliveryOptionsChangeDetail(
        version=UpdateDeliveryOptionsVersion(
            release_notes="Release Notes"
        ),
        delivery_options=[
            UpdateDeliveryOption(
                id="00000000-0000-0000-0000-000000000000",
                details=UpdateDeliveryOptionsDetails(
                    sage_maker_model_package_delivery_option_details=UpdateDeliveryOptionsSageMakerModelPackageDeliveryOptionDetails(
                        usage_instructions="instructions",
                        recommended_instance_types=SageMakerModelPackageRecommendedInstanceTypes(
                            batch_transform="m4.2xlarge"
                        )
                    )
                )
            )
        ]
    )

    actual_json = update_information_change_details.to_json()
    expected_json = {
        "Version": {
            "ReleaseNotes": "Release Notes"
        },
        "DeliveryOptions": [{
            "Id": "00000000-0000-0000-0000-000000000000",
            "Details": {
                "SageMakerModelPackageDeliveryOptionDetails": {
                    "UsageInstructions": "instructions",
                    "RecommendedInstanceTypes": {
                        "BatchTransform": "m4.2xlarge"
                    },
                }
            }
        }]
    }

    assert actual_json == json.dumps(expected_json), "Generated UpdateDeliveryOptionsChangeDetails with algorithm delivery does not match expected json"

def test_algorithm_update_delivery_options_change_detail_serialization():
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.update_delivery_options_change_detail import UpdateDeliveryOptionsChangeDetail
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.update_delivery_options_version import UpdateDeliveryOptionsVersion
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.update_delivery_options_details import UpdateDeliveryOptionsDetails
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.update_delivery_option import UpdateDeliveryOption
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.update_delivery_options_sage_maker_algorithm_delivery_option_details import UpdateDeliveryOptionsSageMakerAlgorithmDeliveryOptionDetails

    update_information_change_details = UpdateDeliveryOptionsChangeDetail(
        version=UpdateDeliveryOptionsVersion(
            release_notes="Release Notes"
        ),
        delivery_options=[
            UpdateDeliveryOption(
                id="00000000-0000-0000-0000-000000000000",
                details=UpdateDeliveryOptionsDetails(
                    sage_maker_algorithm_delivery_option_details=UpdateDeliveryOptionsSageMakerAlgorithmDeliveryOptionDetails(
                        sample_notebook_url="https://aws.amazon.com"
                    )
                )
            )
        ]
    )

    actual_json = update_information_change_details.to_json()
    expected_json = {
        "Version": {
            "ReleaseNotes": "Release Notes"
        },
        "DeliveryOptions": [{
            "Id": "00000000-0000-0000-0000-000000000000",
            "Details": {
                "SageMakerAlgorithmDeliveryOptionDetails": {
                    "SampleNotebookUrl": "https://aws.amazon.com"
                }
            }
        }]
    }

    assert actual_json == json.dumps(expected_json), "Generated UpdateDeliveryOptionsChangeDetails with algorithm delivery does not match expected json"

def test_create_product_change_detail_serialization():
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.create_product_change_detail import CreateProductChangeDetail

    create_product_change_detail = CreateProductChangeDetail(product_title="MyProductTitle")
    actual_json = create_product_change_detail.to_json()
    expected_json = {
        "ProductTitle": "MyProductTitle"
    }

    assert actual_json == json.dumps(expected_json), "Generated CreateProductChangeDetail does not match expected json"

def test_restrict_delivery_options_change_detail_serialization():
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.restrict_delivery_options_change_detail import RestrictDeliveryOptionsChangeDetail

    restrict_delivery_options_change_detail = RestrictDeliveryOptionsChangeDetail(
        delivery_option_ids=["00000000-0000-0000-0000-000000000000"]
    )
    actual_json = restrict_delivery_options_change_detail.to_json()
    expected_json = {
        "DeliveryOptionIds": ["00000000-0000-0000-0000-000000000000"]
    }

    assert actual_json == json.dumps(expected_json), "Generated RestrictDeliveryOptionsChangeDetail does not match expected json"

def test_update_information_change_detail_serialization():
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.update_information_change_detail import UpdateInformationChangeDetail
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.additional_resource import AdditionalResource

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

def test_update_targeting_change_detail_serialization():
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.update_targeting_change_detail import UpdateTargetingChangeDetail
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.positive_targeting import PositiveTargeting

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
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.update_visibility_change_detail import UpdateVisibilityChangeDetail
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.target_visibility import TargetVisibility

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
    from aws_marketplace_catalog_shapes_machinelearningproduct_1_0_changetypes.models.release_product_change_detail import ReleaseProductChangeDetail

    release_product_change_detail = ReleaseProductChangeDetail()
    actual_json = release_product_change_detail.to_json()
    expected_json = {}

    assert actual_json == json.dumps(expected_json), "Generated ReleaseProductChangeDetail does not match expected json"

