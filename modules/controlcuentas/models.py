
from django.db import models
from django.conf import settings



class Client(models.Model):
    cli_id = models.AutoField(primary_key=True)
    cli_name = models.CharField(max_length=25, verbose_name="Nombre del cliente")
    cli_phone = models.CharField(max_length=15)
    cli_fkuser = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default='',db_column='cli_fkuser')

    class Meta:
        managed = True
        db_table = 'client'
        
    def __str__(self):
        phone = ''
        if self.cli_phone.isdigit():
            for i,charac in enumerate(self.cli_phone):
                if i==3:
                    phone+= ' '
                if i==6:
                    phone+= ' '
                phone+= charac
        else:
            phone = self.cli_phone
        return f'{self.cli_name}({phone})'  
class CatTypeAccount(models.Model):
    typacc_id = models.AutoField(primary_key=True)
    typacc_name = models.CharField(max_length=30)
    typacc_image = models.ImageField(upload_to='images/cat-type-account')

    class Meta:
        managed = True
        db_table = 'cat_type_account'
        
    def __str__(self):
        return self.typacc_name
        
class Account(models.Model):
    acc_id = models.AutoField(primary_key=True)
    acc_email = models.CharField(max_length=100)
    acc_password = models.CharField(max_length=100)
    acc_note = models.TextField()
    acc_status = models.IntegerField()
    acc_fktypeaccount = models.ForeignKey(CatTypeAccount, models.DO_NOTHING, db_column='acc_fktypeaccount')
    acc_fkuser = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default='',db_column='acc_fkuser')

    class Meta:
        managed = True
        db_table = 'account'
        
    def __str__(self):
        return f'{self.acc_email}({self.acc_fktypeaccount})'


class Assignments(models.Model):
    assi_id = models.AutoField(primary_key=True)
    assi_status = models.IntegerField(db_column='assi_status', blank=True, null=True,verbose_name="Estatus")  # Field name made lowercase.
    assi_datepurchase = models.DateField(verbose_name="Dia De La Compra")
    assi_daterenovation = models.DateField(verbose_name="Dia De La Renovación")
    assi_profile = models.CharField(max_length=25,verbose_name="Perfil")
    assi_purchaseprice = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Precio De La Compra")
    assi_sellingprice = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Precio de la venta")
    assi_note = models.TextField(verbose_name="Nota")
    assi_fkaccount = models.ForeignKey(Account, models.DO_NOTHING, db_column='assi_fkaccount',verbose_name="Cuenta")
    assi_fkclient = models.ForeignKey(Client, models.DO_NOTHING, db_column='assi_fkclient',verbose_name="Cliente")   
    assi_fkuser = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default='',db_column='assi_fkuser')
    
    class Meta:
        managed = True
        db_table = 'assignments'     
