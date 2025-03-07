from unittest.mock import MagicMock
from uuid import UUID
from src.core.category.application.usecases.create_category import InMemoryCategoryRepository, create_category
import pytest

from src.core.category.application.usecases.exceptions import InvalidCategory

class TestCreateCategory:
    def test_create_active_category_with_name_and_description(self):
        mock_repository = MagicMock(InMemoryCategoryRepository)
        output = create_category(
            repository=mock_repository,
            name="Movies",
            description="Movie category",
            is_active=True
        )

        assert isinstance(output, UUID)
        assert mock_repository.save.called is True

    def test_create_inactive_category_with_name_and_description(self):
        mock_repository = MagicMock(InMemoryCategoryRepository)
        output = create_category(
            repository=mock_repository,
            name="Movies",
            description="Movie category",
            is_active=False
        )

        assert isinstance(output, UUID)
        assert mock_repository.save.called is True

    def test_when_input_is_invalid_then_raise_exception(self):
        with pytest.raises(InvalidCategory, match="name cannot be empty") as exc_info:
            create_category(
                repository=MagicMock(InMemoryCategoryRepository),
                name="",
                description="Movie category"
            )

        assert exc_info.type == InvalidCategory
        assert str(exc_info.value) == "name cannot be empty"
