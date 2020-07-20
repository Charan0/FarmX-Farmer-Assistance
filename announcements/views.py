from django.shortcuts import render
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Announcement


# Create your views here.
# Template Name = <app>/<model>_<viewtype>.html
class AnnouncementsListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    def test_func(self):
        user_group = self.request.user.groups.all().first()
        if user_group.name == 'Staff':
            return True
        return False

    model = Announcement


class AnnouncementsDetailView(LoginRequiredMixin, DetailView):
    def test_func(self):
        user_group = self.request.user.groups.all().first()
        if user_group.name == 'Staff':
            return True
        return False

    model = Announcement


class AnnouncementsCreateView(LoginRequiredMixin, CreateView):
    def test_func(self):
        user_group = self.request.user.groups.all().first()
        if user_group.name == 'Staff':
            return True
        return False

    model = Announcement
    fields = ['title', 'content', 'date_posted']
    success_url = '/user/announcement/'


class AnnouncementsDeleteView(LoginRequiredMixin, DeleteView):
    def test_func(self):
        user_group = self.request.user.groups.all().first()
        if user_group.name == 'Staff':
            return True
        return False

    model = Announcement
    success_url = '/user/announcement'


class AnnouncementsUpdateView(LoginRequiredMixin, UpdateView):
    def test_func(self):
        user_group = self.request.user.groups.all().first()
        if user_group.name == 'Staff':
            return True
        return False

    model = Announcement
    fields = ['title', 'content', 'date_posted']
    success_url = '/user/announcement'
