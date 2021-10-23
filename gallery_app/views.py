from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView

from gallery_app.forms import AutoForm, AnimalForm, ArchitectureForm
from gallery_app.models import Auto, Animal, Architecture


class IndexViews(View):
    """Главная страница."""
    def get(self, request):
        return render(request, 'index.html')


class AutosViews(View):
    """Страница с автомобилями."""
    def get(self, request):
        autos = Auto.objects.all()
        return render(request, 'autos.html', context={'autos': autos})


class AutoView(DetailView):
    """Страница с одним автомобилем."""
    def get(self, request, auto_pk):
        auto = Auto.objects.get(pk=auto_pk)
        return render(request, 'auto.html', context={'auto': auto, 'form': AutoForm})

    def post(self, request, auto_pk):
        auto = Auto.objects.get(pk=auto_pk)
        form = AutoForm(request.POST, instance=auto)
        if form.is_valid():
            form.save()
            return redirect("auto", auto_pk)
        return render(request, 'auto.html', context={'form': form})


class AnimalsViews(View):
    """Страница с животными."""
    def get(self, request):
        animals = Animal.objects.all()
        return render(request, 'animals.html', context={'animals':animals})


class AnimalView(DetailView):
    """Страница с одним животным."""
    def get(self, request, animal_pk):
        animal = Animal.objects.get(pk=animal_pk)
        return render(request, 'animal.html', context={'animal': animal, 'form': AnimalForm})

    def post(self, request, animal_pk):
        animal = Animal.objects.get(pk=animal_pk)
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect("animal", animal_pk)
        return render(request, 'animal.html', context={'form': form})


class ArchitectureViews(View):
    """Страница с архитектурой."""
    def get(self, request):
        architectures = Architecture.objects.all()
        return render(request, 'architecture.html', context={'architectures': architectures})


class ArchitectureDetailView(DetailView):
    """Страница с одной архитектурой."""
    def get(self, request, architecture_pk):
        architecture = Architecture.objects.get(pk=architecture_pk)
        return render(request, 'architecture_detail.html', context={'architecture': architecture, 'form': ArchitectureForm})

    def post(self, request, architecture_pk):
        architecture = Architecture.objects.get(pk=architecture_pk)
        form = ArchitectureForm(request.POST, instance=architecture)
        if form.is_valid():
            form.save()
            return redirect("architecture_detail", architecture_pk)
        return render(request, 'architecture_detail.html', context={'form': form})
