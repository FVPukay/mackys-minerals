import json
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mineral_catalog.settings')

import django
django.setup()

from minerals_app.models import Mineral

def populate():
    with open('minerals.json') as file:
        file = json.loads(file.read())

    for mineral in file:
        mineral_entry = Mineral.objects.get_or_create(**mineral)

if __name__ == '__main__':
    print('Populating database')
    populate()
    print('Database populating complete')
