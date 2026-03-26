import unittest
from unittest.mock import Mock, patch
import weather_service


class TestWeatherService(unittest.TestCase):
    def test_get_weather_success(self):
        with patch("weather_service.api_client.fetch_weather_data") as mock_fetch:
            mock_fetch.return_value = {"city": "Banjaluka", 
                                       "temp": 11, 
                                       "condition": 
                                       "sunny", 
                                       "humidity": 78}
            result = weather_service.get_weather("Banjaluka")
            self.assertEqual(result["temp"], 11)
            self.assertEqual(result["condition"], "sunny")
            self.assertEqual(result["humidity"], 78)
            mock_fetch.assert_called_once_with("Banjaluka")

    def test_get_weather_api_error(self):
        with patch("weather_service.api_client.fetch_weather_data") as mock_fetch:
            mock_fetch.return_value = {"error": "City not found"}

            result = weather_service.get_weather("InvalidCity")

            self.assertIn("error", result)

    def test_get_weather_timeout(self):
        with patch("weather_service.api_client.fetch_weather_data") as mock_fetch:
            mock_fetch.side_effect = TimeoutError("The request has timed out")

            with self.assertRaises(TimeoutError):
                result = weather_service.get_weather("Banjaluka")
         

    @patch("weather_service.api_client.fetch_forecast")
    def test_get_forecast_with_patch(self, mock_fetch):
        mock_fetch.return_value = [{"day": 1, "temp": 11, "condition": "sunny"},
                                   {"day": 2, "temp": 12, "condition": "sunny"}]
        
        result = weather_service.get_forecast("Banjaluka", days=2)
        self.assertEqual(len(result), 2)
        mock_fetch.assert_called_with("Banjaluka", 2)

    @patch("weather_service.api_client.datetime")
    def test_greeting_morning(self, mock_datetime):
        mock_now = Mock()
        mock_now.hour = 9
        mock_datetime.datetime.now.return_value = mock_now

        result = weather_service.get_greeting_based_on_time()
        self.assertEqual(result, "Good morning!")

    @patch("weather_service.api_client.datetime")
    def test_greeting_afternoon(self, mock_datetime):
        mock_now = Mock()
        mock_now.hour = 14
        mock_datetime.datetime.now.return_value = mock_now

        result = weather_service.get_greeting_based_on_time()
        self.assertEqual(result, "Good afternoon!")


if __name__ == "__main__":
    unittest.main()
