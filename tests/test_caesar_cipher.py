import pytest
from caesar_cipher.caesar_cipher import encrypt, decrypt, crack, is_english

# @pytest.mark.skip("TODO")
def test_encrypt_life():
  assert encrypt

# @pytest.mark.skip("TODO")
def test_encrypt_15():
  actual = encrypt("Nick", 15)
  expected = "Cxrz"
  assert actual == expected

# @pytest.mark.skip("TODO")
def test_encrypt_0():
  actual = encrypt("Nick", 0)
  expected = "Nick"
  assert actual == expected

# @pytest.mark.skip("TODO")
def test_decrypt_life():
  assert decrypt

# @pytest.mark.skip("TODO")
def test_decrypt_15():
  actual = decrypt("Cxrz", 15)
  expected = "Nick"
  assert actual == expected

# @pytest.mark.skip("TODO")
def test_decrypt_0():
  actual = decrypt("Nick", 0)
  expected = "Nick"
  assert actual == expected

# @pytest.mark.skip("TODO")
def test_crack_life():
  assert crack

# @pytest.mark.skip("TODO")
def test_crack():
  actual = crack("Cxrz")
  expected = "Nick"
  assert actual == expected

# @pytest.mark.skip("TODO")
def test_is_english_life():
  assert is_english

# @pytest.mark.skip("TODO")
def test_is_english_():
  actual = is_english("Cxrz")
  expected = False
  assert actual == expected

# @pytest.mark.skip("TODO")
def test_is_english_():
  actual = is_english("Cat")
  expected = True
  assert actual == expected

# @pytest.mark.skip("TODO")
def test_is_english_():
  actual = is_english("cat")
  expected = True
  assert actual == expected

# @pytest.mark.skip("TODO")
def test_is_english_():
  actual = is_english("Nick")
  expected = True
  assert actual == expected

# @pytest.mark.skip("TODO")
def test_is_english_():
  actual = is_english("nick")
  expected = True
  assert actual == expected