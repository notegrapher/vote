from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Candidate

def index(request):
	candidates = Candidate.objects.all()
	context = {'candidates' : candidates}

	return render(request, 'elections/index.html', context)
