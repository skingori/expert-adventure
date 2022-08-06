# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import datetime
from flask_login import UserMixin

from apps import db, login_manager
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy import TIMESTAMP, DateTime, exists
from sqlalchemy.sql import func


class Login(db.Model, UserMixin):
    __tablename__ = "Login"
    Login_id = db.Column(db.Integer, primary_key=True)
    Login_username = db.Column(db.String(70), unique=True)
    Login_password = db.Column(db.String(500))
    Login_rank = db.Column(db.String(70))

    def __init__(self, login_id, login_username, login_password, login_rank):
        self.Login_id = login_id
        self.Login_username = login_username
        self.Login_password = login_password
        self.Login_rank = login_rank

    def get_id(self):
        return self.Login_id

    def __repr__(self):
        return str(self.Login_username)


class Reservation(db.Model):
    __tablename__ = "Parking_Slot_Reservation"
    Reservation_slot_id = db.Column(
        db.Integer, primary_key=True, autoincrement=True)
    Parking_slot_reservation_duration = db.Column(db.String(100))
    Parking_slot_reservation_vehicle_category_id = db.Column(
        BIGINT(unsigned=True))
    Parking_slot_reservation_Parking_lot_id = db.Column(BIGINT(unsigned=True))
    Parking_slot_reservation_driver_id = db.Column(BIGINT(unsigned=True))
    Parking_slot_reservation_booking_date = db.Column(
        db.DateTime, default=datetime.datetime.now)
    Parking_slot_reservation_start_timestamp = db.Column(
        TIMESTAMP, nullable=False, server_default=func.now())
    Parking_slot_reservation_vehicle_reg_no = db.Column(db.String(100))

    def __init__(self, duration, category, lot, driver, date, reg):
        self.Parking_slot_reservation_duration = duration
        self.Parking_slot_reservation_vehicle_category_id = category
        self.Parking_slot_reservation_Parking_lot_id = lot
        self.Parking_slot_reservation_driver_id = driver
        self.Parking_slot_reservation_booking_date = date
        self.Parking_slot_reservation_vehicle_reg_no = reg

    def __repr__(self):
        return str(self.Parking_slot_reservation_duration)


class Parking(db.Model):
    __tablename__ = "parking_lot"
    Parking_lot_id = db.Column(BIGINT(unsigned=True), primary_key=True)
    Parking_lot_address = db.Column(db.String(500))
    Parking_lot_code = db.Column(db.String(70))

    def __init__(self, id_, address, code):
        self.Parking_lot_id = id_
        self.Parking_lot_address = address
        self.Parking_lot_code = code

    def __repr__(self):
        return str(self.Parking_lot_id)


class Vehicle(db.Model):
    __tablename__ = "Vehicle_category"
    Vehicle_category_id = db.Column(BIGINT(unsigned=True), primary_key=True)
    Vehicle_category_name = db.Column(db.String(100))
    Vehicle_category_desc = db.Column(db.String(500))
    Vehicle_category_daily_parking_fee = db.Column(db.String(100))

    def __init__(self, id_, name, desc, fee):
        self.Vehicle_category_id = id_
        self.Vehicle_category_name = name
        self.Vehicle_category_desc = desc
        self.Vehicle_category_daily_parking_fee = fee

    def __repr__(self):
        return str(self.Vehicle_category_id)


@login_manager.user_loader
def get_user(ident):
    return Login.query.get(int(ident))


@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    user = Login.query.filter_by(Login_username=username).first()
    return user if user else None
