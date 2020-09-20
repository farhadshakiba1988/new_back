# Generated by Django 3.1.1 on 2020-09-18 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Const',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=100)),
                ('k', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Crel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('left', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='left', to='const.const')),
                ('right', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='right', to='const.const')),
            ],
        ),
    ]
