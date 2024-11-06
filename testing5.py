import unittest

def sayHello(name):
    if len(name) > 5:
        raise Exception("Name greater than 5 characters")
    else:
        return name
class testAplikasi(unittest.TestCase):
    def test_sayHello_success(self):
        result = sayHello("Gallay")
        expectation = "Gallay"
# result = first, second = expectation
        self.assertEqual(result, expectation)
    def test_sayHello_error(self):
        self.assertRaises(Exception, sayHello)

if __name__ == "__main__":
    unittest.main()
