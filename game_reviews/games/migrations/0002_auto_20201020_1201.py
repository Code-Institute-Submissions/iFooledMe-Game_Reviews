# Generated by Django 3.1.2 on 2020-10-20 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genretag',
            name='show_name',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]