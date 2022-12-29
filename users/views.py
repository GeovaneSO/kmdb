from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import User
from .serializers import UserSerializer
from .permissions import IsAccountPermission

from rest_framework.generics import ListCreateAPIView
from .permissions import IsAccountPermission
from .serializers import UserSerializer
from .models import User

class UserView(ListCreateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountPermission]
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

