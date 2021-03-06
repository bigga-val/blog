# Generated by Django 2.2.1 on 2019-10-26 08:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_users_last_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentaires',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='commentaires',
            name='pseudo',
            field=models.CharField(default='anonyme', max_length=20, null=True),
        ),
    ]
