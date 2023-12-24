import threading

def input_thread():
    while True:
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))

        sum_result = num1 + num2
        diff_result = num1 - num2

        print(f"Сумма чисел: {sum_result}")
        print(f"Разность чисел: {diff_result}")

def output_thread():
    while True:
        print(" Ожидание ввода чисел...")

# Создаем и запускаем потоки
input_thread = threading.Thread(target=input_thread)
output_thread = threading.Thread(target=output_thread)
input_thread.start()
output_thread.start()

# Ждем завершения потоков
input_thread.join()
output_thread.join()

