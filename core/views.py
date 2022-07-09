from django.shortcuts import render
from .models import Double


def name_is_valid(name):
    alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
    for c in name:
        if c not in alpha:
            return False
        return True

def double(request):
    doubles = Double.objects.all()

    if request.method == 'GET':
        return render(request, 'double.html', {'doubles': doubles})

    value = int(request.POST.get('value'))
    if value > 1000 or value < -1000:
        error = 'max 1000 min -1000'
        return render(request, 'double.html', {'doubles': doubles, 'error': error})

    name_user = request.POST.get('name_user')
    if not name_is_valid(name_user):
        error = 'Please dont user charctere'
        return render(request, 'double.html', { 'error': error, 'doubles': doubles})

    already_exist = Double.objects.filter(name=name_user, value=value)
    if already_exist.count() == 0:
        Double.objects.create(name=name_user, value=value, double_value=value*2)
    return render(request, 'double.html', {'doubles': doubles})
