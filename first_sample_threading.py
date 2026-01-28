from threading import Thread
import time

def worker(name, duration):
    time.sleep(duration)
    print(f"{name} завершил работу")

# РУЧНОЕ управление потоками
threads = []
for i in range(5):
    thread = Thread(target=worker, args=(f"Работник {i}", i+1))
    thread.start()
    threads.append(thread)#Эти 3 строчки почти мгновенно сработали (создались и запустились 5 потоков
    # и вместе с ними их sleep)
    # и программа перешла дальше

# РУЧНОЕ ожидание завершения
for thread in threads:
    thread.join()#join 5 раз не пустила основной поток к print.
    # До этого почти сразу у пятерых потоков начался sleep и с каждой секундой печатался print

# Если бы thread.join() был после threads.start, то программа выполнялась не 5 сек,
# как сейчас, а 0+1+2+3+4, то есть после join программа бы ждала в цикле завершения каждого потока

print("Все потоки завершены")