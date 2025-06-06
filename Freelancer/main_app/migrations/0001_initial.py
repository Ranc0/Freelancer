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
                ('person2_username', models.CharField(max_length=50, null=True)),
                ('unread_cnt', models.IntegerField(default=0)),
                ('time', models.DateTimeField(null=True)),
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
                ('bdate', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=10)),
                ('syriatel_cash', models.BooleanField(default=False)),
                ('usdt', models.BooleanField(default=False)),
                ('al_haram', models.BooleanField(default=False)),
                ('id_picture', models.TextField(blank=True, default='data:image/jpeg;base64,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', max_length=900000)),
                ('id_picture2', models.TextField(blank=True, default='data:image/jpeg;base64,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', max_length=900000)),
                ('img', models.TextField(blank=True, default='data:image/jpeg;base64,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', max_length=900000)),
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
                ('rate_sum', models.FloatField(default=0.0)),
                ('rate_cnt', models.FloatField(default=0.0)),
                ('rate', models.FloatField(default=0.0)),
                ('is_active', models.BooleanField(default=True)),
                ('seller_account', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='main_app.seller_account')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('image_message', models.TextField(blank=True, max_length=900000, null=True)),
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
                ('end_time', models.DateTimeField(null=True)),
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
                ('bdate', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=10)),
                ('member_since', models.DateField(auto_now_add=True)),
                ('img', models.TextField(blank=True, default='data:image/jpeg;base64,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', max_length=900000)),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
