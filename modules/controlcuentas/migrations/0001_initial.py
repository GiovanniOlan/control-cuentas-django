# Generated by Django 4.0.3 on 2022-04-11 13:08

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
                ('acc_id', models.AutoField(primary_key=True, serialize=False)),
                ('acc_email', models.CharField(max_length=100)),
                ('acc_password', models.CharField(max_length=100)),
                ('acc_note', models.TextField()),
                ('acc_status', models.IntegerField()),
            ],
            options={
                'db_table': 'account',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CatTypeAccount',
            fields=[
                ('typacc_id', models.AutoField(primary_key=True, serialize=False)),
                ('typacc_name', models.CharField(max_length=30)),
                ('typacc_image', models.ImageField(upload_to='images/cat-type-account')),
            ],
            options={
                'db_table': 'cat_type_account',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('cli_id', models.AutoField(primary_key=True, serialize=False)),
                ('cli_name', models.CharField(max_length=25)),
                ('cli_phone', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'client',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Assignments',
            fields=[
                ('assi_id', models.AutoField(primary_key=True, serialize=False)),
                ('assi_status', models.IntegerField(blank=True, db_column='assI_status', null=True)),
                ('assi_datepurchase', models.DateField()),
                ('assi_daterenovation', models.DateField()),
                ('assi_profile', models.CharField(max_length=25)),
                ('assi_purchaseprice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('assi_sellingprice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('assi_note', models.TextField()),
                ('assi_fkaccount', models.ForeignKey(db_column='assi_fkaccount', on_delete=django.db.models.deletion.DO_NOTHING, to='controlcuentas.account')),
                ('assi_fkclient', models.ForeignKey(db_column='assi_fkclient', on_delete=django.db.models.deletion.DO_NOTHING, to='controlcuentas.client')),
            ],
            options={
                'db_table': 'assignments',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='account',
            name='acc_fktypeaccount',
            field=models.ForeignKey(db_column='acc_fktypeaccount', on_delete=django.db.models.deletion.DO_NOTHING, to='controlcuentas.cattypeaccount'),
        ),
    ]