
"""Модель отдельной частицы с ограниченным временем жизни."""

import random
from dataclasses import dataclass


@dataclass
class Particle:
    """Частица с координатами, скоростью и прозрачностью."""

    x: float
    y: float
    vx: float
    vy: float
    radius: float
    lifetime: float
    max_lifetime: float

    @classmethod
    def create(cls, x: float, y: float) -> "Particle":
        """Создаёт частицу со случайными параметрами."""
        lifetime = random.uniform(1.5, 3.0)

        return cls(
            x=x,
            y=y,
            vx=random.uniform(-35, 35),
            vy=random.uniform(-110, -45),
            radius=random.uniform(3, 9),
            lifetime=lifetime,
            max_lifetime=lifetime,
        )

    def update(self, dt: float) -> None:
        """Обновляет положение и оставшееся время жизни."""
        if not self.is_alive or dt <= 0:
            return

        movement_time = min(dt, self.lifetime)

        self.x += self.vx * movement_time
        self.y += self.vy * movement_time

        self.lifetime = max(0.0, self.lifetime - dt)

    @property
    def is_alive(self) -> bool:
        """Проверяет, жива ли частица."""
        return self.lifetime > 0

    @property
    def alpha(self) -> int:
        """Вычисляет прозрачность от 255 до 0."""
        if self.max_lifetime <= 0:
            return 0

        return round(
            255 * self.lifetime / self.max_lifetime
        )
