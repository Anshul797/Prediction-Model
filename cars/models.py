from django.db import models

# Create your models here.
class Cars(models.Model):
    name=models.CharField(max_length=50)   
    seller= models.CharField(max_length=50, choices=(('privat','privat'), ('gewerblich','gewerblich')))
    offerType= models.CharField(max_length=50, choices=(('Angebot','Angebot'), ('Gesuch','Gesuch')))         
    abtest= models.CharField(max_length=50, choices=(('test','test'), ('control','control')))
    vehicleType= models.CharField(max_length=50)   
    yearOfRegistration=models.IntegerField()
    gearbox= models.CharField(max_length=50, choices=(('manuell','manuell'), ('automatik','automatik')))
    powerPS=models.IntegerField()
    model= models.CharField(max_length=50)
    kilometer=models.IntegerField()        
    monthOfRegistration=models.IntegerField()
    fuelType= models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    notRepairedDamage= models.CharField(max_length=50, choices=(('nein','nein'), ('ja','ja')))
    postalCode=models.IntegerField()
    nrOfPictures=models.IntegerField()
    price=models.IntegerField(null=True, blank=True)
    def to_dict(self):
        return {
            'name':self.name,
            'seller':self.seller ,
            'offerType':self.offerType ,
            'abtest':self.abtest ,
            'vehicleType':self.vehicleType ,
            'yearOfRegistration':self.yearOfRegistration ,
            'gearbox':self.gearbox ,
            'powerPS':self.powerPS ,
            'model':self.model ,
            'kilometer':self.kilometer ,
            'monthOfRegistration':self.monthOfRegistration ,
            'fuelType':self.fuelType ,
            'brand':self.brand,
            'notRepairedDamage':self.notRepairedDamage ,
            'nrOfPictures':self.nrOfPictures,
            'postalCode':self.postalCode      
        }                                          

