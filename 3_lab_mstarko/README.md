# Звіт до роботи
## Тема: _Основи ООП_
### Мета роботи: _ Навчитись створювати та працювати з класами та обєктами, розібратись в основних елементах класів, та пропрацювати кодові конструкції які демонструють роботи класів та обєктів_

---
### Виконання роботи
Написали клас об'єкта та на його основі використали різні констуркції в класах
за допомогою Чат нагенерували тестові класи та виконали їх, код програм представлений Пайтон ноутбуці а основний клас знаходиться у файлі
виконали індивідуальні завдання на класі з завдання
1. Створення двох Python файлів .ipynb .py
2. Опис класу / Документаця
3. методи
4. класові зміні
5. Статичні методи
6. класові методи
* результати виконання індивідуального завдання (якщо такі є);
1.У Python, значення None є спеціальним об'єктом, який використовується для позначення відсутності значення або невизначеного стану. Коли ви передаєте None в параметр конструктора або методу, програміст може налаштувати поведінку так, щоб значення за замовчуванням було замінено на інше (наприклад, "Anonymous" у разі імені користувача).
2. Ви можете змінити метод say_hello(), щоб він використовував ім'я користувача або привітання за замовчуванням, якщо ім'я не задано.
class User:
    def __init__(self, name=None):
        self.name = name if name is not None else "Anonymous"
    
    def say_hello(self):
        print(f"Привіт, {self.name}!")

3. Функція len() повертає довжину (кількість символів) рядка. Ви можете додати метод до класу, який буде рахувати кількість букв в імені:
class User:
    def __init__(self, name=None):
        self.name = name if name is not None else "Anonymous"
    
    def say_hello(self):
        print(f"Привіт, {self.name}!")
    
    def count_letters(self):
        return len(self.name)

4.names = ["Іван", "Марія", "Олександр", None, "Анна"]
valid_names = [name for name in names if name is not None]  # Фільтруємо None
print(len(valid_names))  # Виведе: 4
Якщо ви порахуєте лише ті елементи, що не є None, то кількість імен буде 4, оскільки None не є іменем і не буде враховане
---
### Висновок:
> у висновку потрібно відповісти на запитання: Навчився створювати та працювати з класами та обєктами, розібратись в основних елементах класів, та пропрацювати кодові конструкції які демонструють роботи класів та обєктів
- :question: Що зроблено в роботі;. Опис класу / Документаця ,методи ,класові зміні ,Статичні методи , класові методи
- :question: Чи досягнуто мети роботи; так
- :question: Які нові знання отримано;
- :question: Чи вдалось відповісти на всі питання задані в ході роботи; так
- :question: Чи вдалося виконати всі завдання; так
- :question: Чи виникли складності у виконанні завдання; ні
- :question: Чи подобається такий формат здачі роботи (Feedback); так
- :question: Побажання для покращення (Suggestions); все було чудово 

---