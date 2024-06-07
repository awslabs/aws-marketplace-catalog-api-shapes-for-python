import pytest
import json

def test_importable():
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_entitytype.models.resale_authorization_entity_detail import ResaleAuthorizationEntityDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.create_resale_authorization_change_detail import CreateResaleAuthorizationChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.update_buyer_targeting_terms_change_detail import UpdateBuyerTargetingTermsChangeDetail # noqa: F401
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.update_availability_change_detail import UpdateAvailabilityChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.update_buyer_validity_terms_change_detail import UpdateBuyerValidityTermsChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.update_information_change_detail import UpdateInformationChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.update_legal_terms_change_detail import UpdateLegalTermsChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.update_pricing_terms_change_detail import UpdatePricingTermsChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.update_payment_schedule_terms_change_detail import UpdatePaymentScheduleTermsChangeDetail  # noqa: F401

    assert True

def test_resale_authorization_1_0_entity_detail_deserialization():
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_entitytype.models.resale_authorization_entity_detail import ResaleAuthorizationEntityDetail
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_entitytype.models.pre_existing_buyer_agreement import PreExistingBuyerAgreement
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_entitytype.models.dimension import Dimension
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_entitytype.models.offer_details import OfferDetails
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_entitytype.models.term import Term
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_entitytype.models.rate_cards import RateCards
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_entitytype.models.rate_card import RateCard
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_entitytype.models.selector import Selector
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_entitytype.models.constraints import Constraints
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_entitytype.models.grant import Grant
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_entitytype.models.schedule import Schedule
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_entitytype.models.document import Document
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_entitytype.models.positive_targeting import PositiveTargeting
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_entitytype.models.buyer_account import BuyerAccount
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_entitytype.models.rule import Rule

    expected_json = {
        "Name": "CanaryTestOpportunityBackFillCustomDimension",
        "Description": "Canary test description",
        "ProductId": "b199549a-6c5d-49a0-8217-607972c6f4f9",
        "ProductName": "Channel CAPI Integ Test Product (SaaS CCP)",
        "Status": "Active",
        "PreExistingBuyerAgreement": {
            "AcquisitionChannel": "Unknown",
            "PricingModel": "Unknown"
        },
        "Dimensions": [{
            "Name": "Protected Resources",
            "Description": "Additional 100 protected resources",
            "Key": "hundredresources",
            "Unit": "Units",
            "Types": ["Entitled"]
        }, {
            "Name": "Scanned Data",
            "Description": "Additional 10TB of Data Scanned",
            "Key": "tenTBData",
            "Unit": "Units",
            "Types": ["Entitled"]
        }, {
            "Name": "Number of protected resources beyond contract subscription - Monthly",
            "Description": "Number of protected resources beyond contract subscription - Monthly",
            "Key": "resource_number",
            "Unit": "Units",
            "Types": ["Metered", "ExternallyMetered"]
        }, {
            "Name": "Gigabytes of data scanned for malware beyond contract subscription",
            "Description": "Gigabytes of data scanned for malware beyond contract subscription",
            "Key": "scanned_data",
            "Unit": "Units",
            "Types": ["Metered", "ExternallyMetered"]
        }, {
            "Name": "Channel Custom Dimension",
            "Description": "Channel Custom Dimension",
            "Key": "channel_custom",
            "Unit": "Units",
            "Types": ["Entitled"]
        }],
        "OfferDetails": {
            "OfferExtendedStatus": "Not Started",
            "OfferCreatedCount": 0
        },
        "Terms": [{
            "Type": "ResaleUsageBasedPricingTerm",
            "Id": "term_id_placeholder",
            "CurrencyCode": "USD",
            "RateCards": [{
                "RateCard": [{
                    "DimensionKey": "resource_number",
                    "Price": "0.05"
                }, {
                    "DimensionKey": "scanned_data",
                    "Price": "0.05"
                }]
            }]
        }, {
            "Type": "ResaleConfigurableUpfrontPricingTerm",
            "Id": "term_id_placeholder",
            "CurrencyCode": "USD",
            "RateCards": [{
                "Selector": {
                    "Type": "Duration",
                    "Value": "P24M"
                },
                "RateCard": [{
                    "DimensionKey": "hundredresources",
                    "Price": "0.04"
                }, {
                    "DimensionKey": "tenTBData",
                    "Price": "0.03"
                }, {
                    "DimensionKey": "channel_custom",
                    "Price": "0.02"
                }],
                "Constraints": {
                    "MultipleDimensionSelection": "Allowed",
                    "QuantityConfiguration": "Allowed"
                }
            }]
        }, {
            "Type": "ResaleFixedUpfrontPricingTerm",
            "Id": "term-sdh27fb2",
            "CurrencyCode": "USD",
            "Duration": "P180D",
            "Price": "0.0",
            "Grants": [{
                "DimensionKey": "sdf73rbns93nl120d10xm1",
                "MaxQuantity": 1
            }]
        }, {
            "Type": "ResalePaymentScheduleTerm",
            "Id": "term-sdh27fb2",
            "CurrencyCode": "USD",
            "Schedule": [{
                "ChargeDate": "2018-07-01T00:00:00.000Z",
                "ChargeAmount": "200.00"
            }, {
                "ChargeDate": "2019-05-01T00:00:00.000Z",
                "ChargeAmount": "200.00"
            }]
        }, {
            "Type": "BuyerLegalTerm",
            "Id": "term_id_placeholder",
            "Documents": [{
                "Type": "StandardEula",
                "Url": "https://amazon.com"
            }]
        }, {
            "Type": "ResaleLegalTerm",
            "Id": "term_id_placeholder",
            "Documents": [{
                "Type": "StandardResellerContract",
                "Url": "https://amazon.com"
            }]
        }, {
            "Type": "BuyerValidityTerm",
            "Id": "term_id_placeholder",
            "MaximumAgreementStartDate": "2023-09-25T23:59:59.000Z"
        }, {
            "Type": "BuyerTargetingTerm",
            "Id": "term_id_placeholder",
            "PositiveTargeting": {
                "BuyerAccounts": [{
                    "AwsAccountId": "123456789123",
                    "LegalName": "Buyer Account"
                }]
            }
        }],
        "Rules": [{
            "Type": "AvailabilityRule",
            "Id": "availability_rule_id_placeholder",
            "Usage": "Limited",
            "AvailabilityEndDate": "2022-05-31T00:00:00Z",
            "OffersMaxQuantity": 1
        }, {
            "Type": "PartnerTargetingRule",
            "Id": "partner_targeting_rule_id_placeholder",
            "ResellerAccountId": "123456789123",
            "ResellerLegalName": "ChannelCAPICP.Inc"
        }],
        "CreatedDate": "2023-09-12T14:15:02.000Z",
        "ManufacturerLegalName": "ChannelCAPI.Inc",
        "ManufacturerAccountId": "123456789123"
    }

    actual_detail = ResaleAuthorizationEntityDetail.from_json(json.dumps(expected_json))
    expected_detail = ResaleAuthorizationEntityDetail(
        name="CanaryTestOpportunityBackFillCustomDimension",
        description="Canary test description",
        product_id="b199549a-6c5d-49a0-8217-607972c6f4f9",
        product_name="Channel CAPI Integ Test Product (SaaS CCP)",
        status="Active",
        pre_existing_buyer_agreement=PreExistingBuyerAgreement(
            acquisition_channel="Unknown",
            pricing_model="Unknown"
        ),
        dimensions=[
            Dimension(
                name="Protected Resources",
                description="Additional 100 protected resources",
                key="hundredresources",
                unit="Units",
                types=["Entitled"]
            ),
            Dimension(
                name="Scanned Data",
                description="Additional 10TB of Data Scanned",
                key="tenTBData",
                unit="Units",
                types=["Entitled"]
            ),
            Dimension(
                name="Number of protected resources beyond contract subscription - Monthly",
                description="Number of protected resources beyond contract subscription - Monthly",
                key="resource_number",
                unit="Units",
                types=["Metered", "ExternallyMetered"]
            ),
            Dimension(
                name="Gigabytes of data scanned for malware beyond contract subscription",
                description="Gigabytes of data scanned for malware beyond contract subscription",
                key="scanned_data",
                unit="Units",
                types=["Metered", "ExternallyMetered"]
            ),
            Dimension(
                name="Channel Custom Dimension",
                description="Channel Custom Dimension",
                key="channel_custom",
                unit="Units",
                types=["Entitled"]
            )
        ],
        offer_details=OfferDetails(
            offer_extended_status="Not Started",
            offer_created_count=0
        ),
        terms=[
            Term(
                type="ResaleUsageBasedPricingTerm",
                id="term_id_placeholder",
                currency_code="USD",
                rate_cards=[
                    RateCards(
                        rate_card=[
                            RateCard(
                                dimension_key="resource_number",
                                price="0.05"
                            ),
                            RateCard(
                                dimension_key="scanned_data",
                                price="0.05"
                            )
                        ]
                    )
                ]
            ),
            Term(
                type="ResaleConfigurableUpfrontPricingTerm",
                id="term_id_placeholder",
                currency_code="USD",
                rate_cards=[
                    RateCards(
                        selector =Selector(
                            type="Duration",
                            value="P24M"
                        ),
                        rate_card=[
                            RateCard(
                                dimension_key="hundredresources",
                                price="0.04"
                            ),
                            RateCard(
                                dimension_key="tenTBData",
                                price="0.03"
                            ),
                            RateCard(
                                dimension_key="channel_custom",
                                price="0.02"
                            ),
                        ],
                        constraints=Constraints(
                            multiple_dimension_selection="Allowed",
                            quantity_configuration="Allowed"
                        )
                    )
                ]
            ),
            Term(
                type="ResaleFixedUpfrontPricingTerm",
                id="term-sdh27fb2",
                currency_code="USD",
                duration="P180D",
                price="0.0",
                grants=[
                    Grant(
                        dimension_key="sdf73rbns93nl120d10xm1",
                        max_quantity=1
                    )
                ]
            ),
            Term(
                type="ResalePaymentScheduleTerm",
                id="term-sdh27fb2",
                currency_code="USD",
                schedule=[
                    Schedule(
                        charge_date="2018-07-01T00:00:00.000Z",
                        charge_amount="200.00"
                    ),
                    Schedule(
                        charge_date="2019-05-01T00:00:00.000Z",
                        charge_amount="200.00"
                    )
                ]
            ),
            Term(
                type="BuyerLegalTerm",
                id="term_id_placeholder",
                documents=[
                    Document(
                        type="StandardEula",
                        url="https://amazon.com"
                    )
                ]
            ),
            Term(
                type="ResaleLegalTerm",
                id="term_id_placeholder",
                documents=[
                    Document(
                        type="StandardResellerContract",
                        url="https://amazon.com"
                    )
                ]
            ),
            Term(
                type="BuyerValidityTerm",
                id="term_id_placeholder",
                maximum_agreement_start_date="2023-09-25T23:59:59.000Z",
            ),
            Term(
                type="BuyerTargetingTerm",
                id="term_id_placeholder",
                positive_targeting=PositiveTargeting(
                    buyer_accounts=[
                        BuyerAccount(
                            aws_account_id="123456789123",
                            legal_name="Buyer Account"
                        )
                    ]
                )
            )
        ],
        rules=[
            Rule(
                type="AvailabilityRule",
                id="availability_rule_id_placeholder",
                usage="Limited",
                availability_end_date="2022-05-31T00:00:00Z",
                offers_max_quantity=1
            ),
            Rule(
                type="PartnerTargetingRule",
                id="partner_targeting_rule_id_placeholder",
                reseller_account_id="123456789123",
                reseller_legal_name="ChannelCAPICP.Inc"
            )
        ],
        created_date="2023-09-12T14:15:02.000Z",
        manufacturer_legal_name="ChannelCAPI.Inc",
        manufacturer_account_id="123456789123"
    )

    assert actual_detail == expected_detail, "Deserialized object does not match expected object"

def test_create_resale_authorization_change_detail_serialization():
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.create_resale_authorization_change_detail import CreateResaleAuthorizationChangeDetail

    create_resale_authorization_change_detail = CreateResaleAuthorizationChangeDetail(
        product_id="ProductId",
        name="Name",
        description="Description",
        reseller_account_id="123456789012"
    )
    actual_json = create_resale_authorization_change_detail.to_json()
    expected_json = {
        "Name": "Name",
        "Description": "Description",
        "ProductId": "ProductId",
        "ResellerAccountId": "123456789012"
    }

    assert actual_json == json.dumps(expected_json), "Generated CreateResaleAuthorizationChangeDetail does not match expected json"

def test_update_buyer_targeting_terms_change_detail_serialization():
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.update_buyer_targeting_terms_change_detail import UpdateBuyerTargetingTermsChangeDetail
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.buyer_targeting_term import BuyerTargetingTerm
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.buyer_targeting_term_type import BuyerTargetingTermType
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.positive_targeting import PositiveTargeting

    update_buyer_targeting_terms_change_detail = UpdateBuyerTargetingTermsChangeDetail(
        terms=[BuyerTargetingTerm(
            type=BuyerTargetingTermType.BUYERTARGETINGTERM,
            positive_targeting=PositiveTargeting(
                buyer_accounts=["218196967966", "218196967988"]
            )
        )]
    )
    actual_json = update_buyer_targeting_terms_change_detail.to_json()
    expected_json = {
        "Terms": [{
            "Type": "BuyerTargetingTerm",
            "PositiveTargeting": {
                "BuyerAccounts": ["218196967966", "218196967988"]
            }
        }]
    }

    assert actual_json == json.dumps(expected_json), "Generated UpdateBuyerTargetingTermsChangeDetail does not match expected json"

def test_update_availability_change_detail_serialization():
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.update_availability_change_detail import UpdateAvailabilityChangeDetail

    update_availability_change_detail = UpdateAvailabilityChangeDetail(
        availability_end_date="2096-02-29",
        offers_max_quantity=1
    )
    actual_json = update_availability_change_detail.to_json()
    expected_json = {
        "AvailabilityEndDate": "2096-02-29",
        "OffersMaxQuantity": 1
    }

    assert actual_json == json.dumps(expected_json), "Generated UpdateAvailabilityChangeDetail does not match expected json"

def test_update_buyer_validity_terms_change_detail_serialization():
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.update_buyer_validity_terms_change_detail import UpdateBuyerValidityTermsChangeDetail
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.buyer_validity_term import BuyerValidityTerm
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.buyer_validity_term_type import BuyerValidityTermType
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.positive_targeting import PositiveTargeting

    update_buyer_validity_terms_change_detail = UpdateBuyerValidityTermsChangeDetail(
        terms=[BuyerValidityTerm(
            type=BuyerValidityTermType.BUYERVALIDITYTERM,
            maximum_agreement_start_date="2026-05-01"
        )]
    )
    actual_json = update_buyer_validity_terms_change_detail.to_json()
    expected_json = {
        "Terms": [{
            "Type": "BuyerValidityTerm",
            "MaximumAgreementStartDate": "2026-05-01"
        }]
    }

    assert actual_json == json.dumps(expected_json), "Generated UpdateBuyerValidityTermsChangeDetail does not match expected json"

def test_update_information_change_detail_serialization():
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.update_information_change_detail import UpdateInformationChangeDetail
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.pre_existing_buyer_agreement import PreExistingBuyerAgreement
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.acquisition_channel import AcquisitionChannel
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.pricing_model import PricingModel

    update_information_change_detail = UpdateInformationChangeDetail(
        name="name",
        description="description",
        pre_existing_buyer_agreement=PreExistingBuyerAgreement(
            acquisition_channel=AcquisitionChannel.AWSMARKETPLACE,
            pricing_model=PricingModel.BYOL
        )
    )
    actual_json = update_information_change_detail.to_json()
    expected_json = {
        "Name": "name",
        "Description": "description",
        "PreExistingBuyerAgreement": {
            "AcquisitionChannel": "AwsMarketplace",
            "PricingModel": "Byol"
        }
    }

    assert actual_json == json.dumps(expected_json), "Generated UpdateInformationChangeDetail does not match expected json"

def test_update_legal_terms_change_detail_serialization():
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.update_legal_terms_change_detail import UpdateLegalTermsChangeDetail
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.legal_term import LegalTerm
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.legal_term_type import LegalTermType
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.legal_document import LegalDocument
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.legal_document_type import LegalDocumentType

    update_legal_terms_change_detail = UpdateLegalTermsChangeDetail(
        terms=[
            LegalTerm(
                type=LegalTermType.BUYERLEGALTERM,
                documents=[LegalDocument(
                    type=LegalDocumentType.CUSTOMEULA,
                    url="https://s3.amazonaws.com/EULA/custom-eula-1234.txt"
                )]
            ),
            LegalTerm(
                type=LegalTermType.RESALELEGALTERM,
                documents=[LegalDocument(
                    type=LegalDocumentType.CUSTOMRESELLERCONTRACT,
                    url="https://s3.amazonaws.com/reseller/custom-reseller-1234.txt"
                )]
            )
        ]
    )
    actual_json = update_legal_terms_change_detail.to_json()
    expected_json = {
        "Terms": [{
            "Type": "BuyerLegalTerm",
            "Documents": [{
                "Type": "CustomEula",
                "Url": "https://s3.amazonaws.com/EULA/custom-eula-1234.txt"
            }]
        }, {
            "Type": "ResaleLegalTerm",
            "Documents": [{
                "Type": "CustomResellerContract",
                "Url": "https://s3.amazonaws.com/reseller/custom-reseller-1234.txt"
            }]
        }]
    }

    assert actual_json == json.dumps(expected_json), "Generated UpdateLegalTermsChangeDetail does not match expected json"

def test_update_pricing_terms_change_detail_serialization():
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.update_pricing_terms_change_detail import UpdatePricingTermsChangeDetail
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.update_pricing_model import UpdatePricingModel
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.pricing_term import PricingTerm
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.pricing_term_type import PricingTermType
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.pricing_term_currency_code import PricingTermCurrencyCode
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.rate_cards import RateCards
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.rate_card import RateCard
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.selector import Selector
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.selector_type import SelectorType
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.constraints import Constraints
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.constraint import Constraint
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.grant import Grant
    
    update_legal_pricing_change_detail = UpdatePricingTermsChangeDetail(
        pricing_model=UpdatePricingModel.CONTRACT,
        terms=[
            PricingTerm(
                type=PricingTermType.RESALEUSAGEBASEDPRICINGTERM,
                currency_code=PricingTermCurrencyCode.USD,
                rate_cards=[RateCards(
                    rate_card=[
                        RateCard(
                            dimension_key="m3.large",
                            price="0.10"
                        ),
                        RateCard(
                            dimension_key="m4.xlarge",
                            price="0.20"
                        )
                    ]
                )]
            ),
            PricingTerm(
                type=PricingTermType.RESALECONFIGURABLEUPFRONTPRICINGTERM,
                currency_code=PricingTermCurrencyCode.USD,
                rate_cards=[RateCards(
                    selector=Selector(
                        type=SelectorType.DURATION,
                        value="P12M"
                    ),
                    constraints=Constraints(
                        multiple_dimension_selection=Constraint.ALLOWED,
                        quantity_configuration=Constraint.ALLOWED
                    ),
                    rate_card=[
                        RateCard(
                            dimension_key="m3.large",
                            price="300"
                        ),
                        RateCard(
                            dimension_key="m4.xlarge",
                            price="400"
                        )
                    ]
                )]
            ),
            PricingTerm(
                type=PricingTermType.RESALEFIXEDUPFRONTPRICINGTERM,
                currency_code=PricingTermCurrencyCode.USD,
                price="00.00",
                duration="P12M",
                grants=[Grant(
                    dimension_key="Users",
                    max_quantity=10
                )]
            )
        ]
    )
    actual_json = update_legal_pricing_change_detail.to_json()
    expected_json = {
        "PricingModel": "Contract",
        "Terms": [{
            "Type": "ResaleUsageBasedPricingTerm",
            "CurrencyCode": "USD",
            "RateCards": [{
                "RateCard": [{
                    "DimensionKey": "m3.large",
                    "Price": "0.10"
                }, {
                    "DimensionKey": "m4.xlarge",
                    "Price": "0.20"
                }]
            }]
        }, {

            "Type": "ResaleConfigurableUpfrontPricingTerm",
            "CurrencyCode": "USD",
            "RateCards": [{
                "Selector": {
                    "Type": "Duration",
                    "Value": "P12M"
                },
                "Constraints": {
                    "MultipleDimensionSelection": "Allowed",
                    "QuantityConfiguration": "Allowed"
                },
                "RateCard": [{
                    "DimensionKey": "m3.large",
                    "Price": "300"
                }, {
                    "DimensionKey": "m4.xlarge",
                    "Price": "400"
                }]
            }]
        }, {
            "Type": "ResaleFixedUpfrontPricingTerm",
            "CurrencyCode": "USD",
            "Price": "00.00",
            "Grants": [{
                "DimensionKey": "Users",
                "MaxQuantity": 10
            }],
            "Duration": "P12M"
        }]
    }

    assert actual_json == json.dumps(expected_json), "Generated UpdatePricingTermsChangeDetail does not match expected json"

def test_update_payment_schedule_terms_change_detail_serialization():
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.update_payment_schedule_terms_change_detail import UpdatePaymentScheduleTermsChangeDetail
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.update_payment_schedule_term import UpdatePaymentScheduleTerm
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.resale_payment_schedule_term_type import ResalePaymentScheduleTermType
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.update_payment_schedule_term_currency_code import UpdatePaymentScheduleTermCurrencyCode
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.schedule import Schedule

    update_payment_schedule_terms_change_detail = UpdatePaymentScheduleTermsChangeDetail(
        terms=[UpdatePaymentScheduleTerm(
            type=ResalePaymentScheduleTermType.RESALEPAYMENTSCHEDULETERM,
            currency_code=UpdatePaymentScheduleTermCurrencyCode.USD,
            schedule=[
                Schedule(
                    charge_date="2021-12-01",
                    charge_amount="200.00"
                ),
                Schedule(
                    charge_date="2022-03-01",
                    charge_amount="250.00"
                )
            ]
        )]
    )
    actual_json = update_payment_schedule_terms_change_detail.to_json()
    expected_json = {
        "Terms": [{
            "Type": "ResalePaymentScheduleTerm",
            "CurrencyCode": "USD",
            "Schedule": [{
                "ChargeDate": "2021-12-01",
                "ChargeAmount": "200.00"
            }, {
                "ChargeDate": "2022-03-01",
                "ChargeAmount": "250.00"
            }]
        }]
    }

    assert actual_json == json.dumps(expected_json), "Generated UpdatePaymentScheduleTermsChangeDetail does not match expected json"

def test_release_resale_authorization_change_detail_serialization():
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.release_resale_authorization_change_detail import ReleaseResaleAuthorizationChangeDetail

    release_resale_authorization_change_detail = ReleaseResaleAuthorizationChangeDetail()
    actual_json = release_resale_authorization_change_detail.to_json()
    expected_json = {}

    assert actual_json == json.dumps(expected_json), "Generated ReleaseResaleAuthorizationChangeDetail does not match expected json"

def test_restrict_resale_authorization_change_detail_serialization():
    from aws_marketplace_catalog_shapes_resaleauthorization_1_0_changetypes.models.restrict_resale_authorization_change_detail import RestrictResaleAuthorizationChangeDetail

    restrict_resale_authorization_change_detail = RestrictResaleAuthorizationChangeDetail()
    actual_json = restrict_resale_authorization_change_detail.to_json()
    expected_json = {}

    assert actual_json == json.dumps(expected_json), "Generated RestrictResaleAuthorizationChangeDetail does not match expected json"
