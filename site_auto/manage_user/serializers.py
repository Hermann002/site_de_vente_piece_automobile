from site_auto.manage_exception.custom_validation import CustomValidation
from .models import User
from rest_framework import serializers, status
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class RegisterVisiteurSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    email = serializers.CharField(required=True)
    contact = serializers.CharField(required=True, max_lenght=50, min_length=9)
    
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        password = serializers.CharField(max_lenght=128, min_length=8, write_only=True)
        fields = ('id', 'email', 'nom', 'prenom', 'contact', 'photo', 'password', 'confirm_password', 'token')
        extra_kwargs = {'password':{'write_only':True}}
        
    def validate_email(self, value):
        qs = User.objects.filter(email__iexact=value)
        
        if qs.exists():
            raise CustomValidation("l'email existe déjà", 'indication', status_code=status.HTTP_400_BAD_REQUEST)
        return value
    
    def validate_contact(self, value):
        qs = User.objects.filter(contact__iexact=value)
        
        if qs.exists():
            raise CustomValidation("le numéro existe déjà", 'indication', status_code=status.HTTP_400_BAD_REQUEST)
        return value
    
    def get_token(self,obj):
        user = obj
        payload  = jwt_payload_handler(user)
        token    = jwt_encode_handler(payload)
        return token

    def validate(self,data):
        pw  = data.get('password')
        pw2 = data.pop('confirm_password')
        if pw != pw2:
            raise CustomValidation("les mots de passes ne correspondent pas", 'indication',
                               status_code=status.HTTP_400_BAD_REQUEST)
        return data
    
    def create(self,validate_data):
        user_obj = User.objects.create_visiteur(**validate_data)
        return user_obj
    
    
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','password')

class ChangePasswordSerializer(serializers.ModelSerializer):
    newpassword = serializers.CharField(write_only=True)
    confirmnewpassword = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('id','password','newpassword','confirmnewpassword')

class ResetPasswordSerializer(serializers.ModelSerializer):
    newpassword = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('id','newpassword',)