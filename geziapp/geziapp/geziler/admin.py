from django.contrib import admin
from geziler.models import Setting, User,Profile,Comment,Category,Content,image,faq,attend,message,Video
from django.contrib.admin.sites import NotRegistered

class CateGoryAdmin(admin.ModelAdmin):
    list_display = ('title','isActive','isHome',)
    prepopulated_files = {'slug': ('title',)}
    list_filter = ('id', 'title','isActive','isHome',)
    search_fields = ('title', 'description',)


admin.site.register(Setting)
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Category,CateGoryAdmin)
admin.site.register(Content)
admin.site.register(image)
admin.site.register(faq)
admin.site.register(attend)
admin.site.register(message)
admin.site.register(Video)


# Kullanıcı Adı: admin
# eposta: unal90182@gmail.com
# Password: 123
