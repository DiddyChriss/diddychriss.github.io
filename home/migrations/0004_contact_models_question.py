# Generated by Django 3.0.4 on 2020-05-11 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200511_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_models',
            name='question',
            field=models.TextField(default=True),
            preserve_default=False,
        ),
    ]
