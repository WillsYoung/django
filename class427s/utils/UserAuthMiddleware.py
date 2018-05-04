from django.http import HttpResponseRedirect
from django.utils.deprecation import  MiddlewareMixin

from uauth.models import Users


class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):

        # 统一验证登录的位置
        # return none或者不写return表示验证成功进入下一步

        if request.path == '/u/login/' or request.path == '/u/regist/':
            return None
        ticket = request.COOKIES.get('ticket')
        if not ticket:
            return HttpResponseRedirect('/u/login/')

        users = Users.objects.filter(u_ticket=ticket)
        if not users:
            return HttpResponseRedirect('/u/login/')
        request.user = users[0]