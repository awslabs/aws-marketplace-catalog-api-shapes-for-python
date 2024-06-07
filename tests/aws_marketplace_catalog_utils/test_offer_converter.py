import pytest

def test_convert_to_term():
    from aws_marketplace_catalog_utils.offer_converter import convert_to_term
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.legal_term import LegalTerm
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.legal_term_type import LegalTermType
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.document_item import DocumentItem
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.legal_document_type import LegalDocumentType
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.legal_document_version import LegalDocumentVersion
    from aws_marketplace_catalog_shapes_offer_1_0.models.term import Term
    from aws_marketplace_catalog_shapes_offer_1_0.models.document_item import DocumentItem as ExpectedDocumentItem

    term = LegalTerm(
        type=LegalTermType.LEGALTERM,
        documents=[DocumentItem(
            type=LegalDocumentType.STANDARDEULA,
            version=LegalDocumentVersion.ENUM_2019_MINUS_04_MINUS_24
        )]
    )

    actual_term = convert_to_term(term)

    expected_term = Term(
        type="LegalTerm",
        documents=[ExpectedDocumentItem(
            type="StandardEula",
            version="2019-04-24"
        )]
    )
    
    assert actual_term == expected_term

def test_invalid_string_convert_to_term():
    with pytest.raises(Exception):
        from aws_marketplace_catalog_utils.offer_converter import convert_to_term

        convert_to_term("test")

def test_invalid_object_convert_to_term():
    with pytest.raises(Exception):
        from aws_marketplace_catalog_utils.offer_converter import convert_to_term
        from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.update_information_change_detail import UpdateInformationChangeDetail
        from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.pre_existing_agreement import PreExistingAgreement
        from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.acquisition_channel import AcquisitionChannel
        from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.pricing_model import PricingModel

        detail = UpdateInformationChangeDetail(
            name="Updated Offer Name",
            description="Updated offer description",
            pre_existing_agreement=PreExistingAgreement(
                acquisition_channel=AcquisitionChannel.AWSMARKETPLACE,
                pricing_model=PricingModel.FREE
            )
        )

        convert_to_term(detail)

def test_convert_to_update_information_change_detail():
    from aws_marketplace_catalog_utils.offer_converter import convert_to_update_information_change_detail
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.update_information_change_detail import UpdateInformationChangeDetail
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.pre_existing_agreement import PreExistingAgreement
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.acquisition_channel import AcquisitionChannel
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.pricing_model import PricingModel

    from aws_marketplace_catalog_shapes_offer_1_0.models.update_information_change_detail import UpdateInformationChangeDetail as ExpectedUpdateInformationChangeDetail
    from aws_marketplace_catalog_shapes_offer_1_0.models.pre_existing_agreement import PreExistingAgreement as ExpectedPreExistingAgreement

    detail = UpdateInformationChangeDetail(
        name="Updated Offer Name",
        description="Updated offer description",
        pre_existing_agreement=PreExistingAgreement(
            acquisition_channel=AcquisitionChannel.AWSMARKETPLACE,
            pricing_model=PricingModel.FREE
        )
    )
    actual_detail = convert_to_update_information_change_detail(detail)

    expected_detail = ExpectedUpdateInformationChangeDetail(
        name="Updated Offer Name",
        description="Updated offer description",
        pre_existing_agreement=ExpectedPreExistingAgreement(
            acquisition_channel="AwsMarketplace",
            pricing_model="Free"
        )
    )

    assert actual_detail == expected_detail

def test_invalid_string_convert_to_update_information_change_detail():
    with pytest.raises(Exception):
        from aws_marketplace_catalog_utils.offer_converter import convert_to_update_information_change_detail

        convert_to_update_information_change_detail("test")

def test_invalid_object_convert_to_update_information_change_detail():
    with pytest.raises(Exception):
        from aws_marketplace_catalog_utils.offer_converter import convert_to_update_information_change_detail
        from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.legal_term import LegalTerm
        from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.legal_term_type import LegalTermType
        from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.document_item import DocumentItem
        from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.legal_document_type import LegalDocumentType
        from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.legal_document_version import LegalDocumentVersion

        term = LegalTerm(
            type=LegalTermType.LEGALTERM,
            documents=[DocumentItem(
                type=LegalDocumentType.STANDARDEULA,
                version=LegalDocumentVersion.ENUM_2019_MINUS_04_MINUS_24
            )]
        )

        convert_to_update_information_change_detail(term)

def test_convert_to_update_targeting_change_detail():
    from aws_marketplace_catalog_utils.offer_converter import convert_to_update_targeting_change_detail
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.update_targeting_change_detail import UpdateTargetingChangeDetail
    from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.positive_targeting import PositiveTargeting
    from aws_marketplace_catalog_shapes_offer_1_0.models.update_targeting_change_detail import UpdateTargetingChangeDetail as ExpectedUpdateTargetingChangeDetail
    from aws_marketplace_catalog_shapes_offer_1_0.models.positive_targeting import PositiveTargeting as ExpectedPositiveTargeting

    detail = UpdateTargetingChangeDetail(
        positive_targeting=PositiveTargeting(
            country_codes=["US", "CA"]
        )
    )

    actual_detail = convert_to_update_targeting_change_detail(detail)

    expected_detail = ExpectedUpdateTargetingChangeDetail(
        positive_targeting=ExpectedPositiveTargeting(
            country_codes=["US", "CA"]
        )
    )

    assert actual_detail == expected_detail

def test_invalid_string_convert_to_update_targeting_change_detail():
    with pytest.raises(Exception):
        from aws_marketplace_catalog_utils.offer_converter import convert_to_update_targeting_change_detail

        convert_to_update_targeting_change_detail("test")

def test_invalid_object_convert_to_update_targeting_change_detail():
    with pytest.raises(Exception):
        from aws_marketplace_catalog_utils.offer_converter import convert_to_update_targeting_change_detail
        from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.legal_term import LegalTerm
        from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.legal_term_type import LegalTermType
        from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.document_item import DocumentItem
        from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.legal_document_type import LegalDocumentType
        from aws_marketplace_catalog_shapes_offer_1_0_appendix.models.legal_document_version import LegalDocumentVersion

        term = LegalTerm(
            type=LegalTermType.LEGALTERM,
            documents=[DocumentItem(
                type=LegalDocumentType.STANDARDEULA,
                version=LegalDocumentVersion.ENUM_2019_MINUS_04_MINUS_24
            )]
        )

        convert_to_update_targeting_change_detail(term)
