from time import sleep

import hashlib

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = int(hashlib.sha256(password.encode()).hexdigest(), 16)  # Хешируем пароль
        self.age = age


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        hashed_password = int(hashlib.sha256(password.encode()).hexdigest(), 16)
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                return True
        return False

    def register(self, nickname, password, age):
        if any(user.nickname == nickname for user in self.users):
            print(f"Пользователь {nickname} уже существует")
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if not any(existing_video.title == video.title for existing_video in self.videos):
                self.videos.append(video)

    def get_videos(self, search_word):
        return [video.title for video in self.videos if search_word.lower() in video.title.lower()]

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        found_video = next((video for video in self.videos if video.title == title), None)

        if found_video is None:
            print(f"Видео '{title}' не найдено.")
            return

        if found_video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        for second in range(found_video.time_now + 1, found_video.duration + 1):
            print(second)
            sleep(1)

        found_video.time_now = 0
        print("Конец видео")



if __name__ == "__main__":
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавляем видео
    ur.add(v1, v2)

    # Проверяем поиск
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Пробуем посмотреть видео без авторизации
    ur.watch_video('Для чего девушкам парень программист?')

    # Регистрация нового пользователя младше 18 лет
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')  # Возрастное ограничение

    # Регистрация другого пользователя старше 18 лет
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')  # Теперь он сможет посмотреть

    # Попробуем войти под другим пользователем
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user.nickname)

    # Пытаемся воспроизвести несуществующее видео
    ur.watch_video('Лучший язык программирования 2024 года!')