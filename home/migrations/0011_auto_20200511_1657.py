# Generated by Django 3.0.4 on 2020-05-11 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20200511_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_models',
            name='confirmation',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
