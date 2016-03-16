from __future__ import unicode_literals
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

#Store Model
## Store model will contain many Items
class Store(models.Model):
    name = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=1000, default='')

    class Meta:
        ordering = ('name',)

class Item(models.Model):
    name = models.CharField(max_length=100, default='')
    comments = models.CharField(max_length=100, default='')
    expired = models.BooleanField(default=False)
    expiration = models.DateTimeField(default='')
    store = models.ForeignKey(Store, related_name='items', default=0)  

    class Meta:
        ordering = ('expiration',)

    def __unicode__(self):
        return '%d: %s' % (self.expiration, self.name)