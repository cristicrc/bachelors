# Generated by Django 4.0.1 on 2022-02-13 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_alter_bankingaccount_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='banking_account',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='card_id',
        ),
        migrations.AddField(
            model_name='transaction',
            name='card',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.card'),
        ),
    ]
