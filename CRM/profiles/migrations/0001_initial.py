# Generated by Django 5.1.4 on 2025-06-17 10:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DSA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dsa_name', models.CharField(max_length=50)),
                ('dsa_code', models.CharField(max_length=50)),
                ('dsa_phone_number', models.IntegerField()),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('descriptions', models.TextField(blank=True, null=True)),
                ('task_date', models.DateField()),
                ('task_time', models.TimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=50)),
                ('phone_num', models.IntegerField()),
                ('product', models.CharField(choices=[('HL', 'Home LONE'), ('PL', 'Personal Loan'), ('CL', 'Car Loan'), ('BL', 'Business Loan'), ('RF', 'Re-Fenace')], max_length=20)),
                ('bank', models.CharField(choices=[('SBI', 'State Bank Of India'), ('HDFC', 'HDFC'), ('AXIX', 'AXIS'), ('cANARA', 'canara')], max_length=20)),
                ('status', models.CharField(choices=[('login_submit', 'Login Submit'), ('login_complete', 'Login Complete'), ('tec_completed', 'TEC Completed'), ('legal_completed', 'Legal Completed'), ('disp', 'Dispatched'), ('reject', 'Rejected')], max_length=20)),
                ('type', models.CharField(choices=[('DSA', 'DSA'), ('SELF', 'Self')], max_length=4)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('dsa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.dsa')),
            ],
        ),
    ]
