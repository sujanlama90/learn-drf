from students.models import Students
from .serializers import StudentSerializers,EmployeeSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employees.models import Employee
from django.http import Http404
from rest_framework import mixins, generics
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

@api_view(['GET','PUT','DELETE'])
def studentDetailView(request,pk):
    try:
        student = Students.objects.get(pk=pk)
    except Students.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializers(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer =StudentSerializers(student,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class Employees(APIView):
#     def get(self,request):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializers(employees,many = True)
#         return Response(serializer.data,status=status.HTTP_200_OK)

#     def post(self,request):
#         serilizer = EmployeeSerializers(data = request.data)
#         if serilizer.is_valid():
#             serilizer.save()
#             return Response(serilizer.data,status=status.HTTP_201_CREATED)
#         return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)

# class EmployeesDetailView(APIView):
#     def get_object(self,pk):
#         try:
#             return Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist():
#             raise Http404

#     def get(self,request,pk):
#         employee = self.get_object(pk)
#         serilizer = EmployeeSerializers(employee)
#         return Response(serilizer.data,status=status.HTTP_200_OK)
    
#     def put(self,request,pk):
#         empolyee = self.get_object(pk)
#         serilizer = EmployeeSerializers(empolyee,data = request.data)
#         if serilizer.is_valid():
#             serilizer.save()
#             return Response(serilizer.data,status=status.HTTP_201_CREATED)
#         return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)

#     def delete(self,request,pk):
#         employee = self.get_object(pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# Mixins
'''
class Employees(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers

    def get(self,request):
         return self.list(request)

    def post(self,request):
        return self.create(request)

class EmployeesDetailView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers

    def get(self, request, pk):
        return self.retrieve(request,pk)

    def put(self,request,pk):
        return self.update(request,pk)

    def delete(self,request,pk):
        return self.destroy(request,pk)
'''
# Generics
class Employees(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers

class EmployeesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    lookup_field = 'pk'