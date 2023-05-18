from rest_framework.filters import OrderingFilter


class FieldMappedOrdering(OrderingFilter):
    '''
    This class created for solve order keyword problem. Django supports relational model ordering. We must use __ signature
    for related object field.Let's assume we have user field, and we would like to ordering based on first_name on user model.
    We must send 'user__first_name' keyword. It looks very bad and unneccessary.With this class we can pass what order key we want and its value.
    Don't forget to add this class as a parent class and define filter backend.
    '''
    ordering_fields_keymap = {}

    def prepare_fields(self, view):
        self.ordering_fields_keymap = getattr(view, 'ordering_fields_keymap', self.ordering_fields_keymap)
        mapping_keys = list(self.ordering_fields_keymap.keys())
        for k in mapping_keys:
            self.ordering_fields_keymap['-{}'.format(k)] = '-{}'.format(self.ordering_fields_keymap[k])

    def get_ordering(self, request, queryset, view):
        self.prepare_fields(view)
        params = request.query_params.get(self.ordering_param)
        if params:
            fields = [param.strip() for param in params.split(',')]
            ordering = [f for f in fields if f in list(self.ordering_fields_keymap.keys())]
            if ordering:
                return ordering
        return None  # There is no order

    def filter_queryset(self, request, queryset, view):
        ordering = self.get_ordering(request, queryset, view)

        if ordering:
            for n, i in enumerate(ordering):
                ordering[n] = self.ordering_fields_keymap[ordering[n]]
            return queryset.order_by(*ordering)
        return queryset  # There is no order so, return original queryset data