
"""Управление генерацией и жизненным циклом частиц."""

from src.models.particle import Particle


class ParticleSystem:
    """Источник частиц в заданной точке экрана."""

    def __init__(
        self,
        x,
        y,
        emission_rate=60,
        emission_duration=None,
        max_particles=200,
    ):
        """Инициализирует источник частиц."""
        self.x = x
        self.y = y

        # Количество создаваемых частиц в секунду
        self.emission_rate = emission_rate

        # Максимальное количество частиц
        self.max_particles = max_particles

        # None означает постоянный источник
        self.remaining_emission = emission_duration

        self.particles = []
        self.spawn_remainder = 0.0

    @property
    def emitting(self):
        """Проверяет, продолжает ли источник создавать частицы."""
        return (
            self.remaining_emission is None
            or self.remaining_emission > 0
        )

    @property
    def is_alive(self):
        """Проверяет активность системы частиц."""
        return self.emitting or bool(self.particles)

    def update(self, dt):
        """Обновляет частицы и генерирует новые."""
        if dt <= 0:
            return

        # Обновляем существующие частицы
        for particle in self.particles:
            particle.update(dt)

        # Удаляем частицы с истекшим временем жизни
        self.particles = [
            particle
            for particle in self.particles
            if particle.is_alive
        ]

        if not self.emitting:
            return

        # Сколько времени источник работал в этом кадре
        emission_time = dt

        if self.remaining_emission is not None:
            emission_time = min(
                dt,
                self.remaining_emission
            )

            self.remaining_emission = max(
                0.0,
                self.remaining_emission - dt
            )

        # Рассчитываем число новых частиц
        self.spawn_remainder += (
            self.emission_rate * emission_time
        )

        count = int(self.spawn_remainder)
        self.spawn_remainder -= count

        available = max(
            0,
            self.max_particles - len(self.particles)
        )

        # Создаём новые частицы
        for _ in range(min(count, available)):
            particle = Particle.create(self.x, self.y)
            self.particles.append(particle)
