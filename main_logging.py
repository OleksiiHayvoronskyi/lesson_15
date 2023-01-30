import logging
import task_1_server


# Основна функція логування.
def get_logging():

    logger = logging.getLogger("logging")
    logger.setLevel(logging.INFO)

    # Файл, куди буде записуватися інформація про логування.
    file_name = logging.FileHandler("server.log")
    # Формат запису повідомлень у журналі подій (server.log).
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_name.setFormatter(formatter)

    # Обробник подій.
    logger.addHandler(file_name)

    result = task_1_server.get_serv()


if __name__ == "__main__":
    get_logging()
