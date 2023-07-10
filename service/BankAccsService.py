from db import session
from models import BankAccsModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError, NoResultFound
from flask_smorest import abort


class BankAccsService():
    def getBankAccsList(self, company_id):
        bankAccsData = session.query(BankAccsModel).filter(BankAccsModel.company_id == company_id).all()
        return bankAccsData

    def createBankAcc(self, bankAcc_data):
        bankAcc_item = BankAccsModel(**bankAcc_data)
        try:
            session.add(bankAcc_item)
            session.commit()
        except IntegrityError:
            session.rollback()
            abort(
                400,
                message="Company id does not exist."
            )
        except SQLAlchemyError:
            session.rollback()
            abort(500, message="An error occurred creating a new Bank Account. Please contact our Support Channel")
        return bankAcc_item

    def getBankAccById(self, company_id, id):
        try:
            return session.query(BankAccsModel).filter(BankAccsModel.company_id == company_id).filter(
                BankAccsModel.id == id).one()
        except NoResultFound:
            abort(404, message="No bank account was found.")

    def deleteBankAcc(self, company_id, id):
        bankAcc = session.query(BankAccsModel).filter(BankAccsModel.company_id == company_id).filter(
            BankAccsModel.id == id).one()
        session.delete(bankAcc)
        session.commit()
        return {"message": "Bank account deleted."}, 200

    def updateBankAcc(self, bankacc_data, company_id, id):
        newBankAccData = session.query(BankAccsModel).filter(BankAccsModel.company_id == company_id).filter(
            BankAccsModel.id == id).one()

        if newBankAccData:
            newBankAccData.acc = bankacc_data["acc"]
            newBankAccData.agency = bankacc_data["agency"]
            newBankAccData.bank = bankacc_data["bank"]
        else:
            newBankAccData = BankAccsModel(id, **bankacc_data)

        session.add(newBankAccData)
        session.commit()

        return newBankAccData
