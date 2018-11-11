from django.db import models
from apps.users.models import UserProfile


class InstallDocTag(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='标签名称')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    class Meta:
        verbose_name_plural = '文档标签'
        verbose_name = verbose_name_plural

    def __str__(self):
        return self.name


########################################################################################################################
## 项目详情
########################################################################################################################
class InstallDoc(models.Model):
    doc_title = models.CharField(max_length=128, verbose_name='文章标题')
    doc_content = models.TextField(verbose_name='文章正文')
    doc_tag = models.ManyToManyField(InstallDocTag, blank=True, verbose_name='文档标签')
    doc_author = models.ForeignKey(UserProfile, verbose_name='作者', on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    class Meta:
        verbose_name_plural = '产品文档'
        verbose_name = verbose_name_plural

    def __str__(self):
        return self.doc_title
