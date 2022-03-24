from django.views import generic

class IndexView(generic.TemplateView):
    template_name = "index.html"

class AboutView(generic.TemplateView):
    template_name = "about.html"

class ContactView(generic.TemplateView):
    template_name = "contact.html"

class JobListView(generic.TemplateView):
    template_name = "job_list.html"
    
class JobPostView(generic.TemplateView):
    template_name = "job_post.html"