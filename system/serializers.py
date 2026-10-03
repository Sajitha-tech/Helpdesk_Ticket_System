from rest_framework import serializers
from system.models import User,Ticket

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","password","phone"]
        read_only_fields=["id"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class TicketSerializer(serializers.ModelSerializer):
    created_by=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Ticket
        fields="__all__"
        read_only_fields=["id","created_by","created-at","updated_at"]