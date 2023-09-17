from django.http import JsonResponse
from firstApp.models import Employee


def employee_view(request):
    emp = {
        'id': 123,
        'name': 'John',
        'sal': 1000
    }

    data = Employee.objects.all()
    print(type(data.values()))
    response = {'employees': list(data.values('name', 'sal'))}

    return JsonResponse(response)
