from django.db import models
from colorfield.fields import ColorField


class Organization(models.Model):
    name = models.CharField(max_length=256, unique=True, primary_key=True)
    first_ribbon = models.ForeignKey('Ribbon', on_delete=models.PROTECT, null=True, blank=True, related_name='first')
    second_ribbon = models.ForeignKey('Ribbon', on_delete=models.PROTECT, null=True, blank=True,  related_name='second')
    third_ribbon = models.ForeignKey('Ribbon', on_delete=models.PROTECT, null=True, blank=True,  related_name='third')
    fourth_ribbon = models.ForeignKey('Ribbon', on_delete=models.PROTECT, null=True, blank=True,  related_name='fourth')
    fifth_ribbon = models.ForeignKey('Ribbon', on_delete=models.PROTECT, null=True, blank=True,  related_name='fifth')

    @property
    def score(self):
        score = 0
        for attendee in Attendee.objects.filter(organization=self):
            if attendee.enabled:
                for transaction in Transaction.objects.filter(owner=attendee):
                    score += transaction.amount
        return score

    def getSVG(self):
        WIDTH = 9999
        HEIGHT = 150
        start = '<svg width="{}" height="{}" class="flag">'.format(WIDTH, HEIGHT)
        end = '</svg>'
        ribbons = [self.first_ribbon, self.second_ribbon, self.third_ribbon, self.fourth_ribbon, self.fifth_ribbon]
        elements = []
        ypos = 0
        for ribbon in ribbons:
            if ribbon is not None:
                base = '<rect y="{y:d}" width="{width}" height="{height:d}" style="fill:{color}" />'
                height = int(HEIGHT * ribbon.weight)
                elements.append(base.format(y=ypos, height=height, color=ribbon.color, width=WIDTH))
                ypos += height

        return start + '\n'.join(elements) + end

class Ribbon(models.Model):
    name = models.CharField(max_length=256, primary_key=True)
    color = ColorField(default='#FFFFFF')
    weight = models.DecimalField(max_digits=5, decimal_places=4, default=1)

class Attendee(models.Model):
    name = models.CharField(max_length=256, unique=True, primary_key=True)
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

class Item(models.Model):
    name = models.CharField(max_length=256, primary_key=True)
    type = models.ForeignKey(ItemType, on_delete=models.PROTECT)

class Transaction(models.Model):
    owner = models.ForeignKey(Attendee, on_delete=models.PROTECT)
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    amount = models.IntegerField()
    # use personal_amount to seperate bought and consumed Items
    personal_amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=1024, blank=True)
