from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
import xml.etree.ElementTree as ET
import logging

handler404 = 'valutes.views.custom_404',

def page_from_name(request, file_name):
    return render(request, file_name + '.html', {})


def custom_404(request, exception):
    return redirect('404.html')


def color_view(request, color):
    # Обработка значения цвета
    return HttpResponse(f"Выбран цвет: {color}")


def valute_view(request, valute_code):
    valute_data = parse_currency_data(valute_code)
    return render(request, 'valute.html', {'valute_code': valute_code, 'value':valute_data["Value"], 'valute_name':valute_data["Name"]})

def get_exchange_rate(request):
    return render(request, 'exchange_rate_form.html')

def current_exchange_rate(request, valute_code):
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    data = response.json()
    rate = data['Valute'][valute_code]['Value']
    return render(request, 'current_exchange_rate.html', {'rate':rate, 'valute_code':valute_code})

def archive_year(request, year):
    try:
        # Проверка, что год находится в разумном диапазоне
        year = int(year)
        if year < 2000 or year > 2023:
            raise ValueError("Год находится вне допустимого диапазона.")
        # Здесь может быть логика обработки корректного года
        return HttpResponse(f'Архив сайта на момент {year}')
    except ValueError as e:
        # Обработка случая с некорректным годом
        return HttpResponse(f'Ошибка: {e}', status=400)

def parse_currency_data(valute_code):
    base_url = 'https://www.cbr-xml-daily.ru/daily_json.js'

    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        if valute_code in data['Valute']:
            currency_data = data['Valute'][valute_code]
            return currency_data
        else:
            return None
    else:
        return None

def get_exchange_rate(request, valute_code):
    if request.method == 'GET':
        return render(request, 'exchange_rate_form.html')

    elif request.method == 'POST':
        date = request.POST.get('date')
        url = f'https://www.cbr.ru/scripts/XML_daily.asp?date_req={date}'

        response = requests.get(url)

        if response.status_code != 200:
            return HttpResponse('Ошибка получения данных с сайта Центрального Банка России')

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            valute_list = soup.find_all('valute')

            exchange_rates = {}
            for valute in valute_list:
                name = valute.find('charcode').text
                rate = valute.find('value').text
                exchange_rates[name] = rate

            # Найдем курс для конкретной валюты
            specific_exchange_rate = exchange_rates.get(valute_code)

            if specific_exchange_rate == None:
                return HttpResponse('На данную дату нет данных в базе')

            return render(request, 'exchange_rate_result.html', {'specific_exchange_rate': specific_exchange_rate, 'date': date })

def get_currency_rates(request, valute_code):
    rates = []

    end_date = datetime.now().strftime("%d/%m/%Y")
    start_date = (datetime.now() - timedelta(days=29)).strftime("%d/%m/%Y")

    valute_data = parse_currency_data(valute_code)
    url = f"https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={start_date}&date_req2={end_date}&VAL_NM_RQ={valute_data["ID"]}"

    response = requests.get(url)

    if response.status_code != 200:
        return HttpResponse('Ошибка получения данных с сайта Центрального Банка России')

    xml_data = response.text
    root = ET.fromstring(xml_data)

    for record in root.findall('Record'):
        date_str = record.get('Date')
        date = datetime.strptime(date_str, '%d.%m.%Y').strftime('%d/%m/%Y')
        value = float(record.find('Value').text.replace(',', '.'))

        cr_data = {'date': date, 'value': value}
        rates.append(cr_data)

    return render(request, 'currency_chart.html', {'rates': rates})

