# Generated by Django 3.1.7 on 2021-03-14 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_attendee_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='token',
            field=models.CharField(blank=True, default='token', max_length=256),
            preserve_default=False,
        ),
    ]
