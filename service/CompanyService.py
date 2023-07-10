from db import session
from models.CompanyModel import CompanyModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from flask_smorest import abort

class CompanyService():
    def getCompanyList(self):
        return session.query(CompanyModel).all()

    def createNewCompany(self, company_data):
        company = CompanyModel(**company_data)
        try:
            session.add(company)
            session.commit()
        except IntegrityError:
            session.rollback()
            abort(
                400,
                message="Company name provided already exists."
            )
        except SQLAlchemyError:
            session.rollback()
            abort(500, message="An error occurred creating a new Company. Please contact our Support Channel")

        return company
    
    def getCompanyById(self, id):
        return session.query(CompanyModel).filter(CompanyModel.id == id).one_or_none()

    def deleteCompany(self, id):
        company = session.query(CompanyModel).get(id)
        session.delete(company)
        session.commit()
        return {"message": "Company deleted"}, 200
    
    def updateCompany(self, company_data, id):
        newCompany = session.query(CompanyModel).filter(CompanyModel.id == id).one_or_none()

        if newCompany:
            newCompany.address          = company_data["address"]
            newCompany.billing          = company_data["billing"]
            newCompany.companyName      = company_data["companyName"]
            newCompany.phone            = company_data["phone"]
            newCompany.registrationDate = company_data["registrationDate"]
        else:
            newCompany = CompanyModel(id, **company_data)

        session.add(newCompany)
        session.commit()

        return newCompany
