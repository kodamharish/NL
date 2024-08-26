# Generated by Django 5.0.4 on 2024-08-16 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_remove_founder_email_remove_founder_phone_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='captable',
            name='email',
        ),
        migrations.RemoveField(
            model_name='captable',
            name='linkedin_url',
        ),
        migrations.RemoveField(
            model_name='captable',
            name='photo',
        ),
        migrations.AddField(
            model_name='captable',
            name='amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='captable',
            name='details',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='captable',
            name='investedsince',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='captable',
            name='shareholder',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='captable',
            name='valuation',
            field=models.IntegerField(null=True),
        ),
    ]
