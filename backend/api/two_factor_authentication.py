# Nota: Este es solo un ejemplo básico, y se recomienda utilizar una biblioteca de autenticación más robusta en un entorno de producción.

import random
import time

class TwoFactorAuthentication:
    def __init__(self, user):
        self.user = user
        self.token = None
        self.token_expire_time = None

    def generate_token(self):
        self.token = random.randint(100000, 999999)
        self.token_expire_time = time.time() + 300  # Token válido por 5 minutos

    def validate_token(self, token):
        if self.token and self.token_expire_time > time.time() and token == self.token:
            self.token = None
            self.token_expire_time = None
            return True
        return False

    def send_token(self):
        self.generate_token()
        self.user.send_email(f"Your 2FA token is: {self.token}")

