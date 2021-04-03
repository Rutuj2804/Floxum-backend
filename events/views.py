from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Event
from .serializers import EventSerializer
from rest_framework.authentication import TokenAuthentication


class AddEventView(APIView):
    authentication_classes = [TokenAuthentication,]

    def post(self, request, format=None):
        # try:
        data = self.request.data
        title = data['title']
        user = self.request.user
        desc_one = data['desc_one']
        desc_two = data['desc_two']
        location = data['location']
        image_one = data['image_one']
        image_two = data['image_two']
        image_three = data['image_three']
        date = data['date']
        time = data['time']
        contact = data['contact']
        link = data['link']
        event = Event.objects.create(title=title, user=user , desc_one=desc_one, desc_two=desc_two, location=location, date=date, image_one=image_one, image_two=image_two, image_three=image_three, time=time, contact=contact,link=link)
        serializer = EventSerializer(event)
        return Response({'success': 'Event created successfully', 'event': serializer.data})
        # except:
        #     return Response({'error': 'Something went wrong while creating event'})


class GetEventView(APIView):
    authentication_classes = [TokenAuthentication,]

    def get(self, request, format=None):
        try:
            event = Event.objects.filter(remove=False)
            serializer = EventSerializer(event, many=True)
            return Response({'success': 'events fetched successfully', 'events': serializer.data})
        except:
            return Response({'error': 'Something went wrong while fetching event'})



class GetEventDetailView(APIView):
    authentication_classes = [TokenAuthentication,]

    def post(self, request, format=None):
        try:
            id = self.request.data['id']
            event = Event.objects.filter(id=id, remove=False)[0]
            serializer = EventSerializer(event)
            return Response({'success': 'event fetched successfully', 'event': serializer.data})
        except:
            return Response({'error': 'Something went wrong while fetching event'})


class DeleteEventView(APIView):
    authentication_classes = [TokenAuthentication,]

    def post(self, request, format=None):
        try:
            data = self.request.data
            id = data['id']
            Event.objects.filter(id=id).update(remove=True)
            return Response({'success': 'Successfully deleted event'})
        except:
            return Response({'error': 'Something went wrong while delete event'})
