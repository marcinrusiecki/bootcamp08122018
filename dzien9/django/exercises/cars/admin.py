from django.contrib import admin
from cars.models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["brand", "model", "year"]
    search_fields = ["brand"]
    list_filter = ["brand"]
# admin.site.register(Car, CarAdmin)

# Register your models here.
