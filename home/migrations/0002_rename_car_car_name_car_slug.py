# Generated by Django 4.2.6 on 2023-10-21 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='car',
            new_name='name',
        ),
        migrations.AddField(
            model_name='car',
            name='slug',
            field=models.SlugField(default=0),
            preserve_default=False,
        ),
    ]
