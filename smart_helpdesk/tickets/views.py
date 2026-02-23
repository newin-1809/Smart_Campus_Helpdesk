from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django.core.cache import cache

from .models import Ticket
from .serializers import TicketSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    # Filtering, Searching, Ordering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'status']
    search_fields = ['title', 'description']
    ordering_fields = ['priority', 'created_at']

    #  Cache GET /tickets/
    def list(self, request, *args, **kwargs):
        cache_key = f"ticket_list_{request.get_full_path()}"
        cached_data = cache.get(cache_key)

        # If data exists in cache returns cached response
        if cached_data:
            return Response(cached_data)

        # Else fetch from database
        response = super().list(request, *args, **kwargs)

        # Store in cache for 60 seconds
        cache.set(cache_key, response.data, timeout=60)

        return response

    #  Clear only ticket-related cache
    def clear_ticket_cache(self):
        cache.delete_pattern("ticket_list_*")

    # Clear cache on create
    def perform_create(self, serializer):
        serializer.save()
        self.clear_ticket_cache()

    # Clear cache on update
    def perform_update(self, serializer):
        serializer.save()
        self.clear_ticket_cache()

    # Clear cache on delete
    def perform_destroy(self, instance):
        instance.delete()
        self.clear_ticket_cache()