# importar nuestra clase viewset
from .views import BranchViewSet, CategoryViewSet, DepartmentViewSet, EmployeeViewSet, EmployeeAssigmentViewSet, ItemViewSet, TransferHistoryViewSet, UserViewSet
# importar el router de DRF (Django Rest Framework)
from rest_framework.routers import DefaultRouter

# crear una instancia de DefaultRouter
router = DefaultRouter(trailing_slash='/')
# agregar las rutas
router.register(r'branchs', BranchViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'employeeassigments', EmployeeAssigmentViewSet)
router.register(r'items', ItemViewSet)
router.register(r'transferhistories', TransferHistoryViewSet)
router.register(r'users', UserViewSet)

urlpatterns = router.urls

