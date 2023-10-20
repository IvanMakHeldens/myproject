import random

from django.shortcuts import render
from django.http import HttpResponse
import logging


# Create your views here.


# logger = logging.getLogger(__name__)


def one(request):
    # logger.info('First page started')
    answer = ['Орел', 'Решка']
    i = random.randint(0, 1)
    return HttpResponse(f'{answer[i]}')


def two(request):
    # logger.info('Second page started')
    answer = random.randint(1, 6)
    return HttpResponse(f'{answer}')


def three(request):
    # logger.info('Third page started')
    answer = random.randint(0, 100)
    return HttpResponse(f'{answer}')