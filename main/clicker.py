import pyautogui as pg
import time

pg.PAUSE = 0


class rudo:
    def __init__(self):
        self.cps = 1
        self.running = False

    def setCps(self, c):
        if c <= 0:
            raise ValueError("CPS는 1 이상")
        self.cps = c

    def start(self):
        if self.running:
            return

        self.running = True
        interval = 1 / self.cps

        while self.running:
            start = time.perf_counter()
            pg.click()
            elapsed = time.perf_counter() - start

            sleep_time = interval - elapsed
            if sleep_time > 0:
                time.sleep(sleep_time)

    def stop(self):
        self.running = False
