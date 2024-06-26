# Generated by Django 4.2.7 on 2024-06-26 19:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person2_id', models.CharField(max_length=50, null=True)),
                ('unread_cnt', models.IntegerField(default=0)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Seller_Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('second_name', models.CharField(max_length=50, null=True)),
                ('country', models.CharField(max_length=50)),
                ('bdate', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=10)),
                ('syriatel_cash', models.BooleanField(default=False)),
                ('usdt', models.BooleanField(default=False)),
                ('al_haram', models.BooleanField(default=False)),
                ('id_picture', models.CharField(max_length=255, null=True)),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.IntegerField(null=True)),
                ('person2_id', models.CharField(max_length=50, null=True)),
                ('rate', models.IntegerField(default=0)),
                ('comment', models.TextField(null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_seller_id', models.IntegerField(default=1)),
                ('language', models.CharField(max_length=50)),
                ('work_group', models.CharField(max_length=50)),
                ('bio', models.TextField(null=True)),
                ('provided_services', models.IntegerField(default=0)),
                ('member_since', models.DateTimeField(auto_now=True)),
                ('rate', models.FloatField(default=0.0)),
                ('seller_account', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='main_app.seller_account')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('sender', models.CharField(max_length=50, null=True)),
                ('reciever', models.CharField(max_length=50, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('chat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.chat')),
            ],
        ),
        migrations.CreateModel(
            name='Deal_With',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.IntegerField(null=True)),
                ('person2_id', models.CharField(max_length=50, null=True)),
                ('send_date', models.DateField(auto_now_add=True)),
                ('send_time', models.TimeField(auto_now_add=True)),
                ('is_accepted', models.IntegerField(default=0)),
                ('is_active', models.IntegerField(default=1)),
                ('accept_time', models.DateField(null=True)),
                ('end_time', models.DateField(null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer_Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('second_name', models.CharField(max_length=50, null=True)),
                ('country', models.CharField(max_length=50)),
                ('bdate', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=10)),
                ('member_since', models.DateField(auto_now_add=True)),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
