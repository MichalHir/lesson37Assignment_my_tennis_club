# Generated by Django 5.1.1 on 2024-09-19 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_member_court'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='joined_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
