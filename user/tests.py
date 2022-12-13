from django.test import TestCase

# Create your tests here.
"""urlpatterns = [
	path('', views.index, name ='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),



def home(request):
    if request.method == 'POST':
        forml = PersonDetailForm(request.POST)
        if forml.is_valid():
            forml.save()
            return redirect('indices')
    else:
        forml = PersonDetailForm()
    return render(request, 'user/home.html', {'forml': forml, 'title':'registre'})

"""