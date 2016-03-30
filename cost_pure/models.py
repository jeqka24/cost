# coding: utf-8
# Create your models here.
from django.db.models import Model, ManyToManyField, ForeignKey, IntegerField, FloatField, DateTimeField, CharField


class Invoice(Model):
    name = CharField(max_length=120)
    total = FloatField()
    datetime = DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Tag(Model):
    name = CharField(max_length=64)

    def __str__(self):
        return self.name


class Position(Model):
    """
    Part of the cost, one piece of full cost.
    Consists of:
    name - Name of position
    """
    invoice_id = ForeignKey(to=Invoice)
    name = CharField(max_length=120)
    cost = FloatField()
    tags = ManyToManyField(Tag)

    def __str__(self):
        return self.name
