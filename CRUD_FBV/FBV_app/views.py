from django.shortcuts import render
from django.shortcuts import (get_object_or_404,
                                render,HttpResponseRedirect)
from FBV_app.models import GeeksModel
from FBV_app.forms import GeeksForm
from django.views.generic.edit import FormView
# Create your views here.


def delete_view(request,id):
    print(id)
    context = {}
    obj = get_object_or_404(GeeksModel,id = id )
    if request.method == 'POST':
        obj.delete()
        # return HttpResponseRedirect("../"+id+"/delete")
        return HttpResponseRedirect("/")
    return render(request,'delete_view.html',context)

def detail_view(request,id):
    context={}
    context['data'] = GeeksModel.objects.get(id = id)
    return render(request,"detail_view.html",context)

def create_view(request):
    context ={}
    form = GeeksForm(request.POST or None)
    type = request.POST.get('post_type')
    print(type)
    if type == 'add_new_from_list':
        print('change to new function')
        print('\n')
        return HttpResponseRedirect('/')
    else:
        if form.is_valid():
            form.save()
            obj = GeeksModel.objects.last()
            print(obj.pk)
            return HttpResponseRedirect(str(obj.pk)+'/detail')
        else:
            context['form'] = form
            return render(request,"create_view.html",context)

def update_view(request,id):
    context = {}
    obj = get_object_or_404(GeeksModel,id = id)
    print('obj: '+'<br>')
    print(obj)
    form = GeeksForm(request.POST or None,instance = obj)
    print('form: '+'<br>')
    print(form)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id+'/detail')
    context['form'] = form
    return render(request,'update_view.html',context)

def list_view(request):
    context = {}
    all_obj = GeeksModel.objects.all()
    context['data'] = all_obj
    return render(request,'list_view.html',context)
