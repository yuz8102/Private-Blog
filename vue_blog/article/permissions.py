from rest_framework import permissions

#权限管理
class IsAdminUserOrReadOnly(permissions.BasePermission):
	def has_permission(self,request,view):
		# 对所有人允许 GET, HEAD, OPTIONS 请求
		if(request.method in permissions.SAFE_METHODS):
			return True
		# 仅管理员可进行其他操作
		return request.user.is_superuser