from django.contrib import admin
from .models import Property_listing,Testimonial,Inquire

class ListingAdmin(admin.ModelAdmin):
    list_display=('id','title','status','price','list_date','agent','slider',"sale_type")
    list_display_links=('id','title')
    list_filter=('agent',)
    list_editable=('status','slider','list_date',"sale_type")
    search_fields=('title','description','address','city','state','zipcode','price')
    list_per_page=25

admin.site.register(Property_listing,ListingAdmin)
admin.site.register(Testimonial)
admin.site.register(Inquire)