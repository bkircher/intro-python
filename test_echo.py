import unittest
from unittest.mock import patch, MagicMock
import asyncio
from echo import fetch_content_sync, fetch_content_async


class TestMain(unittest.TestCase):

    @patch('requests.get')
    def test_fetch_content_sync(self, mock_get):
        mock_response = MagicMock()
        mock_response.text = "# Mocked Markdown Response"
        mock_get.return_value = mock_response

        url = "https://example.com"
        response = fetch_content_sync(url)

        mock_get.assert_called_with(url)
        self.assertEqual(response.text, "# Mocked Markdown Response")

    @patch('requests.get')
    def test_fetch_content_async(self, mock_get):
        mock_response = MagicMock()
        mock_response.text = "# Mocked Async Markdown Response"
        mock_get.return_value = mock_response

        url = "https://example.com"

        response = asyncio.run(fetch_content_async(url))

        mock_get.assert_called_with(url)
        self.assertEqual(response.text, "# Mocked Async Markdown Response")


if __name__ == '__main__':
    unittest.main()