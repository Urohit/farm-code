from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import *
from .forms import ProductForm


# Create your views here.

def home(request):
    if request.method == 'POST':
        global first_name
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']                               
        
        
        if User.objects.filter(username=username).exists():                   
            messages.info(request, "username already taken")
            return redirect('/')
        elif password1!=password2:
            messages.info(request, "password not matching")
            return redirect('/')            
        elif User.objects.filter(email=email).exists():    
            messages.info(request, "email already exists")        
            return redirect('/')                                
        else:
            user = User.objects.create_user(username=username, password=password1, first_name=first_name, last_name=last_name, email=email)
            user.save()
            messages.info(request, "Congrats! You have been registered successfully.")            
            return redirect('login')            
    else:
        return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('user_panel')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('http://growpital.com')

def user_panel(request):
    investors = Investor.objects.all()
    invests = Investment.objects.all()
    orders = Order.objects.all()
    total_investors = investors.count()
    total_orders = orders.count()
    in_cart = orders.filter(status='In Cart').count()

    yearly_payout = []
    total_payout = []
    no_of_units = 1
    yearly_pay_outs = 0
    total_pay_outs = 0
    for inv in invests:
        total_investment = inv.inv_per_unit * no_of_units
        yearly_pay_outs = total_investment * (inv.return_per/100)
        total_pay_outs = yearly_pay_outs * inv.tenure
        yearly_payout.append(yearly_pay_outs)
        total_payout.append(total_pay_outs)


    context = {'total_payout': total_payout,'in_cart': in_cart,'investors': investors, 'invests': invests, 'total_investors': total_investors, 'total_orders': total_orders}
    return render(request, 'user_panel.html', context)

def navbar(request):
    return render(request, 'navbar.html')

def browse(request):
    invests = Investment.objects.all()

    monthly_payouts = 0
    for i in invests:
        monthly_payouts=i.inv_per_unit*.07
        monthly_payouts=round(monthly_payouts,2)
        
    context = {'invests': invests, 'monthly_payouts' : monthly_payouts}
    return render(request, 'browse.html', context)

def investor_page(request):
        
    context ={}
    return render(request, 'investor_page.html', context)


def investor_detail(request, pk):
    investors = Investor.objects.get(id=pk)
    orders = investors.order_set.all()
    invests = Investment.objects.all()
    orders_count = orders.count()
    context ={'invests': invests,'investors':investors, 'orders': orders, 'orders_count': orders_count}
    return render(request, 'investor.html', context)           


def create_product(request):
    form  = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_panel')

    invests = Investment.objects.all()
    yearly_payout = []
    total_payout = []
    no_of_units = 1
    yearly_pay_outs = 0
    total_pay_outs = 0
    for inv in invests:
        total_investment = inv.inv_per_unit * no_of_units
        yearly_pay_outs = total_investment * (inv.return_per/100)
        total_pay_outs = yearly_pay_outs * inv.tenure
        yearly_payout.append(yearly_pay_outs)
        total_payout.append(total_pay_outs)
        

    context = {'form': form, 'total_investment': total_investment, 'yearly_pay_outs': yearly_pay_outs, 'total_pay_outs': total_pay_outs}
    return render(request, 'product_form.html', context)
