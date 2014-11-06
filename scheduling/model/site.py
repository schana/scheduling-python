from scheduling import db
from scheduling.model import relationships


class SiteType(db.Model):
    __tablename__ = 'site_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    sites = db.relationship('Site', backref=db.backref('site_type'))
    certifications = db.relationship('Certification', secondary=relationships.certifications_site_types,
                                     backref=db.backref('site_types'))

    def __repr__(self):
        return '<{} {}>'.format(self.__tablename__, self.name)


class Site(db.Model):
    __tablename__ = 'site'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    site_type_id = db.Column(db.Integer, db.ForeignKey('site_type.id'))
    events = db.relationship('Event', backref=db.backref('site'))

    def __repr__(self):
        return '<{} {}>'.format(self.__tablename__, self.name)