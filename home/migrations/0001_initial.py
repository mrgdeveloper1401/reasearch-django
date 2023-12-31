# Generated by Django 4.2.6 on 2023-10-25 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='MySkillModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('create_at', models.DateTimeField(blank=True, null=True, verbose_name='create skill')),
            ],
            options={
                'verbose_name': 'skill',
                'verbose_name_plural': 'skills',
                'db_table': 'skill',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateTimeField(blank=True, null=True, verbose_name='date_joined')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='home.group')),
                ('peson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='persons', to='home.person')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(blank=True, through='home.Membership', to='home.person'),
        ),
    ]
