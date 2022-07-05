from rest_framework import serializers
from .models import Article
from user_info.serializers import UserDescSerializer
from .models import Category

'''class ArticleListSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	title = serializers.CharField(allow_blank=True,max_length=100)
	body = serializers.CharField(allow_blank=True)
	created = serializers.DateTimeField()
	updated = serializers.DateTimeField()'''

class ArticleCategoryDetailSerializer(serializers.ModelSerializer):
	url = serializers.HyperlinkedIdentityField(view_name='article-detail')
	class Meta:
		model = Article
		fields = [
			'url',
			'title',
		]

class CategoryDetailSerializer(serializers.ModelSerializer):
	#一对多，多对多用many=true
	articles = ArticleCategoryDetailSerializer(many=True,read_only=True)

	class Meta:
		model = Category
		fields = [
			'id',
			'title',
			'created',
			'articles',
		]

class CategorySerializer(serializers.ModelSerializer):
	#定义嵌套序列化器即可同时控制显示字段
	url=serializers.HyperlinkedIdentityField(view_name='category-detail')
	class Meta:
		model = Category
		fields = '__all__'
		read_only_fields = ['created']

class ArticleListSerializer(serializers.ModelSerializer):
	#嵌套序列化器
	author = UserDescSerializer(read_only=True)
	category = CategorySerializer(read_only=True)
	#允许修改更新category
	category_id = serializers.IntegerField(write_only=True,allow_null=True,required=False)
	def validate_category_id(self,value):
		if not Category.objects.filter(id=value).exists() and value is not None:
			raise serializers.ValidationError("Category with id {} not exists.".format(value))
		return value
	#article:viewname
	url = serializers.HyperlinkedIdentityField(view_name="article:detail")
	#定义使用的模型及需要的模型字段，继承serializers.ModelSerialiazer时
	#fields内容须在model中，或是前面代码用序列化器返回的
	class Meta:
		model = Article
		'''fields = [
			#'id',
			'url',
			'title',
			'created',
			'author',
			'category',
		]'''
		fields = '__all__'

class ArticleDetailSerializer(serializers.ModelSerializer):
	author = UserDescSerializer(read_only=True)
	category = CategorySerializer(read_only=True)
	#允许修改更新category
	category_id = serializers.IntegerField(write_only=True,allow_null=True,required=False)
	def validate_category_id(self,value):
		if not Category.objects.filter(id=value).exists() and value is not None:
			raise serializers.ValidationError("Category with id {} not exists.".format(value))
		return value
	class Meta:
		model = Article
		#取
		fields = '__all__'
