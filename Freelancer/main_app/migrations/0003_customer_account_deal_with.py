# Generated by Django 4.2.5 on 2024-05-24 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_seller_account_profile_profile_seller_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('second_name', models.CharField(max_length=50, null=True)),
                ('country', models.CharField(max_length=50)),
                ('bdate', models.DateField()),
                ('password', models.CharField(max_length=8)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=10)),
                ('member_since', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Deal_With',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('start_service', models.IntegerField(default=0)),
                ('end_service', models.IntegerField(default=0)),
                ('rating', models.IntegerField(default=0)),
                ('comment', models.TextField(null=True)),
                ('customer_account', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='deal_with_seller', to='main_app.customer_account')),
                ('seller_account', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='deal_with_customer', to='main_app.seller_account')),
                ('seller_profile', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='deal_with_customer', to='main_app.profile')),
            ],
        ),
    ]
