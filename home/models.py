from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel, InlinePanel

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

    content_panels = Page.content_panels + [
        InlinePanel('carousel_images', label="Gallery images"),
    ]

class NewsPageGalleryImage(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='carousel_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )

    panels = [
        FieldPanel('image'),
    ]