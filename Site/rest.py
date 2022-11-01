from Shop.models import *
from django.contrib.auth.models import User, Group
from rest_framework import permissions
from rest_framework import routers, serializers, viewsets
from rest_framework.authentication import SessionAuthentication

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return

# Serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'name', 'price', 'promo_price', 'image',
                  'information', 'full_information', 'stock', 'available', 'created', 'updated', 'subcategory']

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'name']
        

class SubcategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategories
        fields = ['id', 'name', 'category']

# ViewSets

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
        
class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

class SubcategoriesViewSet(viewsets.ModelViewSet):
    queryset = Subcategories.objects.all()
    serializer_class = SubcategoriesSerializer
    
# Router

router = routers.DefaultRouter()
router.register(r'users-api', UserViewSet)
router.register(r'groups-api', GroupViewSet)
router.register(r'products-api', ProductsViewSet)
router.register(r'categories-api', CategoriesViewSet)
router.register(r'subcategories-api', SubcategoriesViewSet)
