# Generated by Django 4.2.5 on 2024-06-22 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0003_customer_account_deal_with'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer_account',
            name='password',
        ),
        migrations.RemoveField(
            model_name='seller_account',
            name='password',
        ),
        migrations.AddField(
            model_name='customer_account',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='seller_account',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
