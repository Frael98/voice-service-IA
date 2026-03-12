from unittest.mock import patch

@patch("src.services.tts_services.TTSService")
def test_text_to_voice(mock_tts, client):

    # mock_tts.tts.return_value = "fake_audio"

    response = client.post(
        "/v1/speech/text-to-voice",
        json={
            "text": "Esta es una prueba"
        }
    )

    assert response.status_code == 200