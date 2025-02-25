# Generated by Django 4.2.17 on 2025-01-11 04:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companyAccount', '0002_remove_requestreceived_request_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OutstandingRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carbon_unit_price', models.FloatField(default=0)),
                ('carbon_quantity', models.FloatField(default=0)),
                ('request_reason', models.TextField()),
                ('request_status', models.CharField(default='Pending Approval', max_length=50)),
                ('request_type', models.CharField(choices=[('BUY', 'Buy'), ('SELL', 'Sell')], max_length=4)),
                ('created_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_datetime', models.DateTimeField(auto_now=True)),
                ('requestor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests_made', to='companyAccount.companyaccount')),
                ('target_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests_received', to='companyAccount.companyaccount')),
            ],
        ),
    ]
