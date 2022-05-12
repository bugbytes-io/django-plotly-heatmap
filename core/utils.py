import hashlib
import random
import string
from django.utils import timezone

def generate_hash():
    hash_str = ''.join(random.choices(string.ascii_letters, k=6))
    return hashlib.sha1(hash_str.encode()).hexdigest()

def date_range(start, end):
    delta = end - start
    dates = []
    for i in range(delta.days):
        dates.append(start + timezone.timedelta(days=i))
    return dates