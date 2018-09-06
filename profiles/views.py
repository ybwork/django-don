from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from profiles.models import Info
from profiles.utils import fetch_user_balance_from_1c


@login_required
def get_user_balance(request):
    id = get_user_id(request)
    invoice_num = get_user_invoice_num(user_id=id)
    balance = fetch_user_balance_from_1c(invoice_num)

    return JsonResponse(balance, safe=False)


def get_user_id(request):
    return request.session.get('_auth_user_id')


def get_user_invoice_num(user_id):
    return Info.objects.get(user_id=user_id).invoice_num
