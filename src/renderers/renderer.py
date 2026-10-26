
"""Отрисовка системы частиц с поддержкой прозрачности."""

import tkinter as tk

from PIL import Image, ImageDraw, ImageTk


class ParticleRenderer:
    """Отображает полупрозрачные частицы на Canvas."""

    def __init__(self, canvas: tk.Canvas, width: int, height: int):
        """Инициализирует графический renderer."""
        self.canvas = canvas
        self.width = width
        self.height = height

        self.background_color = (10, 13, 22)

        self.image_id = self.canvas.create_image(
            0,
            0,
            anchor=tk.NW,
        )

        self.photo = None

    def render(self, systems):
        """Отрисовывает все активные системы частиц."""
        image = Image.new(
            "RGB",
            (self.width, self.height),
            self.background_color,
        )

        draw = ImageDraw.Draw(image, "RGBA")

        for system in systems:
            for particle in system.particles:
                if not particle.is_alive:
                    continue

                x = particle.x
                y = particle.y
                r = particle.radius

                draw.ellipse(
                    (x - r, y - r, x + r, y + r),
                    fill=(235, 240, 255, particle.alpha),
                )

        self.photo = ImageTk.PhotoImage(image=image)

        self.canvas.itemconfigure(
            self.image_id,
            image=self.photo,
        )
