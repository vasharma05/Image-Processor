# Generated by Django 3.0.7 on 2020-07-10 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_filteredimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filteredimage',
            name='centroid',
        ),
        migrations.AddField(
            model_name='filteredimage',
            name='centroid_0_url',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AddField(
            model_name='filteredimage',
            name='centroid_1_url',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AddField(
            model_name='filteredimage',
            name='centroid_2_url',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AddField(
            model_name='filteredimage',
            name='centroid_3_url',
            field=models.CharField(default='', max_length=256),
        ),
    ]