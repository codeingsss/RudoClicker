import sys
from threading import Thread

from PyQt6.QtWidgets import (
    QWidget, QApplication, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel
)
from PyQt6.QtCore import Qt
from PyQt6.uic import loadUi

from clicker import rudo


# ---------------- 타이틀 바 ----------------
class TitleBar(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setFixedHeight(36)

        title = QLabel("Rudo Clicker 2.0")
        title.setStyleSheet("color: white; font-weight: 600;")

        btn_close = QPushButton("✕")
        btn_close.setFixedSize(36, 24)
        btn_close.clicked.connect(parent.close)
        btn_close.setStyleSheet("""
            QPushButton {
                border: none;
                color: white;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #e74c3c;
            }
        """)

        layout = QHBoxLayout(self)
        layout.addWidget(title)
        layout.addStretch()
        layout.addWidget(btn_close)
        layout.setContentsMargins(12, 6, 12, 6)

        self.setStyleSheet("background-color: transparent;")

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.parent.drag_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton and self.parent.drag_pos:
            self.parent.move(
                self.parent.pos()
                + event.globalPosition().toPoint()
                - self.parent.drag_pos
            )
            self.parent.drag_pos = event.globalPosition().toPoint()


# ---------------- 메인 윈도우 ----------------
class Win(QWidget):
    def __init__(self):
        super().__init__()

        # 창 설정
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # 클릭러
        self.clicker = rudo()
        self.click_thread = None

        # 메인 컨테이너
        self.container = QWidget(self)
        self.container.setStyleSheet("""
            QWidget {
                background-color: #1f1f1f;
                border-radius: 16px;
            }
        """)

        # 타이틀 바
        self.title_bar = TitleBar(self)

        # UI 로드
        self.ui = QWidget()
        loadUi("ui/form.ui", self.ui)

        # 버튼 연결
        self.ui.start.clicked.connect(self.fstart)
        self.ui.stop.clicked.connect(self.fstop)
        self.ui.enter.clicked.connect(self.fenter)

        # 레이아웃
        container_layout = QVBoxLayout(self.container)
        container_layout.addWidget(self.title_bar)
        container_layout.addWidget(self.ui)
        container_layout.setContentsMargins(0, 0, 0, 0)
        container_layout.setSpacing(0)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.container)
        main_layout.setContentsMargins(12, 12, 12, 12)

        self.resize(500, 300)
        self.drag_pos = None

    # -------- 버튼 기능 --------
    def fstart(self):
        if self.click_thread and self.click_thread.is_alive():
            return

        try:
            cps = int(self.ui.cps.text())
            self.clicker.setCps(cps)
        except Exception as e:
            print("CPS 오류:", e)
            return

        self.click_thread = Thread(
            target=self.clicker.start,
            daemon=True
        )
        self.click_thread.start()

        print("START")

    def fstop(self):
        self.clicker.stop()
        print("STOP")

    def fenter(self):
        try:
            cps = int(self.ui.cps.text())
            self.clicker.setCps(cps)
            print(f"ENTER: CPS = {cps}")
        except Exception as e:
            print("CPS 오류:", e)


# ---------------- 실행 ----------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Win()
    window.show()
    sys.exit(app.exec())
