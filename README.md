# Faker
creates fake data


# To Start Server
```shell
  python3 Faker
```

```
http://localhost:5000/v1
  /dhos-auditentries
  /dhos-clinician/<clinician_id>
  /dhos-locations/
  /dhos-location/<location_id>/users
  /dhos-location/<location_id>/clinician/<clinician_id>/users
  /dhos-notifications/<to_id>
  /dhos-users/user/<user_id>
  /gdm-patienthistory/<user_id>
  /gdm-dose/<reading_id>
  /gdm-readings/<user_id>
```


### Returning an array

endpoints that return an array will return 5 items by default, this can be overridden in the relevant method in the controller (\_\_main\_\_.py).

eg:
```python
  return jsonify(models.array_of(models.notification))
  # returns 5 elements
```

```python
  return jsonify(models.array_of(models.notification, count=3))
  # returns 3 elements
```
