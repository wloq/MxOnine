from django.shortcuts import render

# Create your views here.

def org_list(request):
    return render(request,"org-list.html")
