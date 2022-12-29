from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsMoviePermission
from .serializers import MovieSerializer
from rest_framework import generics
from .models import Movie

class MovieView(generics.ListCreateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsMoviePermission]

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

        
    def perform_create(self, serializer):

        serializer.save(user=self.request.user, **self.request.data)

