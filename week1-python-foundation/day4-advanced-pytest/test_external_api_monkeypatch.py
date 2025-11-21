from external_api import get_weather

class FakeResponse:
    def __init__(self, data):
        self._data = data

    def json(self):
        return self._data


def test_get_weather_monkeypatch(monkeypatch):
    def fake_get(url):
        return FakeResponse({"temp": 25, "status": "sunny"})

    monkeypatch.setattr("external_api.requests.get", fake_get)

    result = get_weather("peshawar")

    assert result == {"temp": 25, "status": "sunny"}
