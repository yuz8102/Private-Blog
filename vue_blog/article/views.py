#from django.http import JsonResponse
#from rest_framework.response import Response
#from rest_framework.views import APIView

from rest_framework import generics
from rest_framework import viewsets
#from rest_framework import status
from .permissions import IsAdminUserOrReadOnly

#from django.http import Http404

from .models import Article
from .models import Category
from .serializers import ArticleListSerializer
from .serializers import ArticleDetailSerializer
from .serializers import CategorySerializer, __fCategoryDetailSerializer

from rest_framework import filters

# Create your views here.
class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    '''def perform_create(self, serializer):
        #request.user从浏览器缓存获取用户id，找到对应的用户对象，由于为设置author的序列化，默认只展示主键（即id）
        #后面新建一个user_info app的操作非必要，只要在Articlelist的序列化器中嵌套author的序列化器
        serializer.save(author=self.request.user)'''
'''
def ArticleList(request):
	articles = Article.objects.all()
	serializer = ArticleListSerializer(articles,many=True)
	return JsonResponse(serializer.data,safe=False)

class ArticleDetail(APIView):
	def get_object(self,pk):
		try:
			#pk为主键，默认为id
			return Article.objects.get(pk=pk)
		except:
			raise Http404

	def get(self,request,pk):
		article = self.get_object(pk)
		serializer = ArticleDetailSerializer(article)
		return Response(serializer.data)

	def put(self,request,pk):
		article = self.get_object(pk)
		serializer = ArticleDetailSerializer(article,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

	def delete(self,request,pk):
		article = self.get_object(pk)
		article.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
'''
class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
	#此view通过
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    permissions_classes = [IsAdminUserOrReadOnly]

class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	#serializer_class = CategorySerializer
	permissions_classes = [IsAdminUserOrReadOnly]

	#列表页&详情页展示不同内容
	def get_serializer_class(self):
		if self.action == 'list':
			return CategorySerializer
		else:
			return CategoryDetailSerializer

