# Generated by Django 4.2.7 on 2024-05-18 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller_Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('syriatel_cash', models.BooleanField(default=False)),
                ('usdt', models.BooleanField(default=False)),
                ('al_haram', models.BooleanField(default=False)),
                ('id_picture', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='seller_account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='main_app.seller_account'),
        ),
    ]
