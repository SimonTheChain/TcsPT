from haystack import indexes
from .models import Provider, Project, Rejection


class ProviderIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    content_auto = indexes.EdgeNgramField(model_attr='name')

    def get_model(self):
        return Provider

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()


class ProjectIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    start_date = indexes.DateTimeField(model_attr='start_date')
    due_date = indexes.DateTimeField(model_attr='due_date')

    content_auto = indexes.EdgeNgramField(model_attr='title')

    def get_model(self):
        return Project

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()


class RejectionIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    content_auto = indexes.EdgeNgramField(model_attr='reason')

    def get_model(self):
        return Rejection

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
