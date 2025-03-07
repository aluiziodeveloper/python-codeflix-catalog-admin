from src.core.category.domain.category import Category
from src.core.category.application.category_repository import CategoryRepository

class InMemoryCategoryRepository(CategoryRepository):
    def __init__(self, categories: Category=None):
        self.categories = categories or []

    def save(self, category):
        self.categories.append(category)
