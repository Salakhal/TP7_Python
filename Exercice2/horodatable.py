from datetime import datetime

class Horodatable:
    def horodatage(self):
        print(f"[LOG] Action à {datetime.now()}")
