from manage_user.models import User
from manage_user.serializers import UserSerializer
from rest_framework import mixins
from rest_framework import generics



class RegistredUser(mixins.CreateModelMixin,
                    generics.GenericAPIView):
    queryset = User.objects.create()
    serializer_class = UserSerializer
    
    # put a get request here later if it's necessary
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class UpdatedUser(mixins.UpdateModelMixin,
                  generics.GenericAPIView):
    queryset = User.objects.create()
    serializer_class = UserSerializer
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
class DeletedUser(mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    queryset = User.objects.create()
    serializer_class = UserSerializer
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)