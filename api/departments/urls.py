from django.urls import path
from .views import CreateAndListDepartmentView, DepartmentView

urlpatterns = [
    path('', CreateAndListDepartmentView.as_view()),
    path('<int:pk>', DepartmentView.as_view())
]