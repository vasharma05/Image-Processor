# Generated by Django 3.0.7 on 2020-07-10 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200710_1048'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FilteredImage',
            new_name='CentroidImage',
        ),
    ]
