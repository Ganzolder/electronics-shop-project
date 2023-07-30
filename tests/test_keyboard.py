from src.keyboard import Keyboard
import pytest
import sys
sys.path.append('../')


kb = Keyboard('Dark Project KD87A', 9600, 5)

def test_creation():
    assert str(kb) == "Dark Project KD87A"

def test_chng_lang():
    assert str(kb.language) == "EN"

    kb.change_lang()
    assert str(kb.language) == "RU"

    # Сделали RU -> EN -> RU
    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"

def test_chng_protection():
    with pytest.raises(AttributeError):
        kb.language = 'CH'

# AttributeError: property 'language' of 'Keyboard' object has no setter
