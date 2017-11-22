from generator import Generator
from pprint import pprint

GEN = Generator()


def array_of(method, count=5):
    array = [method() for i in range(0, count)]
    return array


def identifier():
    return GEN.dict(
        uuid='uuid4',
        uri='uri',
        created='date_time_ad',
        modified='date_time_ad'
    )

def address():
    return GEN.dict(
        address_line_1='building_number',
        address_line_2='street_name',
        address_line_3=None,
        address_line_4=None,
        locality='city',
        region=None,
        postcode='postcode',
        country='override_country'
    )

def location():
    return GEN.dict(
        identifier=identifier(),
        location_type='location_type',
        display_name='user_name',
        address=address(),
        parent=identifier(),
        children=array_of(identifier, count=2)
    )

def personal_address():
    return GEN.dict(
        address=address(),
        lived_from='date',
        lived_until='date',
        status='boolean'
    )

def user():
    return GEN.dict(
        identifier=identifier(),
        first_name='first_name_female',
        last_name='last_name_female',
        dob='date',
        phone_number='phone_number',
        address=personal_address(),
        nhs_number='random_number',
        email_address='email',
        ethnicity='ethnicity',
        sex='sex',
        gender='gender'
    )

def clinician():
    return GEN.dict(
        identifier=identifier(),
        first_name='first_name_female',
        last_name='last_name_female',
        clinician_type='clinician_type',
        phone_number='phone_number',
        email_address='email',
        nhs_smartcard_number='random_number'
)

def note():
    return GEN.dict(
        identifier=identifier(),
        creator=identifier(),
        content='text'
    )

def reading_metadata():
    return GEN.dict(
        meter_id=identifier(),
        meter_serial='md5'
    )

def reading():
    return GEN.dict(
        identifier=identifier(),
        timestamp='date_time',
        blood_glucose_value='random_digit',
        units='units',
        prandial_tag='prandial_tag',
        notes=array_of(note),
        reading_metadata=reading_metadata()
    )

def notification():
    return GEN.dict(
        identifier=identifier(),
        notification_timestamp='date_time',
        from_id=identifier(),
        to_id=identifier(),
        message_type_id='message_type',
        message_content='text',
        status='boolean'
    )

def Medication():
    return GEN.dict(
        identifier=identifier(),
        name='medicine'
    )


# pprint(identifier())

pprint(location())
