from django.core.paginator import Paginator
from django.http import JsonResponse

from logs.models import Log


def index_view(request):
    logs = Log.objects.all()
    paginator = Paginator(logs, 25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return JsonResponse(
        {
            "has_next": page_obj.has_next(),
            "has_previous": page_obj.has_previous(),
            "results": [log.to_json() for log in page_obj],
        }
    )
