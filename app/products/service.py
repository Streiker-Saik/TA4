from app.products.models import Product
from app.services.base import BaseService


class ProductService(BaseService):
    """Сервис работы с продуктом в БД"""

    model = Product
