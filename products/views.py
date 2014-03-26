from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.views import generic
from django.forms import ModelForm, Textarea
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from datetime import datetime
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

from products.models import Product, Opinion

class IndexView(generic.ListView):
    template_name = 'products/index.html'
    context_object_name = 'product_list'
    encoding = 'utf8'

    def get_queryset(self):
        return Product.objects.all()

class DetailView(generic.DetailView):
    model = Product
    template_name = 'products/detail.html'
    encoding = 'utf8'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['form'] = OpinionForm
        return context

#search by product description
def filteredIndexView(request):
    request.encoding = 'utf8'
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        products = Product.objects.filter(description__icontains=q)
        return render(request, 'products/index.html',
            {'product_list': products})
    else:
        products = Product.objects.all()
        return render(request, 'products/index.html',
            {'product_list': products})

class OpinionForm(ModelForm):
   class Meta:
        model = Opinion
        exclude = ["post"]
        fields = ['login', 'text']
        labels = {
            'text': ('Opinion'),
        }
        widgets = {
            'text': Textarea(attrs={'cols': 30, 'rows': 10}),
        }

def addOpinion(request, pk):
    request.encoding = 'utf8'
    p = request.POST

    if p.has_key("text") and p["text"]:
        product = Product.objects.get(id=int(pk))
        opinion = Opinion.create()
        opinion.product = product
        opinion.login = "Anonim"
        if p.has_key("login") and p["login"]:
            opinion.login = p["login"]
        opinion.text = p["text"]
        opinion.pub_date = datetime.now()
        opinion.save()
    return HttpResponseRedirect(reverse("products.views.post", args=[pk]))

def post(request, pk):
    request.encoding = 'utf8'
    product = Product.objects.get(pk=int(pk))
    opinions = Opinion.objects.filter(product=product)
    d = dict(product=product, opinions=opinions, form=OpinionForm(), user=request.user)
    d.update(csrf(request))
    return render_to_response("products/detail.html", d)

@csrf_exempt
def vote(request, pk):
    request.encoding = 'utf8'
    p = request.POST
    product = Product.objects.get(id=int(pk))
    mark = p.get('mark', False)
    product.mark = (product.mark * product.voters + int(mark)) / (product.voters + 1);
    product.voters = product.voters + 1;
    product.save();

    return render_to_response("products/detail.html", {'product': product})