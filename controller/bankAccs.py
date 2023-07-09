from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import session, conn
from models.companyModel import CompanyModel
from models.bankAccsModel import BankAccsModel
from schemas import CompanySchema,BankData

blp = Blueprint("Bank Accounts", "bank", description="Operations on bank accounts")

@blp.route("/bank/<int:company_id>")
class BankAccsList(MethodView):
    @blp.response(200, BankData(many=True))
    def get(self, company_id):
        bankAccsData = session.query(BankAccsModel).filter(BankAccsModel.company_id == company_id).all()
        return bankAccsData
    
@blp.route("/bank")
class CreateBankAccs(MethodView):
    @blp.arguments(BankData)
    @blp.response(201, BankData)
    def post(self, bankAcc_data):
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
