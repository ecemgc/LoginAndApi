from django.urls import path
from .views import CreateAndListDemandView, DemandView

urlpatterns = [
    path('', CreateAndListDemandView.as_view()),
    path('<int:pk>', DemandView.as_view())
]