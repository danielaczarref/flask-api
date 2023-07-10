import json
from unittest import TestCase
from models import CompanyModel


class CompanyTest(TestCase):
    def testCreateCompany(self):
        company = CompanyModel(
            "Test Company",
            "40028922",
            "Rua Aririzal, 12",
            "2023-07-08",
            "10000",
            [])

        self.assertEqual(company.companyName, "Test Company",
                         "The name of the company after creation is not equal to the constructor argument.")
        self.assertEqual(company.phone, "40028922",
                         "The phone of the company after creation is not equal to the constructor argument.")
        self.assertEqual(company.address, "Rua Aririzal, 12",
                         "The address of the company after creation is not equal to the constructor argument.")
        self.assertEqual(company.registrationDate, "2023-07-08",
                         "The registration date of the company after creation is not equal to the constructor argument.")
        self.assertEqual(company.billing, "10000",
                         "The billing of the company after creation is not equal to the constructor argument.")