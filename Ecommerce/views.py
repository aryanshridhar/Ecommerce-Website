from django.shortcuts import render , redirect
from django.contrib import messages
from django.http import HttpResponse 
from .models import Product , Review , Cart
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

def homepage(request): 
    products = list(Product.objects.all())
    desc_list = [products[i].desc for i in range(0,len(products))]
    category = {products[i].category for i in range(len(products))}
    length = list(map(len , desc_list))
    items = {'pro' : products , 'number' : len(products) , 'category':category , 'length': length}
    return render(request , 'Ecommerce/index.html' , items)

def checkout(request): 
    return HttpResponse('<h3>This page is under construction</h3>')

def productview(request , myid):
    pressed_pro = list(Product.objects.filter(id=myid))[0]
    incart = list(Cart.objects.filter(Item_id = myid))
    username = None
    if request.user.is_authenticated:
        username = request.user
    selected_review = list(filter(lambda item: item.for_product == pressed_pro , list(Review.objects.all())))
    form = ReviewForm(request.POST or None)
    if form.is_valid() and 'reviewbtn' in request.POST: #handling multiple forms
        user_review = form.cleaned_data['Review']
        model = Review(for_product = pressed_pro , Name = username , Review = user_review)
        model.save()
        messages.success(request , 'Your review has been posted successfully !')
        return redirect(f'http://127.0.0.1:8000/Ecommerce/productview/{myid}') #handling multiple forms in a single page
    if request.method == 'POST' and 'cartbtn' in request.POST:
        if myid in Cart.objects.values_list('Item_id' , flat = True):
            to_increase = list(Cart.objects.filter(Item_id = myid))[0]
            to_increase.quantity += 1
            to_increase.save()
        else:
            CartModel = Cart(Item = pressed_pro , foruser = username , quantity = 1 , price = pressed_pro.price)
            CartModel.save()
        messages.success(request , 'The item has been added to your cart , Check you cart <a href = "http://127.0.0.1:8000/Ecommerce/cart">here</a>')
        return redirect(f'http://127.0.0.1:8000/Ecommerce/productview/{myid}')
    if request.method == 'POST' and 'remove' in request.POST:
        to_delete = list(Cart.objects.filter(Item_id = myid))[0]
        to_delete.delete()
        messages.success(request , f'{to_delete} has been removed from your cart')
        return redirect(f'http://127.0.0.1:8000/Ecommerce/productview/{myid}')
    item = {'pro': pressed_pro , 'form' : form , 'review' : selected_review,  'full_name' : username , 'incart' : incart}
    return render(request , 'Ecommerce/productview.html' , item)

def products(request , value):
    products = list(filter(lambda item: item.category == value , list(Product.objects.all())))
    total_items = len(products)
    context = {'name' : value , 'products' : products , 'total' : total_items}
    return render(request , 'Ecommerce/products.html' , context)

@login_required(login_url = '/profile/login')
def cart(request): 
    current_user = request.user 
    total= sum(map(lambda x:x.quantity*x.price ,Cart.objects.filter(foruser = current_user)))
    cart_products = list(zip(Cart.objects.filter(foruser = current_user) ,map(lambda x:x.quantity ,Cart.objects.filter(foruser = current_user)) , map(lambda x:x.quantity*x.price ,Cart.objects.filter(foruser = current_user))))
    context = {'item' : cart_products , 'total' : total}
    return render(request , 'Ecommerce/cart.html' , context)

def contact(request): 
    return render(request , 'Ecommerce/contact.html')
