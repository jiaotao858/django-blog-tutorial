"""
django haystack 规定,要相对某个 app 下的数据进行全文检索，就要在该 app 下创建一个 search_indexes.py 文件，
然后创建一个 XXIndex 类（XX 为含有被检索数据的模型，如这里的 Post），并且继承 SearchIndex 和 Indexable。
"""
from .models import Post
from haystack import indexes


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    # document = True,使用此字段的内容作为索引进行检索
    # use_template = True,允许我们使用数据模板去建立搜索引擎索引的文件(索引里存放的内容)
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.all()