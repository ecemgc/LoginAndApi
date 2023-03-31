from django.urls import path
from .views import CreateAndListEmployeeView, EmployeeView

urlpatterns = [
    path('', CreateAndListEmployeeView.as_view()),
    path('<int:pk>', EmployeeView.as_view()),
    
]