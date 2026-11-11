def test_importable():
    from aws_marketplace_catalog_shapes_subsidiaryauthorization_1_0_entitytype.models.subsidiary_authorization_entity_detail import SubsidiaryAuthorizationEntityDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_subsidiaryauthorization_1_0_changetypes.models.create_subsidiary_authorization_change_detail import CreateSubsidiaryAuthorizationChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_subsidiaryauthorization_1_0_changetypes.models.update_information_change_detail import UpdateInformationChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_subsidiaryauthorization_1_0_changetypes.models.update_availability_change_detail import UpdateAvailabilityChangeDetail  # noqa: F401

    assert True


def test_subsidiary_authorization_entity_detail_deserialization():
    from aws_marketplace_catalog_shapes_subsidiaryauthorization_1_0_entitytype.models.subsidiary_authorization_entity_detail import SubsidiaryAuthorizationEntityDetail

    expected_json = {
        "Name": "Acme LATAM - Mexico",
        "Description": "Authorization for Acme Mexico subsidiary to sell Cloud Security Suite in BR and AR",
        "Status": "Active",
        "CreatedDate": "2026-05-12T22:32:19Z",
        "Issuer": {
            "AccountId": "123456789123",
            "LegalName": "Acme Global Inc."
        },
        "Resource": {
            "Arn": "arn:aws:aws-marketplace:us-east-1:123456789123:AWSMarketplace/SaaSProduct/prod-abc123",
            "Name": "Cloud Security Suite",
            "Description": "Enterprise endpoint security suite",
            "ResourceTypeDetails": {
                "ProductDetails": {
                    "Dimensions": [
                        {
                            "Name": "Users - Contract Pricing",
                            "Description": "Licensed users - CUPT term",
                            "Key": "users_id",
                            "Unit": "Units",
                            "Types": ["Entitled"]
                        },
                        {
                            "Name": "API Requests - Contract Only",
                            "Description": "API requests - CUPT term only",
                            "Key": "api_requests_id",
                            "Unit": "Requests",
                            "Types": ["Entitled"]
                        }
                    ]
                }
            }
        },
        "Terms": [
            {
                "Type": "BuyerTargetingTerm",
                "PositiveTargeting": {
                    "CountryCodes": ["BR", "AR"],
                    "OfferTargeting": ["PrivateOffer"]
                }
            },
            {
                "Type": "PartnerTargetingTerm",
                "PositiveTargeting": {
                    "PartnerAccounts": []
                }
            }
        ],
        "Rules": [
            {
                "Type": "SubsidiaryTargetingRule",
                "AccountId": "123456789123",
                "LegalName": "Acme Mexico Ltda"
            }
        ]
    }

    detail = SubsidiaryAuthorizationEntityDetail.from_dict(expected_json)

    assert detail.name == "Acme LATAM - Mexico"
    assert detail.description == "Authorization for Acme Mexico subsidiary to sell Cloud Security Suite in BR and AR"
    assert detail.status == "Active"
    assert detail.created_date == "2026-05-12T22:32:19Z"
    assert detail.issuer.account_id == "123456789123"
    assert detail.issuer.legal_name == "Acme Global Inc."
    assert detail.resource.arn == "arn:aws:aws-marketplace:us-east-1:123456789123:AWSMarketplace/SaaSProduct/prod-abc123"
    assert detail.resource.name == "Cloud Security Suite"
    assert detail.resource.resource_type_details.product_details.dimensions[0].key == "users_id"
    assert detail.resource.resource_type_details.product_details.dimensions[1].key == "api_requests_id"
    assert detail.terms[0].type == "BuyerTargetingTerm"
    assert sorted(detail.terms[0].positive_targeting.country_codes) == ["AR", "BR"]
    assert list(detail.terms[0].positive_targeting.offer_targeting) == ["PrivateOffer"]
    assert detail.terms[1].type == "PartnerTargetingTerm"
    assert detail.rules[0].type == "SubsidiaryTargetingRule"
    assert detail.rules[0].account_id == "123456789123"
    assert detail.rules[0].legal_name == "Acme Mexico Ltda"

    # Round-trip: deserialized object serialized back should match original
    assert detail.to_dict() == expected_json


def test_create_subsidiary_authorization_change_detail_serialization():
    from aws_marketplace_catalog_shapes_subsidiaryauthorization_1_0_changetypes.models.create_subsidiary_authorization_change_detail import CreateSubsidiaryAuthorizationChangeDetail
    from aws_marketplace_catalog_shapes_subsidiaryauthorization_1_0_changetypes.models.resource_input import ResourceInput
    from aws_marketplace_catalog_shapes_subsidiaryauthorization_1_0_changetypes.models.resource_type_details_input import ResourceTypeDetailsInput
    from aws_marketplace_catalog_shapes_subsidiaryauthorization_1_0_changetypes.models.product_details_input import ProductDetailsInput
    from aws_marketplace_catalog_shapes_subsidiaryauthorization_1_0_changetypes.models.dimension_input import DimensionInput
    from aws_marketplace_catalog_shapes_subsidiaryauthorization_1_0_changetypes.models.term_input import TermInput
    from aws_marketplace_catalog_shapes_subsidiaryauthorization_1_0_changetypes.models.positive_targeting_input import PositiveTargetingInput

    detail = CreateSubsidiaryAuthorizationChangeDetail(
        name="Acme LATAM - Mexico",
        description="Authorization for Acme Mexico subsidiary",
        resource=ResourceInput(
            arn="arn:aws:aws-marketplace:us-east-1:123456789123:AWSMarketplace/SaaSProduct/prod-abc123",
            resource_type_details=ResourceTypeDetailsInput(
                product_details=ProductDetailsInput(
                    dimensions=[
                        DimensionInput(key="users_id"),
                        DimensionInput(key="api_requests_id")
                    ]
                )
            )
        ),
        subsidiary_account_id="123456789123",
        terms=[
            TermInput(
                type="BuyerTargetingTerm",
                positive_targeting=PositiveTargetingInput(
                    country_codes=["BR", "AR"],
                    offer_targeting=["PrivateOffer"]
                )
            )
        ]
    )

    result = detail.to_dict()

    assert result["Name"] == "Acme LATAM - Mexico"
    assert result["Description"] == "Authorization for Acme Mexico subsidiary"
    assert result["SubsidiaryAccountId"] == "123456789123"
    assert result["Resource"]["Arn"] == "arn:aws:aws-marketplace:us-east-1:123456789123:AWSMarketplace/SaaSProduct/prod-abc123"
    assert result["Resource"]["ResourceTypeDetails"]["ProductDetails"]["Dimensions"][0]["Key"] == "users_id"
    assert result["Terms"][0]["Type"] == "BuyerTargetingTerm"
    assert sorted(result["Terms"][0]["PositiveTargeting"]["CountryCodes"]) == ["AR", "BR"]


def test_update_information_change_detail_serialization():
    from aws_marketplace_catalog_shapes_subsidiaryauthorization_1_0_changetypes.models.update_information_change_detail import UpdateInformationChangeDetail
    from aws_marketplace_catalog_shapes_subsidiaryauthorization_1_0_changetypes.models.resource_input import ResourceInput
    from aws_marketplace_catalog_shapes_subsidiaryauthorization_1_0_changetypes.models.resource_type_details_input import ResourceTypeDetailsInput
    from aws_marketplace_catalog_shapes_subsidiaryauthorization_1_0_changetypes.models.product_details_input import ProductDetailsInput
    from aws_marketplace_catalog_shapes_subsidiaryauthorization_1_0_changetypes.models.dimension_input import DimensionInput
    from aws_marketplace_catalog_shapes_subsidiaryauthorization_1_0_changetypes.models.term_input import TermInput
    from aws_marketplace_catalog_shapes_subsidiaryauthorization_1_0_changetypes.models.positive_targeting_input import PositiveTargetingInput

    detail = UpdateInformationChangeDetail(
        name="Acme LATAM - Mexico (updated)",
        description="Revised description after PM review.",
        resource=ResourceInput(
            arn="arn:aws:aws-marketplace:us-east-1:123456789123:AWSMarketplace/SaaSProduct/prod-abc123",
            resource_type_details=ResourceTypeDetailsInput(
                product_details=ProductDetailsInput(
                    dimensions=[
                        DimensionInput(key="users_id"),
                        DimensionInput(key="api_requests_id"),
                        DimensionInput(key="storage_gb_id")
                    ]
                )
            )
        ),
        terms=[
            TermInput(
                type="BuyerTargetingTerm",
                positive_targeting=PositiveTargetingInput(
                    country_codes=["BR", "AR", "MX"],
                    offer_targeting=["PrivateOffer"]
                )
            )
        ]
    )

    result = detail.to_dict()

    assert result["Name"] == "Acme LATAM - Mexico (updated)"
    assert result["Description"] == "Revised description after PM review."
    assert len(result["Resource"]["ResourceTypeDetails"]["ProductDetails"]["Dimensions"]) == 3
    assert sorted(result["Terms"][0]["PositiveTargeting"]["CountryCodes"]) == ["AR", "BR", "MX"]


def test_update_availability_change_detail_serialization():
    from aws_marketplace_catalog_shapes_subsidiaryauthorization_1_0_changetypes.models.update_availability_change_detail import UpdateAvailabilityChangeDetail

    detail = UpdateAvailabilityChangeDetail(status="Active")
    result = detail.to_dict()

    assert result == {"Status": "Active"}

    detail_restrict = UpdateAvailabilityChangeDetail(status="Restricted")
    result_restrict = detail_restrict.to_dict()

    assert result_restrict == {"Status": "Restricted"}
