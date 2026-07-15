import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class GitAutoPusher(FileSystemEventHandler):
    def __init__(self):
        self.last_run = 0

    def on_any_event(self, event):
        # Ігноруємо зміни у службових папках Git та PyCharm, щоб не було нескінченного циклу
        if ".git" in event.src_path or ".idea" in event.src_path or "auto_git.py" in event.src_path:
            return

        # Захист від занадто частих запусків (пауза мінімум 5 секунд між пушами)
        current_time = time.time()
        if current_time - self.last_run < 5:
            return
        self.last_run = current_time

        print(f"🔄 Зміни виявлено в: {event.src_path}. Відправляємо на GitHub...")
        try:
            # Послідовно виконуємо стандартні команди Git
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", "Auto-update via script"], check=True)
            subprocess.run(["git", "push"], check=True)
            print("✅ GitHub успішно оновлено!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Помилка Git: {e}")


if __name__ == "__main__":
    event_handler = GitAutoPusher()
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=True)
    observer.start()
    print("🚀 Авто-пуш активовано! Пишіть код, зміни збережуться самі.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n🛑 Скрипт авто-пушу зупинено.")
    observer.join()