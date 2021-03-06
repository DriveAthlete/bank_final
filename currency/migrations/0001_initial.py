# Generated by Django 3.0.3 on 2020-03-02 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.IntegerField(choices=[(1, 'EUR'), (2, 'USD'), (3, 'GPB'), (4, 'RUB'), (5, 'BTC')], verbose_name='Currency')),
                ('value', models.FloatField(verbose_name='Value')),
            ],
        ),
    ]
