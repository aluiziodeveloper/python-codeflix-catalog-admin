from unittest.mock import create_autospec
import uuid

import pytest
from src.core.category.application.category_repository import CategoryRepository
from src.core.category.application.usecases.exceptions import CategoryNotFound, InvalidCategory
from src.core.category.application.usecases.update_category import UpdateCategoryUseCase, UpdateCategoryRequest
from src.core.category.domain.category import Category

class TestUpdateCategory:
    def test_update_category_name(self):
        category = Category(
            name="Filme",
            description="Categoria de filmes",
        )
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = category

        usecase = UpdateCategoryUseCase(mock_repository)
        usecase.execute(UpdateCategoryRequest(
            id=category.id,
            name="Séries",
        ))

        assert category.name == "Séries"
        mock_repository.save.assert_called_once_with(category)

    def test_update_category_description(self):
        category = Category(
            name="Filme",
            description="Categoria de filmes",
        )
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = category

        usecase = UpdateCategoryUseCase(mock_repository)
        usecase.execute(UpdateCategoryRequest(
            id=category.id,
            description="Categoria de séries",
        ))

        assert category.description == "Categoria de séries"
        mock_repository.save.assert_called_once_with(category)


    def test_activate_category(self):
        category = Category(
            name="Filme",
            description="Categoria de filmes",
            is_active=False,
        )
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = category

        usecase = UpdateCategoryUseCase(mock_repository)
        usecase.execute(UpdateCategoryRequest(
            id=category.id,
            name="Séries",
            is_active=True,
        ))

        assert category.is_active is True
        mock_repository.save.assert_called_once_with(category)

    def test_deactivate_category(self):
        category = Category(
            name="Filme",
            description="Categoria de filmes",
            is_active=True,
        )
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = category

        usecase = UpdateCategoryUseCase(mock_repository)
        usecase.execute(UpdateCategoryRequest(
            id=category.id,
            is_active=False,
        ))

        assert category.is_active is False
        mock_repository.save.assert_called_once_with(category)


    def test_update_category_name_and_description(self):
        category = Category(
            name="Filme",
            description="Categoria de filmes",
        )
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = category

        usecase = UpdateCategoryUseCase(mock_repository)
        usecase.execute(UpdateCategoryRequest(
            id=category.id,
            name="Séries",
            description="Categoria de séries",
        ))

        assert category.name == "Séries"
        assert category.description == "Categoria de séries"
        mock_repository.save.assert_called_once_with(category)

    def test_when_category_not_found_then_raise_exception(self):
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = None

        usecase = UpdateCategoryUseCase(mock_repository)
        request = UpdateCategoryRequest(id=uuid.uuid4())

        with pytest.raises(CategoryNotFound) as exc:
            usecase.execute(request)

        mock_repository.save.assert_not_called()
        assert str(exc.value) == f"Category with {request.id} not found"

    def test_when_category_is_updated_to_invalid_state_then_raise_exception(self):
        category = Category(
            name="Filme",
            description="Categoria de filmes",
        )
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = category

        usecase = UpdateCategoryUseCase(mock_repository)
        request = UpdateCategoryRequest(
            id=category.id,
            name="",  # Invalid
        )

        with pytest.raises(InvalidCategory) as exc:
            usecase.execute(request)

        mock_repository.save.assert_not_called()
        assert str(exc.value) == "name cannot be empty"
