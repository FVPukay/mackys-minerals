import random
from minerals_app.models import Mineral

def random_pk(request):
    return {'random_pk': int(random.random() * int(Mineral.objects.count()) + 1)}
