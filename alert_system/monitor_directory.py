from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from alertchecker import AlertSystem
import os

DEFAULT_DIR = os.getenv('DEFAULT_DIR', '../logs/')


class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        alert_system = AlertSystem(event.src_path, check_with_code_zero=True)
        alert_system.check_on_minutes()
        alert_system.check_on_hour()


event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path=DEFAULT_DIR, recursive=False)
observer.start()

while True:
    try:
        pass
    except KeyboardInterrupt:
        observer.stop()