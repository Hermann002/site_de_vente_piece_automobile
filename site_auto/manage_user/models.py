from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, UserManager, PermissionsMixin, Group
from django.utils.translation import ugettext_lazy as _ 



class UserManager(BaseUserManager):
    def create_user(self, email, nom, prenom, contact, photo, password):
        
        user=self.model(
            user=self.normalize_email(email),
            nom=nom,
            prenom=prenom,
            contact=contact,
            photo=photo
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_visiteur(self, email, nom, prenom, contact, photo, password):
        user = self.create_user(
            email=self.normalize_email(email),
            nom=nom,
            prenom=prenom,
            photo=photo,
            contact=contact,
            password=password)
        user.is_visiteur = True
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def user_admin(self, email, nom, prenom, contact, photo, password):
        user = self.create_user(
            email=self.normalize_email(email),
            nom=nom,
            prenom=prenom,
            photo=photo,
            contact=contact,
            password=password)
        user.is_staff = True
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        user = self.model(email=email, password=password,is_superuser=True)
        user.set_password(password)
        user.is_active = True
        user.is_superuser = True
        user.staff = True
        user.save(using=self._db)
        return user
    
    
class User(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    nom = models.CharField(max_lenght=50, default="no_name")
    prenom = models.CharField(max_length=50,default="no_prenom")
    contact= models.CharField(max_length=50,default="no_contact")
    photo = models.CharField(max_length=255,default="no_photo")
    visiteur= models.BooleanField(default=False)
    admin= models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    
    def __str__(self):
        if self.staff == True:
            return f"{self.email} -- is_staff"
        if self.visiteur == True:
            return f"{self.email} -- is_visitor"
        return f"{self.nom} --- {self.email}"
    
    def get_full_name(self):
        return f"{self.nom} {self.prenom}"
    
    def get_short_name(self):
        return f"{self.prenom}"
    
    @property
    def is_staff(self):
        return self.staff