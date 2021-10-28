from django.shortcuts import redirect, render
from .models import *
from django.conf import settings
from django.core.mail import send_mail
import random
# Create your views here.

def GetCategories():
    cat = Categories.objects.all()
    return cat

def index(request):
    print("CALLED")
    return render(request,'app/index.html',{'cat':GetCategories()})


def signup(request):
    return render(request,'app/authentication-signup.html')


def signin(request):
    return render(request,'app/authentication-signin.html')

def Aboutus(request):
    return render(request,'app/about-us.html')


def Account_Address(request):
    return render(request,'app/account-addresses.html')

def Account_Deshboard(request):
    return render(request,'app/account-dashboard.html')

def Account_Download(request):
    return render(request,'app/account-downloads.html')

def Account_Orders(request):
    return render(request,'app/account-orders.html')

def Account_payment_method(request):
    return render(request,'app/account-payment-methods.html')

def Account_user_details(request):
    admin = Admin.objects.get(id=request.session['id'])
    if admin.Role == "User":
        user = User.objects.get(Admin=admin)
    elif admin.Role == "Seller":
        user = Seller.objects.get(Admin=admin)
    else:
        pass
    return render(request,'app/account-user-details.html',{'uid':user})

def Aauthentication_forgot_password(request):
    return render(request,'app/authentication-forgot-password.html')

def Aauthentication_reset_password(request):
    if 'femail' in request.session:
        em = Admin.objects.get(Email=request.session['femail'])
        return render(request,'app/authentication-reset-password.html',{'us':em})
    else:
        return redirect("Aauthentication_forgot_password")

def Blog(request):
    return render(request,'app/blog.html')

def Checkout_complete(request):
    return render(request,'app/checkout-complete.html')

def Checkout_details(request):
    return render(request,'app/checkout-details.html')

def Checkout_payment(request):
    return render(request,'app/checkout-payment.html')

def Checkout_review(request):
    return render(request,'app/checkout-review.html')

def Checkout_shipping(request):
    return render(request,'app/checkout-shipping.html')

def Contact_Us(request):
    return render(request,'app/contact-us.html')

def Order_tracking(request):
    return render(request,'app/order-tracking.html')

def Product_comparison(request):
    return render(request,'app/product-comparison.html')

def Product_details(request):
    return render(request,'app/product-details.html')

def Shop_cart(request):
    return render(request,'app/shop-cart.html')

def Shop_categories(request):
    return render(request,'app/shop-categories.html')

def Shop_grid_Top(request):
    return render(request,'app/shop-grid-filter-on-top.html')

def Shop_grid_left(request):
    return render(request,'app/shop-grid-left-sidebar.html')

def Shop_grid_right(request):
    return render(request,'app/shop-grid-right-sidebar.html')

def Shop_list_Top(request):
    return render(request,'app/shop-list-filter-on-top.html')

def Shop_list_left(request):
    return render(request,'app/shop-list-left-sidebar.html')

def Shop_list_right(request):
    return render(request,'app/shop-list-right-sidebar.html')

def Single(request):
    return render(request,'app/single.html')

def Starter_Page(request):
    return render(request,'app/starter-page.html')

def Wishlistdata(request):
    return render(request,'app/wishlist.html')

def AddProductPage(request):
    cat = Categories.objects.all()
    return render(request, "app/add-product.html",{'cat':cat})

def SellerMyProduct(request):
    sid = Seller.objects.get(Admin=request.session['id'])
    pid = Product.objects.all().filter(Seller=sid)
    print(f"SID------->{sid},PID-------->{pid}")
    return render(request, "app/seller-my-products.html",{'products':pid})

# Functional logic 
def Register(request):
    if request.method == "POST":
        
        role=request.POST['role']
        fname=request.POST['fname']
        lname=request.POST['lname']
        addr=request.POST['address']
        phone= int(request.POST['phone'])
        bdate=request.POST['bdate']
        gender=request.POST['gender']
        email=request.POST['email']
        passwd=request.POST['passwd']

        try:
            tc=request.POST['tc']
            tc = True

            admin = Admin.objects.filter(Email=email)
            if len(admin)>0:
                msg="User Already Exist"
                return render(request,"app/authentication-signup.html",{'err':msg})
            else:
                createadmin=Admin.objects.create(Role=role,Email=email,passwd=passwd,t_c=tc)
                if createadmin.Role == "User":
                    createuser=User.objects.create(Admin=createadmin,Firstname=fname,Lastname=lname,Address=addr,phone=phone,bdate=bdate,Gender=gender)
                    return redirect('index')
                elif createadmin.Role == "Seller":
                    createseller=Seller.objects.create(Admin=createadmin,Firstname=fname,Lastname=lname,Address=addr,phone=phone,bdate=bdate,Gender=gender)
                    return redirect('index')
                else:
                    pass

        except Exception as err:
            err,tc= f"{err}",False 
            print(err,tc)
            msg="Please Accept Terms And Condition"
            return render(request,"app/authentication-signup.html",{'err':msg})
        return render(request,'app/authentication-signup.html')
    
    return redirect("index")

def Login(request):
    role=request.POST['role']
    em=request.POST['email']
    passwd=request.POST['passwd']

    admin=Admin.objects.filter(Role=role,Email=em)
    print(admin)
    if len(admin)>0:
        if admin[0].passwd==passwd:
            if admin[0].Role == 'Seller':
                sel = Seller.objects.get(Admin=admin[0])
                request.session['srole'] = admin[0].Role
                request.session['id'] = admin[0].id
                request.session['sfname'] = sel.Firstname
                request.session['semail'] = admin[0].Email
                return redirect('index')
            elif admin[0].Role == 'User':
                usr = User.objects.get(Admin=admin[0])
                request.session['urole'] = admin[0].Role
                request.session['id'] = admin[0].id
                request.session['ufname'] = usr.Firstname
                request.session['uemail'] = admin[0].Email
                return redirect('index')
        else:
            msg="Password is Incorrect"
            return render(request,'app/authentication-signin.html',{'err':msg})
    else:
        msg="User Doesn't Exist,Please Register"
        return render(request,'app/authentication-signin.html',{'err':msg})

def Logout(request):
    logadmin = Admin.objects.get(id=request.session['id'])
    if logadmin.Role == "Seller":
        del request.session['srole']
        del request.session['id']
        del request.session['sfname']
        del request.session['semail']
        return redirect('index')
    elif logadmin.Role == "User":
        del request.session['urole']
        del request.session['id']
        del request.session['ufname']
        del request.session['uemail']
        return redirect('index')
    else:
        pass

def VerifyForgotEmail(request):
    email = request.POST['email']

    admin = Admin.objects.filter(Email=email)
    if len(admin)>0:
        # OTP Saving
        otp = random.randint(100000,999999)
        admin[0].Fotp = otp
        admin[0].save()
        # Forgot Email Sending
        Subject = 'Forgot Password Mail'
        Message = f'Hello This Is Your OTP---------->{otp}'
        emailFrom = settings.EMAIL_HOST_USER
        recipientList = [email, ]
        send_mail(Subject, Message, emailFrom, recipientList)
        # Storing Forgot Email in Session
        request.session['femail'] = email
        return redirect("Aauthentication_reset_password")
    else:
        msg = "Email Doesn't Exist"
        return render(request,'app/authentication-forgot-password.html',{'err':msg})

    return redirect("Aauthentication_forgot_password")

def VerifyForgotOTP(request):
    otp = int(request.POST['fotp'])
    npaswd = request.POST['npaswd']
    cpaswd = request.POST['cpaswd']

    admin = Admin.objects.get(Email=request.session['femail'])

    if admin.Fotp == otp:
        if npaswd == cpaswd:
            admin.passwd = cpaswd
            admin.save()
            del request.session['femail']
            return redirect("signin")
        else:
            msg = "Password doesn't match"
            return render(request,'app/authentication-reset-password.html',{'err':msg})
    else:
        msg = "OTP is incorrect, Check your OTP"
        return render(request,'app/authentication-reset-password.html',{'err':msg})

def UpdateUser(request):
    admin = Admin.objects.get(id=request.session['id'])
    if admin.Role == "User":
        user = User.objects.get(Admin=admin)
        user.Firstname = request.POST['fname'] if request.POST['fname'] else user.Firstname
        user.Lastname = request.POST['lname'] if request.POST['lname'] else user.Lastname
        user.Address = request.POST['address'] if request.POST['address'] else user.Address
        user.phone = request.POST['phone'] if request.POST['phone'] else user.phone
        
        Check_Eml = Admin.objects.filter(Email=request.POST['email'])
        if len(Check_Eml)>0:
            msg = "Email Already Exist"
            return render(request,'app/account-user-details.html',{'err':msg,'uid':user  })
        else:
            admin.Email = request.POST['email'] if request.POST['email'] else admin.Email
        admin.passwd = request.POST['passwd'] if request.POST['passwd'] else admin.passwd
        user.save()
        admin.save()
        return redirect("Account_user_details")
    elif admin.Role == "Seller":
        user = Seller.objects.get(Admin=admin)
        user.Firstname = request.POST['fname'] if request.POST['fname'] else user.Firstname
        user.Lastname = request.POST['lname'] if request.POST['lname'] else user.Lastname
        user.Address = request.POST['address'] if request.POST['address'] else user.Address
        user.phone = request.POST['phone'] if request.POST['phone'] else user.phone
        
        Check_Eml = Admin.objects.filter(Email=request.POST['email'])
        if len(Check_Eml)>0:
            msg = "Email Already Exist"
            return render(request,'app/account-user-details.html',{'err':msg,'uid':user  })
        else:
            admin.Email = request.POST['email'] if request.POST['email'] else admin.Email
        admin.passwd = request.POST['passwd'] if request.POST['passwd'] else admin.passwd
        user.save()
        admin.save()
        return redirect("Account_user_details")
    else:
        pass

def AddProduct(request):
    cat = request.POST['cat']
    pimg1 = request.FILES['pimg1']
    pimg2 = request.FILES['pimg2']
    pimg3 = request.FILES['pimg3']
    pname = request.POST['pname'].casefold()
    pdes = request.POST['pdes']
    pprice = float(request.POST['pprice'])

    aid = Admin.objects.get(id=request.session['id'])
    sid = Seller.objects.get(Admin=aid)
    cat = Categories.objects.get(category_name=cat)

    uppro = Product.objects.create(
        Seller=sid,
        cat=cat,
        pimg1=pimg1,
        pimg2=pimg2,
        pimg3=pimg3,
        pname=pname,
        pdes=pdes,
        price=pprice
        )
    return redirect("Account_Deshboard")

def UpdateProductPage(request,pk):
    pid = Product.objects.get(pk=pk)
    cat = Categories.objects.all()
    print(pid)
    return render(request, "app/updateProduct.html",{'pid':pid,'cat':cat})


def UpdateProduct(request,pk):
    pro = Product.objects.get(pk=pk)
    print(f"GOT PRODUCT FOR UPDATE------->{pro}")
    pro.cat.category_name = request.POST['cat'] if request.POST['cat'] else pro.cat.category_name
    
    if 'upimg1' in request.FILES:
        pro.pimg1 = request.FILES['upimg1'] if request.FILES['upimg1'] else pro.pimg1
    if 'upimg2' in request.FILES:
        pro.pimg2 = request.FILES['upimg2'] if request.FILES['upimg2'] else pro.pimg2
    if 'upimg3' in request.FILES:
        pro.pimg3 = request.FILES['upimg3'] if request.FILES['upimg3'] else pro.pimg3

    pro.pname = request.POST['pname'].casefold() if request.POST['pname'].casefold() else pro.pname
    pro.pdes = request.POST['pdes'] if request.POST['pdes'] else pro.pdes
    pro.price = float(request.POST['pprice']) if float(request.POST['pprice']) else pro.price
    pro.save()
    return redirect("sellermyproduct")

def DeleteProduct(request,pk):
    pro = Product.objects.get(pk=pk)
    print(f"GOT PRODUCT FOR DELETE------->{pro}")
    pro.delete()
    return redirect("sellermyproduct")

def SearchProduct(request):
    pro = request.GET['sprod'].casefold()
    cat = request.GET['scat']
    print(f"IN SEARCH PRODUCT------->{pro,cat}")
    if pro == '' and cat == "All Categories":
        print("IN IF")
        getpro = Product.objects.all()
        for i in getpro:
            print("SEARCHED PRODUCT------->",i.pname,i.id)
        return render(request, "app/shop-grid-filter-on-top.html",{'pro':pro,'prod':getpro,'cat':GetCategories()})
        
        # if request.GET['searchbase'] == "filter":
        #     fp = request.GET['fprice']
        #     sr = request.GET['sort']

        #     if fp:
        #         fprng = fp.split("to")
        #         print("FPRNG---------->",fprng)
        #         return render(request, "app/shop-grid-filter-on-top.html",{'pro':pro,'prod':getpro,'cat':GetCategories()})

    if pro and cat == "All Categories":
        print("IN PRO-CAT-ALL IF")
        getpro = Product.objects.all().filter(pname__startswith=pro)
        for i in getpro:
            print("SEARCHED PRODUCT------->",i.pname,i.id)
        return render(request, "app/shop-grid-filter-on-top.html",{'pro':pro,'prod':getpro,'cat':GetCategories()})

    if pro and cat:
        print("IN PRO-CAT IF")
        getcat = Categories.objects.get(category_name=cat)
        getpro = Product.objects.all().filter(pname__startswith=pro,cat=getcat)
        for i in getpro:
            print("SEARCHED PRODUCT------->",i.pname,i.id)
        return render(request, "app/shop-grid-filter-on-top.html",{'pro':pro,'prod':getpro,'cat':GetCategories()})