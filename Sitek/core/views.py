from django.shortcuts import render

# создавть тут, так что приступим к работе. Я могу лучше, чем большинство ;))

def index(request):
    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')