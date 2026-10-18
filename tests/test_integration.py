from unittest.mock import MagicMock, patch

from app.llm_service import generate_response


@patch("app.llm_service.chat")
def test_generate_response(mock_chat):
    mock_chat.return_value = MagicMock()
    mock_chat.return_value.message.content = "delhi"

    result = generate_response("capital of india")

    assert result == "delhi"
