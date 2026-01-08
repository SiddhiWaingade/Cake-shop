from django.contrib import admin
from .models import *






# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display=['name','email','phone','month','date','size','flavour','code','description']
admin.site.register(Booking,BookingAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display=['name','email','phone','month','date','size','flavour','code','description']
admin.site.register(Order,OrderAdmin)


class PurchaseAdmin(admin.ModelAdmin):
    list_display=['name','email','phone','month','date','size','flavour','code','description']
admin.site.register(Purchase,PurchaseAdmin)


class BuyAdmin(admin.ModelAdmin):
    list_display=['name','email','phone','month','date','size','flavour','code','description']
admin.site.register(Buy,BuyAdmin)



class FeedbackAdmin(admin.ModelAdmin):
    list_display=['rate','comments','name','email']
admin.site.register(Feedback,FeedbackAdmin)




