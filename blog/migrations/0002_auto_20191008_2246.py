# Generated by Django 2.2.1 on 2019-10-08 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='categorie',
        ),
        migrations.AddField(
            model_name='articles',
            name='categorie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='blog.Categories'),
        ),
    ]