# Generated by Django 2.2.1 on 2019-11-04 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20191104_1118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentaires',
            name='pseudo',
        ),
    ]
