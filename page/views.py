from django.shortcuts import render,redirect
from .models import Products
# Create your views here.
def get_product(requset):
    product=Products.objects.all()
    context = {'product':product}
    return render(requset, 'product/list.html', context)


def detail_product(request, pk):
    product = Products.objects.get(pk=pk)
    context = {'product':product}
    return render(request, 'product/detail.html', context)

def create_product(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        description = request.POST.get('description')
        if title and price and description:
            Products.objects.create(
                title=title,
                price=price,
                description=description
            )
            return redirect('list')

    return render(request,  'product/create.html')


# update

def update_product(request, pk):
    product=Products.objects.get(pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title',product.title)
        price = request.POST.get('price',product.price)
        description = request.POST.get('description',product.description)
        product.title=title
        product.price=price
        product.description=description
        product.save()
        return redirect('list')
    else:
        return render(request,'product/update.html',{'product':product})


def delete_product(request, pk):
    product = Products.objects.get(pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('list')
    else:
        return render(request,'product/delete.html',{'product':product})
