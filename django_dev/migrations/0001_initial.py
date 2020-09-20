from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
