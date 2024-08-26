# Generated by Django 5.0.4 on 2024-08-12 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='heterogenousproduct',
            name='company_id',
        ),
        migrations.RemoveField(
            model_name='homogenousproduct',
            name='company_id',
        ),
        migrations.AlterField(
            model_name='company',
            name='business_type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='sector',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='CompanyRevenue',
        ),
        migrations.DeleteModel(
            name='HeterogenousProduct',
        ),
        migrations.DeleteModel(
            name='HomogenousProduct',
        ),
    ]