# Generated by Django 2.2.3 on 2019-08-01 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_auto_20190731_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='payment',
            field=models.CharField(choices=[('cs', 'CASH'), ('ca', 'CREDIT|DEBIT CARD')], max_length=2),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('In', 'IN'), ('Out', 'OUT')], default='re', max_length=4),
        ),
    ]
