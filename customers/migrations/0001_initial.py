# Generated by Django 3.1.5 on 2021-01-29 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('account_balance', models.FloatField(default=0.0)),
                ('purchases', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0)),
                ('item', models.CharField(max_length=150)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='customers.customer')),
            ],
        ),
    ]
