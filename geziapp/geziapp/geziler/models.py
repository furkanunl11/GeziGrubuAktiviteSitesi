from django.core import validators
from django.db import models
from django.core.validators import MinLengthValidator
from django.db.models.fields import CharField



class Setting(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone  = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    smtpserver = models.CharField(max_length=50)
    smtpemail = models.CharField(max_length=50)
    smtppassword = models.CharField(max_length=50)
    smtpport = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    aboutus = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    references = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    created_at = models.CharField(max_length=50)
    updated_at = models.CharField(max_length=50)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    created_at = models.CharField(max_length=50)
    updated_at = models.CharField(max_length=50)

class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    created_at = models.CharField(max_length=50)
    updated_at = models.CharField(max_length=50)

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=50)
    rate = models.CharField(max_length=50)
    content_id = models.CharField(max_length=50)
    user_id = models.CharField(max_length=50)
    ip = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    created_at = models.CharField(max_length=50)
    updated_at = models.CharField(max_length=50)


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    parent_id = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    created_at = models.CharField(max_length=50)
    updated_at = models.CharField(max_length=50)
    

class Content(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    categoryid = models.CharField(max_length=50)
    detail = models.CharField(max_length=50)



class image(models.Model):
    id = models.AutoField(primary_key=True)
    content_id = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    image = models.CharField(max_length=50)


class faq(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=50)
    answer = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    created_at = models.CharField(max_length=50)
    updated_at = models.CharField(max_length=50)

class attend(models.Model):
    id = models.AutoField(primary_key=True)
    content_id = models.CharField(max_length=50)
    user_id = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

class message(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=50)
    ip = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    created_at = models.CharField(max_length=50)
    updated_at = models.CharField(max_length=50)


