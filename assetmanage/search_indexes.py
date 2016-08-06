from haystack import indexes
from .models import Video, Audio, Subtitle, Image, Note


class VideoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    content_auto = indexes.EdgeNgramField(model_attr='file_name')

    def get_model(self):
        return Video

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()


class AudioIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    content_auto = indexes.EdgeNgramField(model_attr='file_name')

    def get_model(self):
        return Audio

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()


class SubtitleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    content_auto = indexes.EdgeNgramField(model_attr='file_name')

    def get_model(self):
        return Subtitle

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
