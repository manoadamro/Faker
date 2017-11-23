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

    data = [
        {
          "reading_timestamp": "2017-09-30T08:30:51.620Z",
          "blood_glucose_value": 8.2,
          "reading_meal_id": 0,
          "prandial_tag": "before_breakfast"
          "reading_notes": models.array_of(note, count=1),
          "reading_id": "fbf60c03-66f7-4320-a39c-8b83e950dfe4",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-30T09:30:21.440Z",
          "blood_glucose_value": 8.5,
          "reading_meal_id": 1,
          "prandial_tag": "after_breakfast"
          "reading_notes": models.array_of(note, count=1),
          "reading_id": "425f4d00-16f5-445f-bfe8-3345580738e4",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-29T07:40:44.110Z",
          "blood_glucose_value": 7,
          "reading_meal_id": 0,
          "prandial_tag": "before_breakfast"
          "reading_notes": []
          "reading_id": "eabe05a3-077f-4b3c-85cb-5bc68c2f934d",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-29T09:20:17.020Z",
          "blood_glucose_value": 8.4,
          "reading_meal_id": 1,
          "prandial_tag": "after_breakfast"
          "reading_notes": models.array_of(note, count=1),
          "reading_id": "a5bef158-0646-470a-914d-cbc8dbe2006f",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-29T11:55:14.079Z",
          "blood_glucose_value": 7.2,
          "reading_meal_id": 2,
          "prandial_tag": "before_lunch"
          "reading_notes": [],
          "reading_id": "ef534c20-24bf-4c65-99e2-293e7c971155",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-29T13:32:31.820Z",
          "blood_glucose_value": 7.1,
          "reading_meal_id": 3,
          "prandial_tag": "after_lunch"
          "reading_notes": models.array_of(note, count=1),
          "reading_id": "f58587da-17c0-4539-9b89-84c9a8fa7c4b",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-29T17:20:21.412Z",
          "blood_glucose_value": 6.9,
          "reading_meal_id": 4,
          "prandial_tag": "before_dinner"
          "reading_notes": [],
          "reading_id": "d1b00524-42e0-4adf-8e98-a7624cb08a88",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-29T18:50:44.311Z",
          "blood_glucose_value": 7,
          "reading_meal_id": 5,
          "prandial_tag": "after_dinner"
          "reading_notes": [],
          "reading_id": "de3fa67f-415e-494d-ab07-482fa71fba95",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-28T09:45:22.870Z",
          "blood_glucose_value": 7.1,
          "reading_meal_id": 0,
          "prandial_tag": "before_breakfast"
          "reading_notes": models.array_of(note, count=1),
          "reading_id": "4964dab1-676b-4c5b-ac03-1567c4214c2b",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-28T11:02:44.879Z",
          "blood_glucose_value": 6.9,
          "reading_meal_id": 1,
          "prandial_tag": "after_breakfast"
          "reading_notes": models.array_of(note, count=1),
          "reading_id": "a1bff4ab-72d6-4b33-88eb-7075dadb6b81",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-28T12:52:41.100Z",
          "blood_glucose_value": 7.2,
          "reading_meal_id": 2,
          "prandial_tag": "before_lunch"
          "reading_notes": [],
          "reading_id": "a93b2317-3d85-4aaf-b32a-66a397d5df21",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-28T13:24:21.412Z",
          "blood_glucose_value": 7,
          "reading_meal_id": 3,
          "prandial_tag": "after_lunch"
          "reading_notes": models.array_of(note, count=1),
          "reading_id": "a8b1e612-6ed6-4326-bde2-7b328740c7d4",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-28T18:02:22.666Z",
          "blood_glucose_value": 6.9,
          "reading_meal_id": 4,
          "prandial_tag": "before_dinner"
          "reading_notes": models.array_of(note, count=1),
          "reading_id": "c1ac39f6-6f68-4ae4-81e9-470cce57c411",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-28T18:52:22.666Z",
          "blood_glucose_value": 6.9,
          "reading_meal_id": 5,
          "prandial_tag": "after_dinner"
          "reading_notes": [],
          "reading_id": "c1ac39f6-6f68-4ae4-81e9-470cce57c411",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-27T08:25:11.101Z",
          "blood_glucose_value": 7.1,
          "reading_meal_id": 0,
          "prandial_tag": "before_breakfast"
          "reading_notes": [],
          "reading_id": "27b19578-1b82-4996-b5c6-5c22fab0a3c5",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-27T08:55:23.170Z",
          "blood_glucose_value": 7,
          "reading_meal_id": 1,
          "prandial_tag": "after_breakfast"
          "reading_notes": [],
          "reading_id": "5a8126e0-e368-4d0a-b3fd-184c53faee38",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-27T12:50:32.049Z",
          "blood_glucose_value": 7,
          "reading_meal_id": 2,
          "prandial_tag": "before_lunch"
          "reading_notes": models.array_of(note, count=1),
          "reading_id": "6f33e86d-bf83-4d98-bf4e-bd06ed92313a",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-27T13:42:41.100Z",
          "blood_glucose_value": 7.2,
          "reading_meal_id": 3,
          "prandial_tag": "after_lunch"
          "reading_notes": models.array_of(note, count=1),
          "reading_id": "ac6ff93f-8746-43a1-a579-22891778456d",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-27T17:30:44.012Z",
          "blood_glucose_value": 7.1,
          "reading_meal_id": 4,
          "prandial_tag": "before_dinner"
          "reading_notes": [],
          "reading_id": "db4e2060-0308-4158-8369-9f99316998af",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-27T18:51:33.666Z",
          "blood_glucose_value": 8.2,
          "reading_meal_id": 5,
          "prandial_tag": "after_dinner"
          "reading_notes": [],
          "reading_id": "9289ef11-603b-43b1-833e-4cabd4e3c5cd",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-26T09:30:42.770Z",
          "blood_glucose_value": 7.3,
          "reading_meal_id": 0,
          "prandial_tag": "before_breakfast"
          "reading_notes": models.array_of(note, count=1),
          "reading_id": "b2531865-f663-46a8-a337-cd981e01a0ff",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-26T10:05:42.770Z",
          "blood_glucose_value": 7.3,
          "reading_meal_id": 1,
          "prandial_tag": "after_breakfast"
          "reading_notes": models.array_of(note, count=1),
          "reading_id": "b2531865-f663-46a8-a337-cd981e01a0ff",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-26T11:57:31.321Z",
          "blood_glucose_value": 8.2,
          "reading_meal_id": 2,
          "prandial_tag": "before_lunch"
          "reading_notes": [],
          "reading_id": "374dca42-1652-4e81-b90e-d70cd1bf0b81",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-26T13:12:55.220Z",
          "blood_glucose_value": 7.3,
          "reading_meal_id": 3,
          "prandial_tag": "after_lunch"
          "reading_notes": models.array_of(note, count=1),
          "reading_id": "786bbcc8-828b-4388-a3e0-dd15e344b9e1",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-26T17:22:35.552Z",
          "blood_glucose_value": 7.3,
          "reading_meal_id": 4,
          "prandial_tag": "before_dinner"
          "reading_notes": models.array_of(note, count=1),
          "reading_id": "c40596ef-c940-4667-9511-2e252a9bf7f0",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-26T18:55:11.312Z",
          "blood_glucose_value": 5.9,
          "reading_meal_id": 5,
          "prandial_tag": "after_dinner"
          "reading_notes": [],
          "reading_id": "8418e026-5859-4d7b-8467-8b0aaed3e3d5",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-25T08:12:09.111Z",
          "blood_glucose_value": 5.6,
          "reading_meal_id": 0,
          "prandial_tag": "before_breakfast"
          "reading_notes": [],
          "reading_id": "ddf8413f-a39a-433a-af43-09844e469a08",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-25T09:23:59.119Z",
          "blood_glucose_value": 7.1,
          "reading_meal_id": 1,
          "prandial_tag": "after_breakfast"
          "reading_notes": models.array_of(note, count=1),
          "reading_id": "f0cc3aa1-304c-4230-964b-2c5e06434cbf",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-25T11:54:23.111Z",
          "blood_glucose_value": 8.2,
          "reading_meal_id": 2,
          "prandial_tag": "before_lunch"
          "reading_notes": models.array_of(note, count=1),
          "reading_id": "5f3dee37-e11f-4fee-be06-1688538ae67b",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-25T13:08:41.100Z",
          "blood_glucose_value": 6.9,
          "reading_meal_id": 3,
          "prandial_tag": "after_lunch"
          "reading_notes": [],
          "reading_id": "6269f3a2-7a57-497c-8b28-9d9ac6c50872",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-25T17:35:01.001Z",
          "blood_glucose_value": 8.2,
          "reading_meal_id": 4,
          "prandial_tag": "before_dinner"
          "reading_notes": [],
          "reading_id": "77f41ecc-b6b0-4a3e-824f-4d4e5ded4e0c",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-25T19:12:33.431Z",
          "blood_glucose_value": 7.1,
          "reading_meal_id": 5,
          "prandial_tag": "after_dinner"
          "reading_notes": models.array_of(note, count=1),
          "reading_id": "b1504982-101b-4592-8477-ab7a3c720a48",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-24T08:34:09.121Z",
          "blood_glucose_value": 8.2,
          "reading_meal_id": 0,
          "prandial_tag": "before_breakfast"
          "reading_notes": [],
          "reading_id": "903a11b7-c251-4121-96db-cdd24fe832c2",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-24T08:56:44.120Z",
          "blood_glucose_value": 8.2,
          "reading_meal_id": 1,
          "prandial_tag": "after_breakfast"
          "reading_notes": models.array_of(note, count=1),
          "reading_id": "3256db8f-db93-4211-8958-75ca379548e3",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-24T13:01:05.009Z",
          "blood_glucose_value": 7.2,
          "reading_meal_id": 2,
          "prandial_tag": "before_lunch"
          "reading_notes": [],
          "reading_id": "c98621c7-bcf2-415e-95e9-6d5f55debfda",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-24T14:30:21.100Z",
          "blood_glucose_value": 8,
          "reading_meal_id": 3,
          "prandial_tag": "after_lunch"
          "reading_notes": [],
          "reading_id": "7a709654-bb05-4e5a-aef5-3f8e53e30f12",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-24T17:26:19.832Z",
          "blood_glucose_value": 6.9,
          "reading_meal_id": 4,
          "prandial_tag": "before_dinner"
          "reading_notes": [],
          "reading_id": "2bde73b0-43ff-4b35-8538-f67471986518",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-24T19:14:33.986Z",
          "blood_glucose_value": 7.3,
          "reading_meal_id": 5,
          "prandial_tag": "after_dinner"
          "reading_notes": models.array_of(note, count=1),
          "reading_id": "c085a0f3-06c5-48a5-ad12-8ccf0edd7966",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-23T08:34:09.121Z",
          "blood_glucose_value": 7.2,
          "reading_meal_id": 0,
          "prandial_tag": "before_breakfast"
          "reading_notes": models.array_of(note, count=1),
          "reading_id": "bcf75e62-7755-4d06-bca1-b6e3002d9634",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-23T08:55:11.963Z",
          "blood_glucose_value": 7,
          "reading_meal_id": 1,
          "prandial_tag": "after_breakfast"
          "reading_notes": models.array_of(note, count=1),
          "reading_id": "8c68d9df-7a0d-41c7-ad8f-df66d2ee5d03",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-23T12:29:19.331Z",
          "blood_glucose_value": 7.1,
          "reading_meal_id": 2,
          "prandial_tag": "before_lunch"
          "reading_notes": models.array_of(note, count=1),
          "reading_id": "06f36fe0-48a6-4e6f-a190-e133fe2fb65b",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-23T14:01:05.009Z",
          "blood_glucose_value": 7.2,
          "reading_meal_id": 3,
          "prandial_tag": "after_lunch"
          "reading_notes": [],
          "reading_id": "57049044-6783-43a4-9d56-064c1244821d",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-23T17:30:21.100Z",
          "blood_glucose_value": 8,
          "reading_meal_id": 4,
          "prandial_tag": "before_dinner"
          "reading_notes": [],
          "reading_id": "940ca602-1737-45ae-8d3f-8499a8c44c9b",
          "reading_metadata": models.reading_metadata()
        },
        {
          "reading_timestamp": "2017-09-23T18:26:19.832Z",
          "blood_glucose_value": 6.9,
          "reading_meal_id": 5,
          "prandial_tag": "after_dinner"
          "reading_notes": [],
          "reading_id": "940ca602-1737-45ae-8d3f-8499a8c44c9b",
          "reading_metadata": models.reading_metadata()
        }
    ]
    return jsonify(data)

app.run()
