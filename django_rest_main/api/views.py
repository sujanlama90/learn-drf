from students.models import Students
from .serializers import StudentSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET','POST'])
def studentView(request):
    if request.method == 'GET':
        #get all data from the students table
        students = Students.objects.all()
        serializer = StudentSerializers(students,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    