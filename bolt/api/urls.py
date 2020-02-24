from django.urls import path
from .views import *

urlpatterns = [
    path('recognize/', FileUploadView.as_view())
]
