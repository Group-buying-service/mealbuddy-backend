from rest_framework import serializers

class NotificationSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    title = serializers.CharField(max_length=30)

    