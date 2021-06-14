from django.db import models

class OneTimeLinkModel(models.Model):
    one_time_code = models.CharField(max_length=20)
    expiry_time = models.DateTimeField(auto_now_add=True, blank=True)
