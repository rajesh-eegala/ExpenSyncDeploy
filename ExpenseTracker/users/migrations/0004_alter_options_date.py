# Generated by Django 5.0.7 on 2024-07-28 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_options_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='options',
            name='date',
            field=models.DateTimeField(),
        ),
    ]