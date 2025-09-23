import pytest
from unittest.mock import AsyncMock
from telegram import Update, Message, User, Chat
from telegram.ext import ContextTypes


@pytest.fixture
def mock_update():
    """Фикстура для создания mock Update"""
    update = AsyncMock(spec=Update)
    update.message = AsyncMock(spec=Message)
    update.message.text = "test message"
    update.message.reply_text = AsyncMock()
    update.message.reply_html = AsyncMock()

    user = AsyncMock(spec=User)
    user.mention_html.return_value = "<b>Test User</b>"
    update.effective_user = user

    chat = AsyncMock(spec=Chat)
    chat.id = 12345
    update.message.chat = chat

    return update


@pytest.fixture
def mock_context():
    """Фикстура для создания mock Context"""
    context = AsyncMock(spec=ContextTypes.DEFAULT_TYPE)
    context.args = []
    return context


@pytest.fixture
def mock_context_with_args():
    """Фикстура для Context с аргументами"""
    context = AsyncMock(spec=ContextTypes.DEFAULT_TYPE)
    context.args = ['Moscow']
    return context
