from django.http import JsonResponse
from bboard.models import Rubric
from api.serializers import RubricSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response



# def api_rubrics(request):
#     if request.method == 'GET':
#         rubrics = Rubric.objects.all()
#         serializer = RubricSerializer(rubrics, many=True)
        
#         return JsonResponse(serializer.data, safe=False)



@api_view(['GET'])
def api_rubrics(request):
    rubrics = Rubric.objects.all()
    serializer = RubricSerializer(rubrics, many=True)

    return Response(serializer.data)
    
@api_view(['GET'])
def api_rubric_detail(request, pk):
    rubric = Rubric.objects.get(pk=pk)
    serializer = RubricSerializer(rubric)
    
    return Response(serializer.data)


    