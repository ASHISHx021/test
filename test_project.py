import unittest
from project import get_grok_response, update_chat_history, create_gui

class TestGrokChatbot(unittest.TestCase):
    def test_grok_response(self):
        """Test if we get a response from Grok"""
        response = get_grok_response("Hello")
        # Check if we get back a string
        self.assertTrue(isinstance(response, str))
        # Check if the response isn't empty
        self.assertTrue(len(response) > 0)

    def test_empty_message(self):
        """Test sending an empty message to Grok"""
        response = get_grok_response("")
        # Check if we get some kind of response even with empty input
        self.assertTrue(isinstance(response, str))

    def test_long_message(self):
        """Test sending a long message to Grok"""
        long_message = "hello " * 100
        response = get_grok_response(long_message)
        # Check if we still get a response with a long message
        self.assertTrue(isinstance(response, str))

if __name__ == '__main__':
    unittest.main()
