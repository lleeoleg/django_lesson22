from django.urls import path, include
from api.views import api_rubrics, api_rubric_detail, APIRubrics, APIRubricDetail
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

app_name = 'api'

urlpatterns = [
    # path('rubrics/<int:pk>/', api_rubric_detail),
    path('rubrics/<int:pk>/', APIRubricDetail.as_view()),
     # path('rubrics/', api_rubrics),
    path('rubrics/', APIRubrics.as_view()),
    
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('drf-auth/', include('rest_framework.urls')),
]
