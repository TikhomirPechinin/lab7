import requests

BASE_URL = "http://127.0.0.1:8000"

def test_root():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_mean():
    response = requests.get(f"{BASE_URL}/mean?numbers=10,20,30")
    assert response.status_code == 200
    assert response.json()["result"] == 20.0

def test_mean_empty():
    response = requests.get(f"{BASE_URL}/mean?numbers=")
    assert response.status_code == 400

def test_factorial():
    response = requests.get(f"{BASE_URL}/factorial/5")
    assert response.status_code == 200
    assert response.json()["result"] == 120

def test_factorial_negative():
    response = requests.get(f"{BASE_URL}/factorial/-5")
    assert response.status_code == 400

def test_is_prime():
    response = requests.get(f"{BASE_URL}/is_prime/17")
    assert response.status_code == 200
    assert response.json()["result"] is True

def test_reverse():
    response = requests.get(f"{BASE_URL}/reverse?text=hello")
    assert response.status_code == 200
    assert response.json()["result"] == "olleh"

def test_count_vowels():
    response = requests.get(f"{BASE_URL}/count_vowels?text=hello")
    assert response.status_code == 200
    assert response.json()["result"] == 2

def test_capitalize():
    response = requests.get(f"{BASE_URL}/capitalize?text=hello world")
    assert response.status_code == 200
    assert response.json()["result"] == "Hello World"