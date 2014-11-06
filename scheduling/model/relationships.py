from scheduling import db


certifications_members = db.Table('certifications_members', db.Model.metadata,
                                  db.Column('cert_id', db.Integer, db.ForeignKey('certification.id')),
                                  db.Column('member_id', db.Integer, db.ForeignKey('member.id')))

certifications_site_types = db.Table('certifications_site_types', db.Model.metadata,
                                     db.Column('cert_id', db.Integer, db.ForeignKey('certification.id')),
                                     db.Column('site_type_id', db.Integer, db.ForeignKey('site_type.id')))


events_members = db.Table('events_members', db.Model.metadata,
                          db.Column('event_id', db.Integer, db.ForeignKey('event.id')),
                          db.Column('member_id', db.Integer, db.ForeignKey('member.id')))


class Certification(db.Model):
    __tablename__ = 'certification'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<{} {}>'.format(self.__tablename__, self.name)
