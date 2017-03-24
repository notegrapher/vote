from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Candidate

def index(request):
	candidates = Candidate.objects.all()
	str = ""
	for candidate in candidates:
		str += "Person {} {} ({})<br>".format(candidate.name, candidate.party_number, candidate.area)
		str += candidate.introduction + "<P>"

	return HttpResponse(str)
