# Generated by Django 4.2 on 2024-03-22 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlgorithmTask',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('pid', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(choices=[('running', 'running'), ('success', 'success'), ('canceled', 'canceled'), ('created', 'created')], default='created', max_length=20)),
            ],
            options={
                'db_table': 'task',
            },
        ),
    ]
