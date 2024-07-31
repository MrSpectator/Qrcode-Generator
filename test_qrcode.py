import pytest
import qrcode



from qrcode import code, custom_color, save_code

def test_code():
    data = "Hello, QR Code!"
    with pytest.raises(Exception):
        code("1 inincinco" * 10000000000000000000000)

def test_custom_color(monkeypatch):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data("Test")
    qr.make(fit=True)

    # Mock inputs
    monkeypatch.setattr('builtins.input', lambda _: '#FF0000')

    img = custom_color(qr)
    assert img is not None

def test_save_code():
    img = qrcode.make("Test")
    try:
        save_code(img)
    except Exception:
        pytest.fail("showcode raised an exception unexpectedly!")