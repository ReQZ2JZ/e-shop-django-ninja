from ninja import NinjaAPI, Schema
from .models import VideoCard


api = NinjaAPI(urls_namespace="api")


class ProductOut(Schema):
    id: int
    name: str
    price: float
    description: str


@api.get("/products", response=list[ProductOut])
def list_products(request):
    products = VideoCard.objects.all().values("id", "name", "price", "description")
    return [
        {
            "id": product["id"],
            "name": product["name"],
            "price": float(product["price"]),
            "description": product["description"] or "",
        }
        for product in products
    ]


@api.get("/products/{product_id}", response=ProductOut)
def get_product(request, product_id: int):
    product = VideoCard.objects.get(id=product_id)
    return {
        "id": product.id,
        "name": product.name,
        "price": float(product.price),
        "description": product.description or "",
    }


@api.get("/health")
def health(request):
    return {"status": "ok"}