import mysql.connector
from config import DB_CONFIG


def get_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        print("🟢 Connected DB")
        return conn
    except Exception as e:
        print("❌ DB Connection Error:", e)
        return None


def insert_attendance(name, time_str, date):
    conn = None

    try:
        conn = get_connection()
        if conn is None:
            return False

        cursor = conn.cursor()

        print(f"🔍 Inserting: {name} {date}")

        query = """
        INSERT INTO attendance_new (name, time, date)
        VALUES (%s, %s, %s)
        """

        cursor.execute(query, (name, time_str, date))
        conn.commit()

        print("💾 INSERT SUCCESS")
        return True

    except mysql.connector.errors.IntegrityError:
        print("⚠️ Duplicate entry skipped")
        return False

    except Exception as e:
        print("❌ DB ERROR:", e)
        return False

    finally:
        if conn:
            conn.close()