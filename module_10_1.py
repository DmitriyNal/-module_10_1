from threading import Thread
from time import sleep
from datetime import datetime


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


if __name__ == "__main__":
    start_time_functions = datetime.now()
    write_words(10, "example1.txt")
    write_words(30, "example2.txt")
    write_words(200, "example3.txt")
    write_words(100, "example4.txt")
    end_time_functions = datetime.now()
    print(end_time_functions - start_time_functions)

    start = datetime.now()

    t1 = Thread(target=write_words, args=(10, "example5.txt"))
    t2 = Thread(target=write_words, args=(30, "example6.txt"))
    t3 = Thread(target=write_words, args=(200, "example7.txt"))
    t4 = Thread(target=write_words, args=(100, "example8.txt"))

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    end = datetime.now()
    print(f"Время выполнения: {end - start} секунд")
