from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm, TextInput, Textarea
from django.core.validators import MinLengthValidator
from django.db.models.fields import CharField

from django.utils.safestring import mark_safe



class Setting(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=150, null=True)
    keywords = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
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


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True)
    surname = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)
    role = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=50, null=True)
    image = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=50, null=True)
    rate = models.CharField(max_length=50, null=True)
    content_id = models.CharField(max_length=50, null=True)
    user_id = models.CharField(max_length=50, null=True)
    ip = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class Category(models.Model):
    STATUS = (
        ('True','Evet'),
        ('False',"Hayır")
    )
    id = models.AutoField(primary_key=True)
    parent_id = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=50, null=True)
    keywords = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=50, null=True)
    image = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    

class Content(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=True)
    keywords = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=50, null=True)
    images = models.CharField(max_length=50, null=True)
    categoryid = models.CharField(max_length=50, null=True)
    detail = models.CharField(max_length=50, null=True)
    comment = models.OneToOneField(Comment, on_delete= models.CASCADE, null=True) ## içerik silinince, Comment'de silinir.
    category = models.OneToOneField(Category, on_delete=models.CASCADE, null=True) ## içerik silinince, kategori de silinir.



class image(models.Model):
    id = models.AutoField(primary_key=True)
    content_id = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=50, null=True)
    image = models.CharField(max_length=50, null=True)
    content_id = models.OneToOneField(Content, on_delete=models.CASCADE, null=True)


class faq(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=50, null=True)
    answer = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    content = models.OneToOneField(Content, on_delete=models.CASCADE, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)






class attend(models.Model):
    id = models.AutoField(primary_key=True)
    content_id = models.CharField(max_length=50, null=True)
    user_id = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=50, null=True)




class message(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    subject = models.CharField(max_length=50, null=True)
    message = models.CharField(max_length=50, null=True)
    ip = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


