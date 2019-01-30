from rest_framework import serializers
from . import models

class HelloSerializer(serializers.Serializer):
    """Serialize a name field for testing our APIView."""
    # check valid character that has a maximum length of 10
    name = serializers.CharField(max_length=10)

# Model serializer
class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer from our user profile objects."""
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only':True}}
    def create(self, validated_data):
        """Create and return a new user."""
        user = models.UserProfile(
        email=validated_data['email'],
        name=validated_data['name']
        )
        user.set_password(validated_data['password'])
        #saves the user object to the database
        user.save()
        return user
