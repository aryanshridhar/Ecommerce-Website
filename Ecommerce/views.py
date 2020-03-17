from django.shortcuts import render , redirect
from django.contrib import messages
from django.http import HttpResponse , JsonResponse
from .models import Product , Review , Cart
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializers import ProductApi ,ReviewApi
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import mixins , generics
from rest_framework.views import APIView

# Performing CRUD operations

#Way - 1

@csrf_exempt
def crudproducts(request,id = None):
    try:
        instance = Product.objects.filter(id=id)
    except:
        return JsonResponse(status=404)
    
    if request.method == 'GET':
        serial = ProductApi(instance , many = True)
        return JsonResponse(serial.data , safe=False)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        pro = ProductApi(instance , data=data)
        if pro.is_valid():
            pro.save()
            return JsonResponse(pro.data , status=200)
        return JsonResponse(pro.errors , status=400)

    elif request.method == 'DELETE':
        instance.delete()
        return JsonResponse(status=204)

@csrf_exempt
def crudprod(request):
    if request.method == 'GET':
        all_products = Product.objects.all()
        serial = ProductApi(all_products , many = True)
        return JsonResponse(serial.data , safe = False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serail = ProductApi(data=data)
        if serial.is_valid():
            serial.save()
            return JsonResponse(serial.data,status=200)
        return JsonResponse(serial.errors , status=400)

#Way - 2 -- Using classes

class ProductView(APIView):
    def get(self , request):
        products = Product.objects.all()
        serial = ProductApi(products , many = True)
        return JsonResponse(serial.data , status=200)
    
    def post(self , request):
        data = request.data
        serial = ProductApi(data=data)
        if serial.is_valid():
            serial.save()
            return JsonResponse(serial.data , status=201)
        return JsonResponse(serial.errors , status=400)

class ProductInstanceView(APIView):
    def get_object(self, id):
        try:
            return Product.objects.filter(id=id)
        except:
            return JsonResponse({'error':'the product is not found'} , status=404)
        
    def get(self , request , id = None):
        instance = self.get_object(id)
        serial = ProductApi(instance)
        return JsonResponse(serial.data , status=200)
    
    def put(self,request,id = None):
        data = request.data
        instance = self.get_object(id)
        serial = ProductApi(instance,data=data)
        if serial.is_valid():
            serial.save()
            return JsonResponse(serial.data , status=201)
        return JsonResponse(serial.errors , status=400)

    def delete(self,request,id=None):
        instance = self.get_object(id=id)
        instance.delete()
        return HttpResponse(status=204)
    
#Way-3 , the best if you are using classes 

class ProductListView(generics.GenericAPIView , 
                        mixins.ListModelMixin , 
                        mixins.CreateModelMixin , 
                        mixins.UpdateModelMixin , 
                        mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin):


    serializer_class = ProductApi
    queryset = Product.objects.all()
    lookup_field = id

    # perform_create(self, serializer) - Called by CreateModelMixin when saving a new object instance.
    # perform_update(self, serializer) - Called by UpdateModelMixin when saving an existing object instance.
    # perform_destroy(self, instance) - Called by DestroyModelMixin when deleting an object instance.

    #These hooks are particularly useful for setting attributes that are implicit in the request, 
    #but are not part of the request data. For instance, you might set an attribute on the 
    # object based on the request user, or based on a URL keyword argument.
    #These override points are also particularly useful for adding behavior that occurs before or after saving an object, 
    # such as emailing a confirmation, or logging the update.

    def get(self , request , id = None):
        if id:
            return self.retrieve(request,id)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def perform_create(self,serializer):
        serializer.save(created_by = self.request.user)

    def put(self , request , id = None):
        return self.update(request , id)
    
    def perform_update(self , serializer):
        serializer.save(created_by = self.request.user)

    def delete(self , request , id=None):
        return self.destory(request , id)

    
##########


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
