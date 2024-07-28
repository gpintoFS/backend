from rest_framework.serializers import ModelSerializer
from .models import Branch, Category, Department, Employee, EmployeeAssigment, Item, TransferHistory, User
from django.contrib.auth.hashers import make_password
# Luego de importar las clases podemos crear los serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass

class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('mail', 'name', 'lastname' )

class BranchSerializer(ModelSerializer):
    class Meta:        
        model = Branch        
        fields = '__all__'

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class DepartmentSerializer(ModelSerializer):
    class Meta:        
        model = Department        
        fields = '__all__'

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class EmployeeAssigmentSerializer(ModelSerializer):
    class Meta:        
        model = EmployeeAssigment        
        fields = '__all__'

class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class TransferHistorySerializer(ModelSerializer):
    class Meta:
        model = TransferHistory
        fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    # queremos pasar el password de un texto a un hash
    def create(self, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)