import random

def generate_random_numbers(count):
    return [random.randint(1, 100) for _ in range(count)]

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def find_maximum(numbers):
    return max(numbers)

def main():
    num_count = 10
    random_numbers = generate_random_numbers(num_count)

    print(f"Сгенерированные случайные числа: {random_numbers}")
    print(f"Среднее значение: {calculate_average(random_numbers)}")
    print(f"Максимальное значение: {find_maximum(random_numbers)}")

if __name__ == "__main__":
    main()
