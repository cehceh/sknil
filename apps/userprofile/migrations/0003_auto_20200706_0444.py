# Generated by Django 3.0.6 on 2020-07-06 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_userprofile_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='subscription',
            field=models.CharField(default='', max_length=100),
        ),
    ]