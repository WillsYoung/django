from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from stu.serializers import StudentSerializer

from stu.models import Student, StudentInfo

import logging

from rest_framework import mixins, viewsets

logger = logging.getLogger('stu')


def index(request):

    if request.method == 'GET':
        # 获取所有学生信息，先确认有没有cookie
        # ticket = request.COOKIES.get('ticket')
        # if not ticket:
        #     return HttpResponseRedirect('/u/login')
        # # 判断当前浏览的网页是否有相关的Cookie
        # if Users.objects.filter(u_ticket=ticket).exists():
        stuinfos = StudentInfo.objects.all()
        logger.info('获取学生信息成功')
        return render(request, 'index.html', {'stuinfos': stuinfos})
        # else:
        #     return HttpResponseRedirect('/u/login')


def stu_page(request):

    if request.method == 'GET':
        page_id = request.GET.get('page_id', 1)
        stuinfos = StudentInfo.objects.all()
        paginator = Paginator(stuinfos, 5)
        page = paginator.page(int(page_id))
        return render(request, 'index.html', {'stuinfos': page})


def add_stu(request):

    if request.method == 'GET':
        return  render(request, 'add_stu.html')

    if request.method == 'POST':
        # 跳转到添加学生详情页面
        name = request.POST.get('name')
        tel = request.POST.get('tel')

        stu = Student.objects.create(
            s_name=name,
            s_tel=tel
        )
        return HttpResponseRedirect(
            reverse('s:addinfo', kwargs={'stu_id': stu.id})
        )


def add_stu_info(request, stu_id):

    if request.method == 'GET':

        return render(request, 'add_stu_info.html', {'stu_id': stu_id})

    if request.method == 'POST':
        stu_id = request.POST.get('stu_id')
        addr = request.POST.get('addr')
        # 添加头像图片
        img = request.FILES.get('img')
        StudentInfo.objects.create(
            i_addr=addr,
            s_id=stu_id,
            i_image=img
        )
        return HttpResponseRedirect('/s/index/')


def get(request):

    if request.method == 'GET':

        return render(request, 'get.html')


class StudentEdit(mixins.ListModelMixin,  # 获取所有的资源
                  # 获取具体的某个资源
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):

    # 查询所有信息
    queryset = Student.objects.all()
    # 序列化
    serializer_class = StudentSerializer


