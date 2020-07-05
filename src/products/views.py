from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm
# Create your views here.
# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#     my_context = {
#         "form" : my_form
#     }
#     return render(request, "products/product_create.html", my_context)

def product_create_view(request):
    # initial value for form
    initial_data = {
        "title" : "This is my title"
    }
    # form = ProductForm(request.POST or None, initial=initial_data)
    
    # Get object from database
    obj = Product.objects.get(id=1)
    # form = ProductForm(request.POST or None, instance=obj)
    
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        # form = ProductForm()
        return redirect('/product')

    my_context = {
        'form' : form
    }
    return render(request, "products/product_create.html", my_context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # my_context = {
    #     'title' : obj.title,
    #     'description' : obj.description,
    #     'price' : obj.price,
    #     'summary' : obj.summary,
    #     'featured' : obj.featured
    # }

    my_context = {
        'object' : obj
    }
    return render(request, "products/product_detail.html", my_context)

def dynamic_lookup_view(request, id):
    # obj = Product.objects.get(id=id)
    # obj = get_object_or_404(Product, id=id)
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    my_context = {
        "object" : obj
    }
    return render(request, "products/product_detail.html", my_context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":    
        obj.delete()
        # return redirect('/product')
        return redirect('../../')
    my_context = {
        "object" : obj
    }
    return render(request, "products/product_delete.html", my_context)
    

def product_list_view(request):
    query_set = Product.objects.all()
    my_context={
        "object_list" : query_set
    }
    return render(request, "products/product_list.html", my_context)
