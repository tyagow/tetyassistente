from django.http import Http404


class RedirectSuccessURLMixin(object):

    def get_success_url(self):
        next_url = self.request.GET.get('next')

        if next_url:
            return next_url
        else:
            return super().get_success_url()


class NextParameterMixin(object):

    def get_context_data(self, **kwargs):
        next_url = self.request.GET.get('next')
        data = super().get_context_data(**kwargs)

        if next_url:
            next_url
            data['next'] = next_url

        return data


class ObjectOnwerMixin(object):

    def get_object(self, queryset=None):
        obj = super().get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj