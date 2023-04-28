from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from django.http import HttpResponse
from django.db.models import F
from .models import Newskg, Purpose, Tag, Tree
from .forms import LangForm, UserRegisterForm, UserLoginForm, EmailForm
from .utils import Mixin

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LangsSerializer
from django.http.response import JsonResponse
import json


class MainLang (Mixin, ListView):
    model = Newskg
    template_name = 'newskg/main_langs_list.html'
    context_object_name = 'news'
    mix_prop = 'Web Development'
    paginate_by = 6
    # extra_context = {'title': 'IT Languages'}
    # queryset = Newskg.objects.select_related ('purpose')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'IT Languages'
        # context ['title'] = self.get_upper('IT Languages')
        context ['mix_prop'] = self.get_prop()
        return context

    def get_queryset(self):
        return Newskg.objects.filter (is_published=True).select_related ('purpose')


class PurposeLang (Mixin, ListView):
    model = Newskg
    template_name = 'newskg/purpose.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context ['title'] = Purpose.objects.get (pk=self.kwargs['purpose_id'])
        context['title'] = self.get_upper(Purpose.objects.get(pk=self.kwargs['purpose_id']))
        return context

    def get_queryset(self):
        return Newskg.objects.filter (purpose_id=self.kwargs['purpose_id'], is_published=True).select_related ('purpose')


class InfoLang (DetailView):
    model = Newskg
    context_object_name = 'fw'
    # template_name = 'newskg/newskg_detail.html'
    # pk_url_kwarg = 'framework_id'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Newskg.objects.get (pk=self.kwargs['pk'])
        self.object.browsing = F ('browsing') + 1
        self.object.save ()
        self.object.refresh_from_db ()
        return context


class TagLang (ListView):
    template_name = 'newskg/index.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'DBMS: ' + str (Tag.objects.get (slug=self.kwargs['slug']))
        return context

    def get_queryset(self):
        return Newskg.objects.filter (tags__slug=self.kwargs['slug']).prefetch_related ('tags')


class AddLang (LoginRequiredMixin, CreateView):
    form_class = LangForm
    template_name = 'newskg/lang_add.html'
    # success_url = reverse_lazy ('main')
    login_url = '/login/'
    # raise_exception = True
    # redirect_field_name = reverse_lazy ('main')


class Search (ListView):
    template_name = 'newskg/search.html'
    context_object_name = 'news'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['s'] = f"s={self.request.GET.get('s')}&"
        return context

    def get_queryset(self):
        return Newskg.objects.filter (title__icontains=self.request.GET.get('s'))


# class LangListView (APIView):
#     def get (self, request):
#         langs = Newskg.objects.filter (draft=False)
#         serializer = LangsSerializer (langs, many=True)
#         return Response (serializer.data)

def api (request):
    langs = Newskg.objects.all ()
    # serializer = json.dumps(LangsSerializer(langs, many=True).data, ensure_ascii=False)
    # return HttpResponse (serializer)
    # return HttpResponse (LangsSerializer(langs, many=True).data)
    return JsonResponse (LangsSerializer(langs, many=True).data, safe=False)

def jason (request):
    langs = Newskg.objects.all ()
    # pur = Purpose.objects.get (pk=9)
    # pur.get_langs.all ()
    serializer = LangsSerializer (langs, many=True).data
    return HttpResponse (rest(serializer))

def rest (serializer):
    html = '<p>[</p>'
    for subject in range (0, len (serializer)):
        html += '<p>' + json.dumps(serializer[subject], ensure_ascii=False)
        if subject < (len(serializer) - 1):
            html += ','
        html += '</p>'
    html += '<p>]</p>'
    return html


def vuejs (request):
    return render(request, 'newskg/vuejs.html')


def email (request):
    if request.method == 'POST':
        form = EmailForm (request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'omega_kid@mail.ru', ['dyushaliev08@mail.ru'], fail_silently=True)
            if mail:
                messages.success(request, 'Message sent!')
                return redirect('captcha')
            else:
                messages.error(request, 'Send email error!')
        else:
            messages.error(request, 'Validation error!')
    else:
        form = EmailForm ()
    return render(request, 'newskg/mail.html', {'form': form})


def registration (request):
    if request.method == 'POST':
        form = UserRegisterForm (request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'You registered!')
            return redirect('main')
        else:
            messages.error(request, 'Error!')
    else:
        form = UserRegisterForm ()
    return render(request, 'newskg/registration.html', {'form': form})

def user_login (request):
    if request.method == 'POST':
        form = UserLoginForm (data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')
    else:
        form = UserLoginForm ()
    return render(request, 'newskg/login.html', {'form': form})

def user_logout (request):
    logout(request)
    return redirect('login')


def get_mptt (request):
    return render(request, 'newskg/recursetree.html', {'trees': Tree.objects.all()})

def get_tree (request):
    pass


# def index (request):
#    news = Newskg.objects.all ()
#    context = {
#        'news': news,
#        'title': 'IT Languages',
#    }
#    return render(request, template_name='newskg/index.html', context=context)


# def get_purpose (request, purpose_id):
#     news = Newskg.objects.filter (purpose_id=purpose_id)
#     purpose = Purpose.objects.get (pk=purpose_id)
#     return render(request, 'newskg/purpose.html', {'news': news, 'purpose': purpose})


# def framework (request, framework_id):
#     #fw = Newskg.objects.get (pk=framework_id)
#     fw = get_object_or_404(Newskg, pk=framework_id)
#     return render(request, 'newskg/info_fw.html', {'fw': fw})


# def lang_add (request):
#     if request.method == 'POST':
#         form = LangForm (request.POST)
#         if form.is_valid ():
#             langs = form.save ()
#             return redirect (langs)
#             # print (form.cleaned_data)
#             # Newskg.objects.create (**form.cleaned_data)
#             # return redirect ('main')
#             # langs = Newskg.objects.create (**form.cleaned_data)
#             # return redirect (langs)
#     else:
#         form = LangForm ()
#     return render(request, 'newskg/lang_add.html', {'form': form})