# Generated by Django 3.1 on 2020-08-24 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userprofile_is_premium'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCommentsScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.userprofile')),
            ],
        ),
    ]
