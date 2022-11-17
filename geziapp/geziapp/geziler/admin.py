from django.contrib import admin
from geziler.models import Setting, User,Profile,Comment,Category,Content,image,faq,attend,message
from django.contrib.admin.sites import NotRegistered

admin.site.register(Setting)
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Content)
#admin.site.register(Content)
admin.site.register(image)
admin.site.register(faq)
admin.site.register(attend)
admin.site.register(message)

# Kullanıcı Adı: admin
# eposta: unal90182@gmail.com
# Password: 123
