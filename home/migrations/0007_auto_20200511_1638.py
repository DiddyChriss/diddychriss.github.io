# Generated by Django 3.0.4 on 2020-05-11 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200511_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_models',
            name='Surname',
            field=models.CharField(max_length=200),
        ),
    ]
