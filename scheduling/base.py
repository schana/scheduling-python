from scheduling import app
from scheduling.model import member
from flask import send_from_directory, render_template, request
from sqlalchemy.orm import joinedload
from pkg_resources import resource_filename
from datetime import date
import calendar


@app.route('/')
def base():
    year, month = request.args.get('month', date.today().strftime('%Y-%m')).split('-')
    cal = calendar.Calendar()
    now = date(int(year), int(month), 1)
    days = [day for day in cal.itermonthdates(now.year, now.month) if day.month == now.month]
    members = member.Member.query.options(joinedload('events')).all()
    return render_template('schedule.html', members=members, days=days)


@app.route('/static/<path:filename>')
def get_static(filename):
    return send_from_directory(resource_filename(__name__, 'static'), filename)
