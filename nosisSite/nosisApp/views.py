from django.shortcuts import render
import infermedica_api
from .models import * 

# Application ID: 71c2aef2
# API KEY: 3d15b5418db93ab2e687c159a6dffa37


def home(request):
    return render(request, 'nosisApp/home.html')

def product(request):
    cur_form = 'info'
    infoIsNotDone = True
    
    context = {
        'curForm': cur_form,
        'IsInfo': infoIsNotDone,
    }
    return render(request, 'nosisApp/product.html', context)

def apiData(request):
    infoIsNotDone = True
    SymptomesIsNotDone = False
    api = infermedica_api.APIv3Connector(app_id='71c2aef2', app_key='3d15b5418db93ab2e687c159a6dffa37')
    sex = request.POST.get('sex')
    age = request.POST.get('age')
    

    cur_form = 'info';
    
    if sex and age != '':
        dataInfo = User_data(sex=request.POST['sex'], age=request.POST['age'])
        dataInfo.save()
        cur_form = 'Symptomes'
        infoIsNotDone = False
        SymptomesIsNotDone = True



    context = {
        'data': dataInfo,
        'curForm': cur_form,
        'IsInfo': infoIsNotDone,
        'IsSymp': SymptomesIsNotDone,
    }

    return render(request, 'nosisApp/product.html', context)

def apiSymp(request):
    Info = User_data.objects.order_by('id').reverse()[0]
    
    
   

    context = {
        'Info': Info,

    }

    return render(request, 'nosisApp/productSymp.html', context)