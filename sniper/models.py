from django.db import models

from django.contrib.auth.models import User

class CLSniper(models.Model):
    owner = models.ForeignKey(User, unique=False)
    site = models.TextField(max_length=30, null=False, blank=False)
    query = models.TextField(max_length=140, null=False, blank=False)
    min_price = models.IntegerField(null=True, blank=True)
    max_price = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=True)
    search_titles = models.BooleanField(default=False)

    def _get_num_hits(self):
        return Hit.objects.filter(sniper=self).count()
    num_hits = property(_get_num_hits)

    def _get_hits(self):
        return Hit.objects.filter(sniper=self)
    hits = property(_get_hits)

    def __unicode__(self):
        return self.owner.username+' | '+self.site+' | '+self.query

class Hit(models.Model):
    sniper = models.ForeignKey(CLSniper, unique=False)
    post_name = models.TextField()
    price = models.IntegerField()
    url = models.URLField()
    post_id = models.TextField()
    date = models.DateTimeField()

    def __unicode__(self):
        return unicode(self.post_name)

