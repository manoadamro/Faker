# Faker
creates fake data


### To Start Server
```shell
  python3 Faker
```


### Arrays

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


### End Points
```
http://localhost:5000/v1

  # gets a list of audit entries (array)
  /dhos-auditentries          
  
  # gets a single clinician by id (object)
  /dhos-clinician/<clinician_id>
  
  # gets all locations (array)
  /dhos-locations/
  
  # gets all users at a specified location (array)
  /dhos-location/<location_id>/users
  
  # gets all patients for a specified clinician at a specified location (array)
  /dhos-location/<location_id>/clinician/<clinician_id>/users
   
  # gets all notifications for a specified recipient (array)
  /dhos-notifications/<to_id>
  
  # gets a specified user (object)
  /dhos-users/user/<user_id>
  
  # gets the patient history for a specified user (object)
  /gdm-patienthistory/<user_id>
  
  # gets the dose information for a specified reading (object)
  /gdm-dose/<reading_id>
  
  # gets all readings for a specified user (array)
  /gdm-readings/<user_id>
```
