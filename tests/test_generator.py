import unittest
from password_generator.generator import PasswordGenerator


class TestPasswordGenerator(unittest.TestCase):

    def test_generate_length(self):
        gen = PasswordGenerator(length=20)
        pwd = gen.generate()
        self.assertEqual(len(pwd), 20)

    def test_generate_pools(self):
        gen = PasswordGenerator(use_lower=False, use_upper=False,
                                use_digits=True, use_special=False)
        pwd = gen.generate()
        self.assertTrue(all(c.isdigit() for c in pwd))

    def test_phrase_length(self):
        gen = PasswordGenerator()
        phrase = gen.generate_phrase(words=3, add_digits=False)
        self.assertEqual(len(phrase.split('-')), 3)

    def test_entropy(self):
        gen = PasswordGenerator()
        pwd = "abcd"
        ent = gen.entropy(pwd)
        self.assertAlmostEqual(ent, 4 * 2.0, places=1)

    def test_ambiguous(self):
        gen = PasswordGenerator(ambiguous=False)
        pwd = gen.generate()
        if gen.use_digits:
            self.assertNotIn('0', pwd)
            self.assertNotIn('1', pwd)


if __name__ == "__main__":
    unittest.main()