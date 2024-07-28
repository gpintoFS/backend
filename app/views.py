from .models import Branch, Category, Department, Employee, EmployeeAssigment, Item, TransferHistory, User  # model
from .serializers import BranchSerializer, CategorySerializer, DepartmentSerializer, EmployeeSerializer, EmployeeAssigmentSerializer, ItemSerializer, TransferHistorySerializer, UserSerializer  # serializer
# la clase de rest framework que permite crear un CRUD
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, status

from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import CustomTokenObtainPairSerializer, CustomUserSerializer
from rest_framework.generics import GenericAPIView

from .permissions import SoloAdministrador

class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        mail = request.data.get('mail', '')
        password = request.data.get('password', '')
        user = authenticate(
            mail=mail,
            password=password
        )

        if user:
            logim_serializer = self.serializer_class(data=request.data)
            if logim_serializer.is_valid():
                user_serializer = CustomUserSerializer(user)
                return Response({
                    'token': logim_serializer.validated_data.get('access'),
                    'refresh-token': logim_serializer.validated_data.get('refresh'),
                    'user': user_serializer.data,
                    'message': 'Login exitoso'
                }, status=status.HTTP_200_OK)
            return Response({'error': 'Datos incorrectos'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Datos incorrectos'}, status=status.HTTP_400_BAD_REQUEST)

class Logout(GenericAPIView):
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(user_id=request.data.get('user', 0))
        
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message': 'Logout exitoso'}, status=status.HTTP_200_OK)
        return Response({'error': 'Usuario no existe'}, status=status.HTTP_400_BAD_REQUEST)

class BranchViewSet(ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeAssigmentViewSet(ModelViewSet):
    queryset = EmployeeAssigment.objects.all()
    serializer_class = EmployeeAssigmentSerializer

class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class TransferHistoryViewSet(ModelViewSet):
    queryset = TransferHistory.objects.all()
    serializer_class = TransferHistorySerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, SoloAdministrador]
    
    


