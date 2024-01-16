from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, UserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, email, nom, prenom, contact, photo, password):

        user = self.model(
            email=self.normalize_email(email),
            nom=nom,
            prenom=prenom,
            photo=photo,
            contact=contact)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_visiteur(self,email,nom,prenom,contact,photo,password):
        user = self.create_user(
            email=self.normalize_email(email),
            nom=nom,
            prenom=prenom,
            photo=photo,
            contact=contact,
            password=password)
        user.visiteur = True
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    
    def create_admin(self,email,nom,prenom,contact,photo,password):
        user = self.create_user(
            email=self.normalize_email(email),
            nom=nom,
            prenom=prenom,
            photo=photo,
            contact=contact,
            password=password)
        user.admin = True
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        # ajout au groupe staff
        # my_group = Group.objects.get(name='admin')
        # my_group.user_set.add(user)
        return user
    
class User(AbstractBaseUser,PermissionsMixin):
    username = None
    email = models.EmailField(('email address'), unique=True)
    nom = models.CharField(max_length=50,default="no_nom")
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
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS  = []
    objects = UserManager()
    
    
    def __str__(self):
        if self.staff == True:
            return f"{self.email} -- is_staff"
        if self.visiteur == True:
            return f"{self.email} -- is_visiteur"
        if self.annonceur == True:
            return f"{self.email} -- is_annonceur"
        return f"{self.nom} --- {self.email}" 

    def get_full_name(self):
        return f"{self.nom} {self.prenom}"

    def get_short_name(self):
        return f"{self.prenom}"

    @property
    def is_staff(self):
        return self.staff