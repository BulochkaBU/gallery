from django.contrib import admin
from .models import Auto, Architecture, Animal


class AutoAdmin(admin.ModelAdmin):
    """Поля для редактирования модель Автомобиль в админке."""
    fields = ('picture',)


class AnimalAdmin(admin.ModelAdmin):
    """Поля для редактирования модель Животное в админке."""
    fields = ('picture',)


class ArchitectureAdmin(admin.ModelAdmin):
    """Поля для редактирования модель Архитектура в админке."""
    fields = ('picture',)


admin.site.register(Auto, AutoAdmin)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(Architecture, ArchitectureAdmin)
