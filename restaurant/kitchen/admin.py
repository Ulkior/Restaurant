from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
# Register your models here.


class PhotoInline(admin.TabularInline):
    fk_name = 'meal'
    model = Photo
    extra = 3



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent',)
    prepopulated_fields = {'slug': ('title',)}


class MealAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'kitchen', 'price', 'get_first_photo')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('price',)
    list_display_links = ('title',)
    list_filter = ('category', 'kitchen', 'price')
    inlines = [PhotoInline]

    def get_first_photo(self, obj):
        if obj.images:
            try:
                return mark_safe(f"<img src='{obj.images.all()[0].images.url}' width='50'>")
            except:
                return '-'
        else:
            return '-'

    get_first_photo.short_description = 'Миниатюра'



class EventsAdmin(admin.ModelAdmin):
    list_display = ('title', 'price',)
    list_editable = ('price',)
    list_display_links = ('title',)




class ChefsAdmin(admin.ModelAdmin):
    list_display = ('name', 'chef_title',)
    list_editable = ('chef_title',)
    list_display_links = ('name',)
    list_filter = ('chef_title',)



class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'data', 'phone', 'people_quantity','checked_booking',)
    list_editable = ('checked_booking',)
    list_display_links = ('name',)
    list_filter = ('data', 'people_quantity', 'checked_booking', 'booking_time',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Kitchen)
admin.site.register(Meal, MealAdmin)
admin.site.register(Photo)
admin.site.register(Events, EventsAdmin)
admin.site.register(Chefs, ChefsAdmin)
admin.site.register(Profile)
admin.site.register(Booking_table, BookingAdmin)












