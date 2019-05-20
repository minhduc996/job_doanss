from django.contrib import admin
from .models import DichVu, LinhVuc, ThanhPho, ViecTheoDuAn

# Register your models here.
class DvAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title','slug','created_on']

    fieldsets = [
        ('Tiêu đề', {'fields': ['title']}),
        ('Slug', {'fields': ['slug']}),
        ('Nội dung', {'fields': ['text']}),
        #('Hình ảnh', {'fields': ['img']}),
    
    ]

    def __str__(self):
        return self.title
    list_filter = ['created_on']
admin.site.register(DichVu, DvAdmin)
admin.site.register(LinhVuc, DvAdmin)
admin.site.register(ViecTheoDuAn)

admin.site.register(ThanhPho)


