from scheduling import db
from scheduling.model import relationships

class Squad(db.Model):
    __tablename__ = 'squad'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    crews = db.relationship('Crew', backref=db.backref('squad'))

    def __repr__(self):
        return '<{} {}>'.format(self.__tablename__, self.name)


class Crew(db.Model):
    __tablename__ = 'crew'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, unique=True)
    squad_id = db.Column(db.Integer, db.ForeignKey('squad.id'))
    members = db.relationship('Member', backref=db.backref('crew'))

    def __repr__(self):
        return '<{} {}>'.format(self.__tablename__, self.name)


class Position(db.Model):
    __tablename__ = 'position'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    jobs = db.relationship('Job', backref=db.backref('position'))

    def __repr__(self):
        return '<{} {}>'.format(self.__tablename__, self.name)


class Job(db.Model):
    __tablename__ = 'job'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    alert_count = db.Column(db.Integer)
    backup_count = db.Column(db.Integer)
    event_count = db.Column(db.Integer)
    position_id = db.Column(db.Integer, db.ForeignKey('position.id'))
    members = db.relationship('Member', backref=db.backref('job'))

    def __repr__(self):
        return '<{} {}>'.format(self.__tablename__, self.name)


class Leave(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.Date)
    end = db.Column(db.Date, db.CheckConstraint('end>=start'))
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'))

    def __repr__(self):
        return '<{} {} {}>'.format(self.__tablename__, self.start, self.end)


class Member(db.Model):
    __tablename__ = 'member'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'))
    crew_id = db.Column(db.Integer, db.ForeignKey('crew.id'))
    certifications = db.relationship('Certification', secondary=relationships.certifications_members,
                                     backref=db.backref('members'))
    leave = db.relationship('Leave', backref=db.backref('member'))
    events = db.relationship('Event', secondary=relationships.events_members, backref=db.backref('member'))

    def __repr__(self):
        return '<{} {}>'.format(self.__tablename__, self.name)
