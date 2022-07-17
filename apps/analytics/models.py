# analytics.models.py

from django.conf import settings
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from apps.analytics.mixins import ObjectViewMixin
from apps.analytics.utils import get_client_ip
from .signals import  object_viewed_signal

User = settings.AUTH_USER_MODEL

class ObjectViewed(models.Model):
    user            = models.ForeignKey(User, blank=True, null=True,on_delete=models.SET_NULL)
    content_type    = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True)
    object_id       = models.PositiveIntegerField()
    ip_address      = models.CharField(max_length=120, blank=True, null=True)
    content_object  = GenericForeignKey('content_type', 'object_id')
    timestamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self, ):
        return "%s viewed: %s" %(self.content_object, self.timestamp)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Object Viewed'
        verbose_name_plural = 'Objects Viewed'

#class ObjectViewed(models.Model):
    
    #class ProductDetailView(ObjectViewMixin, DetailView):
        #model = Product

def object_viewed_receiver(sender, instance, request, *args, **kwargs):
    c_type = ContentType.objects.get_for_model(sender)
    ip_address = None
    try:
        ip_address = get_client_ip(request)
    except:
        pass
    new_view_instance = ObjectViewed.objects.create(
                user=request.user, 
                content_type=c_type,
                object_id=instance.id,
                ip_address=ip_address
                )

object_viewed_signal.connect(object_viewed_receiver)