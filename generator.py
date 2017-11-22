from faker import Faker as FakerBase
from types import Types

from random import choice
from json import dumps

class Generator(Types):

    base = FakerBase('en_GB')

    def _resolve(self, name):
        if hasattr(self.base, name):
            return getattr(self.base, name)()
        else:
            method = getattr(self, name)
            if callable(method):
                return method()
            else:
                return choice(method)

    def __call__(self, name):
        if name is None or isinstance(name, dict): return name
        item = self._resolve(name)
        if not isinstance(item, (int, float, bool)) and item is not None:
            return str(item)
        else:
            return item

    def list(self, *attrs):
        '''
        f.list('name', 'address', 'medicine', 'units')
        # Rachel Jones
        # Unit 4389 Box 5768
        # DPO AP 92072-9929
        # codeine
        # mmol/l
        '''
        return [self(i) for i in attrs]

    def dict(self, **attrs):
        '''
        f.dict(some_name='name', some_address='address')
        # {'some_address': '337 Kimberly Drives Suite 567\n'
        #                  'South Stephanie, SC 30383-6482',
        #  'some_name': 'Isaiah White'}
        '''
        d = {}
        for attr in attrs: d[attr] = self(attrs[attr])
        return d
    #
    # def json(self, **attrs):
    #     '''
    #     f.json(some_name='name', some_address='address')
    #     # ('{"some_name": "William House", "some_address": "862 Jose '
    #     #  'Mills\\nJohnnymouth, AK 08515-2330"}')
    #     '''
    #     return dumps(self.dict(**attrs))
