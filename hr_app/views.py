from django.views import generic

class IndexView(generic.TemplateView):
    template_name = "index.html"

class AboutView(generic.TemplateView):
    template_name = "about.html"

class ContactView(generic.TemplateView):
    template_name = "contact.html"

class PostView(generic.TemplateView):
    template_name = "post.html"