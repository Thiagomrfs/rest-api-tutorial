# Generated by Django 4.0.1 on 2022-09-03 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=80)),
                ('priority', models.CharField(choices=[('B', 'Baixa'), ('M', 'Media'), ('A', 'Alta')], max_length=1)),
            ],
        ),
    ]