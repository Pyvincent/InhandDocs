from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse, Http404
from django.views import View
from django.urls import reverse
from django.http import HttpResponse
from django.db.models import Q
from django.views.decorators.csrf import csrf_protect

import json
import datetime
import time
from pure_pagination import PageNotAnInteger, Paginator, EmptyPage

from apps.product_docs.forms import *
from apps.product_docs.models import *
from apps.utils.mixin_utils import *
from InhandDocs.settings import BASE_DIR


class InstallDocListView(LoginRequiredMixin, View):
    def get(self, request):
        web_title = '产品文档'
        web_func = '产品文档'
        content_title = '文档列表'

        tags = InstallDocTag.objects.all()

        docs = InstallDoc.objects.all().order_by('-add_time')

        # 用户搜索
        keywords = request.GET.get('keywords', '')

        if keywords != '':
            docs = docs.filter(
                Q(doc_title__icontains=keywords) | \
                Q(doc_content__icontains=keywords) | \
                Q(doc_tag__name__icontains=keywords)
            )
            content_title = '关键字 <span style="color:orangered">"' + str(keywords) + '"</span> 搜索结果'

        docs = docs.distinct()

        # 记录数量
        doc_nums = docs.count()

        # 判断页码
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # 对取到的数据进行分页，记得定义每页的数量
        p = Paginator(docs, 9, request=request)

        # 分页处理后的 QuerySet
        docs = p.page(page)

        context = {
            'web_title': web_title,
            'web_func': web_func,
            'content_title': content_title,
            'tags': tags,
            'doc_nums': doc_nums,
            'docs': docs,
        }
        return render(request, 'product_docs/project_doc_list.html', context=context)


########################################################################################################################
## 添加安装文档
########################################################################################################################
class AddInstallDocView(LoginRequiredMixin, View):
    def post(self, request):
        add_ins_doc_form = AddInstallDocForm(request.POST)
        if add_ins_doc_form.is_valid():
            doc = InstallDoc()
            doc.doc_title = request.POST.get('doc_title')
            doc.doc_content = request.POST.get('doc_content')
            doc.doc_author = request.user
            doc.save()

            # 保存 Tag
            tag_list = request.POST.getlist('doc_tag')
            if len(tag_list):
                for each in tag_list:
                    tag = InstallDocTag.objects.get(id=int(each))
                    doc.doc_tag.add(tag)
                    doc.save()

            return HttpResponse('{"status":"success", "msg":"添加文档成功！"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"添加文档失败！"}', content_type='application/json')


########################################################################################################################
## 管理安装文档
########################################################################################################################
class ManaInstallDocView(LoginRequiredMixin, View):
    def post(self, request):
        doc_id = request.POST.get('doc_id')
        doc = InstallDoc.objects.get(id=int(doc_id))
        try:
            doc.delete()
            return HttpResponse('{"status":"success", "msg":"删除文档成功！"}', content_type='application/json')
        except Exception as e:
            return HttpResponse('{"status":"fail", "msg":"删除文档失败！"}', content_type='application/json')


########################################################################################################################
## 安装文档详情
########################################################################################################################
class InstallDocDetailView(LoginRequiredMixin, View):
    def get(self, request, doc_id):
        web_title = '产品文档'
        web_func = '产品文档'
        tags = InstallDocTag.objects.all()
        doc_info = InstallDoc.objects.get(id=int(doc_id))
        context = {
            'web_title': web_title,
            'web_func': web_func,
            'tags': tags,
            'doc_info': doc_info,
        }
        return render(request, 'product_docs/project_doc_detail.html', context=context)


########################################################################################################################
## 修改安装文档
########################################################################################################################
class ChangeInstallDocView(LoginRequiredMixin, View):
    def post(self, request, doc_id):
        cha_ins_doc_form = AddInstallDocForm(request.POST)
        if cha_ins_doc_form.is_valid():
            old_doc = InstallDoc.objects.get(id=int(doc_id))
            old_doc.delete()
            new_doc = InstallDoc()
            new_doc.id = int(doc_id)
            new_doc.doc_title = request.POST.get('doc_title')
            new_doc.doc_content = request.POST.get('doc_content')
            new_doc.doc_author = request.user
            new_doc.save()

            # 保存 Tag
            tag_list = request.POST.getlist('doc_tag')
            if len(tag_list):
                for each in tag_list:
                    tag = InstallDocTag.objects.get(id=int(each))
                    new_doc.doc_tag.add(tag)
                    new_doc.save()

            return HttpResponse('{"status":"success", "msg":"修改文档成功！"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"修改文档失败！"}', content_type='application/json')
