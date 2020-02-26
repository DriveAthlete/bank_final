# Generated by Django 3.0.3 on 2020-02-26 07:38

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True, verbose_name='Email')),
                ('currency', models.IntegerField(choices=[(1, 'EUR'), (2, 'USD'), (3, 'GPB'), (4, 'RUB'), (5, 'BTC')], verbose_name='Currency')),
                ('money', models.IntegerField(verbose_name='Money')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
