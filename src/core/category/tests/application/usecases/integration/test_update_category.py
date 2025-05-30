from src.core.category.application.usecases.update_category import (
    UpdateCategoryUseCase,
    UpdateCategoryRequest,
)
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import (
    InMemoryCategoryRepository,
)

class TestUpdateCategory:
    def test_update_category_with_provided_fields(self):
        category = Category(
            name="Filme",
            description="Categoria de filmes",
        )
        repository = InMemoryCategoryRepository()
        repository.save(category=category)
        usecase = UpdateCategoryUseCase(repository=repository)

        request = UpdateCategoryRequest(
            id=category.id,
            name="Séries",
            description="Séries de filmes",
            is_active=False,
        )
        response = usecase.execute(request)

        updated_category = repository.get_by_id(category.id)
        assert response is None
        assert updated_category.name == "Séries"
        assert updated_category.description == "Séries de filmes"
        assert updated_category.is_active is False
