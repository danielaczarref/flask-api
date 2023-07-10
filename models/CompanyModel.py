from db import Base
from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.orm import relationship


class CompanyModel(Base):
    __tablename__ = "company"

    id = Column(Integer, primary_key=True, autoincrement=True)
    companyName = Column(String(300), unique=True, nullable=False)
    phone = Column(String(20), unique=False, nullable=True)
    address = Column(String(300), unique=False, nullable=True)
    registrationDate = Column(Date, nullable=False)
    billing = Column(Float, unique=False, nullable=False)
    bankAccs = relationship("BankAccsModel", back_populates="company", lazy="dynamic")

    def __init__(self, companyName, phone, address, registrationDate, billing, bankAccs):
        self.companyName = companyName
        self.phone = phone
        self.address = address
        self.registrationDate = registrationDate
        self.billing = billing
        self.bankAccs = bankAccs
