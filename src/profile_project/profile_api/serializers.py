from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serialize a name field for testing our APIView."""
    # check valid character that has a maximum length of 10
    name = serializers.CharField(max_length=15)


#could uses this instead of post man
