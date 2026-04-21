from django.http import JsonResponse
from .models import VideoCard


def products_django(request):
    data = list(
        VideoCard.objects.all().values("id", "name", "price", "description")
    )

    products = []
    for item in data:
        products.append(
            {
                "id": item["id"],
                "name": item["name"],
                "price": float(item["price"]),
                "description": item["description"] or "",
            }
        )

    return JsonResponse({"products": products})