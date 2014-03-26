from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    mark = models.DecimalField(max_digits=10, decimal_places=5)
    voters = models.IntegerField(default=0)
    categories = models.ManyToManyField(Category, blank=True)

    def __unicode__(self):
        return self.name

class Opinion(models.Model):
    product = models.ForeignKey(Product)
    login = models.CharField(max_length=64)
    text = models.CharField(max_length=512)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.text

    @classmethod
    def create(cls):
        opinion = cls()
        return opinion