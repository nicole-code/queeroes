# Generated by Django 3.2.4 on 2021-07-08 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_remove_queero_quotes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.TextField(max_length=2000)),
            ],
        ),
    ]
