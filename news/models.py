from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField
from wagtail import blocks
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.search import index
from wagtail.images.blocks import ImageChooserBlock


class NewsIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    def get_context(self, request):
        context = super().get_context(request)
        newspages = self.get_children().live().order_by('-first_published_at')
        context['newspages'] = newspages
        return context

class NewsPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    # card = StreamField([
    #     ('heading', blocks.CharBlock(max_length=255)),
    #     ('intro', blocks.RichTextBlock()),
    #     ('image', ImageChooserBlock())
    # ], use_json_field=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    # search_fields = Page.search_fields + [
    #     index.SearchField('intro'),
    #     index.SearchField('body'),
    # ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
        InlinePanel('gallery_images', label="Gallery images"),
    ]

class NewsPageGalleryImage(Orderable):
    page = ParentalKey(NewsPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]