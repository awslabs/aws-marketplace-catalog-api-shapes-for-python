def convert_to_term(obj):
    from aws_marketplace_catalog_shapes_offer_1_0.models.term import Term
    try:
        term = Term.from_json(obj.to_json())
        # Check that at least one field is not None and was converted
        if sum(1 for val in term.to_dict() if val is not None) == 0:
            raise RuntimeError("No recognized fields")
        return term
    except BaseException as e:
        raise RuntimeError("Error converting to Term:", e)


def convert_to_update_information_change_detail(obj):
    from aws_marketplace_catalog_shapes_offer_1_0.models.update_information_change_detail import UpdateInformationChangeDetail
    try:
        detail = UpdateInformationChangeDetail.from_json(obj.to_json())
        # Check that at least one field is not None and was converted
        if sum(1 for val in detail.to_dict() if val is not None) == 0:
            raise RuntimeError("No recognized fields")
        return detail
    except BaseException as e:
        raise RuntimeError("Error converting to UpdateInformationChangeDetail:", e)

def convert_to_update_targeting_change_detail(obj):
    from aws_marketplace_catalog_shapes_offer_1_0.models.update_targeting_change_detail import UpdateTargetingChangeDetail
    try:
        detail= UpdateTargetingChangeDetail.from_json(obj.to_json())
        # Check that at least one field is not None and was converted
        if sum(1 for val in detail.to_dict() if val is not None) == 0:
            raise RuntimeError("No recognized fields")
        return detail
    except BaseException as e:
        raise RuntimeError("Error converting to UpdateTargetingChangeDetail:", e)