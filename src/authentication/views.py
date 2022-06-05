from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django import views
from django.utils.decorators import method_decorator

# mine
from product.models import Product


def index(request):
    products = Product.objects.all().order_by("created_at")

    return render(request, ('list_all.html'), {'products': products})


@method_decorator(login_required, name='dispatch')
class DashboardView(views.generic.TemplateView):
    template_name = 'dashboard.html'
