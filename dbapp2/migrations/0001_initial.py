# Generated by Django 3.1.7 on 2021-04-29 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
                ('desc', models.CharField(max_length=600)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Source', models.CharField(max_length=255)),
                ('destination', models.CharField(max_length=255)),
                ('Date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Train_No', models.IntegerField()),
                ('Train_Source', models.CharField(max_length=255)),
                ('Train_Destination', models.CharField(max_length=255)),
                ('Train_Name', models.CharField(max_length=255)),
                ('Train_Type', models.CharField(max_length=255)),
                ('Arrival_Type', models.CharField(max_length=255)),
                ('Departure_Time', models.CharField(max_length=255)),
            ],
        ),
    ]
