from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    
    critic = serializers.SerializerMethodField(read_only=True)
    
    class Meta:

        model = Review
        fields =  [
            "id", "stars", "review", "spoilers", "movie_id", "critic",
        ]

    def get_critic(self, obj: Review):
       
        critic = dict(id=obj.critic.id, first_name=obj.critic.first_name, last_name=obj.critic.last_name)

        return critic

    def create(self, validated_data: dict) -> Review:
        
        return Review.objects.create(**validated_data)

       