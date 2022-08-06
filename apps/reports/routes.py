from jinja2 import TemplateNotFound
from apps import db
from apps.reports import blueprint
from flask import render_template, request, url_for, redirect
from apps.authentication.models import Reservation, Parking
from flask_login import login_required


@blueprint.route('/get_reservations', methods=['GET', 'POST'])
@login_required
def get_reservations():
    try:
        reservations = Reservation.query.all()
        return render_template('home/reservations.html', segment='reservations', reservations=reservations)
    except TemplateNotFound:
        return render_template('home/page-404.html'), 404
    except:
        return render_template('home/page-500.html'), 500


@blueprint.route('/parking', methods=['GET', 'POST'])
@login_required
def get_parking():
    try:
        return render_template('home/reservations.html', segment='transactions')
    except TemplateNotFound:
        return render_template('home/page-404.html'), 404
    except:
        return render_template('home/page-500.html'), 500


@blueprint.route('/add_parking', methods=['GET', 'POST'])
@login_required
def add_parking():
    if request.method == 'GET':
        return render_template('home/add_parking.html', segment='parking')

    if request.method == 'POST':
        parking_id = request.form['parking_id']
        address = request.form['address']
        code = request.form['code']
        new_user = Parking(parking_id, address, code)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home_blueprint.index'))

