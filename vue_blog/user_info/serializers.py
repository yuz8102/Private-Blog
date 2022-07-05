from django.contrib.auth.models import User
from rest_framework import serializers

class UserDescSerializer(serializers.ModelSerializer):
	#定义使用的模型及需要的模型字段，继承serializers.ModelSerialiazer时
	class Meta:
		model = User
		fields = [
			'id',
			'username',
			'last_login',
			'date_joined'
		]