# Generated by Django 3.0.4 on 2020-05-11 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20200511_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_models',
            name='Company',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
