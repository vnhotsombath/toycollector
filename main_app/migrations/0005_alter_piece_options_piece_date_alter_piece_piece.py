# Generated by Django 4.1 on 2022-08-31 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_piece'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='piece',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='piece',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='piece',
            name='piece',
            field=models.CharField(choices=[('W', 'Weapon'), ('I', 'Interchangeable body piece'), ('B', 'Bonus piece to build a special character')], default='W', max_length=1),
        ),
    ]
