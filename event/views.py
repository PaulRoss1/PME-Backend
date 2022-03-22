from django.db.models import Q

from django.shortcuts import render
from django.http import Http404
from rest_framework import serializers

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView

from datetime import date, timedelta

from .models import Event
from .serializers import EventSerializer



class BasicPagination(PageNumberPagination):
    page_size_query_param = 'limit'


class EventsList(APIView):
    pagination_class = PageNumberPagination
    serializer_class = EventSerializer

    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        else:
            pass
        return self._paginator

    def paginate_queryset(self, queryset):
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset,
                   self.request, view=self)

    def get_paginated_response(self, data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)

    def get(self, request, category, time_frame, format=None, *args, **kwargs):
        today = date.today().strftime("%d. %m. %Y")
        tomorrow = (date.today() + timedelta(days=1)).strftime("%d. %m. %Y")
        monday  = (date.today() - timedelta(days=date.today().weekday()))
        this_week = []
        for i in range(7): 
            this_week.append(str((monday + timedelta(days=i)).strftime("%d. %m. %Y")))
        this_weekend =  this_week[5:7]



        if time_frame == 'whole-period':
            if category == 'live-music':
                events = Event.objects.filter(event_type='Live Music')
            if category == 'djs':
                events = Event.objects.filter(event_type="DJ's")
            if category == 'all-events':
                events = Event.objects.all()

        if time_frame == 'today':
            if category == 'live-music':
                events = Event.objects.filter(event_type='Live Music').filter(date__contains=today)
            if category == 'djs':
                events = Event.objects.filter(event_type="DJ's").filter(date__contains=today)
            if category == 'all-events':
                events = Event.objects.filter(date__contains=today)

        if time_frame == 'tomorrow':
            if category == 'live-music':
                events = Event.objects.filter(event_type='Live Music').filter(date__contains=tomorrow)
            if category == 'djs':
                events = Event.objects.filter(event_type="DJ's").filter(date__contains=tomorrow)
            if category == 'all-events':
                events = Event.objects.filter(date__contains=tomorrow)


        if time_frame == 'this-week':
            if category == 'live-music':
                events = Event.objects.filter(event_type='Live Music').filter(Q(date__contains=this_week[0]) | Q(date__contains=this_week[1]) | Q(date__contains=this_week[2]) | Q(date__contains=this_week[3]) | Q(date__contains=this_week[4]) | Q(date__contains=this_week[5]) | Q(date__contains=this_week[6]))
            if category == 'djs':
                events = Event.objects.filter(event_type="DJ's").filter(Q(date__contains=this_week[0]) | Q(date__contains=this_week[1]) | Q(date__contains=this_week[2]) | Q(date__contains=this_week[3]) | Q(date__contains=this_week[4]) | Q(date__contains=this_week[5]) | Q(date__contains=this_week[6]))
            if category == 'all-events':
                events = Event.objects.filter(Q(date__contains=this_week[0]) | Q(date__contains=this_week[1]) | Q(date__contains=this_week[2]) | Q(date__contains=this_week[3]) | Q(date__contains=this_week[4]) | Q(date__contains=this_week[5]) | Q(date__contains=this_week[6]))


        if time_frame == 'this-weekend':
            if category == 'live-music':
                events = Event.objects.filter(event_type='Live Music').filter(Q(date__contains=this_weekend[0]) | Q(date__contains=this_weekend[1]))
            if category == 'djs':
                events = Event.objects.filter(event_type="DJ's").filter(Q(date__contains=this_weekend[0]) | Q(date__contains=this_weekend[1]))
            if category == 'all-events':
                events = Event.objects.filter(Q(date__contains=this_weekend[0]) | Q(date__contains=this_weekend[1]))

        page = self.paginate_queryset(events)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page,
 many=True).data)
        else:
            serializer = self.serializer_class(events, many=True)
        return Response(serializer.data)


class EventDetail(APIView):
    def get_object(self, slug, id):
        try:
            return Event.objects.filter(slug=slug).filter(id=id)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, slug, id, format=None):
        event = self.get_object(slug,id)
        serializer = EventSerializer(event, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        events = Event.objects.filter(Q(name__icontains=query) | Q(slug__icontains=query) | Q(venue__icontains=query))[0:45]
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
    else:
        return Response({"events": []})


class TodayEventsList(APIView):
    def get(self, request, date, format=None):
        
        events = Event.objects.filter(date=date)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)


