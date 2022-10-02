import unittest
from .StopTimer import StopTimer

class StopTimerTest(unittest.TestCase):
    def test_iteration_should_not_be_done_if_nothing_is_done(self):
        item = StopTimer()
        self.assertRaises(Exception, item.is_done)

    def test_iteration_stop(self):
        item = StopTimer()
        for _ in range(100):
            item.tick()
        assert item.is_done()

    def test_time_iteration_stop(self):
        item = StopTimer(
            timeout_seconds=0
        )
        item.tick()
        assert item.is_done()

if __name__ == '__main__':
    unittest.main()
