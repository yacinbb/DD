# Generated by Django 5.0.2 on 2024-03-28 02:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudenHelp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudenHelp.poste')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudenHelp.user')),
            ],
        ),
    ]
