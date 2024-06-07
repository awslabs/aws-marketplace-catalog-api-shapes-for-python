import pytest
import json

def test_importable():
    from aws_marketplace_catalog_shapes_offer_1_0.models.offer_entity_detail import OfferEntityDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_offer_1_0.models.create_offer_change_detail import CreateOfferChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_offer_1_0.models.create_replacement_offer_change_detail import CreateReplacementOfferChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_offer_1_0.models.update_information_change_detail import UpdateInformationChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_offer_1_0.models.update_legal_terms_change_detail import UpdateLegalTermsChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_offer_1_0.models.update_availability_change_detail import UpdateAvailabilityChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_offer_1_0.models.update_support_terms_change_detail import UpdateSupportTermsChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_offer_1_0.models.update_pricing_terms_change_detail import UpdatePricingTermsChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_offer_1_0.models.update_targeting_change_detail import UpdateTargetingChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_offer_1_0.models.update_customer_verification_terms_change_detail import UpdateCustomerVerificationTermsChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_offer_1_0.models.update_payment_schedule_terms_change_detail import UpdatePaymentScheduleTermsChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_offer_1_0.models.update_renewal_terms_change_detail import UpdateRenewalTermsChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_offer_1_0.models.update_validity_terms_change_detail import UpdateValidityTermsChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_offer_1_0.models.create_offer_using_resale_authorization_change_detail import CreateOfferUsingResaleAuthorizationChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_offer_1_0.models.create_replacement_offer_using_resale_authorization_change_detail import CreateReplacementOfferUsingResaleAuthorizationChangeDetail  # noqa: F401
    from aws_marketplace_catalog_shapes_offer_1_0.models.update_markup_change_detail import UpdateMarkupChangeDetail  # noqa: F401

    assert True

def test_offer_1_0_entity_detail_deserialization():
    from aws_marketplace_catalog_shapes_offer_1_0.models.offer_entity_detail import OfferEntityDetail
    from aws_marketplace_catalog_shapes_offer_1_0.models.pre_existing_agreement import PreExistingAgreement
    from aws_marketplace_catalog_shapes_offer_1_0.models.rule import Rule
    from aws_marketplace_catalog_shapes_offer_1_0.models.positive_targeting import PositiveTargeting
    from aws_marketplace_catalog_shapes_offer_1_0.models.negative_targeting import NegativeTargeting
    from aws_marketplace_catalog_shapes_offer_1_0.models.term import Term
    from aws_marketplace_catalog_shapes_offer_1_0.models.rate_cards_item import RateCardsItem
    from aws_marketplace_catalog_shapes_offer_1_0.models.selector import Selector
    from aws_marketplace_catalog_shapes_offer_1_0.models.rate_card_item import RateCardItem
    from aws_marketplace_catalog_shapes_offer_1_0.models.constraints import Constraints
    from aws_marketplace_catalog_shapes_offer_1_0.models.grant_item import GrantItem
    from aws_marketplace_catalog_shapes_offer_1_0.models.schedule_item import ScheduleItem
    from aws_marketplace_catalog_shapes_offer_1_0.models.document_item import DocumentItem

    expected_json = {
        "Description": "Worldwide offer for Test Product",
        "Id": "offer-3rEXAMPLErn",
        "State": "Released",
        "MarkupPercentage": "20",
        "Name": "Test Offer",
        "PreExistingAgreement": {
            "AcquisitionChannel": "External",
            "PricingModel": "Contract"
        },
        "ProductId": "prod-ad8EXAMPLE51",
        "Rules": [{
            "Type": "TargetingRule",
            "PositiveTargeting": {
                "CountryCodes": ["US", "CA"],
                "BuyerAccounts": ["444455556666"]
            },
            "NegativeTargeting": {
                "CountryCodes": ["XX"]
            }
        }, {
            "Type": "AvailabilityRule",
            "AvailabilityEndDate": "2024-08-30T01:56:03.000Z"
        }],
        "Terms": [{
            "Type": "ConfigurableUpfrontPricingTerm",
            "CurrencyCode": "USD",
            "RateCards": [{
                "Selector": {
                    "Type": "Duration",
                    "Value": "P365D"
                },
                "Constraints": {
                    "MultipleDimensionSelection": "Allowed",
                    "QuantityConfiguration": "Allowed"
                },
                "RateCard": [{
                    "DimensionKey": "m3.large",
                    "Price": "300.00"
                }, {
                    "DimensionKey": "m4.xlarge",
                    "Price": "400.00"
                }]
            }]
        }, {
            "Type": "ByolPricingTerm"
        }, {
            "Type": "FreeTrialPricingTerm",
            "Duration": "P30D",
            "Grants": [{
                "DimensionKey": "m3.xlarge",
                "MaxQuantity": 10
            }, {
                "DimensionKey": "m4.xlarge",
                "MaxQuantity": 10
            }]
        }, {
            "Type": "UsageBasedPricingTerm",
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
            "Type": "RecurringPaymentTerm",
            "CurrencyCode": "USD",
            "BillingPeriod": "Monthly",
            "Price": "100.0"
        }, {
            "Type": "FixedUpfrontPricingTerm",
            "CurrencyCode": "USD",
            "Grants": [{
                "DimensionKey": "Users",
                "MaxQuantity": 10
            }],
            "Price": "200.0"
        }, {
            "Type": "PaymentScheduleTerm",
            "CurrencyCode": "USD",
            "Schedule": [{
                "ChargeDate": "2020-12-01T00:00:00.000Z",
                "ChargeAmount": "1000.00"
            }, {
                "ChargeDate": "2021-06-15T00:00:00.000Z",
                "ChargeAmount": "1250.00"
            }]
        }, {
            "Type": "LegalTerm",
            "Documents": [{
                "Type": "CustomEula",
                "Url": "https://s3.amazonaws.com/EULA/custom-eula-1234.txt"
            }, {
                "Type": "StandardEula",
                "Version": "2022-07-14"
            }]
        }, {
            "Type": "RenewalTerm"
        }, {
            "Type": "SupportTerm",
            "RefundPolicy": "If you need to request a refund for software sold by Amazon Web Services, LLC, please contact AWS Customer Service."
        }, {
            "Type": "ValidityTerm",
            "AgreementDuration": "P30D",
            "AgreementStartDate": "2021-08-01"
        }, {
            "Type": "ValidityTerm",
            "AgreementStartDate": "2021-08-01",
            "AgreementEndDate": "2022-08-01"
        }]
    }

    actual_detail = OfferEntityDetail.from_json(json.dumps(expected_json))
    expected_detail = OfferEntityDetail(
        description="Worldwide offer for Test Product",
        id="offer-3rEXAMPLErn",
        state="Released",
        markup_percentage="20",
        name="Test Offer",
        pre_existing_agreement=PreExistingAgreement(
            acquisition_channel="External",
            pricing_model="Contract"
        ),
        product_id="prod-ad8EXAMPLE51",
        rules=[
            Rule(
                type="TargetingRule",
                positive_targeting=PositiveTargeting(
                    country_codes=["US", "CA"],
                    buyer_accounts=["444455556666"]
                ),
                negative_targeting=NegativeTargeting(country_codes=["XX"])
            ),
            Rule(
                type="AvailabilityRule",
                availability_end_date="2024-08-30T01:56:03.000Z"
            )
        ],
        terms=[
            Term(
                type="ConfigurableUpfrontPricingTerm",
                currency_code="USD",
                rate_cards=[
                    RateCardsItem(
                        selector=Selector(
                            type="Duration",
                            value="P365D"
                        ),
                        rate_card=[
                            RateCardItem(
                                dimension_key="m3.large",
                                price="300.00"
                            ),
                            RateCardItem(
                                dimension_key="m4.xlarge",
                                price="400.00"
                            )
                        ],
                        constraints=Constraints(
                            multiple_dimension_selection="Allowed",
                            quantity_configuration="Allowed"
                        )
                    )
                ]
            ),
            Term(
                type="ByolPricingTerm"
            ),
            Term(
                type="FreeTrialPricingTerm",
                duration="P30D",
                grants=[
                    GrantItem(
                        dimension_key="m3.xlarge",
                        max_quantity=10
                    ),
                    GrantItem(
                        dimension_key="m4.xlarge",
                        max_quantity=10
                    )
                ]
            ),
            Term(
                type="UsageBasedPricingTerm",
                currency_code="USD",
                rate_cards=[
                    RateCardsItem(
                        rate_card=[
                            RateCardItem(
                                dimension_key="m3.large",
                                price="0.10"
                            ),
                            RateCardItem(
                                dimension_key="m4.xlarge",
                                price="0.20"
                            )
                        ]
                    )
                ]
            ),
            Term(
                type="RecurringPaymentTerm",
                currency_code="USD",
                billing_period="Monthly",
                price="100.0"
            ),
            Term(
                type="FixedUpfrontPricingTerm",
                currency_code="USD",
                price="200.0",
                grants=[GrantItem(
                    dimension_key="Users",
                    max_quantity=10
                )]
            ),
            Term(
                type="PaymentScheduleTerm",
                currency_code="USD",
                schedule=[
                    ScheduleItem(
                        charge_date="2020-12-01T00:00:00.000Z",
                        charge_amount="1000.00"
                    ),
                    ScheduleItem(
                        charge_date="2021-06-15T00:00:00.000Z",
                        charge_amount="1250.00"
                    )
                ]
            ),
            Term(
                type="LegalTerm",
                documents=[
                    DocumentItem(
                        type="CustomEula",
                        url="https://s3.amazonaws.com/EULA/custom-eula-1234.txt"
                    ),
                    DocumentItem(
                        type="StandardEula",
                        version="2022-07-14"
                    )
                ]
            ),
            Term(
                type="RenewalTerm"
            ),
            Term(
                type="SupportTerm",
                refund_policy="If you need to request a refund for software sold by Amazon Web Services, LLC, please contact AWS Customer Service.",
            ),
            Term(
                type="ValidityTerm",
                agreement_start_date=("2021-08-01"),
                agreement_duration=("P30D")
            ),
            Term(
                type="ValidityTerm",
                agreement_start_date=("2021-08-01"),
                agreement_end_date=("2022-08-01")
            )
        ]
    )

    assert actual_detail == expected_detail, "Deserialized object does not match expected object"

def test_create_offer_change_detail_serialization():
    from aws_marketplace_catalog_shapes_offer_1_0.models.create_offer_change_detail import CreateOfferChangeDetail

    create_offer_change_detail = CreateOfferChangeDetail(
        name="New name",
        product_id="prod-12345"
    )
    actual_json = create_offer_change_detail.to_json()
    expected_json = {
        "Name": "New name",
        "ProductId": "prod-12345"
    }

    assert actual_json == json.dumps(expected_json), "Generated CreateOfferChangeDetail does not match expected json"

def test_create_replacement_offer_change_detail_serialization():
    from aws_marketplace_catalog_shapes_offer_1_0.models.create_replacement_offer_change_detail import CreateReplacementOfferChangeDetail

    create_replacement_offer_change_detail = CreateReplacementOfferChangeDetail(
        name="New name",
        agreement_id="agmt-12345"
    )
    actual_json = create_replacement_offer_change_detail.to_json()
    expected_json = {
        "Name": "New name",
        "AgreementId": "agmt-12345"
    }

    assert actual_json == json.dumps(expected_json), "Generated CreateReplacementOfferChangeDetail does not match expected json"

def test_update_information_change_detail_serialization():
    from aws_marketplace_catalog_utils.offer_converter import convert_to_update_information_change_detail
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.update_information_change_detail import UpdateInformationChangeDetail
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.pre_existing_agreement import PreExistingAgreement
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.acquisition_channel import AcquisitionChannel
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.pricing_model import PricingModel

    update_information_change_detail = convert_to_update_information_change_detail(
        UpdateInformationChangeDetail(
            name="Updated Offer Name",
            description="Updated offer description",
            pre_existing_agreement=PreExistingAgreement(
                acquisition_channel=AcquisitionChannel.AWSMARKETPLACE,
                pricing_model=PricingModel.FREE
            )
        )
    )

    actual_json = update_information_change_detail.to_json()
    expected_json = {
        "Name": "Updated Offer Name",
        "Description": "Updated offer description",
        "PreExistingAgreement": {
            "AcquisitionChannel": "AwsMarketplace",
            "PricingModel": "Free"
        }
    }

    assert actual_json == json.dumps(expected_json), "Generated UpdateInformationChangeDetail does not match expected json"

def test_update_legal_terms_change_detail_standard_serialization():
    from aws_marketplace_catalog_utils.offer_converter import convert_to_term
    from aws_marketplace_catalog_shapes_offer_1_0.models.update_legal_terms_change_detail import UpdateLegalTermsChangeDetail
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.legal_term import LegalTerm
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.legal_term_type import LegalTermType
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.document_item import DocumentItem
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.legal_document_type import LegalDocumentType
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.legal_document_version import LegalDocumentVersion

    terms = [LegalTerm(
        type=LegalTermType.LEGALTERM,
        documents=[DocumentItem(
            type=LegalDocumentType.STANDARDEULA,
            version=LegalDocumentVersion.ENUM_2019_MINUS_04_MINUS_24
        )]
    )]

    update_legal_terms_change_detail = UpdateLegalTermsChangeDetail(
        terms=map(convert_to_term, terms)
    )
    actual_json = update_legal_terms_change_detail.to_json()
    expected_json = {
        "Terms": [{
            "Type": "LegalTerm",
            "Documents": [{
                "Type": "StandardEula",
                "Version": "2019-04-24"
            }]
        }]
    }

    assert actual_json == json.dumps(expected_json), "Generated UpdateLegalTermsChangeDetail does not match expected json"

def test_update_legal_terms_change_detail_custom_serialization():
    from aws_marketplace_catalog_utils.offer_converter import convert_to_term
    from aws_marketplace_catalog_shapes_offer_1_0.models.update_legal_terms_change_detail import UpdateLegalTermsChangeDetail
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.legal_term import LegalTerm
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.legal_term_type import LegalTermType
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.document_item import DocumentItem
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.legal_document_type import LegalDocumentType

    terms=[LegalTerm(
        type=LegalTermType.LEGALTERM,
        documents=[DocumentItem(
            type=LegalDocumentType.CUSTOMEULA,
            url="https://s3.amazonaws.com/offer"
        )]
    )]

    update_legal_terms_change_detail = UpdateLegalTermsChangeDetail(
        terms=map(convert_to_term, terms)
    )
    actual_json = update_legal_terms_change_detail.to_json()
    expected_json = {
        "Terms": [{
            "Type": "LegalTerm",
            "Documents": [{
                "Type": "CustomEula",
                "Url": "https://s3.amazonaws.com/offer"
            }]
        }]
    }

    assert actual_json == json.dumps(expected_json), "Generated UpdateLegalTermsChangeDetail does not match expected json"

def test_update_availability_change_detail_serialization():
    from aws_marketplace_catalog_shapes_offer_1_0.models.update_availability_change_detail import UpdateAvailabilityChangeDetail

    update_availability_change_detail = UpdateAvailabilityChangeDetail(
        availability_end_date="2019-01-17"
    )
    actual_json = update_availability_change_detail.to_json()
    expected_json = {
        "AvailabilityEndDate": "2019-01-17"
    }

    assert actual_json == json.dumps(expected_json), "Generated UpdateAvailabilityChangeDetail does not match expected json"

def test_update_support_terms_change_detail_serialization():
    from aws_marketplace_catalog_utils.offer_converter import convert_to_term
    from aws_marketplace_catalog_shapes_offer_1_0.models.update_support_terms_change_detail import UpdateSupportTermsChangeDetail
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.support_term import SupportTerm
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.support_term_type import SupportTermType

    terms=[SupportTerm(
        type=SupportTermType.SUPPORTTERM,
        refund_policy="refund policy"
    )]

    update_support_terms_change_detail = UpdateSupportTermsChangeDetail(
        terms=map(convert_to_term, terms)
    )
    actual_json = update_support_terms_change_detail.to_json()
    expected_json = {
        "Terms": [{
            "Type": "SupportTerm",
            "RefundPolicy": "refund policy"
        }]
    }

    assert actual_json == json.dumps(expected_json), "Generated UpdateSupportTermsChangeDetail does not match expected json"

def test_update_pricing_terms_change_detail_serialization():
    from aws_marketplace_catalog_utils.offer_converter import convert_to_term
    from aws_marketplace_catalog_shapes_offer_1_0.models.update_pricing_terms_change_detail import UpdatePricingTermsChangeDetail
    from aws_marketplace_catalog_shapes_offer_1_0.models.pricing_model import PricingModel
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.byol_pricing_term import ByolPricingTerm
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.byol_pricing_term_type import ByolPricingTermType
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.free_trial_pricing_term import FreeTrialPricingTerm
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.free_trial_pricing_term_type import FreeTrialPricingTermType
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.grant_item import GrantItem
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.usage_based_pricing_term import UsageBasedPricingTerm
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.usage_based_pricing_term_type import UsageBasedPricingTermType
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.currency_code import CurrencyCode
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.usage_based_rate_card_item import UsageBasedRateCardItem
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.rate_card_item import RateCardItem
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.configurable_upfront_pricing_term import ConfigurableUpfrontPricingTerm
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.configurable_upfront_pricing_term_type import ConfigurableUpfrontPricingTermType
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.configurable_upfront_rate_card_item import ConfigurableUpfrontRateCardItem
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.selector import Selector
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.selector_type import SelectorType
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.constraints import Constraints
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.constraint import Constraint
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.fixed_upfront_pricing_term import FixedUpfrontPricingTerm
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.fixed_upfront_pricing_term_type import FixedUpfrontPricingTermType
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.recurring_payment_term import RecurringPaymentTerm
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.recurring_payment_term_type import RecurringPaymentTermType
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.billing_period import BillingPeriod

    terms = [
        ByolPricingTerm(
            type=ByolPricingTermType.BYOLPRICINGTERM
        ),
        FreeTrialPricingTerm(
            type=FreeTrialPricingTermType.FREETRIALPRICINGTERM,
            duration="P30D",
            grants=[
                GrantItem(
                    dimension_key="m3.xlarge",
                    max_quantity=20
                ),
                GrantItem(
                    dimension_key="m4.xlarge",
                    max_quantity=10
                )
            ]
        ),
        UsageBasedPricingTerm(
            type=UsageBasedPricingTermType.USAGEBASEDPRICINGTERM,
            currency_code=CurrencyCode.USD,
            rate_cards=[UsageBasedRateCardItem(
                rate_card=[
                    RateCardItem(
                        dimension_key="m3.large",
                        price="0.10123"
                    ),
                    RateCardItem(
                        dimension_key="m4.xlarge",
                        price="0.20"
                    )
                ]
            )]
        ),
        ConfigurableUpfrontPricingTerm(
            type=ConfigurableUpfrontPricingTermType.CONFIGURABLEUPFRONTPRICINGTERM,
            currency_code=CurrencyCode.USD,
            rate_cards=[ConfigurableUpfrontRateCardItem(
                selector=Selector(
                    type=SelectorType.DURATION,
                    value="P12M"
                ),
                constraints=Constraints(
                    multiple_dimension_selection=Constraint.ALLOWED,
                    quantity_configuration=Constraint.ALLOWED
                ),
                rate_card=[
                    RateCardItem(
                        dimension_key="m3.large",
                        price="300.00"
                    ),
                    RateCardItem(
                        dimension_key="m4.xlarge",
                        price="400.00"
                    )
                ]
            )]
        ),
        FixedUpfrontPricingTerm(
            type=FixedUpfrontPricingTermType.FIXEDUPFRONTPRICINGTERM,
            currency_code=CurrencyCode.USD,
            duration="P180D",
            price="200.00",
            grants=[GrantItem(
                dimension_key="Users",
                max_quantity=10
            )]
        ),
        RecurringPaymentTerm(
            type=RecurringPaymentTermType.RECURRINGPAYMENTTERM,
            currency_code=CurrencyCode.USD,
            price="10.00",
            billing_period=BillingPeriod.MONTHLY
        )
    ]

    update_pricing_terms_change_detail = UpdatePricingTermsChangeDetail(
        pricing_model=PricingModel.CONTRACT,
        terms=map(convert_to_term, terms)
    )
    actual_json = update_pricing_terms_change_detail.to_json()
    expected_json = {
        "PricingModel": "Contract",
        "Terms": [{
            "Type": "ByolPricingTerm"
        }, {
            "Type": "FreeTrialPricingTerm",
            "Duration": "P30D",
            "Grants": [{
                "DimensionKey": "m3.xlarge",
                "MaxQuantity": 20
            }, {
                "DimensionKey": "m4.xlarge",
                "MaxQuantity": 10
            }]
        }, {
            "Type": "UsageBasedPricingTerm",
            "CurrencyCode": "USD",
            "RateCards": [{
                "RateCard": [{
                    "DimensionKey": "m3.large",
                    "Price": "0.10123"
                }, {
                    "DimensionKey": "m4.xlarge",
                    "Price": "0.20"
                }]
            }]
        }, {
            "Type": "ConfigurableUpfrontPricingTerm",
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
                    "Price": "300.00"
                }, {
                    "DimensionKey": "m4.xlarge",
                    "Price": "400.00"
                }]
            }]
        }, {
            "Type": "FixedUpfrontPricingTerm",
            "CurrencyCode": "USD",
            "Duration": "P180D",
            "Grants": [{
                "DimensionKey": "Users",
                "MaxQuantity": 10
            }],
            "Price": "200.00"
        }, {
            "Type": "RecurringPaymentTerm",
            "CurrencyCode": "USD",
            "BillingPeriod": "Monthly",
            "Price": "10.00"
        }]
    }

    assert actual_json == json.dumps(expected_json), "Generated UpdatePricingTermsChangeDetail does not match expected json"

def test_update_targeting_change_detail_positive_buyer_accounts_serialization():
    from aws_marketplace_catalog_utils.offer_converter import convert_to_update_targeting_change_detail
    from aws_marketplace_catalog_shapes_offer_1_0.models.update_targeting_change_detail import UpdateTargetingChangeDetail
    from aws_marketplace_catalog_shapes_offer_1_0.models.positive_targeting import PositiveTargeting

    update_targeting_change_detail = convert_to_update_targeting_change_detail(
        UpdateTargetingChangeDetail(
            positive_targeting=PositiveTargeting(
                buyer_accounts=["118033953248"]
            )
        )
    )
    actual_json = update_targeting_change_detail.to_json()
    expected_json = {
        "PositiveTargeting": {
            "BuyerAccounts": ["118033953248"]
        }
    }

    assert actual_json == json.dumps(expected_json), "Generated UpdateTargetingChangeDetail for positive targeting of buyer accounts does not match expected json"

def test_update_targeting_change_detail_positive_country_codes_serialization():
    from aws_marketplace_catalog_utils.offer_converter import convert_to_update_targeting_change_detail
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.update_targeting_change_detail import UpdateTargetingChangeDetail
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.positive_targeting import PositiveTargeting

    update_targeting_change_detail = convert_to_update_targeting_change_detail(
        UpdateTargetingChangeDetail(
            positive_targeting=PositiveTargeting(
                country_codes=["US", "CA"]
            )
        )
    )
    actual_json = update_targeting_change_detail.to_json()
    expected_json = {
        "PositiveTargeting": {
            "CountryCodes": ["US", "CA"]
        }
    }

    assert actual_json == json.dumps(expected_json), "Generated UpdateTargetingChangeDetail for positive targeting of country codes does not match expected json"

def test_update_targeting_change_detail_negative_serialization():
    from aws_marketplace_catalog_utils.offer_converter import convert_to_update_targeting_change_detail
    from aws_marketplace_catalog_shapes_offer_1_0.models.update_targeting_change_detail import UpdateTargetingChangeDetail
    from aws_marketplace_catalog_shapes_offer_1_0.models.negative_targeting import NegativeTargeting

    update_targeting_change_detail = convert_to_update_targeting_change_detail(
        UpdateTargetingChangeDetail(
            negative_targeting=NegativeTargeting(
                country_codes=["US", "CA"]
            )
        )
    )
    actual_json = update_targeting_change_detail.to_json()
    expected_json = {
        "NegativeTargeting": {
            "CountryCodes": ["US", "CA"]
        }
    }

    assert actual_json == json.dumps(expected_json), "Generated UpdateTargetingChangeDetail for negative targeting does not match expected json"

def test_update_customer_verification_terms_change_detail_serialization():
    from aws_marketplace_catalog_utils.offer_converter import convert_to_term
    from aws_marketplace_catalog_shapes_offer_1_0.models.update_customer_verification_terms_change_detail import UpdateCustomerVerificationTermsChangeDetail
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.customer_verification_term import CustomerVerificationTerm
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.customer_verification_term_type import CustomerVerificationTermType
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.approval_strategy import ApprovalStrategy

    terms = [CustomerVerificationTerm(
        type=CustomerVerificationTermType.CUSTOMERVERIFICATIONTERM,
        approval_strategy=ApprovalStrategy.AUTOAPPROVEONEXPIRATION,
        expiration_duration="P22D"
    )]

    update_customer_verification_terms_change_detail = UpdateCustomerVerificationTermsChangeDetail(
        terms=map(convert_to_term, terms)
    )
    actual_json = update_customer_verification_terms_change_detail.to_json()
    expected_json = {
        "Terms": [{
            "Type": "CustomerVerificationTerm",
            "ApprovalStrategy": "AutoApproveOnExpiration",
            "ExpirationDuration": "P22D"
        }]
    }

    assert actual_json == json.dumps(expected_json), "Generated UpdateCustomerVerificationTermsChangeDetail does not match expected json"

def test_update_payment_schedule_terms_change_detail_serialization():
    from aws_marketplace_catalog_utils.offer_converter import convert_to_term
    from aws_marketplace_catalog_shapes_offer_1_0.models.update_payment_schedule_terms_change_detail import UpdatePaymentScheduleTermsChangeDetail
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.payment_schedule_term import PaymentScheduleTerm
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.payment_schedule_term_type import PaymentScheduleTermType
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.currency_code import CurrencyCode
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.schedule_item import ScheduleItem

    terms = [PaymentScheduleTerm(
        type=PaymentScheduleTermType.PAYMENTSCHEDULETERM,
        currency_code=CurrencyCode.USD,
        schedule=[
            ScheduleItem(
                charge_date="2020-12-01",
                charge_amount="1000.00"
            ),
            ScheduleItem(
                charge_date="2021-06-15",
                charge_amount="1250.00"
            )
        ]
    )]

    update_payment_schedule_terms_change_detail = UpdatePaymentScheduleTermsChangeDetail(
        terms=map(convert_to_term, terms)
    )
    actual_json = update_payment_schedule_terms_change_detail.to_json()
    expected_json = {
        "Terms": [{
            "Type": "PaymentScheduleTerm",
            "CurrencyCode": "USD",
            "Schedule": [{
                "ChargeDate": "2020-12-01",
                "ChargeAmount": "1000.00"
            }, {
                "ChargeDate": "2021-06-15",
                "ChargeAmount": "1250.00"
            }]
        }]
    }

    assert actual_json == json.dumps(expected_json), "Generated UpdatePaymentScheduleTermsChangeDetail does not match expected json"

def test_update_renewal_terms_change_detail_serialization():
    from aws_marketplace_catalog_utils.offer_converter import convert_to_term
    from aws_marketplace_catalog_shapes_offer_1_0.models.update_renewal_terms_change_detail import UpdateRenewalTermsChangeDetail
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.renewal_term import RenewalTerm
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.renewal_term_type import RenewalTermType

    terms = [RenewalTerm(
        type=RenewalTermType.RENEWALTERM
    )]

    update_renewal_terms_change_detail = UpdateRenewalTermsChangeDetail(
        terms=map(convert_to_term, terms)
    )
    actual_json = update_renewal_terms_change_detail.to_json()
    expected_json = {
        "Terms": [{
            "Type": "RenewalTerm"
        }]
    }

    assert actual_json == json.dumps(expected_json), "Generated UpdateRenewalTermsChangeDetail does not match expected json"

def test_update_validity_terms_change_detail_agreement_duration_serialization():
    from aws_marketplace_catalog_utils.offer_converter import convert_to_term
    from aws_marketplace_catalog_shapes_offer_1_0.models.update_validity_terms_change_detail import UpdateValidityTermsChangeDetail
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.validity_term import ValidityTerm
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.validity_term_type import ValidityTermType

    terms =[ValidityTerm(
        type=ValidityTermType.VALIDITYTERM,
        agreement_start_date="2021-08-01",
        agreement_duration="P30D"
    )]

    update_validity_terms_change_detail = UpdateValidityTermsChangeDetail(
        terms=map(convert_to_term, terms)
    )
    actual_json = update_validity_terms_change_detail.to_json()
    expected_json = {
        "Terms": [{
            "Type": "ValidityTerm",
            "AgreementDuration": "P30D",
            "AgreementStartDate": "2021-08-01"
        }]
    }

    assert actual_json == json.dumps(expected_json), "Generated UpdateValidityTermsChangeDetail with agreement duration does not match expected json"

def test_update_validity_terms_change_detail_agreement_end_date_serialization():
    from aws_marketplace_catalog_utils.offer_converter import convert_to_term
    from aws_marketplace_catalog_shapes_offer_1_0.models.update_validity_terms_change_detail import UpdateValidityTermsChangeDetail
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.validity_term import ValidityTerm
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.validity_term_type import ValidityTermType

    terms =[ValidityTerm(
        type=ValidityTermType.VALIDITYTERM,
        agreement_start_date="2021-08-01",
        agreement_end_date="2022-08-01"
    )]

    update_validity_terms_change_detail = UpdateValidityTermsChangeDetail(
        terms=map(convert_to_term, terms)
    )
    actual_json = update_validity_terms_change_detail.to_json()
    expected_json = {
        "Terms": [{
            "Type": "ValidityTerm",
            "AgreementStartDate": "2021-08-01",
            "AgreementEndDate": "2022-08-01"
        }]
    }

    assert actual_json == json.dumps(expected_json), "Generated UpdateValidityTermsChangeDetail with agreement end date does not match expected json"

def test_create_offer_using_resale_authorization_change_detail_serialization():
    from aws_marketplace_catalog_shapes_offer_1_0.models.create_offer_using_resale_authorization_change_detail import CreateOfferUsingResaleAuthorizationChangeDetail

    create_offer_using_resale_authorization_change_detail = CreateOfferUsingResaleAuthorizationChangeDetail(
        resale_authorization_id="resaleAuthorizationId",
        name="name",
        description="description"
    )
    actual_json = create_offer_using_resale_authorization_change_detail.to_json()
    expected_json = {
        "ResaleAuthorizationId": "resaleAuthorizationId",
        "Name": "name",
        "Description": "description"
    }

    assert actual_json == json.dumps(expected_json), "Generated CreateOfferUsingResaleAuthorizationChangeDetail does not match expected json"

def test_create_replacement_offer_using_resale_authorization_change_detail_serialization():
    from aws_marketplace_catalog_shapes_offer_1_0.models.create_replacement_offer_using_resale_authorization_change_detail import CreateReplacementOfferUsingResaleAuthorizationChangeDetail

    create_replacement_offer_using_resale_authorization_change_detail = CreateReplacementOfferUsingResaleAuthorizationChangeDetail(
        resale_authorization_id="resaleAuthorizationId",
        name="name",
        agreement_id="agreementId"
    )
    actual_json = create_replacement_offer_using_resale_authorization_change_detail.to_json()
    expected_json = {
        "ResaleAuthorizationId": "resaleAuthorizationId",
        "AgreementId": "agreementId",
        "Name": "name"
    }

    assert actual_json == json.dumps(expected_json), "Generated CreateReplacementOfferUsingResaleAuthorizationChangeDetail does not match expected json"

def test_update_markup_change_detail_serialization():
    from aws_marketplace_catalog_shapes_offer_1_0.models.update_markup_change_detail import UpdateMarkupChangeDetail

    update_markup_change_detail = UpdateMarkupChangeDetail(
        percentage="15.123456789"
    )
    actual_json = update_markup_change_detail.to_json()
    expected_json = {
        "Percentage": "15.123456789",
    }

    assert actual_json == json.dumps(expected_json), "Generated UpdateMarkupChangeDetail does not match expected json"

def test_release_offer_change_detail_serialization():
    from aws_marketplace_catalog_shapes_offer_1_0.models.release_offer_change_detail import ReleaseOfferChangeDetail

    release_offer_change_detail = ReleaseOfferChangeDetail()
    actual_json = release_offer_change_detail.to_json()
    expected_json = {}

    assert actual_json == json.dumps(expected_json), "Generated ReleaseOfferChangeDetail does not match expected json"
