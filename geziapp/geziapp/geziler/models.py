from django.db import models


class Setting(models.Model):
    id = models.CharField(primary_key=True)
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=100)
    description = models.TextField()

class User(models.Model):
    pass

class Profile(models.Model):
    pass

class Comment(models.Model):
    pass

class Category(models.Model):
    id = models.CharField(max_lengt=100)
    

class Content(models.Model):
    pass


class image(models.Model):
    pass


class faq(models.Model):
    pass

class attend(models.Model):
    pass

class message(models.Model):
    pass

