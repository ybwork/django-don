from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from don.utils import work_soap


@login_required
def home(request):
    return HttpResponse(work_soap())
    return render(request, 'home.html')