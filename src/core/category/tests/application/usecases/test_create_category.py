from unittest.mock import MagicMock
from uuid import UUID
import pytest

from src.core.category.application.usecases.create_category import CreateCategoryRequest, CreateCategoryUseCase, InMemoryCategoryRepository
from src.core.category.application.usecases.exceptions import InvalidCategory

class TestCreateCategory:
    def test_create_category_with_valid_data(self):
        mock_repository = MagicMock(InMemoryCategoryRepository)
        usecase = CreateCategoryUseCase(repository=mock_repository)
        request = CreateCategoryRequest(
            name="Filme",
            description="Categoria para filmes",
            is_active=True,
        )
        category_id = usecase.execute(request)

        assert category_id is not None
        assert isinstance(category_id, UUID)
        assert mock_repository.save.called is True

    def test_create_category_with_invalid_data(self):
        usecase = CreateCategoryUseCase(repository=MagicMock(InMemoryCategoryRepository))
        with pytest.raises(InvalidCategory, match="name cannot be empty") as exc_info:
            usecase.execute(CreateCategoryRequest(name=""))

        assert exc_info.type == InvalidCategory
        assert str(exc_info.value) == "name cannot be empty"
