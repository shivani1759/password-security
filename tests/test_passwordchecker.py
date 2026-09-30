import unittest

from passwordchecker import (
    check_character_types,
    check_common_password,
    calculate_strength,
    give_recommendations
)


class TestPasswordSecurity(unittest.TestCase):

    def test_character_types(self):
        result = check_character_types("Password123!")

        self.assertEqual(result, (True, True, True, True))

    def test_common_password(self):
        self.assertTrue(check_common_password("password"))
        self.assertTrue(check_common_password("PASSWORD"))
        self.assertFalse(check_common_password("MySecurePassword123!"))

    def test_weak_password(self):
        has_upper, has_lower, has_number, has_special = \
            check_character_types("abc")

        is_common = check_common_password("abc")

        strength, score = calculate_strength(
            "abc",
            has_upper,
            has_lower,
            has_number,
            has_special,
            is_common
        )

        self.assertEqual(strength, "Weak")

    def test_strong_password(self):
        password = "Secure@123"

        has_upper, has_lower, has_number, has_special = \
            check_character_types(password)

        is_common = check_common_password(password)

        strength, score = calculate_strength(
            password,
            has_upper,
            has_lower,
            has_number,
            has_special,
            is_common
        )

        self.assertEqual(strength, "Strong")

    def test_recommendations(self):
        password = "password"

        has_upper, has_lower, has_number, has_special = \
            check_character_types(password)

        is_common = check_common_password(password)

        recommendations = give_recommendations(
            password,
            has_upper,
            has_lower,
            has_number,
            has_special,
            is_common
        )

        self.assertTrue(len(recommendations) > 0)


if __name__ == "__main__":
    unittest.main()
