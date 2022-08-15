from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator
import passlib.hash as hash


class User(models.Model):
    id = fields.UUIDField(pk=True)
    first_name = fields.CharField(max_length=255)
    last_name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255)
    password = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "users"

    def __str__(self):
        return self.email

    def verify_password(self, password: str):
        return hash.bcrypt.verify(password, self.password)


# UserSchema = pydantic_model_creator(User)
