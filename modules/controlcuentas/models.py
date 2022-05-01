
from django.db import models


class Client(models.Model):
    cli_id = models.AutoField(primary_key=True)
    cli_name = models.CharField(max_length=25, verbose_name="Nombre del cliente")
    cli_phone = models.CharField(max_length=15)

    class Meta:
        managed = True
        db_table = 'client'
        
        
class CatTypeAccount(models.Model):
    typacc_id = models.AutoField(primary_key=True)
    typacc_name = models.CharField(max_length=30)
    typacc_image = models.ImageField(upload_to='images/cat-type-account')

    class Meta:
        managed = True
        db_table = 'cat_type_account'
        
class Account(models.Model):
    acc_id = models.AutoField(primary_key=True)
    acc_email = models.CharField(max_length=100)
    acc_password = models.CharField(max_length=100)
    acc_note = models.TextField()
    acc_status = models.IntegerField()
    acc_fktypeaccount = models.ForeignKey(CatTypeAccount, models.DO_NOTHING, db_column='acc_fktypeaccount')

    class Meta:
        managed = True
        db_table = 'account'


class Assignments(models.Model):
    assi_id = models.AutoField(primary_key=True)
    assi_status = models.IntegerField(db_column='assI_status', blank=True, null=True)  # Field name made lowercase.
    assi_datepurchase = models.DateField()
    assi_daterenovation = models.DateField()
    assi_profile = models.CharField(max_length=25)
    assi_purchaseprice = models.DecimalField(max_digits=10, decimal_places=2)
    assi_sellingprice = models.DecimalField(max_digits=10, decimal_places=2)
    assi_note = models.TextField()
    assi_fkaccount = models.ForeignKey(Account, models.DO_NOTHING, db_column='assi_fkaccount')
    assi_fkclient = models.ForeignKey(Client, models.DO_NOTHING, db_column='assi_fkclient')   
    
    class Meta:
        managed = True
        db_table = 'assignments'     
