from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=256, unique=True)
    pass

class Attendee(models.Model):
    name = models.CharField(max_length=256, unique=True)
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT)
    # if this attendee is currently frozen (frozen means no changes to this account can occur)
    frozen = models.BooleanField(default=False)
    # if the transaction of this member should count for his organization
    enabled = models.BooleanField(default=True)
    pass

# for identification purposes
class Tag(models.Model):
    # TODO add the id method
    attendee = models.ForeignKey(Attendee, on_delete=models.PROTECT)
    comment = models.CharField(max_length=1024, blank=True)
    pass

# to group items
class ItemType(models.Model):
    name = models.CharField(max_length=256, primary_key=True)
    pass

class Item(models.Model):
    name = models.CharField(max_length=256, primary_key=True)
    pass

class Transaction(models.Model):
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    amount = models.IntegerField()
    # use personal_amount to seperate bought and consumed Items
    personal_amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=1024, blank=True)
