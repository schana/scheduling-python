from scheduling import db


class EventType(db.Model):
    __tablename__ = 'event_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    events = db.relationship('Event', backref=db.backref('event_type'))

    def __repr__(self):
        return '<{} {}>'.format(self.__tablename__, self.name)


class Event(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    date = db.Column(db.Date)
    event_type_id = db.Column(db.Integer, db.ForeignKey('event_type.id'))
    site_id = db.Column(db.Integer, db.ForeignKey('site.id'))

    def __repr__(self):
        return '<{} {} {}>'.format(self.__tablename__, self.date, self.name)


