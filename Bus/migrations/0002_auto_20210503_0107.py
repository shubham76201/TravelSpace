# Generated by Django 3.0.7 on 2021-05-02 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='nos',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bus',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bus',
            name='rem',
            field=models.IntegerField(),
        ),
    ]