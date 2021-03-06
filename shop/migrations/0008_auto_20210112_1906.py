# Generated by Django 2.2.3 on 2021-01-12 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_vtu_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='vtu_transaction',
            name='transaction_time',
            field=models.CharField(max_length=100, null=True, verbose_name='transaction time'),
        ),
        migrations.AlterField(
            model_name='vtu_transaction',
            name='phone',
            field=models.CharField(max_length=100, null=True, verbose_name='phone number credited'),
        ),
        migrations.AlterField(
            model_name='vtu_transaction',
            name='ref_id',
            field=models.CharField(max_length=100, verbose_name='reference number'),
        ),
    ]
