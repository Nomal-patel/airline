# Generated by Django 4.1.5 on 2023-05-09 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_airport_alter_flight_destination_alter_flight_origin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='destination',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='flight',
            name='origin',
            field=models.CharField(max_length=64),
        ),
        migrations.DeleteModel(
            name='Airport',
        ),
    ]
