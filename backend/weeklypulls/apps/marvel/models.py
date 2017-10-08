import json
from django.db import models


class ApiCache(models.Model):
    key = models.TextField(primary_key=True)
    value = models.TextField()


class DjangoCache():
    def get(self, key):
        try:
            x = ApiCache.objects.get(key=key)
            return json.loads(x.value)
        except:
            return None

    def store(self, key, value):
        print('Storing!')
        ApiCache.objects.create(key=key, value=json.dumps(value))
        return value
