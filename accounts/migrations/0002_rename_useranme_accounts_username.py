# Generated by Django 4.2.3 on 2023-07-27 00:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accounts',
            old_name='useranme',
            new_name='username',
        ),
    ]
