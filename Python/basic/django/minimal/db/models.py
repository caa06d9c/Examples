from django.db import models


class Entry(models.Model):
    value = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.value
