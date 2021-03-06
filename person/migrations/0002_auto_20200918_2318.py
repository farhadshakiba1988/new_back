# Generated by Django 3.1.1 on 2020-09-18 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='created',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='first',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='last',
            field=models.CharField(max_length=100),
        ),
    ]
