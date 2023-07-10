def test_get_company(client, created_company_id):
    response = client.get(
        f"/company/{created_company_id}"
    )

    assert response.status_code == 200
    assert response.json == {
        "address": "Test Address",
        "bankAccs": [],
        "billing": 10000,
        "companyName": "Test Company",
        "id": 1,
        "phone": "(98) 3256-9823",
        "registrationDate": "2002-02-10"
    }


def test_create_company(client):
    response = client.post(
        "/company",
        json={
            "billing": 200000,
            "companyName": "Test Company",
            "bankAccs": [],
            "registrationDate": "2002-01-10",
            "phone": "(98) 98254-9823",
            "address": "Test Address"
        })
    assert response.status_code == 201
    assert response.json["name"] == "Test Company"


def test_delete_company(client, created_company_id):
    response = client.delete(
        f"/company/{created_company_id}"
    )
    assert response.status_code == 200
    assert response.json == {"message": "Company deleted"}
