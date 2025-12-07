from fastapi import APIRouter, Depends

from app.exceptions import ProductNotFoundException
from app.products.schemas import SProductCreate, SProductResponse, SProductUpdate
from app.products.service import ProductService
from app.auth.dependencies import get_current_user, get_current_user_is_admin
from app.users.models import User

router = APIRouter(prefix="/products", tags=["Товары"])


@router.post("", response_model=SProductResponse)
async def create_product(
        product_data: SProductCreate,
        user: User = Depends(get_current_user_is_admin)
) -> SProductResponse:
    """Добавление продукта"""

    new_product = await ProductService.add(**dict(product_data))
    return new_product


@router.get("", response_model=list[SProductResponse])
async def get_products(
        user: User = Depends(get_current_user)
) -> list[SProductResponse]:
    """Просмотр всех продуктов"""

    return await ProductService.find_all(is_active=True)


@router.get("/{product_id}", response_model=SProductResponse)
async def get_product(
        product_id: int,
        user: User = Depends(get_current_user)
) -> SProductResponse:
    """Получение продукта по ID"""

    product = await ProductService.find_by_id(model_id=product_id)
    if not product:
        raise ProductNotFoundException
    return product


@router.put("/{product_id}", response_model=SProductResponse)
async def update_product(
        product_id: int,
        product_data: SProductUpdate, user: User = Depends(get_current_user_is_admin)
) -> SProductResponse:
    """Обновление продукта по ID"""

    updated_product =  await ProductService.update(product_id, **dict(product_data))
    if not updated_product:
        raise ProductNotFoundException
    return updated_product


@router.delete("/{product_id}")
async def delete_product(
        product_id: int,
        user: User = Depends(get_current_user_is_admin)
) -> dict:
    """Удаление продукта по ID"""

    success = await ProductService.delete(product_id)
    if not success:
        raise ProductNotFoundException
    return {"detail": "Продукт удален успешно"}
