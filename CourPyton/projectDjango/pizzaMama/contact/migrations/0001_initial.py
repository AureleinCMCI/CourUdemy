# Generated by Django 5.2.1 on 2025-05-21 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('prenom', models.CharField(max_length=400)),
                ('email', models.CharField(max_length=400)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
