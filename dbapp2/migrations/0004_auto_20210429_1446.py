# Generated by Django 3.1.7 on 2021-04-29 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbapp2', '0003_contact_locations_train'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Locations',
        ),
        migrations.DeleteModel(
            name='Train',
        ),
    ]