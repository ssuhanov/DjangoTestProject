from django.shortcuts import render


def index(request):
    return render(request, 'mainApp/homePage.html')


def contacts(request):
    return render(request,
                  'mainApp/basic.html',
                  {'values': ['Ask me anything you want, please.',
                              'Kyiv 🇺🇦',
                              '(050) 000-00-00']})
