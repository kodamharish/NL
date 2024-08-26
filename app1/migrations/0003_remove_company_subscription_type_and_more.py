# Generated by Django 5.0.4 on 2024-08-12 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_remove_heterogenousproduct_company_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='subscription_type',
        ),
        migrations.AddField(
            model_name='company',
            name='a_yearbefore_pl',
            field=models.DecimalField(decimal_places=2, max_digits=25, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='a_yearbefore_revenue',
            field=models.DecimalField(decimal_places=2, max_digits=25, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='additional',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='competitor',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='current_pl',
            field=models.DecimalField(decimal_places=2, max_digits=25, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='current_revenue',
            field=models.DecimalField(decimal_places=2, max_digits=25, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='customers',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='no_of_employees',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='previous_pl',
            field=models.DecimalField(decimal_places=2, max_digits=25, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='previous_revenue',
            field=models.DecimalField(decimal_places=2, max_digits=25, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='products',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='vision',
            field=models.CharField(max_length=255, null=True),
        ),
    ]