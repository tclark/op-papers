import unittest
import person

class TestPerson(unittest.TestCase):

    def setUp(self):
        self.person = person.Person("Homer", "Simpson")
        self.person.age = 45

    def test_constructor(self):
        self.assertIsInstance(self.person, person.Person)
        self.assertEqual(self.person.first_name, "Homer")
        self.assertEqual(self.person.last_name, "Simpson")

    def test_change_name(self):
        self.person.change_name("Nelson", "Muntz")
        self.assertEqual(self.person.first_name, "Nelson")
        self.assertEqual(self.person.last_name, "Muntz")

    def test_increment_age(self):
        new_age = self.person.age + 1
        self.assertEqual(self.person.increment_age(), new_age);

    def test_kill(self):
        self.person.kill()
        self.assertTrue(self.person.dead)

if __name__ == '__main__':
    unittest.main()
