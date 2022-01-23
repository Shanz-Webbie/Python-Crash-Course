import unittest
from survey import AnonymousSurvey

class TestAnanymousSurvey(unittest.TestCase):
	"""Tests for the class AnonymousServey"""

	def setUp(self):
		"""
		Create a survey and a set of responses for use in all test methods.
		"""
		question = "What language did you first learn to speak?"
		self.my_survey = AnonymousSurvey(question)
		self.responses = ['English', 'Spanish', 'Mandarin']

	def test_store_single_response(self):
		"""Test that a single reponse is stored properly."""
		self.my_survey.store_response(self.responses[0])

	def test_store_three_responses(self):
		"""Test that the three individual responses are stored properly."""
		for response in self.responses:
			self.my_survey.store_response(response)
		for response in self.responses:
			self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
	unittest.main()