def test_get_bank_acc(client, created_company_id):
    response = client.get(
        f"/bank/{created_company_id}"
    )
    assert response.status_code == 200
    assert response.json == {
        "acc": 54168,
        "agency": 1325479,
        "bank": "Test Bank",
        "company_id": 1,
        "id": 1
    }


def test_create_bank_acc(client):
    response = client.post(
        "/bank",
        json={
            "company_id": 1,
            "bank": "Test Bank",
            "agency": 1325479,
            "acc": 54168
        })
    assert response.status_code == 201
    assert response.json["bank"] == "Test Bank"


def test_delete_bank_acc(client, created_company_id, created_bank_acc_id):
    response = client.delete(
        f"/bank/{created_company_id}/bank-acc/{created_bank_acc_id}"
    )
    assert response.status_code == 200
    assert response.json == {"message": "Bank account deleted."}
