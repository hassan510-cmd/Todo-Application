from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User=get_user_model()
class UserProfileSerializer(serializers.ModelSerializer):
    password_conf=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=('email','username','password','password_conf')
        extra_kwargs={'password':{'write_only':True}}



    def save(self, **kwargs):
        user = User(email=self.validated_data.get('email'),username=self.validated_data.get('username'))
        if self.validated_data.get('password') != self.validated_data.get('password_conf'):
            raise serializers.ValidationError({'password':'confirmed password did not match'})
        else:
            user.set_password(self.validated_data.get('password'))
            user.save()
            return user

    # def create(self, validated_data):
    #     user=UserProfile(
    #         email=validated_data['email']
    #         ,name=validated_data['name']
    #                      )
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user