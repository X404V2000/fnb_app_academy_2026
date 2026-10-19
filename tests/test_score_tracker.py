import unittest

from helpers import load_module

tracker = load_module("unit_5/score_tracker.py")


class ScoreTrackerTests(unittest.TestCase):
	def setUp(self):
		tracker.player = {"best": 0, "rounds": 0}
		tracker.computer = {"best": 0, "rounds": 0}

	def test_score_message(self):
		self.assertEqual(tracker.score_message(101), "Wow! That's a new high score!")
		self.assertEqual(tracker.score_message(100), "Good try, keep playing!")

	def test_add_score_tracks_best_not_sum(self):
		tracker.add_score(tracker.player, tracker.computer, "40", "60")
		tracker.add_score(tracker.player, tracker.computer, "30", "20")
		self.assertEqual(tracker.player["best"], 60)
		self.assertEqual(tracker.computer["best"], 40)
		self.assertEqual(tracker.player["rounds"], 2)

	def test_invalid_input_does_not_count_a_round(self):
		self.assertFalse(tracker.add_score(tracker.player, tracker.computer, "abc", "10"))
		self.assertFalse(tracker.add_score(tracker.player, tracker.computer, "-5", "10"))
		self.assertEqual(tracker.player["rounds"], 0)
		self.assertEqual(tracker.computer["rounds"], 0)


if __name__ == "__main__":
	unittest.main()
