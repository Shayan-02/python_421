import sqlite3

connection = sqlite3.connect("hospital.db")

cursor = connection.cursor()

cursor.execute("PRAGMA foreign_keys = ON")


cursor.execute("""
CREATE TABLE IF NOT EXISTS patient (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    national_code TEXT UNIQUE NOT NULL,
    phone TEXT
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS doctor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    medical_code TEXT UNIQUE NOT NULL,
    specialty TEXT
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS visit (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    doctor_id INTEGER NOT NULL,
    cost INTEGER NOT NULL,
    tracking_code TEXT UNIQUE NOT NULL,

    FOREIGN KEY (patient_id)
        REFERENCES patient(id),

    FOREIGN KEY (doctor_id)
        REFERENCES doctor(id)
)
""")


patients = [
    ("علی احمدی", "0012345678", "09120000001"),
    ("رضا محمدی", "0023456789", "09120000002"),
    ("مریم کریمی", "0034567890", "09120000003"),
]

cursor.executemany("""
INSERT INTO patient
(name, national_code, phone)
VALUES (?, ?, ?)
""", patients)


doctors = [
    ("دکتر محمد رضایی", "D1001", "قلب"),
    ("دکتر سارا احمدی", "D1002", "مغز و اعصاب"),
    ("دکتر علی مرادی", "D1003", "داخلی"),
]

cursor.executemany("""
INSERT OR IGNORE INTO doctor
(name, medical_code, specialty)
VALUES (?, ?, ?)
""", doctors)


connection.commit()



visits = [
    (1, 1, 500000, "V10001"),
    (2, 1, 500000, "V10002"),
    (1, 2, 700000, "V10003"),
    (3, 3, 400000, "V10004"),
]

cursor.executemany("""
INSERT OR IGNORE INTO visit
(patient_id, doctor_id, cost, tracking_code)
VALUES (?, ?, ?, ?)
""", visits)


connection.commit()

cursor.execute("""
SELECT
    p.national_code,
    p.name,
    d.medical_code,
    d.name,
    v.cost,
    v.tracking_code

FROM visit AS v

JOIN patient AS p
    ON v.patient_id = p.id

JOIN doctor AS d
    ON v.doctor_id = d.id
""", )


result = cursor.fetchall()


if result:
    patient_code = result[0]
    patient_name = result[1]
    doctor_code = result[2]
    doctor_name = result[3]
    # cost = result[4]
    # tracking_code = result[5]

    print(
        f"بیمار با کد {patient_code} توسط پزشک با کد "
        f"{doctor_code}"
    )
else:
    print("ویزیتی پیدا نشد.")


connection.close()