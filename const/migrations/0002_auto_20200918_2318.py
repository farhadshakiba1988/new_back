# Generated by Django 3.1.1 on 2020-09-18 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('const', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='const',
            name='active',
            field=models.BooleanField(null=True),
        ),
        migrations.DeleteModel(
            name='Crel',
        ),
    ]