import pytest

from bot.handlers.echo import echo_handler


@pytest.mark.asyncio
async def test_echo_handler(mock_update, mock_context):
    """Тест эхо-обработчика"""
    test_text = "Hello, World!"
    mock_update.message.text = test_text

    await echo_handler(mock_update, mock_context)

    mock_update.message.reply_text.assert_called_once_with(f"Вы сказали: {test_text}")


@pytest.mark.asyncio
async def test_echo_handler_empty_message(mock_update, mock_context):
    """Тест с пустым сообщением"""
    mock_update.message.text = ""

    await echo_handler(mock_update, mock_context)

    mock_update.message.reply_text.assert_called_once_with("Вы сказали: ")
