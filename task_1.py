from queue import Queue
import random
import time


def generate_request(queue: Queue, req_id: int):
    request = f"Заявка №{req_id}"
    queue.put(request)
    print(f"Створено нову заявку №{req_id}")


def process_request(queue: Queue):
    if not queue.empty():
        request = queue.get()
        print(f"Обробка заявки: {request}")
        # Симуляція затримки обробки
        time.sleep(random.uniform(0.5, 2))
    else:
        print(f"Черга заявок пуста")


def main():
    request_queue = Queue()
    request_id = 0

    try:
        while True:
            # Симуляція затримки генерації
            time.sleep(1)

            # Генерація заявок
            if random.choice([True, False]):
                request_id += 1
                generate_request(request_queue, request_id)

            # Обробка заявок
            if random.choice([True, False]):
                process_request(request_queue)
    except KeyboardInterrupt:
        print("\nUser interrupted")


if __name__ == "__main__":
    main()
