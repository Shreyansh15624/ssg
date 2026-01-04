import unittest

from getcontent import extract_title

class TestContentManipulation(unittest.TestCase):
    def test_extract_title(self):
        # Simple Test for the over all function
        markdown = "# Hello World"
        self.assertEqual(extract_title(markdown), "Hello World")
    
    def test_extract_title_with_extra_whitespace(self):
        # Testing the 'lstip' & 'rstrip' functionality specifically
        markdown = "#         Hello World        "
        self.assertEqual(extract_title(markdown), "Hello World")
    
    def test_extract_title_multiline(self):
        # Testing if there is no issue with the logic of identifying the right line
        markdown = """
## Not this line
# This is the line
### Not this line either
        """
        self.assertEqual(extract_title(markdown), "This is the line")
    
    def test_extract_title_None(self):
        # Testing to see if the established exception is raised properly
        markdown = """
## Not this line
### Definitely not this line
Just some regular text
        """
        with self.assertRaises(Exception):
            extract_title(markdown)

if __name__=="__main__":
    unittest.main()