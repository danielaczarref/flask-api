from db import session
from models.BankAccsModel import BankAccsModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
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
        bankAccsData = session.query(BankAccsModel).filter(BankAccsModel.company_id == company_id).filter(BankAccsModel.id == id).one()
        print(bankAccsData)
        return bankAccsData
    
    def deleteBankAcc(self, company_id, id):
        bankAcc = session.query(BankAccsModel).filter(BankAccsModel.company_id == company_id).filter(BankAccsModel.id == id).one()
        session.delete(bankAcc)
        session.commit()
        return {"message": "Bank account deleted."}, 200