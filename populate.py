import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'paginationProject.settings')

import django

django.setup()

from testapp.models import Witness

from random import *

from faker import Faker

fake = Faker()

def populate(n):
    for i in range(n):
        




n = int(input("Enter how many records to insert : "))

print(f'{n} Record Inserted Successfully ')


populate(n)