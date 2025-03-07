from uuid import UUID
from src.core.category.application.usecases.exceptions import InvalidCategory
from src.core.category.domain.category import Category

class InMemoryCategoryRepository:
    def __init__(self, categories=None):
        self.categories = categories or []

    def save(self, category):
        self.categories.append(category)

# input: name, description, is_active
# output: category_id (UUID)
def create_category(
        repository: InMemoryCategoryRepository,
        name: str,
        description: str = "",
        is_active: bool = True
    ) -> UUID:
    try:
        category = Category(name=name, description=description, is_active=is_active)
    except ValueError as error:
        raise InvalidCategory(error)

    repository.save(category)

    return category.id
