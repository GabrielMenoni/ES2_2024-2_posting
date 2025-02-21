from pathlib import Path
from unittest.mock import AsyncMock, patch

import pytest

from posting.__main__ import make_posting
import posting.app
from posting.widgets.confirmation import ConfirmationModal

TEST_DIR = Path(__file__).parent
CONFIG_DIR = TEST_DIR / "sample-configs"
ENV_DIR = TEST_DIR / "sample-envs"
THEME_DIR = TEST_DIR / "sample-themes"
SAMPLE_COLLECTIONS = TEST_DIR / "sample-collections"
POSTING_MAIN = TEST_DIR / "posting_snapshot_app.py"

def test_confirmetion_model_init():
    confirmation_message = "Mensagem exemplo"
            
    confirmation_model = ConfirmationModal(
        message=confirmation_message,
    )

    assert confirmation_model.message == confirmation_message
    assert confirmation_model.id is None

    assert confirmation_model.confirm_text == "Yes \\[y]"
    assert confirmation_model.confirm_binding == "y"
    assert confirmation_model.cancel_text == "No \\[n]"
    assert confirmation_model.cancel_binding == "n"
    assert confirmation_model.auto_focus == "confirm"
    assert confirmation_model.name is None  


@pytest.mark.asyncio()
async def test_xpto():
    env_path = str((ENV_DIR / "sample_base.env").resolve())
    app = make_posting(
        collection=SAMPLE_COLLECTIONS / "jsonplaceholder" / "todos",
        env=(env_path,),
    )
    screen = app.get_default_screen()

    with patch.object(screen, "notify", new=AsyncMock()):
        screen.xpto()

    assert posting.app.FLAG is True

