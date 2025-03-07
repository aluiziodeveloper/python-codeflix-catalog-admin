import uuid
import pytest
from src.core.category.application.usecases.exceptions import CategoryNotFound
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository
from src.core.category.application.usecases.get_category import GetCategoryUseCase, GetCategoryRequest, GetCategoryResponse

class TestGetCategory:
    def test_get_category_by_id(self):
        category_filme = Category(
            id=uuid.uuid4(),
            name="Filme",
            description="Categoria para filmes",
            is_active=True,
        )
        category_serie = Category(
            id=uuid.uuid4(),
            name="Série",
            description="Categoria para séries",
            is_active=True,
        )
        repository = InMemoryCategoryRepository(
            categories=[
                category_filme,
                category_serie,
            ]
        )

        usecase = GetCategoryUseCase(repository=repository)
        request = GetCategoryRequest(id=category_filme.id)
        response = usecase.execute(request)

        assert response == GetCategoryResponse(
            id=category_filme.id,
            name="Filme",
            description="Categoria para filmes",
            is_active=True,
        )

    def test_when_category_with_id_does_not_exist_then_raise_not_found(self):
        category_filme = Category(
            id=uuid.uuid4(),
            name="Filme",
            description="Categoria para filmes",
            is_active=True,
        )
        category_serie = Category(
            id=uuid.uuid4(),
            name="Série",
            description="Categoria para séries",
            is_active=True,
        )
        repository = InMemoryCategoryRepository(
            categories=[
                category_filme,
                category_serie,
            ]
        )

        use_case = GetCategoryUseCase(repository=repository)
        request = GetCategoryRequest(id="non-existent-id")

        with pytest.raises(CategoryNotFound) as exc:
            use_case.execute(request)
