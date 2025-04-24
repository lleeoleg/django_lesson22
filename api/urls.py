from django.urls import path
from api.views import api_rubrics, api_rubric_detail


app_name = 'api'

urlpatterns = [
    path('rubrics/', api_rubrics),
    path('rubrics/<int:pk>', api_rubric_detail)
]
