# Generated by Django 3.1.7 on 2021-03-14 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_item_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendee',
            name='token',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
