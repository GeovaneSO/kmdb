from rest_framework import generics
from .permissions import IsReviewPermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Review
from movies.models import Movie
from django.shortcuts import get_object_or_404
from .serializers import ReviewSerializer


class ReviewView(generics.ListCreateAPIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsReviewPermission]
    
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):

        movie_id = self.kwargs["movie_id"]
        
        movie_obj = get_object_or_404(Movie, pk=movie_id)
        
        serializer.save(critic=self.request.user, movie=movie_obj,**self.request.data)