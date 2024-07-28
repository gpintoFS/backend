from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .auth_manager import UserManager
# Create your models here.

# UsuarioModelo video JWT en Django
class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=100, null=True, blank=True)
    lastname = models.CharField(max_length=100, null=True, blank=True)
    mail = models.EmailField(max_length=100, unique=True, null=True)
    password = models.TextField(null=False, blank=False)
    tipo = models.CharField(max_length=50, choices=[('ADMIN', 'ADMIN'), ('REGISTRO', 'REGISTRO'), ('CONSULTA', 'CONSULTA')], default='ADMIN', db_column='tipo')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #establecer campos para ingresar al panel administrativo
    USERNAME_FIELD = 'mail'

    #atributos requeridos para crear un superusuario
    REQUIRED_FIELDS = [ 'name', 'lastname']

    objects = UserManager()

    def __str__(self) -> str:
        return f"{self.user_id} {self.name}"
        
    class Meta:
        db_table = 'users'

class Department(models.Model):
    department_id = models.AutoField(primary_key=True, unique=True, null=False)
    department = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    #is_active = models.BooleanField(default=True)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.deparment_id} {self.name}"

    class Meta:
        db_table = 'departments'

class Branch(models.Model):
    branch_id = models.AutoField(primary_key=True, unique=True, null=False)
    location = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    #contact = models.TextField(null=True, blank=True)        
    #is_active = models.BooleanField(default=True)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.branch_id} {self.name}"

    class Meta:
        db_table = 'branches'

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=255, null=True, blank=True)    
    #contact = models.TextField(null=True, blank=True)        
    #is_active = models.BooleanField(default=True)
    department_id = models.ForeignKey(
        Department, on_delete=models.CASCADE, blank=True, null=True)
    branch_id = models.ForeignKey(
        Branch, on_delete=models.CASCADE, blank=True, null=True)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.employee_id} {self.name}"

    class Meta:
        db_table = 'employees'

class Category(models.Model):
    category_id = models.AutoField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    #is_active = models.BooleanField(default=True)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.category_id} {self.name}"

    class Meta:
        db_table = 'categories'

class Item(models.Model):
    item_id = models.AutoField(primary_key=True, unique=True, null=False)
    tag = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    serial_number = models.CharField(max_length=255, null=True, blank=True)
    cost = models.FloatField(null=True, blank=True)
    date_purchased = models.DateTimeField(null=False, blank=False)
    quantity = models.PositiveIntegerField(default=0)
    #is_active = models.BooleanField(default=True)
    category_id = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True, null=True)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    #image = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'items'

class EmployeeAssigment(models.Model):
    assigment_id = models.AutoField(primary_key=True, unique=True, null=False)    
    quantity = models.PositiveIntegerField(default=0)
    condition = models.CharField(max_length=255, null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)
    date_assigned = models.DateTimeField(null=False, blank=False)    
    employee_id = models.ForeignKey(
        Employee, on_delete=models.CASCADE, blank=True, null=True)
    item_id = models.ForeignKey(
        Item, on_delete=models.CASCADE, blank=True, null=True)
    branch_id = models.ForeignKey(
        Branch, on_delete=models.CASCADE, blank=True, null=True)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'employeeassigments'

class TransferHistory(models.Model):
    history_id = models.AutoField(primary_key=True, unique=True, null=False)        
    transferred_from = models.CharField(max_length=255, null=True, blank=True)
    transferred_to = models.CharField(max_length=255, null=True, blank=True)    
    quantity = models.PositiveIntegerField(default=0)
    date_transfer = models.DateTimeField(null=False, blank=False)  
    remarks = models.CharField(max_length=255, null=True, blank=True)
    item_id = models.ForeignKey(
        Item, on_delete=models.CASCADE, blank=True, null=True)    
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'transferhistories'