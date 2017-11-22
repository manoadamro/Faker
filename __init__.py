from datafaker import Faker

FAKER = Faker()

def identity():
    return FAKER.dict(
        uuid='uuid4',
        uri='uri',
        created='date_time_ad',
        modified='date_time_ad'
    )

pprint(identity())
