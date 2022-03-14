# Generated by Django 4.0.3 on 2022-03-14 17:33

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0004_alter_account_address_alter_account_bidding_settings_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('first_name', models.CharField(blank=True, max_length=250, null=True)),
                ('surname', models.CharField(blank=True, max_length=250, null=True)),
                ('d_o_b', models.DateField(blank=True, null=True)),
                ('company_name', models.CharField(blank=True, max_length=250, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('telephone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('bidding_settings', models.CharField(blank=True, max_length=250, null=True)),
                ('google_id', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Account',
        ),
    ]
