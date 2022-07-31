from django.db import models
from django.utils.timezone import now
from django.conf import settings

User = settings.AUTH_USER_MODEL
class NWP(models.Model):
    user = models.ForeignKey(User, blank=True, null=True,on_delete=models.SET_NULL)
    object_id = models.AutoField(primary_key=True,null=False)
    sentence = models.CharField(max_length = 5000)
    predicted = models.TextField(null=True)
    created = models.DateTimeField(default=now)
    selected = models.TextField(null=True)

    def __str__(self):
        return f"{self.user} wrote {self.sentence} at {self.created} and the model predicted - {self.predicted}"