# Generated by Django 3.2.4 on 2021-07-08 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_quotes'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotes',
            name='queero',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.queero'),
            preserve_default=False,
        ),
    ]