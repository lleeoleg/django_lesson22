from django.urls import path
from api.views import api_rubrics, api_rubric_detail, APIRubrics, APIRubricDetail


app_name = 'api'

urlpatterns = [
    # path('rubrics/<int:pk>/', api_rubric_detail),
    path('rubrics/<int:pk>/', APIRubricDetail.as_view()),
    
     # path('rubrics/', api_rubrics),
    path('rubrics/', APIRubrics.as_view()),
]
