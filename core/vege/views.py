from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse

# Create your views here.
def recipies(request):

    if request.method=="POST":
        data = request.POST
        # brings data from front end

        recipie_image = request.FILES.get('recipie_image')
        # request.FILES.get('reqd_file') is to retrive image files or files from front end

        recipie_name = data.get('recipie_name')
        recipie_description = data.get('recipie_description') #getting data from frnt-end

        print(recipie_description)
        print(recipie_name)
        print(recipie_image)

        # saving to database
        Recipie.objects.create(
            recipie_image = recipie_image,
            recipie_name = recipie_name,
            recipie_description = recipie_description,
        )

        return redirect('/recepies/') #used so that page don't need to be reloaded after each adding

    
    queryset = Recipie.objects.all() #retriving data
    context = {'recipies': queryset} #sending data


    return render(request, 'recipies.html' , context)

def delete_recepie(request, id):
    queryset = Recipie.objects.get(id = id) #retriving data
    queryset.delete() #deleting data
    return redirect('/recepies/')

def update_recepie(request, id):
    queryset = Recipie.objects.get(id = id) #retriving data

    if request.method == "POST":
        data = request.POST


        recipie_image = request.FILES.get('recipie_image')
        # request.FILES.get('reqd_file') is to retrive image files or files from front end

        recipie_name = data.get('recipie_name')
        recipie_description = data.get('recipie_description') #getting data from frnt-end

        queryset.recipie_name = recipie_name
        queryset.recipie_description = recipie_description
        if recipie_image:
            queryset.recipie_image = recipie_image
        queryset.save()
        return redirect('/recepies/')

        
    
    context = {'recipie': queryset} #sending data

    return render(request, 'update_recipies.html' , context)
