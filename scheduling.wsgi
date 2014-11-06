from scheduling import app, admin, db
from scheduling.model import event, member, site, relationships
from flask_admin.contrib.sqla import ModelView

db.create_all()

admin.add_view(ModelView(member.Member, db.session))
admin.add_view(ModelView(member.Leave, db.session))
admin.add_view(ModelView(event.Event, db.session))
admin.add_view(ModelView(member.Squad, db.session))
admin.add_view(ModelView(member.Crew, db.session))
admin.add_view(ModelView(member.Position, db.session))
admin.add_view(ModelView(member.Job, db.session))
admin.add_view(ModelView(event.EventType, db.session))
admin.add_view(ModelView(site.Site, db.session))
admin.add_view(ModelView(site.SiteType, db.session))
admin.add_view(ModelView(relationships.Certification, db.session))

application = app

if __name__ == '__main__':
    application.run(debug=True)
