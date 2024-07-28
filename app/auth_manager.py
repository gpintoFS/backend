from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_superuser(self, mail, name, lastname, password):
        if not mail:
            raise ValueError('El usuario debe tener un correo')
        
        mail_normalizer = self.normalize_email(mail)
        user_new = self.model(mail=mail_normalizer, name=name, lastname=lastname)
        user_new.set_password(password)

        user_new.is_superuser = True
        user_new.is_staff = True

        user_new.save()
