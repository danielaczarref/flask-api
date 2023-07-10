import pytest


@pytest.fixture()
def created_company_id(client):
    response = client.post(
        "/company",
        json={"companyName": "Test Company"}
    )

    return response.json["id"]


@pytest.fixture()
def created_bank_acc_id(client, created_company_id):
    response = client.post(
        f"/bank/{created_company_id}",
        json={"bank": "Test Bank Acc"}
    )

    return response.json["id"]
