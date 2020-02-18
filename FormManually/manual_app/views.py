from django.shortcuts import render,redirect
from manual_app.forms import InputForm
from manual_app.models import ManualModel
# Create your views here.

def form_view(request):
    form ={}
    if request.method == 'POST':
        form_data = InputForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('home')
        else:
            form_data = InputForm()
    else:
        form_data = InputForm()
    form['form_manual'] = form_data
    return render(request,'register_form.html',form)

def list_view_home(request):
    context ={}
    data = ManualModel.objects.all()
    context['data'] = data

    return render(request,'list_view_home.html',context)
