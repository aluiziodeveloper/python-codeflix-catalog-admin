from dataclasses import dataclass
from uuid import UUID
from src.core.category.application.usecases.exceptions import InvalidCategory
from src.core.category.domain.category import Category

@dataclass
class CreateCategoryRequest:
    name: str
    description: str = ""
    is_active: bool = True

@dataclass
class CreateCategoryResponse:
    id: UUID

class InMemoryCategoryRepository:
    def __init__(self, categories=None):
        self.categories = categories or []

    def save(self, category):
        self.categories.append(category)

class CreateCategoryUseCase:
    def __init__(self, repository: InMemoryCategoryRepository):
        self.repository = repository

    def execute(self, request: CreateCategoryRequest) -> CreateCategoryResponse:
        try:
            category = Category(
                name=request.name,
                description=request.description,
                is_active=request.is_active
            )
        except ValueError as error:
            raise InvalidCategory(error)

        self.repository.save(category)

        return category.id
