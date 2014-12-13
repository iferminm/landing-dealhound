from django.http import JsonResponse


class AjaxResponseMixin(object):
    """
    Must be used with a Form based view
    """

    def form_invalid(self, form):
        response = super(AjaxResponseMixin, self).form_invalid(form)
        return JsonResponse(form.errors, status=400)

    def form_valid(self, form):
        form.save()
        data = {
            'message': "We will let you know"
        }
        return JsonResponse(data)
