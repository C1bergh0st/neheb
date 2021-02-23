# Generated by Django 3.1.7 on 2021-02-22 23:34

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_transaction_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ribbon',
            fields=[
                ('color', colorfield.fields.ColorField(default='#FFFFFF', max_length=18, primary_key=True, serialize=False)),
                ('weight', models.DecimalField(decimal_places=4, default=1, max_digits=5)),
            ],
        ),
        migrations.AddField(
            model_name='organization',
            name='fifth_ribbon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='fifth', to='core.ribbon'),
        ),
        migrations.AddField(
            model_name='organization',
            name='first_ribbon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='first', to='core.ribbon'),
        ),
        migrations.AddField(
            model_name='organization',
            name='fourth_ribbon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='fourth', to='core.ribbon'),
        ),
        migrations.AddField(
            model_name='organization',
            name='second_ribbon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='second', to='core.ribbon'),
        ),
        migrations.AddField(
            model_name='organization',
            name='third_ribbon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='third', to='core.ribbon'),
        ),
    ]