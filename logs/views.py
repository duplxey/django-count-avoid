from django.http import JsonResponse

from logs.models import Log
from logs.paginators import CountlessPaginator


def index_view(request):
    logs = Log.objects.all()

    page_number = request.GET.get("page")
    paginator = CountlessPaginator(logs, 25)
    page = paginator.get_page(page_number)

    return JsonResponse(
        {
            "has_next": page.has_next(),
            "has_previous": page.has_previous(),
            "results": [log.to_json() for log in page],
        }
    )
