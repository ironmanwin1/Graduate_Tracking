import flet as ft
import httpx

class ProfileView(ft.View):
    def __init__(self, page: ft.Page):
        # ตั้ง route เป็น "/profile" เหมือนเดิม
        super().__init__("/profile")
        self.page = page

        # เรียกใช้ฟังก์ชันโหลดข้อมูล
        student = self.get_logged_in_student()

        # ปุ่มกลับหน้า Home
        back_button = ft.IconButton(
            icon=ft.icons.ARROW_BACK,
            tooltip="กลับไปหน้า Home",
            on_click=lambda e: page.go("/home")
        )

        header = ft.Row(
            controls=[
                back_button,
                ft.Text("หน้าข้อมูลส่วนตัว (ProfileView)", size=24, weight="bold")
            ],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        )

        if not student:
            # ถ้าไม่เจอนักศึกษาหรือไม่มี student_id
            self.controls = [
                header,
                ft.Divider(),
                ft.Text("ไม่พบนักศึกษา", size=20, color="red")
            ]
        else:
            # สร้าง UI จากข้อมูลนักศึกษา
            left_column = ft.Column([
                ft.CircleAvatar(
                    foreground_image_src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
                    radius=60
                ),
                ft.Text(f"{student.get('prefix', '')} {student.get('name', '')}", weight="bold"),
                ft.Text(f"รหัสนักศึกษา: {student.get('student_id', '')}"),
                ft.Text(f"เบอร์โทรศัพท์: {student.get('phone', '')}"),
                ft.Text(f"อีเมล: {student.get('email', '')}"),
                ft.Text("ลายเซ็นออนไลน์:", weight="bold", top=10),
                ft.Image(src=student.get('signature_url', ''), width=200, height=60)
            ], spacing=10)

            right_column = ft.Column([
                ft.Text("ข้อมูลการศึกษา", weight="bold", size=16),
                ft.Text(f"ระดับปริญญา: {student.get('degree_level', '')}"),
                ft.Text(f"หลักสูตร: {student.get('program', '')}"),
                ft.Text(f"แผนการเรียน: {student.get('study_plan', '')}"),
                ft.Divider(),
                ft.Text("ข้อมูลวิทยานิพนธ์", weight="bold", size=16),
                ft.Text(f"ชื่อเรื่อง: {student.get('thesis', {}).get('title', '')}"),
                ft.Text(f"อาจารย์ที่ปรึกษาหลัก: {student.get('thesis', {}).get('advisor', '')}"),
                ft.Text(f"อาจารย์ที่ปรึกษาร่วม: {student.get('thesis', {}).get('co_advisor', '')}"),
                ft.Text(
                    f"สอบหัวข้อ: {student.get('thesis', {}).get('proposal_exam', {}).get('status', '')}"
                    f" (วันที่: {student.get('thesis', {}).get('proposal_exam', {}).get('date', '-')})"
                ),
                ft.Text(
                    f"สอบสุดท้าย: {student.get('thesis', {}).get('final_exam', {}).get('status', '')}"
                ),
                ft.Divider(),
                ft.Text("คะแนนสอบภาษาอังกฤษ", weight="bold", size=16),
                ft.Text(
                    f"{student.get('english_test', {}).get('type', '')}"
                    f" คะแนน {student.get('english_test', {}).get('score', '')}"
                )
            ], spacing=8)

            layout = ft.Row(
                controls=[
                    ft.Container(left_column, expand=1, padding=20),
                    ft.Container(right_column, expand=2, padding=20),
                ],
                spacing=20,
                scroll="AUTO"
            )

            self.controls = [
                header,
                ft.Divider(),
                layout
            ]

    def get_logged_in_student(self):
        # ฟังก์ชันโหลดข้อมูลจาก FastAPI
        # ดึง student_id จาก client_storage
        student_id = self.page.client_storage.get("student_id")
        print("📦 student_id from storage:", student_id)

        if not student_id:
            return None

        try:
            res = httpx.get(f"http://127.0.0.1:8000/api/student/{student_id}")
            print("📡 API Status:", res.status_code)
            print("📡 API Response:", res.json())
            if res.status_code == 200 and "student_id" in res.json():
                return res.json()
        except Exception as e:
            print("❌ Error connecting to API:", e)

        return None
