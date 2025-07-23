from app.extension import db
from app.model.convention import Convention
from datetime import datetime

class ConventionDao:
    # get all conventions
    @staticmethod
    def get_all_conventions():
        return Convention.query.all()

    # get convention by id
    @staticmethod
    def get_convention_by_id(id):
        return Convention.query.get(id)

    # create a new convention
    @staticmethod
    def create_convention(internship_id, document_filename=None, note=None):
        new_convention = Convention(
            internship_id=internship_id,
            document_filename=document_filename,
            note=note
        )
        db.session.add(new_convention)
        db.session.commit()
        return new_convention

    # Update a convention by ID
    @staticmethod
    def update_convention(id, downloaded=None, signed=None, download_date=None, signed_date=None, signed_by=None, note=None, document_filename=None):
        convention = Convention.query.get(id)
        if not convention:
            return None

        if downloaded is not None:
            convention.downloaded = downloaded
            if downloaded and download_date is None:
                convention.download_date = datetime.utcnow()
        if signed is not None:
            convention.signed = signed
            if signed and signed_date is None:
                convention.signed_date = datetime.utcnow()
        if signed_date is not None:
            convention.signed_date = signed_date
        if download_date is not None:
            convention.download_date = download_date
        if signed_by is not None:
            convention.signed_by = signed_by
        if note is not None:
            convention.note = note
        if document_filename is not None:
            convention.document_filename = document_filename

        db.session.commit()
        return convention

    # Delete a convention by ID
    @staticmethod
    def delete_convention(id):
        convention = Convention.query.get(id)
        if not convention:
            return None

        db.session.delete(convention)
        db.session.commit()
        return convention

    # get signed conventions
    @staticmethod
    def get_signed_conventions():
        return Convention.query.filter_by(signed=True).all()

    # get downloaded conventions
    @staticmethod
    def get_downloaded_conventions():
        return Convention.query.filter_by(downloaded=True).all()

    # get conventions by internship ID
    @staticmethod
    def get_conventions_by_internship_id(internship_id):
        return Convention.query.filter_by(internship_id=internship_id).all()

    # get conventions by user ID
    @staticmethod
    def get_conventions_by_user_id(user_id):
        return Convention.query.filter(Convention.internship.has(user_id=user_id)).all()

    # get conventions downloaded but not signed:
    @staticmethod
    def get_downloaded_but_not_signed():
        return Convention.query.filter_by(downloaded=True, signed=False).all()

    # get conventions by document filename
    @staticmethod
    def get_conventions_by_document_filename(document_filename):
        return Convention.query.filter_by(document_filename=document_filename).all()
