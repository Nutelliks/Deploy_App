from django.http import HttpResponse
from django.shortcuts import render
from myapp1.models import Worker, Department


def index_page(request):

    workers = Worker.objects.all()

    info = {'data': workers, 'data2': "It's the best course"}

    return render(request, 'index.html', context=info)

def department_page(request):
    departments = Department.objects.all()

    # 1-method
    worker_macrodata_dept = Worker.objects.filter(department__title='Обработка макроданных')

    print(f'Обработка макроданных: {worker_macrodata_dept}')

    # 2-method
    dept_optic_design = Department.objects.get(title='Оптика и дизайн')
    worker_optic_design_dept = Worker.objects.filter(department=dept_optic_design)

    print(f'Оптика и дизайн: {worker_optic_design_dept}')

    # 3-method
    dept_health_center = Department.objects.get(title='Центр здоровья')
    worker_health_center_dept = dept_health_center.worker_set.all()

    print(f'Центр здоровья: {worker_health_center_dept}')

    return render(request, 'department.html', context={'data': departments})