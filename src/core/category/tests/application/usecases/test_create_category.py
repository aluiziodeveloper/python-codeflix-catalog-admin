from uuid import UUID
from src.core.category.application.usecases.create_category import create_category
import pytest

from src.core.category.application.usecases.exceptions import InvalidCategory

class TestCreateCategory:
    def test_create_active_category_with_name_and_description(self):
        output = create_category(
            name="Movies",
            description="Movie category",
            is_active=True
        )

        assert isinstance(output, UUID)

    def test_create_inactive_category_with_name_and_description(self):
        output = create_category(
            name="Movies",
            description="Movie category",
            is_active=False
        )

        assert isinstance(output, UUID)

    def test_when_input_is_invalid_then_raise_exception(self):
        with pytest.raises(InvalidCategory, match="name cannot be empty") as exc_info:
            create_category("", "Movie category")

        assert exc_info.type == InvalidCategory
        assert str(exc_info.value) == "name cannot be empty"
