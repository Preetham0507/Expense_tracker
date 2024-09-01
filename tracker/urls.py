from . import views
from django.urls import path

urlpatterns = [
    path('login/',views.login_view,name="login"),
    path('register/',views.register_view,name="register"),
    path('logout/',views.logout_view,name="logout_view"),
    path('',views.index,name="index"),
    path('delete-transaction/<id>',views.delete_transaction,name="delete_transaction")
]