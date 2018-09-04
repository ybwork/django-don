from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from requests import session

from don.utils import fetch_client_balance_from_1c
from profiles.models import Profile


@login_required
def home(request):
    user = Profile.objects.get(user_id=request.session.get('_auth_user_id'))
    return HttpResponse(user.invoice_num)
    return HttpResponse(fetch_client_balance_from_1c())
    return render(request, 'home.html')