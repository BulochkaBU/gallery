from django import forms

from gallery_app.models import Auto, Animal, Architecture


class AutoForm(forms.ModelForm):
    """Форма отправки модели Автомобиль."""
    class Meta:
        model = Auto
        fields = ('comments', 'like', )
        labels = {'comments': " Ваш комментарий"}


class AnimalForm(forms.ModelForm):
    """Форма отправки модели Животное."""
    class Meta:
        model = Animal
        fields = ('comments', 'like', )
        labels = {'comments': " Ваш комментарий"}


class ArchitectureForm(forms.ModelForm):
    """Форма отправки модели Архитектура."""
    class Meta:
        model = Architecture
        fields = ('comments', 'like', )
        labels = {'comments': " Ваш комментарий"}
