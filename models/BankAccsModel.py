from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, mapped_column


class BankAccsModel(Base):
    __tablename__ = "bankAccs"

    id = Column(Integer, primary_key=True)
    acc = Column(Integer, nullable=False)
    agency = Column(Integer, nullable=False)
    bank = Column(String(100), nullable=False)
    company_id = mapped_column(ForeignKey("company.id"))
    company = relationship("CompanyModel", back_populates="bankAccs")

    def __init__(self, acc, agency, bank, company_id):
        self.acc = acc
        self.agency = agency
        self.bank = bank
        self.company_id = company_id
