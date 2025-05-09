# Generated by Django 5.1.4 on 2024-12-23 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=50)),
                ('phone_num', models.IntegerField()),
                ('product', models.CharField(choices=[('HL', 'Home LONE'), ('PL', 'Personal Loan'), ('CL', 'Car Loan'), ('BL', 'Business Loan'), ('RF', 'Re-Fenace')], max_length=4)),
                ('bank', models.CharField(choices=[('SBI', 'State Bank Of India'), ('HDFC', 'hdfc'), ('AXIS', 'hdfc'), ('CNR', 'canara')], max_length=4)),
                ('status', models.CharField(choices=[('login_submit', 'Login Submit'), ('login_complete', 'Login Complete'), ('tec_completed', 'TEC Completed'), ('legal_completed', 'Legal Completed'), ('disp', 'Dispatched'), ('reject', 'Rejected')], max_length=20)),
                ('type', models.CharField(choices=[('DSA', 'DSA'), ('SELF', 'Self')], max_length=4)),
                ('dsa_name', models.CharField(blank=True, max_length=50, null=True)),
                ('dsa_number', models.CharField(blank=True, max_length=15, null=True)),
                ('dsa_connector_code', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
