# #Task 1
# try:
#     def get_keys_with_value_true(input_dict):
#         return [key for key, value in input_dict.items() if value == True]
#     user_input_dict = {}
#     num_of_entries = int(input("Введите количество статей в словаре: "))
#     for _ in range(num_of_entries):
#         key = input("Введите клавишу: ")
#         value = input("Введите значение (True/False): ")
#         user_input_dict[key] = value.lower() == 'true'
#     result = get_keys_with_value_true(user_input_dict)
#     print("Клавиш со значением True:", result)
# except ValueError:
#    print ("Error")

# #Task 2
# try:
#     def unique_elements_from_user():
#         input_list_str = input("Введите список чисел, разделенный пробелами: ")
#         input_list = [int(x) for x in input_list_str.split()]
#         unique_elements = []
#         element_counter = {}
#         for element in input_list:
#             element_counter[element] = element_counter.get(element, 0) + 1
#         for element, count in element_counter.items():
#             if count <= 1:
#                 unique_elements.append(element)
#         return unique_elements
#     output_list = unique_elements_from_user()
#     print("Уникальные элементы:", output_list)
# except ValueError:
#     print ("Error")


# #Task 3
# try:
#     from datetime import datetime

#     def date_in_format():
#         date_input = input("Введите дату (ГГГГ.ММ.ДД): ")
#         try:
#             date_object = datetime.strptime(date_input, '%Y.%m.%d')
#             formatted_date = date_object.strftime('%d.%m.%Y')
#             return formatted_date
#         except ValueError:
#             print("Неверный формат даты. Пожалуйста введите дату в формате ГГГГ.ММ.ДД.")
#             return None
#     output_date = date_in_format()
#     if output_date:
#         print("Форматированная дата:", output_date)
# except ValueError:
#     print ("Error")


# #Task 4
# try:
#     def get_elements_with_no_more_than_two_occurrences(input_list):
#         # Создаем словарь для подсчета количества ввода каждого элемента
#         occurrences = {}
        
#         # Проходимся по каждому элементу в списке и увеличиваем счетчик в словаре
#         for element in input_list:
#             occurrences[element] = occurrences.get(element, 0) + 1
        
#         # Создаем новый список, включая только те элементы, у которых больше одного повторения
#         result_list = [element for element in input_list if occurrences[element] > 1]

#         # Удаляем повторяющиеся элементы, чтобы результат не содержал дубликатов
#         result_list = list(set(result_list))
#         return result_list

#     # Вводим данные с помощью функции input
#     user_input = input("Введите список чисел через пробел: ")
#     input_list = [int(num) for num in user_input.split()]

#     # Вызываем функцию и выводим результат
#     result = get_elements_with_no_more_than_two_occurrences(input_list)
#     print("Результат:", result)
# except Exception as e:
#     print ("Error")


# #Task 5
# try:
#     def get_words_from_string():
#         # Получаем данные от пользователя
#         input_string = input("Введите строку: ")
        
#         # Разбиваем строку на слова
#         words = input_string.split()
#         return words
#     output_list = get_words_from_string()
#     print(output_list)
# except Exception as e:
#     print ("Error")


# #Task 6
# try:
#     def get_unique_elements_with_count(lst):
#         unique_elements_count = {}
        
#         for element in lst:
#             if element in unique_elements_count:
#                 unique_elements_count[element] += 1
#             else:
#                 unique_elements_count[element] = 1
        
#         return unique_elements_count

#     # Ввод данных с использованием input
#     input_list = input("Введите элементы списка через запятую: ").split(',')
#     input_list = [int(item.strip()) for item in input_list]

#     result = get_unique_elements_with_count(input_list)
#     print(result)
# except Exception as e:
#     print ("Error")


# #Task 7
# try:
#     def is_prime(num):
#         if num < 2:
#             return False
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 return False
#         return True
#     def get_prime_numbers(n):
#         primes = [num for num in range(2, n + 1) if is_prime(num)]
#         return primes
#     def main():
#         try:
#             n = int(input("Введите число n: "))
#             result = get_prime_numbers(n)
#             print(result)
#         except ValueError:
#             print("Ошбика. Пожалуйста, введите корректное число.")
#     if __name__ == "__main__":
#         main()
# except Exception as e:
#     print ("Error")


# #Task 8
# try:
#     def is_prime(num):
#         if num < 2:
#             return False
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 return False
#         return True

#     def get_prime_numbers_in_list(input_list):
#         prime_numbers = [num for num in input_list if is_prime(num)]
#         return prime_numbers

#     # Получаем ввод от пользователя
#     user_input = input("Введите числа через пробел: ")
#     user_numbers = list(map(int, user_input.split()))

#     # Вызываем функцию и выводим результат
#     result = get_prime_numbers_in_list(user_numbers)
#     print("Простые числа из введенного списка:", result)

#     #В выводе не считается 1, так как простые числа обычно считаются с 2 
# except Exception as e:
#     print ("Error")


# #Task 9
# try:
#     from datetime import datetime

#     def get_difference_between_dates(date1, date2):
#         # Преобразовываем строки в объекты datetime
#         date1 = datetime.strptime(date1, "%Y.%m.%d")
#         date2 = datetime.strptime(date2, "%Y.%m.%d")

#         # Рассчитываем разницу между датами
#         date_difference = abs((date2 - date1).days)

#         return date_difference

#     # Ввод дат с помощью input
#     date_input1 = input("Введите первую дату в формате ГГГГ.ММ.ДД: ")
#     date_input2 = input("Введите вторую дату в формате ГГГГ.ММ.ДД: ")

#     # Получение разницы между датами и вывод результата
#     difference = get_difference_between_dates(date_input1, date_input2)
#     print("Разница между датами в днях:", difference)
# except Exception as e:
#     print ("Error")


# #Task 10
# try:
#     def is_prime_number(num):
#         if num < 2:
#             return False
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 return False
#         return True
#     def get_decimal_number_from_binary_string(binary_string):
#         decimal_number = int(binary_string, 2)
#         return decimal_number
#     def combine_digits_to_numbers(digits):
#         combined_numbers = []
#         for i in range(len(digits) - 1):
#             combined_numbers.append(int(str(digits[i]) + str(digits[i + 1])))
#         return combined_numbers
#     def get_prime_numbers_from_binary_input():
#         # Ввод двоичных чисел через запятую
#         binary_inputs = input("Введите двоичные числа через запятую: ")

#         # Разделение введенных данных на список двоичных чисел
#         binary_numbers = binary_inputs.split(',')

#         # Преобразование каждого двоичного числа в десятичное и объединение цифр
#         combined_digits = []
#         for binary_number in binary_numbers:
#             decimal_number = get_decimal_number_from_binary_string(binary_number.strip())
#             combined_digits.extend(str(decimal_number))

#         # Объединение отдельных цифр в числа
#         combined_numbers = combine_digits_to_numbers(combined_digits)

#         # Печать объединенных чисел
#         print("Объединенные числа:", combined_numbers)

#         # Проверка, являются ли объединенные числа простыми
#         for num in combined_numbers:
#             if is_prime_number(int(num)):
#                 print(f"Число {num} является простым.")
#             else:
#                 print(f"Число {num} не является простым.")
#     if __name__ == "__main__":
#         get_prime_numbers_from_binary_input()
# except Exception as e:
#     print("Error")


# #Task 11
# try:
#     def is_perfect_square(num):
#         square_root = int(num ** 0.5)
#         return square_root * square_root == num
#     def is_expression_true(expression):
#         try:
#             numbers = [int(x) for x in expression.split(',')]
#             all_perfect_squares = all(is_perfect_square(num) for num in numbers)
#             return all_perfect_squares
#         except ValueError:
#             return "Ошибка ввода. Введите числа, разделенные запятой."
#     # Ввод данных с помощью input
#     input_expression = input("Введите числа, разделенные запятой: ")
#     output = is_expression_true(input_expression)
#     print(output)
# except Exception as e:
#     print ("Error")


# #Task 12
# try:
#     def sort_by_price(shopping_list):
#         return sorted(shopping_list, key=lambda x: x.get('price', 0))
#     def input_shopping_list():
#         shopping_list = []
#         while True:
#             user_input = input("Введите название товара и цену (или нажмите Enter для завершения ввода): ")
#             if user_input.lower() == '':
#                 break
#             # Разделяем ввод на название и цену
#             parts = user_input.split(',')
#             if len(parts) != 2:
#                 print("Неверный формат ввода. Пожалуйста, введите название и цену через запятую.")
#                 continue
#             name, price_str = parts
#             try:
#                 price = float(price_str)
#             except ValueError:
#                 print("Неверный формат цены. Пожалуйста, введите число.")
#                 continue
#             item = {"name": name.strip(), "price": price}
#             shopping_list.append(item)
#         return shopping_list
#     if __name__ == "__main__":
#         shopping_list = input_shopping_list()
#         sorted_list = sort_by_price(shopping_list)
#         print("Отсортированный список покупок по цене:")
#         print(sorted_list)
# except Exception as e:
#     print ("Error")


# #Task 13
# try:
#     def get_words_starting_with_vowel(words):
#         vowels = "aeiouyAEIOUY"
#         result = [word for word in words if word[0] in vowels]
#         return result
#     # Получаем ввод от пользователя
#     input_words = input("Введите список слов через запятую: ")
#     # Проверяем, что введены хотя бы какие-то буквы
#     if not any(c.isalpha() for c in input_words):
#         print("Ошибка: Введите хотя бы одно слово.")
#     else:
#         # Разбиваем строку на список слов
#         word_list = input_words.split(", ")
#         # Вызываем функцию и выводим результат
#         result_list = get_words_starting_with_vowel(word_list)
#         print(result_list)
# except Exception as e:
#     print ("Error")