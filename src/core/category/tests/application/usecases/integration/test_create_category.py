from uuid import UUID
from src.core.category.application.usecases.create_category import CreateCategoryRequest, CreateCategoryUseCase
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository

class TestCreateCategory:
    def test_create_category_with_valid_data(self):
        repository = InMemoryCategoryRepository()
        usecase = CreateCategoryUseCase(repository=repository)
        request = CreateCategoryRequest(
            name="Filme",
            description="Categoria para filmes",
            is_active=True,
        )
        response = usecase.execute(request)

        assert response.id is not None
        assert isinstance(response.id, UUID)
        assert len(repository.categories) == 1
        assert repository.categories[0].id == response.id
        assert repository.categories[0].name == "Filme"
        assert repository.categories[0].description == "Categoria para filmes"
        assert repository.categories[0].is_active == True
