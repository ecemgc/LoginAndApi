from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class StandardPagination(PageNumberPagination):
    page_size = 20

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
            },
            'current_page': self.page.number,
            'total_pages': self.page.paginator.num_pages,
            'per_page': self.page.paginator.per_page,
            'total_count': self.page.paginator.count,
            'results': data
        })