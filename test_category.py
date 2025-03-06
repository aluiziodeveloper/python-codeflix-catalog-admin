import unittest
from uuid import UUID
import uuid

from category import Category

class TestCategory(unittest.TestCase):
    def test_name_is_required(self):
        with self.assertRaisesRegex(TypeError, "missing 1 required positional argument: 'name'"):
            Category()

    def test_name_must_have_less_than_255_characters(self):
        with self.assertRaisesRegex(ValueError, "name must have less than 256 characters"):
            Category(name="a" * 256)

    def test_category_must_be_created_with_id_as_uuid_by_default(self):
        category = Category(name="Filme")
        self.assertEqual(type(category.id), UUID)

    def test_create_category_with_default_values(self):
        category = Category(name="Filme")
        self.assertEqual(category.name, "Filme")
        self.assertEqual(category.description, "")
        self.assertEqual(category.is_active, True)

    def test_create_category_as_active_by_default(self):
        category = Category(name="Filme")
        self.assertEqual(category.is_active, True)

    def test_create_category_with_provided_values(self):
        category_id = uuid.uuid4()
        category = Category(
            id=category_id,
            name="Filme",
            description="Capitão América",
            is_active=False,
        )
        self.assertEqual(category.id, category_id)
        self.assertEqual(category.name, "Filme")
        self.assertEqual(category.description, "Capitão América")
        self.assertEqual(category.is_active, False)

if __name__ == "__main__":
    unittest.main()
