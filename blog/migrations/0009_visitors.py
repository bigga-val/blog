# Generated by Django 2.2.1 on 2019-12-20 17:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20191106_2128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('page_visited', models.TextField()),
                ('date_visite', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
