from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse

from .models import Pet
from .forms import PetForm


def home(request):
    template = loader.get_template('templates/home.html')
    pets =  Pet.objects.all().order_by("-votes")
    
    context = {
        'pets': pets
    }
    return HttpResponse(template.render(context, request))


def post_new(request):
    if request.method == "POST":
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('home')
    else:
        form = PetForm()
    return render(request, 'templates/post_edit.html', {'form': form})
