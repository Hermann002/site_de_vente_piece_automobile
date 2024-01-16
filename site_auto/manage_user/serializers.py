from rest_framework import serializers
from manage_user.models import User

class UserSerializer(serializers.Serializer):
    
    class Meta:
        model = User
        fields = ['id', 'email', 'nom', 'prenom', 'contact', 'photo']
    