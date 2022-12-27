from django.http import JsonResponse


class JSONResponseMixin:
    def render_to_json_response(self, context, **response_kwargs):
        return JsonResponse(
            self.get_data(context),
            **response_kwargs,
            safe=False,
        )

    def get_data(self, context):
        return list(context)
