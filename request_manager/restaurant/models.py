from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return "%s" % self.name

