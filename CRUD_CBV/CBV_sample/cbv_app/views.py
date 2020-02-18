from django.shortcuts import render
from cbv_app import models
from django.views.generic.edit import CreateView,DeleteView,UpdateView,FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
# use self_defined Form
from cbv_app.forms import myForm
# Create your views here.

class cbv_create(CreateView):
    model = models.CBVModel
    fields = ['title','description']
    success_url = '/'


class cbv_detail(DetailView):
    model = models.CBVModel

    def get_context_data(self,*args,**kwargs):
        context_test = super(cbv_detail,self)
        # print(context_test)
        context = super(cbv_detail,self).get_context_data(*args,**kwargs)
    #     context["categories"]  = 'MISC'
        return context

class cbv_list(ListView):
    model = models.CBVModel
    # do a QUERY for exact url/id/method
    def get_queryset(self,*args,**kwargs):
        qs = super(cbv_list,self).get_queryset(*args,**kwargs)
        qs = qs.order_by("-id")
        return qs

class cbv_delete(DeleteView):
    model = models.CBVModel
    # to redirect after delete successfully
    success_url = '/'

class cbv_update(UpdateView):
    model = models.CBVModel
    fields = [
        'title',
        'description'
    ]
    obj = model.objects.last()
    success_url = 'detail/'+str(obj.pk)

# INDIVIDUAL template name
class cbv_my_form(FormView):
    form_class = myForm
    # template_name
    template_name = "cbv_app/myform.html"
    # after success_redirect
    success_url = '/thanks/'

    def form_valid(self,form):
        form.save()
        print('form_valid')
        return super().form_valid(form)
