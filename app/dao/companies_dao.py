from app.extension import db
from app.model.companies import Companies

class CompaniesDAO:
    # get all companies
    @staticmethod
    def get_all_companies():
        return Companies.query.all()

    # get company by id
    @staticmethod
    def get_company_by_id(id):
        return Companies.query.get(id)

    # create a new company
    @staticmethod
    def create_company(number, companyName, address, email, province, note, city, cap, partitaIVA, type_id):
        new_company = Companies(
            number=number,
            companyName=companyName,
            address=address,
            email=email,
            province=province,
            note=note,
            city=city,
            cap=cap,
            partitaIVA=partitaIVA,
            type_id=type_id
        )
        db.session.add(new_company)
        db.session.commit()
        return new_company

    # update company by id
    @staticmethod
    def update_company(id, number=None, companyName=None, address=None, email=None, province=None, note=None, city=None, cap=None, partitaIVA=None, type_id=None):
        company = Companies.query.get(id)
        if not company:
            return None

        if number is not None:
            company.number = number
        if companyName is not None:
            company.companyName = companyName
        if address is not None:
            company.address = address
        if email is not None:
            company.email = email
        if province is not None:
            company.province = province
        if note is not None:
            company.note = note
        if city is not None:
            company.city = city
        if cap is not None:
            company.cap = cap
        if partitaIVA is not None:
            company.partitaIVA = partitaIVA
        if type_id is not None:
            company.type_id = type_id

        db.session.commit()
        return company

    # delete company by id
    @staticmethod
    def delete_company(id):
        company = Companies.query.get(id)
        if not company:
            return None

        db.session.delete(company)
        db.session.commit()
        return company
    
    # Ricerca per settore
    @staticmethod
    def search_by_sector(sector):
        from app.model.companyTipes import CompanyTypes
        return Companies.query.join(Companies.company_type).filter(CompanyTypes.name.ilike(f"%{sector}%")).all()

    # Ricerca per città
    @staticmethod
    def search_by_city(city):
        return Companies.query.filter(Companies.city.ilike(f"%{city}%")).all()

    # Ricerca per numero minimo di studenti ospitati
    @staticmethod
    def search_by_min_students(min_students):
        from sqlalchemy import func
        return Companies.query.outerjoin(Companies.internship)\
            .group_by(Companies.id)\
            .having(func.count(Companies.internship) >= min_students).all()

    # Ricerca per disponibilità in un periodo
    @staticmethod
    def search_available_in_period(start_date, end_date):
        from app.model.internships import Internship
        subquery = db.session.query(Internship.company_id)\
            .filter(
                Internship.start_date <= end_date,
                Internship.end_date >= start_date,
                Internship.status != 'annullato'
            )
        return Companies.query.filter(~Companies.id.in_(subquery)).all()

    # Ricerca combinata
    @staticmethod
    def advanced_search(sector=None, city=None, min_students=None):
        from app.model.companyTipes import CompanyTypes
        from sqlalchemy import func
        query = Companies.query
        if sector:
            query = query.join(Companies.company_type).filter(CompanyTypes.name.ilike(f"%{sector}%"))
        if city:
            query = query.filter(Companies.city.ilike(f"%{city}%"))
        if min_students:
            query = query.outerjoin(Companies.internship)\
                .group_by(Companies.id)\
                .having(func.count(Companies.internship) >= min_students)
        return query.all()
    