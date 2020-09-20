# Generated by Django 3.1.1 on 2020-09-08 12:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('first', models.TextField(blank=True, null=True)),
                ('last', models.TextField(blank=True, null=True)),
                ('created', models.DateField(blank=True, null=True)),
                ('active', models.BooleanField()),
            ],
        ),
    ]
