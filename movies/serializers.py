from genres.serializers import GenreSerializer
from rest_framework import serializers
from genres.models import Genre
from datetime import timedelta
from datetime import datetime
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):

    genres = GenreSerializer(many=True)

    class Meta:

        model = Movie

        fields = [
            "id", "title", "duration", "premiere", "budget", "overview",  "genres" 
        ]
        
        depth = 1


    def create(self, validated_data):

        duration = validated_data.pop("duration")

        hours = datetime.strptime(duration, "%H:%M:%S").time().hour
        minutes = datetime.strptime(duration, "%H:%M:%S").time().minute
        seconds = datetime.strptime(duration, "%H:%M:%S").time().second

        time = timedelta(hours=hours, minutes=minutes, seconds=seconds)

        genres = validated_data.pop("genres")
 
        genre_objects = [
            Genre.objects.get_or_create(**genre)[0] for genre in genres
        ]

        movie_obj = Movie.objects.create(**validated_data, duration=time)

        movie_obj.genres.set(genre_objects)

        return movie_obj

