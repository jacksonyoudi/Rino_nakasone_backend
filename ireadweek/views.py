from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from .services import get_books

from django.http import HttpResponse
import datetime
import decimal
import json


def custom_converter(obj):
    if isinstance(obj, datetime.datetime):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(obj, datetime.date):
        return obj.strftime('%Y-%m-%d')
    elif isinstance(obj, decimal.Decimal):
        return float(obj)


def HttpJSONResponse(js):
    return HttpResponse(json.dumps(js, default=custom_converter), content_type='application/json')


@csrf_exempt
def list_books(request):
    """
    获取列表数据
    :param request:
    :return:
    """
    where = request.GET.dict()

    # 每页的数据
    limit = where.get('n', 20)
    offset = (where.get('p', 1) - 1) * limit

    if where.get('p'):
        del where['p']
    if where.get('n'):
        del where['n']

    data = get_books(where, limit, offset)
    return HttpJSONResponse({'c': '1', 'd': data})
