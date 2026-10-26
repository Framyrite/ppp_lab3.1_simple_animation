
"""Тесты модели отдельной частицы."""

import unittest

from src.models.particle import Particle


class TestParticle(unittest.TestCase):
    """Проверяет движение и жизненный цикл частицы."""

    def setUp(self):
        """Создаёт тестовую частицу."""
        self.particle = Particle(
            x=100,
            y=200,
            vx=10,
            vy=-20,
            radius=5,
            lifetime=2,
            max_lifetime=2,
        )

    def test_initial_state(self):
        """Проверяет начальное состояние."""
        self.assertTrue(self.particle.is_alive)
        self.assertEqual(self.particle.alpha, 255)

    def test_movement(self):
        """Проверяет перемещение за половину секунды."""
        self.particle.update(0.5)

        self.assertAlmostEqual(self.particle.x, 105)
        self.assertAlmostEqual(self.particle.y, 190)

    def test_fading(self):
        """Проверяет уменьшение прозрачности."""
        self.particle.update(1.0)

        self.assertEqual(self.particle.alpha, 128)

    def test_particle_expiration(self):
        """Проверяет завершение жизни частицы."""
        self.particle.update(3.0)

        self.assertFalse(self.particle.is_alive)
        self.assertEqual(self.particle.alpha, 0)

    def test_random_creation(self):
        """Проверяет создание случайной частицы."""
        particle = Particle.create(150, 250)

        self.assertEqual(particle.x, 150)
        self.assertEqual(particle.y, 250)
        self.assertGreater(particle.radius, 0)
        self.assertTrue(particle.is_alive)


if __name__ == "__main__":
    unittest.main()
