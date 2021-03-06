from django.contrib import admin
from rango.models import Category, Page, PageAdmin, UserProfile


admin.site.register(Page, PageAdmin)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(UserProfile)
