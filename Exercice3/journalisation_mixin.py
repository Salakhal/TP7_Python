from datetime import datetime

class JournalisationMixin:
    def journaliser(self, message):
        print(f"[Journal] {datetime.now()}: {message}")
