from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class PageAdmin(admin.ModelAdmin):
    list_display=('title','category','url')
    def __str__(self):
        return self.list_display
    
# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Page,PageAdmin)
admin.site.register(UserProfile)

