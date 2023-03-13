from django.shortcuts import render

from djangoforms.form1 import ResultForm
from djangoforms.forms import StudentForm


def index(request):
    student = StudentForm()
    return render(request, 'index.html', {'form': student})
def results(request):
    results = ResultForm()
    return render(request, 'results.html', {'form': results})
