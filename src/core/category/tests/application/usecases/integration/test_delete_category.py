import uuid
from src.core.category.application.usecases.delete_category import DeleteCategoryUseCase, DeleteCategoryRequest
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository

class TestDeleteCategory:
    def test_delete_category_from_repository(self):
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

        usecase = DeleteCategoryUseCase(repository=repository)
        request = DeleteCategoryRequest(id=category_filme.id)

        assert repository.get_by_id(category_filme.id) is not None
        response = usecase.execute(request)

        assert repository.get_by_id(category_filme.id) is None
        assert response is None
