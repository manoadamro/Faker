import models
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/v1/dhos-auditentries')
def auditentries():
    return jsonify(models.array_of(models.audit_entry))

@app.route('/v1/dhos-clinician/<clinician_id>')
def clinician(clinician_id=None):
    assert clinician_id is not None, 'no clinician id was provided'
    return jsonify(models.clinician())

@app.route('/v1/dhos-locations/')
def locations():
    return jsonify(models.array_of(models.location))

@app.route('/v1/dhos-location/<location_id>/users')
def location_users(location_id=None):
    assert location_id is not None, 'no location id was provided'
    return jsonify(models.array_of(models.location))

@app.route('/v1/dhos-location/<location_id>/clinician/<clinician_id>/users')
def users_for_clinician_at_location(location_id=None, clinician_id=None):
    assert location_id is not None, 'no location id was provided'
    assert clinician_id is not None, 'no clinician id was provided'
    return jsonify(models.array_of(models.user))

@app.route('/v1/dhos-notifications/<to_id>')
def notifications(to_id=None):
    assert to_id is not None, 'no \'to id\' was provided'
    return jsonify(models.array_of(models.notification))

@app.route('/v1/dhos-users/user/<user_id>')
def user(user_id=None):
    assert user_id is not None, 'no user id was provided'
    return jsonify(models.user())

@app.route('/v1/gdm-patienthistory/<user_id>')
def patient_history(user_id=None):
    assert user_id is not None, 'no user id was provided'
    return jsonify(models.patient_history())

@app.route('/v1/gdm-dose/<reading_id>')
def dose(reading_id=None):
    assert reading_id is not None, 'no reading id was provided'
    return jsonify(models.dose())

@app.route('/v1/gdm-readings/<user_id>')
def readings(user_id=None):
    assert user_id is not None, 'no user id was provided'
    return jsonify(models.array_of(models.reading))

app.run()
