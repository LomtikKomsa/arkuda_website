from django.db import models

from wagtail.models import Page

from news.models import NewsIndexPage

class HomePage(Page):
    def get_context(self, request):
        context = super().get_context(request)
        newsindexpage = self.get_first_child()
        newspages = newsindexpage.get_children().live().order_by('-first_published_at')
        context = {
            'newsindexpage': newsindexpage,
            'newspages': newspages,
        }
        return context
