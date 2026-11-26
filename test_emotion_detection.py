from EmotionDetection.emotion_detector import emotion_analyzer
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_emotion_analyzer(self):
        res1 = emotion_analyzer('I love working with Python')
        self.assertEqual(res1['dominant_emotion'], 'joy')
        res2 = emotion_analyzer('I am so sad that she leaves me')
        self.assertEqual(res2['dominant_emotion'], 'sadness')
        res3 = emotion_analyzer('I am scared of losing this job')
        self.assertEqual(res3['dominant_emotion'], 'fear')

unittest.main()