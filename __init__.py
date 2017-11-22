from generator import Generator
from pprint import pprint

GEN = Generator()

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

def medication():
    return GEN.dict(
        identifier=identifier(),
        name='medicine_name'
)

def note():
    return GEN.dict(
        identifier=identifier(),
        creator=identifier(),
        content='text'
    )

def array_of(method, count=5):
    array = [method() for i in range(0, count)]
    return array

# pprint(identifier())
pprint(array_of(user))
