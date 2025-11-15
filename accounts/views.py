from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Profile


# ⭐ إنشاء حساب جديد
def register_view(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        # تحقق من تطابق كلمة المرور
        if password != confirm:
            messages.error(request, "كلمة المرور غير متطابقة")
            return redirect('register')

        # تحقق إن كان اسم المستخدم مستخدم مسبقًا
        if User.objects.filter(username=username).exists():
            messages.error(request, "اسم المستخدم مستخدم مسبقًا")
            return redirect('register')

        # إنشاء المستخدم
        user = User.objects.create_user(
            username=username,
            password=password
        )

        # إنشاء ملف Profile وربط رقم الجوال
        Profile.objects.create(
            user=user,
            phone=phone
        )

        messages.success(request, "تم إنشاء الحساب بنجاح! يمكنك تسجيل الدخول الآن.")
        return redirect('login')

    return render(request, 'accounts-templates/register.html')



# ⭐ تسجيل الدخول
def login_view(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        # التحقق من صحة البيانات
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "تم تسجيل الدخول بنجاح")
            return redirect('/')      # الصفحة الرئيسية
        else:
            messages.error(request, "بيانات الدخول غير صحيحة")
            return redirect('login')

    return render(request, 'accounts-templates/login.html')
