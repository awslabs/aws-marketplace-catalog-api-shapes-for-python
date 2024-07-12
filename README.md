# AWS Marketplace Catalog API Shape Library for Python
AWS Marketplace Catalog API Shape Library for Python contains a collection of change type and entity type shapes used in
[AWS Marketplace Catalog API](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html),
modeled using Python classes. You can use this library to serialize to, and deserialize from the JSON payloads needed to
programmatically call Catalog API.

## How to install
You can include this library as a dependency by utilizing the 
[direct url dependencies](https://setuptools.pypa.io/en/latest/userguide/dependency_management.html) feature of
Setuptools (under `dependencies` or `install_requires`):
```
aws-marketplace-catalog-api-shape-library-for-python @ git+https://github.com/awslabs/aws-marketplace-catalog-api-shapes-for-python@main
```
or install from source by downloading the source and running:
```
python -m pip install -e .
```

### Running tests
From the root directory, run:
```
python -m pip install '.[test]'
python -m pytest
```

## Overview
You may need to reference [AWS Marketplace Catalog API](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html)
documentation for the terminologies used for this section.  
AWS Marketplace Catalog API utilizes freeform JSONs as part of the StartChangeSet request and DescribeEntity response
structures.  
AWS Marketplace entities are containers of data which serve different business purposes. 
Entities are categorized by types. Each entity type encapsulates data related to a specific business domain
(for example, a product or a seller account).  
When you call DescribeEntity, the operation returns the metadata and the content of the entity as a JSON payload under
the `DetailsDocument` field. This library contains classes that represents the various entity types available in AWS
Marketplace Catalog API.
JSON payloads are similarly used in StartChangeSet to define the changes you want to make to an entity. Each entity
type may contain several types of changes available, and each accepts JSON payload that is specific to each change type.
This library contains classes that represents the various change types available in AWS Marketplace Catalog API. When
constructing a StartChangeSet request, you would put your JSON payload under the `DetailsDocument` field.

## Conventions
You may need to reference [AWS Marketplace Catalog API](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html)
documentation for the terminologies used for this section.  
This library separates entity types in individual Python packages with its entity name and version as part of the package name.
For example, `amiproduct_1_0` and `offer_1_0`.
Within each package contains all shapes associated with the entity type.  
Classes with suffix `entity_detail` indicate it is the root shape of an entity type.
For example, `ami_product_entity_detail` is the root shape of `AmiProduct` entity type.
This class represents the JSON payload you would receive when you call DescribeEntity on an Ami product.  
Classes with suffix `change_detail` indicate it is the root shape of a change type.
For example, `add_delivery_options_change_detail` is the root shape of `AddDeliveryOptions` change type.
This class represents the JSON payload you would need to construct in order to call StartChangeSet with an Ami product
AddDeliveryOptions change type.

This library provides some basic validation when constructing a shape, though further validations will be performed 
on the service side when calling AWS Marketplace Catalog API.

## Usage with AWS SDK for Python (Boto3)
This library is intended to be used with [AWS SDK for Python](https://aws.amazon.com/sdk-for-python/). See the link for
documentations on how to download and use the SDK.  

Below is some sample code to make an StartChangeSet call with AddDeliveryOptions change on an Ami product 
and to deserialize the results of a DescribeEntity call into an object:
```python
import boto3
import json

client = boto3.client("marketplace-catalog", region_name='us-east-1')

def ami_add_delivery_options(): 
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.add_delivery_options_change_detail import AddDeliveryOptionsChangeDetail
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.add_version import AddVersion
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.add_delivery_option import AddDeliveryOption
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.add_details import AddDetails
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.add_ami_delivery_option_details import AddAmiDeliveryOptionDetails
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.ami_source import AmiSource
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.access_endpoint_url import AccessEndpointUrl
    from aws_marketplace_catalog_shapes_amiproduct_1_0_changetypes.models.security_group import SecurityGroup
    
    detail = AddDeliveryOptionsChangeDetail(
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
    change_set = [
        {
            'ChangeType': 'AddDeliveryOptions',
            'Entity': {
                'Identifier': 'example1-abcd-1234-5ef6-7890abcdef12',
                'Type': 'AmiProduct@1.0'
            },
            'DetailsDocument': detail.to_dict()
        }
    ]
    response = client.start_change_set(
        Catalog='AWSMarketplace',
        ChangeSet=change_set
    )
    print(response)

def saas_describe_entity_call():
    from aws_marketplace_catalog_shapes_saasproduct_1_0_entitytype.models.saa_s_product_entity_detail import SaaSProductEntityDetail
    
    response = client.describe_entity(
        Catalog='AWSMarketplace',
        EntityId='example1-abcd-1234-5ef6-7890abcdef12'
    )
    
    entity_detail = SaaSProductEntityDetail.from_json(json.dumps(response['DetailsDocument']))
    
    print(entity_detail)
```

You may additionally reference the tests in the tests directory on how to construct all change types available with this
library.

## Working with Offers
The intended process for making updates through Offer change types is to call DescribeEntity and copy relevant field instances
directly from the deserialized results. Below is some sample code demonstrating how to deserialize a DescribeEntity
response and use it to construct the details for the UpdatePricingTerm changetype in order to update the currency code 
for the ConfigurableUpfrontPricingTerm.

```python
import boto3
import json

client = boto3.client("marketplace-catalog", region_name='us-east-1')

def update_offer_terms_example():
    from aws_marketplace_catalog_shapes_offer_1_0.models.offer_entity_detail import OfferEntityDetail
    from aws_marketplace_catalog_shapes_offer_1_0.models.update_pricing_terms_change_detail import UpdatePricingTermsChangeDetail
    from aws_marketplace_catalog_shapes_offer_1_0.models.pricing_model import PricingModel 

    response = client.describe_entity(
        Catalog='AWSMarketplace',
        EntityId='example1-abcd-1234-5ef6-7890abcdef12'
    )
    
    entity_detail = OfferEntityDetail.from_json(json.dumps(response['DetailsDocument']))

    terms = entity_detail.terms
    for term in terms:
        if term.type is not None and term.type == "ConfigurableUpfrontPricingTerm":
            term.currency_code = "AUD"

    update_pricing_terms_change_detail = UpdatePricingTermsChangeDetail(
        pricing_model=PricingModel.CONTRACT,
        terms=terms
    )

    change_set = [
        {
            'ChangeType': 'UpdatePricingTerms',
            'Entity': {
                'Identifier': 'example1-abcd-1234-5ef6-7890abcdef12',
                'Type': 'OfferProduct@1.0'
            },
            'DetailsDocument': update_pricing_terms_change_detail.to_dict()
        }
    ]
    response = client.start_change_set(
        Catalog='AWSMarketplace',
        ChangeSet=change_set
    )
    print(response)
```

You may notice that Offer has an additional appendix with specific Term types (e.g. LegalTerm, FreeTrialPricingTerm, etc.).
These shapes are included to help you construct the corresponding change type details (e.g. UpdateLegalTerms, UpdatePricingTerms,
etc.) with the proper fields/values if you choose to do so freehand (instead of copying from DescribeEntity results).
There are converters included in the utils package which will allow you to convert between a specific term (such as
ConfigurableUpfrontPricingTerm) to the general Term that is used in the change type. Please see the unit test suite for 
examples on how to use the converters.

There is also a converter for the UpdateInformationChangeDetail change type to allow you to leverage the AcquisitionChannel
and PricingModel enums and ensure that the values are correct.


## License
AWS Marketplace Catalog API Shape Library for Python is licensed under the Apache 2.0 License. See LICENSE and NOTICE
for more information.
