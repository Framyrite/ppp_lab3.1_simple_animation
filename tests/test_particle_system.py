
"""Тесты генерации и управления системой частиц."""

import unittest

from src.models.particle_system import ParticleSystem


class TestParticleSystem(unittest.TestCase):
    """Проверяет работу источников частиц."""

    def test_particle_generation(self):
        """Проверяет генерацию частиц за одну секунду."""
        system = ParticleSystem(
            x=300,
            y=500,
            emission_rate=60,
        )

        system.update(1.0)

        self.assertEqual(len(system.particles), 60)

    def test_particle_limit(self):
        """Проверяет ограничение количества частиц."""
        system = ParticleSystem(
            x=300,
            y=500,
            emission_rate=100,
            max_particles=20,
        )

        system.update(1.0)

        self.assertEqual(len(system.particles), 20)

    def test_particle_coordinates(self):
        """Проверяет создание частиц в заданной точке."""
        system = ParticleSystem(
            x=150,
            y=250,
            emission_rate=10,
        )

        system.update(0.1)

        self.assertEqual(len(system.particles), 1)
        self.assertEqual(system.particles[0].x, 150)
        self.assertEqual(system.particles[0].y, 250)

    def test_temporary_source(self):
        """Проверяет остановку временного источника."""
        system = ParticleSystem(
            x=300,
            y=500,
            emission_rate=10,
            emission_duration=0.1,
        )

        system.update(0.1)

        self.assertFalse(system.emitting)
        self.assertEqual(len(system.particles), 1)

        system.update(5.0)

        self.assertEqual(len(system.particles), 0)
        self.assertFalse(system.is_alive)

    def test_zero_delta_time(self):
        """Проверяет отсутствие генерации при нулевом dt."""
        system = ParticleSystem(300, 500)

        system.update(0)

        self.assertEqual(len(system.particles), 0)


if __name__ == "__main__":
    unittest.main()
