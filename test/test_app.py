import requests
import unittest

BASE = "http://127.0.0.1:5000/"

dev = {'name':'Henrique Nishi', 'gender': 'Male',
    'age':28,'hobby': 'series','date_of_birth': "07/11/1992"}

dev_with_error = {'name':'Henrique Sueno Nishi', 'gender': 'Male', #'age':28,
    'hobby': 'series', 'date_of_birth': "07/11/1992"}

class TestApp(unittest.TestCase):

    """"
    Class used to implement the Unit Test
    """"

    def test_post(self):
        """
        Test for the post(insert) method

        1 - Add a developer with all the information
        """
        response = requests.post(BASE + "developer", data=dev)
        self.assertEqual(response.json(), {'name': 'Henrique Nishi', 'gender': 'Male', 'age': 28, 'hobby': 'series', 'date_of_birth': '07/11/1992'})
       
    def test_get(self):
        """
        Test for the get method

        1 - Get the entire table
        2 - Get the developer information based in the ID
        3 - Get the developers information based in a Query
        """
        response = requests.get(BASE + "developer")
        self.assertIsNotNone(response)

        response = requests.get(BASE + "developer/1")
        self.assertIsNotNone(response)

        #response = requests.get(BASE + "developer/?")
        #self.assertIsNotNone(response)
    

    def test_put(self):
        """
        Test for the put(update) method

        1 - Updates the information of an existing developer
        2 - Try to update the information of an developer that does not exist
        """
        response = requests.put(BASE + "developer/1", data={"age": 30})
        self.assertEqual(response.json(), {'id': 1, 'name': 'Henrique Nishi', 
              'gender': 'Male', 'age': 30, 'hobby': 'series', 'date_of_birth': '07/11/1992'})
        self.assertEqual(str(response), "<Response [200]>")

        response = requests.put(BASE + "developer/2", data={"age": 30})
        self.assertEqual(response.json(), {'message': 'Developer not found, cannot update'})
        self.assertEqual(str(response), "<Response [400]>")

    def test_delete(self):
        """
        Test for delete method

        1 - Delete existent Developer ID
        2 - Delete a Developer ID already deleted
        """
        response = requests.delete(BASE + "developer/1")
        self.assertEqual(str(response), "<Response [204]>")

        response = requests.delete(BASE + "developer/1")
        self.assertEqual(str(response), "<Response [400]>")


if __name__ == '__main__':
    unittest.main()