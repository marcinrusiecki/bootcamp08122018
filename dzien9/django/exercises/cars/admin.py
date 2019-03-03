from django.contrib import admin
from cars.models import Car, Engine

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["brand", "model", "year"]
    search_fields = ["brand"]
    list_filter = ["brand"]
# admin.site.register(Car, CarAdmin)


@admin.register(Engine)
class EngineAdmin(admin.ModelAdmin):
    list_display = ["type", "power"]
# Register your models here.
