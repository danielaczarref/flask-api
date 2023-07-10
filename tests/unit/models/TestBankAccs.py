import json
from unittest import TestCase
from models import BankAccsModel


class CompanyTest(TestCase):
    def testCreateCompany(self):
        bankAcc = BankAccsModel(
            126521,
            5655,
            "Banco do Brasil",
            1)

        self.assertEqual(bankAcc.acc, 126521,
                         "The bank acc's number after creation is not equal to the constructor argument.")
        self.assertEqual(bankAcc.agency, 5655,
                         "The bank acc's agency after creation is not equal to the constructor argument.")
        self.assertEqual(bankAcc.bank, "Banco do Brasil",
                         "The bank's name after creation is not equal to the constructor argument.")
        self.assertEqual(bankAcc.company_id, 1,
                         "The Company's identification number after creation is not equal to the constructor argument.")