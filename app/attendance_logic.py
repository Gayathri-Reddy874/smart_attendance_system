import time
from datetime import datetime
from app.database import insert_attendance
from app.alert_system import EmailAlertSystem
from config import DUPLICATE_TIME_LIMIT

email_system = EmailAlertSystem()
last_seen = {}

def mark_attendance(name):

    now = time.time()

    # ✅ cooldown protection
    if name in last_seen:
        if now - last_seen[name] < DUPLICATE_TIME_LIMIT:
            print(f"⚠️ Cooldown skipped: {name}")
            return

    last_seen[name] = now

    dt = datetime.now()
    date = dt.strftime("%Y-%m-%d")
    time_str = dt.strftime("%H:%M:%S")

    print(f"✅ Marking attendance: {name}")

    success = insert_attendance(name, time_str, date)

    # 🔥 EMAIL ONLY IF SUCCESS
    if success:
        try:
            email_system.attendance_alert(name)
            print("📧 Email sent")
        except Exception as e:
            print("❌ Email error:", e)
    else:
        print("⚠️ Not inserted (duplicate or DB issue)")