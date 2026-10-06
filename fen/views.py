from django.shortcuts import render, get_object_or_404
from .models import ExchangeProgram, HomePageContent, Program, Department

def home_view(request):
    content = HomePageContent.objects.first()
    return render(request, 'fen/home.html', {'content': content})

def programs_list_view(request):
    programs = Program.objects.all()
    return render(request, 'fen/programs_list.html', {'programs': programs})

def program_detail_view(request, pk):
    program = get_object_or_404(Program, pk=pk)
    return render(request, 'fen/program_detail.html', {'program': program})

def departments_list_view(request):
    departments = Department.objects.all()
    return render(request, 'fen/departments_list.html', {'departments': departments})

def department_detail_view(request, pk):
    department = get_object_or_404(Department, pk=pk)
    teachers = department.teachers.all()
    programs = department.programs.all()
    
    return render(request, 'fen/department_detail.html', {
        'department': department,
        'teachers': teachers,
        'programs': programs
    })

def exchange_list(request):
    programs = ExchangeProgram.objects.all()
    return render(request, 'fen/exchange_list.html', {'programs': programs})