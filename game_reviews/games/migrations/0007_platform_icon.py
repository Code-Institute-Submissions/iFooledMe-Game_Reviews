# Generated by Django 3.1 on 2020-08-06 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_auto_20200804_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='platform',
            name='icon',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
