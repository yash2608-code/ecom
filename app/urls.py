from django.contrib import admin
from django.urls import path,include
from app.views import *

urlpatterns = [

        # Path urls 
        path('',index,name="index"),
        path('signup/',signup,name="signup"),
        path('signin/',signin,name="signin"),
        path('Aboutus/',Aboutus,name="Aboutus"),

        path('Account_Address/',Account_Address,name="Account_Address"),

        path('Account_Deshboard/',Account_Deshboard,name="Account_Deshboard"),

        path('Account_Download/',Account_Download,name="Account_Download"),

        path('Account_Orders/',Account_Orders,name="Account_Orders"),

        path('Account_payment_method/',Account_payment_method,name="Account_payment_method"),

        path('Account_user_details/',Account_user_details,name="Account_user_details"),

        path('Authentication_forgot_password/',Aauthentication_forgot_password,name="Aauthentication_forgot_password"),

        path('Aauthentication_reset_password/',Aauthentication_reset_password,name="Aauthentication_reset_password"),

        path('Blog/',Blog,name="Blog"),

        path('Checkout_complete/',Checkout_complete,name="Checkout_complete"),

        path('Checkout_details/',Checkout_details,name="Checkout_details"),

        path('Checkout_payment/',Checkout_payment,name="Checkout_payment"),

        path('Checkout_review/',Checkout_review,name="Checkout_review"),

        path('Checkout_shipping/',Checkout_shipping,name="Checkout_shipping"),

        path('Contact_Us/',Contact_Us,name="Contact_Us"),

        path('Order_tracking/',Order_tracking,name="Order_tracking"),

        path('Product_comparison/',Product_comparison,name="Product_comparison"),

        path('Product_details/',Product_details,name="Product_details"),

        path('Shop_cart/',Shop_cart,name="Shop_cart"),

        path('Shop_categories/',Shop_categories,name="Shop_categories"),

        path('Shop_grid_Top/',Shop_grid_Top,name="Shop_grid_Top"),

        path('Shop_grid_left/',Shop_grid_left,name="Shop_grid_left"),

        path('Shop_grid_right/',Shop_grid_right,name="Shop_grid_right"),

        path('Shop_list_Top/',Shop_list_Top,name="Shop_list_Top"),

        path('Shop_list_left/',Shop_list_left,name="Shop_list_left"),

        path('Shop_list_right/',Shop_list_right,name="Shop_list_right"),

        path('Single/',Single,name="Single"),

        path('Starter_Page/',Starter_Page,name="Starter_Page"),

        path('Wishlistdata/',Wishlistdata,name="Wishlistdata"),

        path("add-product-page/",AddProductPage,name="addproductpage"),

        path("seller-my-product/",SellerMyProduct,name="sellermyproduct"),

        path("update-product/<int:pk>/",UpdateProductPage,name="updateproduct"),
        # Functional Urls :-

        path('Register_data/',Register,name="Register"),
        path('Login_data',Login,name="Login"),
        path('logout/',Logout,name="logout"),
        path('Verify-Forgot-Email/',VerifyForgotEmail,name="VerifyForgotEmail"),
        path('Verify-forgot-OTP/',VerifyForgotOTP,name="VerifyForgotOTP"),
        path("update-user/",UpdateUser,name="update-user"),
        path("seller-add-product/",AddProduct,name="selleraddproduct"),
        path("update-products/<int:pk>/",UpdateProduct,name="updateproducts"),
        path("delete-product/<int:pk>/",DeleteProduct,name="delpro"),
        path("search-prod/",SearchProduct,name="searchprod"),
]
