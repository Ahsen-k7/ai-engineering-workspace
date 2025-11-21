from unittest.mock import patch, MagicMock
from external_api import get_weather

def test_get_weather_patch():
    fake_response = MagicMock()
    fake_response.json.return_value = {"temp": 20, "status": "clear"}

    with patch("external_api.requests.get", return_value=fake_response):
        result = get_weather("peshawar")

    assert result == {"temp": 20, "status": "clear"}
