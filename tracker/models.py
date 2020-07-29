from django.db import models


# Create your models here.
class Track(models.Model):
    name = models.CharField(max_length=30)
    unit = models.CharField(max_length=30)
    description = models.CharField(max_length=300)

    def __str__(self):
        return "{%s, %s, %s}" % (self.name, self.unit, self.description)

    def __repr__(self):
        return "Track{name=%s, unit=%s, description=%s}" % (self.name, self.unit, self.description)


class Record(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    value = models.FloatField(default=0.0)
    date = models.DateTimeField('date published')

    def __str__(self):
        return "{%s}" % (self.value)
