from rest_framework import generics
from users.permissions import IsMoviePermission
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Movie
from .serializers import MovieSerializer
import ipdb
class MovieView(generics.ListCreateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsMoviePermission]

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

        
    def perform_create(self, serializer):
        # ipdb.set_trace()
        serializer.save(user=self.request.user, **self.request.data)
        # print(serializer.data)

