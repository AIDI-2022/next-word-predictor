from django.db import models
from django.utils.timezone import now
class NWP(models.Model):
    object_id = models.AutoField(primary_key=True)
    sentence = models.CharField(max_length = 5000)
    predicted = models.TextField(null=True)
    created = models.DateTimeField(default=now)

    def __str__(self):
        return self.sentence