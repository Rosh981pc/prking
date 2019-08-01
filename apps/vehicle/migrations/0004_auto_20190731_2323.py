# Generated by Django 2.2.3 on 2019-08-01 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0003_remove_vehicle_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='park',
            name='floor',
        ),
        migrations.RemoveField(
            model_name='park',
            name='parking_spot',
        ),
        migrations.RemoveField(
            model_name='vehicletype',
            name='description',
        ),
        migrations.AddField(
            model_name='park',
            name='parkingspace',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15')], default=0, max_length=4),
            preserve_default=False,
        ),
    ]
