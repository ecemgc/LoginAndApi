from django.urls import path
from .views import CreateAndListProduct, ProductView

urlpatterns = [
    path('', CreateAndListProduct.as_view()),
    path('<int:pk>', ProductView.as_view())
]