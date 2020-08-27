from django.http import HttpResponse
from django.shortcuts import redirect, render
def home(request):
    return HttpResponse('<h1>this is the home page</h1>')
def newlink(request):
    return render(request,'newlink.html')
def google(request):
    return redirect('https://www.google.com')
def zoom(request):
    return redirect('https://us04web.zoom.us/j/9590737998?pwd=T0ttdmU0eVo0R25JRHJUZEhyWkw5Zz09')
def english_lit(request):
    return redirect('https://us04web.zoom.us/j/3233781386?pwd=TWNPbHdsbUhmTFozWFZWSFNzZk56QT09')
def hindi(request):
    return redirect('https://us04web.zoom.us/j/9450266921?pwd=dU5qSFVUWm0wK0hjcHdnQjJiZ2pMUT09')
def eng_tut(request):
    return redirect('https://meet.google.com/qoe-mgsp-cnp')