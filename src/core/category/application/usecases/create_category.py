from uuid import UUID
from src.core.category.application.usecases.exceptions import InvalidCategory
from src.core.category.domain.category import Category

# input: name, description, is_active
# output: category_id (UUID)
def create_category(name: str, description: str = "", is_active: bool = True) -> UUID:
    try:
        category = Category(name=name, description=description, is_active=is_active)
    except ValueError as error:
        raise InvalidCategory(error)

    # TODO: persist category

    return category.id
