from django.shortcuts import render, redirect
from .models import Member, Payment, Attendance
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
def dashboard(request):
    total_members = Member.objects.count()
    total_payments = Payment.objects.count()
    total_attendance = Attendance.objects.count()
    return render(request, 'gymapp/dashboard.html', {
        'members': total_members,
        'payments': total_payments,
        'attendance': total_attendance
    })


def members_list(request):
    members = Member.objects.all()
    return render(request, 'gymapp/members.html', {'members': members})


def add_member(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        membership = request.POST.get('membership')
        Member.objects.create(name=name, email=email, phone=phone, membership_type=membership)
        return redirect('members')
    return render(request, 'gymapp/add_member.html')


def payments_list(request):
    payments = Payment.objects.all()
    return render(request, 'gymapp/payments.html', {'payments': payments})


def attendance_page(request):
    attendance = Attendance.objects.all()
    return render(request, 'gymapp/attendance.html', {'attendance': attendance})



def admin_login(request):
    # POST request
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:  # only staff/admin
            login(request, user)
            return redirect('/admin/')  # go to admin dashboard
        else:
            messages.error(request, "Invalid credentials or not staff user")

    # GET request
    return render(request, 'admin_login.html')  # your template
