from fastapi import FastAPI, HTTPException
from my_library import calculate_mean, factorial, is_prime
from my_library import reverse_string, count_vowels, capitalize_words

app = FastAPI(
    title="API для библиотеки my_library",
    description="REST API для математических и строковых функций",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {
        "message": "Добро пожаловать в API библиотеки",
        "endpoints": [
            "/mean?numbers=1,2,3",
            "/factorial/{n}",
            "/is_prime/{n}",
            "/reverse?text=hello",
            "/count_vowels?text=hello",
            "/capitalize?text=hello world"
        ]
    }

@app.get("/mean")
def get_mean(numbers: str):
    """Вычисляет среднее арифметическое списка чисел"""
    try:
        numbers_list = [float(n) for n in numbers.split(",")]
        if not numbers_list:
            raise HTTPException(status_code=400, detail="Список чисел не может быть пустым")
        result = calculate_mean(numbers_list)
        return {"input": numbers, "result": result}
    except ValueError:
        raise HTTPException(status_code=400, detail="Неверный формат чисел. Ожидается: 1,2,3")

@app.get("/factorial/{n}")
def get_factorial(n: int):
    """Вычисляет факториал числа"""
    try:
        result = factorial(n)
        return {"input": n, "result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/is_prime/{n}")
def get_is_prime(n: int):
    """Проверяет, является ли число простым"""
    result = is_prime(n)
    return {"input": n, "result": result}

@app.get("/reverse")
def get_reverse(text: str):
    """Переворачивает строку"""
    try:
        result = reverse_string(text)
        return {"input": text, "result": result}
    except TypeError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/count_vowels")
def get_count_vowels(text: str):
    """Подсчитывает количество гласных в строке"""
    try:
        result = count_vowels(text)
        return {"input": text, "result": result}
    except TypeError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/capitalize")
def get_capitalize(text: str):
    """Преобразует первую букву каждого слова в заглавную"""
    try:
        result = capitalize_words(text)
        return {"input": text, "result": result}
    except TypeError as e:
        raise HTTPException(status_code=400, detail=str(e))
    