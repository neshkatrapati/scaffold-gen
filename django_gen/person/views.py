from django.shortcuts import render
from django.http import HttpResponse
from person.models import *
def person_index(request):
	return HttpResponse('You are @ person/index')
def person_detail(request,id):
	return HttpResponse('You are @ person/detail')
def person_update(request, id):
	return HttpResponse('You are @ person/update')
def person_create(request):
	return HttpResponse('You are @ person/create')
def person_delete(request, id):
	return HttpResponse('You are @ person/delete')

def job_index(request):
	return HttpResponse('You are @ job/index')
def job_detail(request,id):
	return HttpResponse('You are @ job/detail')
def job_update(request, id):
	return HttpResponse('You are @ job/update')
def job_create(request):
	return HttpResponse('You are @ job/create')
def job_delete(request, id):
	return HttpResponse('You are @ job/delete')
