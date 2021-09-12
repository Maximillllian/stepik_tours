from random import shuffle

from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.urls import reverse
from data import tours, departures


class MainView(View):

    def get(self, request):
        random_tours = list(tours.items())
        shuffle(random_tours)
        random_tours = {key: value for key, value in random_tours[:6]}
        context = {'tours': random_tours}
        return render(request, 'tours/index.html', context=context)


class DepartureView(View):

    def get(self, request, departure):
        ru_departure = departures[departure]
        filtered_tours = {key: value for key, value in list(tours.items()) if value['departure'] == departure}
        tours_count = len(filtered_tours)
        prices = [value['price'] for value in list(filtered_tours.values())]
        min_price, max_price = min(prices), max(prices)
        nigths = [value['nights'] for value in list(filtered_tours.values())]
        min_night, max_night = min(nigths), max(nigths)

        context = {'departure': ru_departure, 'tours': filtered_tours, 'min_price': min_price,
                   'max_price': max_price, 'min_night': min_night, 'max_night': max_night,
                   'tours_count': tours_count}
        return render(request, 'tours/departure.html', context=context)


class TourView(View):

    def get(self, request, id):
        tour = tours[id]
        stars = '★' * int(tour['stars'])
        departure = departures[tour['departure']]
        context = {'tour': tour, 'stars': stars, 'departure': departure}
        return render(request, 'tours/tour.html', context=context)


class TestView(View):

    def get(self, request, year, **kwargs):
        summary = kwargs.get('summary', False)
        context = {'name': 'Max', 'cat': 'Phenix', 'summary': summary, 'year': year}
        if year < 1900:
            return HttpResponseRedirect(reverse('time-loop', args=[2000]))
        elif year > 2000:
            return HttpResponseRedirect(reverse('time-loop', kwargs={'year': 1900}))
        return render(request, 'test.html', context=context)
