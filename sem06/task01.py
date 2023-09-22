'''Контекст
В каждом телефоне есть это замечательное приложение.
Секундомер - это программа, которая засекает сколько
времени прошло от момента запуска до момента остановки.
Также, как правило там присутствует функция “паузы”,
которая позволяет временно приостановить секундомер, с
возможностью продолжить отсчет в будущем.
● Ваша задача
Реализовать секундомер на любом языке программирования
в любой парадигме. Секундомер должен поддерживать
следующий функционал:
○ Запуск
○ Пауза
○ Выход из паузы
○ Остановка"
'''

import time

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.pause_time = None
        self.total_pause_duration = 0
    
    def start(self):
        if self.start_time is not None:
            print("Stopwatch is already running.")
        else:
            self.start_time = time.time()
            print("Stopwatch started.")
    
    def pause(self):
        if self.start_time is None:
            print("Stopwatch is not running.")
        elif self.pause_time is not None:
            print("Stopwatch is already paused.")
        else:
            self.pause_time = time.time()
            print("Stopwatch paused.")
    
    def resume(self):
        if self.start_time is None:
            print("Stopwatch is not running.")
        elif self.pause_time is None:
            print("Stopwatch is not paused.")
        else:
            self.total_pause_duration += time.time() - self.pause_time
            self.pause_time = None
            print("Stopwatch resumed.")
    
    def stop(self):
        if self.start_time is None:
            print("Stopwatch is not running.")
        else:
            elapsed_time = time.time() - self.start_time - self.total_pause_duration
            self.start_time = None
            self.pause_time = None
            self.total_pause_duration = 0
            print(f"Stopwatch stopped. Elapsed time: {elapsed_time:.2f} seconds.")


# Пример использования

stopwatch = Stopwatch()

stopwatch.start()
time.sleep(2)  # имитируем прошедшее время
stopwatch.pause()
time.sleep(1)
stopwatch.resume()
time.sleep(2)
stopwatch.stop()