from django.shortcuts import render
from django.http.response import HttpResponse, Http404
# from django.template import loader
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


# Create your views here.
def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args: \n"
        body += "\n".join(["\t%s" % a for a in args])

    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")


class PostListView(ListView):
    model = Post
    template_name = 'blogging/list.html'


# def list_view(request):
#     published = Post.objects.exclude(published_date__exact=None)
#     posts = published.order_by('-published_date')
#     # template = loader.get_template('blogging/list.html')
#     context = {'posts': posts}
#     # body = template.render(context)
#     # return HttpResponse(body, content_type="text/html")
#     return render(request, 'blogging/list.html', context)

class PostDetailView(DetailView):
    model = Post
    template_engine = 'blogging/detail.html'

    def publish(self, request, post_id):
        # def detail_view(request, post_id):
        blog = self.get_object()
        published = blog.objects.exclude(published_date__exact=None)
        try:
            post = published.get(pk=post_id)
        except Post.DoesNotExist:
            raise Http404
        context = {'post': post}
        return render(request, 'blogging/detail.html', context)
