# Generated by Django 5.0.6 on 2024-08-23 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_alter_cashflow_beginning_cash_position_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productsandservices',
            old_name='a_year_befor_pl',
            new_name='a_year_before_pl',
        ),
        migrations.RenameField(
            model_name='productsandservices',
            old_name='a_year_befor_revenue',
            new_name='a_year_before_revenue',
        ),
    ]
