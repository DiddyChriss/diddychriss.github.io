# Generated by Django 3.0.4 on 2020-05-11 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_contact_models_confirmation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_models',
            name='Surname',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
