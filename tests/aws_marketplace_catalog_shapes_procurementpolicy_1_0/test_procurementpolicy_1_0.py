import pytest
import json

def test_importable():
    from aws_marketplace_catalog_shapes_procurementpolicy_1_0_entitytype.models.procurement_policy_entity_detail import ProcurementPolicyEntityDetail # noqa: F401

    assert True

def test_procurementpolicy_1_0_entity_detail_deserialization():
    from aws_marketplace_catalog_shapes_procurementpolicy_1_0_entitytype.models.procurement_policy_entity_detail import ProcurementPolicyEntityDetail
    from aws_marketplace_catalog_shapes_procurementpolicy_1_0_entitytype.models.statement import Statement
    from aws_marketplace_catalog_shapes_procurementpolicy_1_0_entitytype.models.resource import Resource
    from aws_marketplace_catalog_shapes_procurementpolicy_1_0_entitytype.models.configuration import Configuration

    expected_json = {
        "Name": "Procurement Policy",
        "Description": "Procurement Policy for Private Marketplace",
        "Statements": [{
            "Effect": "Deny",
            "Resources": [{
                "Type": "Product",
                "Ids": ["abcdefgh-1234-1234-abcd-123abc456def"],
                "Notes": "Declined"
            }, {
                "Type": "Product",
                "Ids": ["abcdefgh-1234-1234-abcd-abc123def456"]
            }, {
                "Type": "Product",
                "Ids": ["abcdefgh-1234-1234-abcd-246abc135def"],
                "Notes": "Declined for no reason"
            }]
        }, {
            "Effect": "Allow",
            "Resources": [{
                "Type": "Product",
                "Ids": ["abcdefgh-1234-1234-abcd-abc246def135"]
            }, {
                "Type": "Product",
                "Ids": ["abcdefgh-1234-1234-abcd-135abc246def"],
                "Notes": "Approved"
            }]
        }],
        "Configuration": {
            "PolicyResourceRequests": "Deny"
        }
    }

    actual_detail = ProcurementPolicyEntityDetail.from_json(json.dumps(expected_json))
    expected_detail = ProcurementPolicyEntityDetail(
        name="Procurement Policy",
        description="Procurement Policy for Private Marketplace",
        statements=[
            Statement(
                effect="Deny",
                resources=[
                    Resource(
                        type="Product",
                        ids=["abcdefgh-1234-1234-abcd-123abc456def"],
                        notes="Declined"
                    ),
                    Resource(
                        type="Product",
                        ids=["abcdefgh-1234-1234-abcd-abc123def456"]
                    ),
                    Resource(
                        type="Product",
                        ids=["abcdefgh-1234-1234-abcd-246abc135def"],
                        notes="Declined for no reason"
                    )
                ]
            ),
            Statement(
                effect="Allow",
                resources=[
                    Resource(
                        type="Product",
                        ids=["abcdefgh-1234-1234-abcd-abc246def135"]
                    ),
                    Resource(
                        type="Product",
                        ids=["abcdefgh-1234-1234-abcd-135abc246def"],
                        notes="Approved"
                    )
                ]
            )
        ],
        configuration=Configuration(
            policy_resource_requests="Deny"
        )
    )

    assert actual_detail == expected_detail, "Deserialized object does not match expected object"
