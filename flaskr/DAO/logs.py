# TODO REFACTOR AS DISCUSSED VENKAT
from flaskr.models import db, Logs, Users, Aircrafts, CategoryEnum, CertificateEnum, Ratings


def createLogs(**kwargs):
    newLog = Logs(
        sic_time=kwargs.get('sic_time', None),
        total_time=kwargs.get('total_time', None),
        pic_time=kwargs.get('pic_time', None),
        date=kwargs.get('date', None),
        night_time=kwargs.get('night_time', None),
        day_time=kwargs.get('day_time', None),
        xc_time=kwargs.get('xc_time', None),
        dual_received=kwargs.get('dual_received', None),
        dual_given=kwargs.get('dual_given', None),
        actual_instrument=kwargs.get('actual_instrument', None),
        simulated_instrument=kwargs.get('simulated_instrument', None),
        departure=kwargs.get('departure', None),
        destination=kwargs.get('destination', None),
        via=kwargs.get('via', None),
        day_landings=kwargs.get('day_landings', None),
        night_landings=kwargs.get('night_landings', None),
        num_instrument_approaches=kwargs.get('num_instrument_approaches', None),
        remarks=kwargs.get('remarks', None),
        user_id=kwargs.get('user_id', None),
        aircraft_id=kwargs.get('aircraft_id', None),
        created=kwargs.get('created', None),
        updated=kwargs.get('updated', None)
    )

    db.session.add(newLog)
    db.session.commit()


def updateLogs(params):
    return -1


def findLogsById(id):
    obj = db.session.query(Logs).get(id)
    return obj


def findAllLogs():
    obj = db.session.query(Logs).all()
    return obj


def deleteLogs(id):
    obj = db.session.query.get(id)
    db.session.delete(obj)
    db.session.commit()
