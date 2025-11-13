from datetime import datetime

class Journalisable:
    def journaliser(self, message):
        print(f"[Journal] {datetime.now()}: {message}")
