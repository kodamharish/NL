# Generated by Django 5.0.4 on 2024-08-15 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_founder_date_joined_alter_founder_photo_company_ask'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='founder',
            name='email',
        ),
        migrations.RemoveField(
            model_name='founder',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='founder',
            name='title',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
