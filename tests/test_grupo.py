import pytest
from posting.widgets.confirmation import ConfirmationModal

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