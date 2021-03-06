# Generated by Django 2.2.3 on 2020-04-15 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20200415_0259'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('item_order', models.CharField(max_length=1000, null=True, verbose_name='Cart Item')),
                ('date_order', models.DateTimeField(auto_now_add=True, verbose_name='date join')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='price of product')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_id', to='shop.UserProfile')),
            ],
        ),
    ]
