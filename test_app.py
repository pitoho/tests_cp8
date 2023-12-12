import pytest
import asyncio
from app import get_json

@pytest.mark.asyncio
async def test_get_json():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    result = await get_json(url)
    assert result is not None
    assert "userId" in result
    assert "id" in result
    assert "title" in result
    assert "body" in result
