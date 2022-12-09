from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm, TextInput, Textarea
from django.core.validators import MinLengthValidator
from django.db.models.fields import CharField
from django.core.validators import MinLengthValidator, MaxLengthValidator

from django.utils.safestring import mark_safe



class Setting(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=150, null=True)
    keywords = models.CharField(max_length=255, null=True)
    description = models.TextField("Açıklama",validators= [MinLengthValidator(20)],null=True)
    company = models.CharField(max_length=50, null=True)
    address = models.CharField( max_length=150, null=True)
    phone = models.CharField(max_length=15, null=True)
    fax = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=50, null=True)
    smptpserver = models.CharField(max_length=30, null=True)
    smptemail = models.CharField(max_length=30, null=True)
    smptpassword = models.CharField(max_length=150, null=True)
    smptport = models.CharField(max_length=15, null=True)
    facebook = models.CharField(max_length=50, null=True)
    instagram = models.CharField(max_length=50, null=True)
    twitter = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=10, choices=STATUS, null=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    uptade_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("İsim",max_length=50, null=True)
    surname = models.CharField("Soyisim", max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    password = models.CharField("Şifre",max_length=50, null=True)
    role = models.CharField("Rol",max_length=50, null=True)
    status = models.BooleanField("Durum",max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return  f"{self.name} {self.surname}"


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=50, null=True)
    image = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.address







class Category(models.Model):
    STATUS = (
        ('True','Evet'),
        ('False',"Hayır")
    )
    id = models.AutoField(primary_key=True)
    title = models.CharField("Başlık",max_length=50, null=True)
    slug = models.CharField("slugs",max_length=50, null=True)
    description = models.TextField("Açıklama",validators= [MinLengthValidator(20)])
    image = models.CharField("Resim",max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    isActive = models.BooleanField(default=False)
    isHome = models.BooleanField(default=False)
    titleforhead = models.CharField("Kafa Başlığı", max_length=50,null=True)

    def __str__(self):
        return self.title

class Slider(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="img")
    gezi = models.ForeignKey(Category, on_delete=models.SET_NULL, null = True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    full_name = models.CharField(max_length=100, null = True)
    email = models.EmailField(default="", null = True)
    text = models.TextField(max_length=500, null = True)
    rating = models.IntegerField(null= True)
    date_added = models.DateTimeField(null =True, auto_now=True)
    gezi = models.ForeignKey(Category, on_delete=models.CASCADE, related_name ="comments", null = True)

    def __str__(self):
        return self.text

class Video(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    gezi = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class Content(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=True)
    slug = models.CharField(max_length=50, null=True)
    description = models.TextField("Özet",validators = [MinLengthValidator(20)])
    images = models.CharField(max_length=50, null=True)
    categoryid = models.CharField(max_length=50, null=True)
    detail = models.CharField(max_length=50, null=True)
    comment = models.OneToOneField(Comment, on_delete= models.CASCADE, null=True) ## içerik silinince, Comment'de silinir.
    category = models.OneToOneField(Category, on_delete=models.CASCADE, null=True) ## içerik silinince, kategori de silinir.

    def __str__(self):
        return self.title

class image(models.Model):
    id = models.AutoField(primary_key=True)
    content_id = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=50, null=True)
    image = models.CharField(max_length=50, null=True)
    content_id = models.OneToOneField(Content, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

class faq(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=500, null=True)
    answer = models.CharField(max_length=500, null=True)
    status = models.BooleanField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    content = models.OneToOneField(Content, on_delete=models.CASCADE, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,blank=True)


    def __str__(self):
        return self.question



class attend(models.Model):
    id = models.AutoField(primary_key=True)
    content_id = models.CharField(max_length=50, null=True)
    user_id = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.content_id


class message(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=50, null=True)
    subject = models.CharField(max_length=50, null=True)
    message = models.CharField(max_length=50, null=True)
    ip = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    

    def __str__(self):
        return self.message


