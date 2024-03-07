from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse


menu_dict = {
    'Протокол': '0', 'заключение': '1'
}

defect_dict = {
    'Трещина': '<p>Тре́щина — экстремальный дефект, представляющий собой области с полностью нарушенными межатомными связями (берега трещин) и частично нарушенными межатомными связями (вершина трещины). Поверхность раздела берегов называется фронтом трещины. Закономерности образования и роста трещин изучаются разделом физики твёрдого тела — механика разрушения твёрдых тел.</p>',
    'TOFD': 'Дифракционно-временной метод (ДВМ), также известный под названием TOFD (time-of-flight diffraction), что переводится как время пролета дифракции, является одним из методов акустического неразрушающего контроля (НК), Он регламентируется международным стандартом ГОСТ ISO 10863 – 20.',
    'Потеря металла': 'самопроизвольное разрушение металлов и сплавов в результате химического, электрохимического или физико-химического взаимодействия с окружающей средой. Разрушение по физическим причинам не является коррозией, а характеризуется понятиями «эрозия», «истирание», «износ»',
}


# Create your views here.

def main_page(request):
    data = {
        'description': menu_dict
    }
    return render(request, 'main/main_page.html', context=data)


def defect(request, defe):
    description = defect_dict.get(defe)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponse(f'Неудалось найти информацию - {defe}')


def defect_by_number(request, defe):
    articles = list(defect_dict)
    if articles:
        return HttpResponse(f'{defe}')
