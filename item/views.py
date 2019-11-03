from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from django.views.generic import TemplateView, ListView, DetailView
from . models import Video, Category, SmallBanner, BigBanner, AboutUs
from datetime import datetime

# Create your views here.
class IndexView(TemplateView):
    template_name = 'item/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['video'] = Video.objects.all()
        context['catlist'] = Category.objects.all()
        context['recommend'] = Video.objects.filter(recommend=True)
        context['latest'] = Video.objects.filter(latest=True)[:4]
        context['featured'] = Video.objects.filter(featured=True)[:3]
        big_banner = BigBanner.objects.filter(show=True)[:2]
        for item in big_banner:
            if item.valid_date < datetime.now().date():
                item.show=False
                item.save()
        context['big_banner'] = BigBanner.objects.filter(show=True)[:2]
        return context


class VideoList(ListView):
    template_name = 'item/video-list.html'
    model = Video
    context_object_name = 'video'
    paginate_by = 9

class VideoDetail(DetailView):
    model = Video
    template_name = 'item/video-detail.html'
    context_object_name = 'video'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['related'] = Video.objects.filter(category=self.object.category)[:3]
        small_banner = SmallBanner.objects.filter(show=True)[:2]
        for item in small_banner:
            if item.valid_date < datetime.now().date():
                item.show=False
                item.save()
        context['small_banner'] = SmallBanner.objects.filter(show=True)[:2]
        return context

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Video, pk=id_)

def category_list(request, *args, **kwargs):
    cat_list = Video.objects.filter(category_id=kwargs.get('pk'))
    category = Category.objects.get(pk=kwargs.get('pk')).name
    paginator = Paginator(cat_list, 9)

    page = request.GET.get('page')
    catlist = paginator.get_page(page)
    return render(request, 'item/category.html', {'video': catlist,'category':category, })


class SearchView(ListView):
    template_name= "item/search-list.html"
    paginate_by = 9
    context_object_name = "video"

    def get_queryset(self):
        return Video.objects.filter(Q(category__name__icontains=self.request.GET.get('srh')) | Q(video_caption__icontains=self.request.GET.get('srh')))

class AboutUs(TemplateView):
    template_name = 'item/about.html'
    model = AboutUs
    context_object_name = 'about'