from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, full_name, mobile_phone, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        if not mobile_phone:
            raise ValueError("Users must have an mobile_phone")
        
        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
            mobile_phone=mobile_phone
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, mobile_phone, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email=email,
            password=password,
            full_name=full_name,
            mobile_phone=mobile_phone
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user