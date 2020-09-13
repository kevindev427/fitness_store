from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

from markdownx.utils import markdownify

from store_project.pages.models import Page


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class SinglePageView(DetailView):
    model = Page
    context_object_name = "page"
    template_name = "pages/single.html"

    def get_context_data(self, **kwargs):
        context = super(SinglePageView, self).get_context_data(**kwargs)
        context["content"] = markdownify(self.object.content)
        return context