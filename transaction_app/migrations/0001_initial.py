# Generated by Django 4.1.3 on 2022-11-04 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('from_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_account', to='transaction_app.account')),
                ('to_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_account', to='transaction_app.account')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summa', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True, verbose_name='summa')),
                ('time', models.DateTimeField(auto_now=True, null=True, verbose_name='time')),
                ('org', models.CharField(max_length=100, null=True, verbose_name='org')),
                ('description', models.CharField(max_length=200, null=True, verbose_name='description')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='transaction_app.category')),
            ],
        ),
    ]
