from django.shortcuts import render, redirect
from .models import *
from .forms import OrderForm, UserRegisterForm, CustomerForm
from .filters import OrderFilter

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .decorators import unauthenticated_user, allowed_users, admin_only

@unauthenticated_user
def register(request):

    form  = UserRegisterForm()

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'accounts/register.html', context={'form': form})

@unauthenticated_user
def login_view(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')

    context = {}
    return render(request, 'accounts/login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@admin_only
def dashboard(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()

    total_orders = orders.count()
    pending = orders.filter(status="Pending").count()
    delivered = orders.filter(status="Delivered").count()

    context = {
        "customers": customers,
        "orders": orders,
        "total_orders": total_orders,
        "pending": pending,
        "delivered": delivered,
    }

    return render(request, "accounts/dashboard.html", context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all()
    return render(request, "accounts/products.html", {"products": products})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customers(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    count = orders.count()

    orderFilter = OrderFilter(request.GET, queryset=orders)

    orders = orderFilter.qs

    context = {
        "customer": customer,
        "orders": orders,
        "total_orders": count,
        "filter": orderFilter,
    }
    return render(request, "accounts/customers.html", context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def create_order(request):
    form = OrderForm()

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")

    context = {"form": form}
    return render(request, "accounts/create_order.html", context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("dashboard")

    context = {"form": form}
    return render(request, "accounts/create_order.html", context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_order(request, pk):
    order = Order.objects.get(id=pk)

    if request.method == "POST":
        order.delete()
        return redirect("dashboard")

    context = {"item": order}
    return render(request, "accounts/delete_order.html", context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def user_view(request):

    orders = request.user.customer.order_set.all()

    total_orders = orders.count()
    pending = orders.filter(status="Pending").count()
    delivered = orders.filter(status="Delivered").count()

    context = {
        'orders': orders,
        "total_orders": total_orders,
        "pending": pending,
        "delivered": delivered,
    }

    return render(request, 'accounts/user.html', context=context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def profile_setting(request):

    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

    context = {'form': form}

    return render(request, 'accounts/profile_setting.html', context)
