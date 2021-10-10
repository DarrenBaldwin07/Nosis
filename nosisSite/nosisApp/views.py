from django.shortcuts import render
import infermedica_api
from django.shortcuts import redirect
from .models import * 

# Application ID: 71c2aef2
# API KEY: 3d15b5418db93ab2e687c159a6dffa37


def home(request):
    return render(request, 'nosisApp/home.html')

def product(request):
    return render(request, 'nosisApp/product.html')

def apiData(request):

    
    sex = request.POST.get('sex')
    age = request.POST.get('age')
    symptoms = request.POST.get('symptoms')


    
    if sex and age != '':
        dataInfo = User_data(sex=request.POST['sex'], age=request.POST['age'], symptoms=symptoms)
        dataInfo.save()
 
    


    context = {
        'data': dataInfo,
    }

    return redirect('/apiSymp/')

def apiSymp(request):
    Info = User_data.objects.order_by('id').reverse()[0]
    sex = str(Info.sex).lower()
    api = infermedica_api.APIv3Connector(app_id='71c2aef2', app_key='3d15b5418db93ab2e687c159a6dffa37')
    symptoms = str(Info.symptoms).split(',')
    


    evidence = [
        # data for api to determine diag
    ]

    for i in symptoms:
        evidence.append({"id": i, "choice_id": "present"})

    response = api.diagnosis(evidence=evidence, sex=sex, age=str(Info.age))
    question = response['question']['text']
    conditions = {}

    # test symps: s_21,s_98,s_107
    for i in response['conditions']:
        conditions[i['common_name']] = int(i['probability']*100) 
        

    context = {
        'Info': Info,
        'sex': sex,
        'question': question,
        'conditions': conditions,
    }

    return render(request, 'nosisApp/productSymp.html', context)

def symptoms(request):
    return render(request, 'nosisApp/symptoms.html')