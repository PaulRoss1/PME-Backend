# Generated by Django 4.0 on 2021-12-30 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_alter_event_date_alter_event_event_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eventss',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
