from django.db import models
from django.urls import reverse

class Robot(models.Model):
    name = models.CharField(max_length=100,verbose_name='Ad',blank=True)

    def __str__(self):
        return "{} ".format(self.name)


class Register(models.Model):

	name = models.CharField(blank=True,verbose_name='Ad',max_length=100,help_text='Adınızı giriniz.')
	surname = models.CharField(blank=True,verbose_name='Soyad',max_length=100,help_text='Soyadınızı giriniz.')
	robot_name= models.CharField(blank=True,verbose_name='Robot adı',max_length=100,help_text='Robot adını giriniz.')
	category = models.ForeignKey(Robot, blank=True, null=True, on_delete=models.SET_NULL ,verbose_name='Kategori seçiniz.')
	email = models.EmailField(max_length=50, null=True, verbose_name='E-posta :',help_text="E-postanızı giriniz.")
	phone = models.CharField(max_length=100, blank=False, null=True,verbose_name='Telefon :', help_text='Telefonunuzu giriniz.')
	school_name = models.CharField(blank=True,verbose_name='Okul Adı',max_length=100,help_text='Okulunuzun adını giriniz.')

	class Meta:
		verbose_name_plural="Kayıt"
		ordering = ['id']

	def __str__(self):
		return "%s %s" %(self.name, self.surname)

	def get_absolute_url(self):
		return reverse("robonish:register_view_id", kwargs={"id": self.id})