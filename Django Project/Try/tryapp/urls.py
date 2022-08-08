from django.urls import path
from .views import *


urlpatterns = [
    path("", index, name="home"),
    path("contact/", contact, name="contact"),
    path("signup/", signup, name="signup"),
    path("signin/", signin, name="signin"),
    path("signout/", signout, name="signout"),
    path("profile/", profile, name="profile"),
    path("change_password/", change_password, name="change_password"),

    path("view_product/<int:pk>/",view_product,name="view_product"),

    # path("view_product/<int:pk>/", view_product, name="view_product"),

    
    path("seller-home/", seller_index, name="seller_home"),
    path("seller-signup/", seller_signup, name="seller_signup"),
    path("seller-signin/", seller_signin, name="seller_signin"),
    path("seller-signout/", seller_signout, name="seller_signout"),
    path("add-product/", add_product, name="add_product"),
    path("view-product/<int:pk>/", view_product_seller, name="view_product_seller"),
    path("delete-product/<int:pk>/", delete_product_seller, name="delete_product_seller"),
    path("edit-product/<int:pk>/", edit_product_seller, name="edit_product_seller"),

]