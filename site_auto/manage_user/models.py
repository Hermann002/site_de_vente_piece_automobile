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
    
    def admin(self, email, nom, prenom, contact, photo, password):
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