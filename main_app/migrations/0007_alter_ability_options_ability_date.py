# Generated by Django 4.1 on 2022-09-01 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_remove_ability_toy_toy_abilities'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ability',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='ability',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
