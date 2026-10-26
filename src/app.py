
"""Графическое приложение для анимации системы частиц."""

import time
import tkinter as tk

from src.models.particle_system import ParticleSystem
from src.renderers.renderer import ParticleRenderer


class App:
    """Управляет окном, источниками частиц и анимацией."""

    def __init__(self):
        """Создаёт графическое окно и компоненты приложения."""
        self.width = 800
        self.height = 600

        self.root = tk.Tk()
        self.root.title("Лабораторная 3.1 — Система частиц")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(
            self.root,
            width=self.width,
            height=self.height,
            bg="#0a0d16",
            highlightthickness=0,
        )
        self.canvas.pack()

        self.renderer = ParticleRenderer(
            self.canvas,
            self.width,
            self.height,
        )

        # Постоянный источник в нижней части окна
        self.systems = [
            ParticleSystem(
                x=400,
                y=540,
                emission_rate=80,
                max_particles=220,
            )
        ]

        # Создаём новые источники кликом мыши
        self.canvas.bind("<Button-1>", self.add_source)

        self.previous_time = time.perf_counter()

    def add_source(self, event):
        """Добавляет источник частиц в точке нажатия мыши."""
        system = ParticleSystem(
            x=event.x,
            y=event.y,
            emission_rate=120,
            emission_duration=1.5,
            max_particles=200,
        )

        self.systems.append(system)

    def animate(self):
        """Обновляет модель и перерисовывает частицы."""
        current_time = time.perf_counter()

        dt = current_time - self.previous_time
        self.previous_time = current_time

        # Защита от больших скачков времени
        dt = min(dt, 0.05)

        for system in self.systems:
            system.update(dt)

        # Удаляем завершённые временные системы
        self.systems = [
            system
            for system in self.systems
            if system.is_alive
        ]

        self.renderer.render(self.systems)

        # Следующее обновление примерно через 33 мс
        self.root.after(33, self.animate)

    def run(self):
        """Запускает анимацию и главный цикл tkinter."""
        self.animate()
        self.root.mainloop()
