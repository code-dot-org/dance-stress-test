import unittest
from DancePage import DancePage
from DanceXmlBuilder import set_background, set_foreground, heavy, heaviest


class DanceStressTest(unittest.TestCase):

    def setUp(self):
        self.page = DancePage()
        self.page.setup()
        self.background_test_runs = 4
        self.background_test_duration = 15

    def tearDown(self):
        self.page.teardown()

    # Basic scripted dance
    # very common - every student will make some variant of this
    # 4 sprites each with different character
    # All sprites may be doing different dances
    def testCase1(self):
        self.page.run_fixture('case1.xml', repeat_runs=4)
        self.assertTrue(self.page.is_not_running())

    # "Try every character" basic scripted dance
    # common - multiple students in a class would make a variant like this
    # 11 sprites each with different character
    # All sprites may be doing different dances
    def testCase2(self):
        self.page.run_fixture('case2.xml', repeat_runs=4)
        self.assertTrue(self.page.is_not_running())

    # Main dancer w/ lots of backup dancers (common - multiple students in a class would make a variant like this)
    # 20 sprites char 1
    # 1 sprite char 2
    # All Char 1 sprites always doing same dance move
    def testCase3(self):
        self.page.run_fixture('case3.xml', repeat_runs=4)
        self.assertTrue(self.page.is_not_running())

    # Complex main dancer w/ backup dancers
    # less common - one student in a class is likely to make a variant like this
    # 20 sprites char 1 (ex: outer circle, border)
    # 10 sprites char 2 (ex: inner circle)
    # All char 1 sprites doing same dance
    # All char 2 sprites doing same dance
    def testCase4(self):
        self.page.run_fixture('case4.xml', repeat_runs=4)
        self.assertTrue(self.page.is_not_running())

    # Many dancers (> 30 and <50) all doing same moves (less common)
    # Sprites of different characters
    # All sprites with a group doing same moves
    # Example: 40 ducks, all moving together; 10 dogs all moving together
    # This is less common because the N dropdown in the "make N ducks" block is limited,
    # so students would have to write more complex code
    def testCase5(self):
        self.page.run_fixture('case5.xml', repeat_runs=4)
        self.assertTrue(self.page.is_not_running())

    # Many dancers (> 30 and < 50) all doing different moves (very rare)
    # Sprites of different characters
    # All sprites doing different moves
    # This is very rare because the code required to make 30-50 sprites all do different
    # things is very long and complex.
    def testCase6(self):
        self.page.run_fixture('case6.xml', repeat_runs=4)
        self.assertTrue(self.page.is_not_running())

    # Many dancers (> 50) all doing different  moves (very rare)
    # Sprites of different characters
    # All sprites doing different moves
    # This is very rare because the code required to make 30-50 sprites all do different
    # things is very long and complex.
    def testCase7(self):
        self.page.run_fixture('case7.xml', repeat_runs=4)
        self.assertTrue(self.page.is_not_running())

    # JoshC reported this dance crashes his phone browser about 6 beats in
    # https://studio.code.org/projects/dance/-9BgFCKwWnZfmNfYbu6XFHIT7cOfRBZPhWz2p3w4k1E
    # iPhone 6 / iOS 12.1
    def testStealthCat(self):
        self.page.run_fixture('stealthCat.xml', run_duration=30)
        self.assertTrue(self.page.is_not_running())

    # Test cycling through many backgrounds and foregrounds to see if they
    # have memory leaks
    def testBackgrouds(self):
        self.page.run_fixture('backgrounds.xml', run_duration=30)
        self.assertTrue(self.page.is_not_running())

    # This next block tests all backgrounds and foregrounds individually
    # in an effort to isolate performance problems to the particular effects
    # causing them.

    def testBackgroundColorCycle(self):
        self.page.run_program(set_background('color_cycle'), 'color_cycle', run_duration=self.background_test_duration, repeat_runs=self.background_test_runs)
        self.assertTrue(self.page.is_not_running())

    def testBackgroundColorLights(self):
        self.page.run_program(set_background('color_lights'), 'color_lights', run_duration=self.background_test_duration, repeat_runs=self.background_test_runs)
        self.assertTrue(self.page.is_not_running())

    def testBackgroundDisco(self):
        self.page.run_program(set_background('disco'), 'disco', run_duration=self.background_test_duration, repeat_runs=self.background_test_runs)
        self.assertTrue(self.page.is_not_running())

    def testBackgroundKaleidoscope(self):
        self.page.run_program(set_background('kaleidoscope'), 'kaleidoscope', run_duration=self.background_test_duration, repeat_runs=self.background_test_runs)
        self.assertTrue(self.page.is_not_running())

    def testBackgroundRainbow(self):
        self.page.run_program(set_background('rainbow'), 'rainbow', run_duration=self.background_test_duration, repeat_runs=self.background_test_runs)
        self.assertTrue(self.page.is_not_running())

    def testBackgroundDiamonds(self):
        self.page.run_program(set_background('diamonds'), 'diamonds', run_duration=self.background_test_duration, repeat_runs=self.background_test_runs)
        self.assertTrue(self.page.is_not_running())

    def testBackgroundSparkles(self):
        self.page.run_program(set_background('sparkles'), 'sparkles', run_duration=self.background_test_duration, repeat_runs=self.background_test_runs)
        self.assertTrue(self.page.is_not_running())

    def testBackgroundSplatter(self):
        self.page.run_program(set_background('splatter'), 'splatter', run_duration=self.background_test_duration, repeat_runs=self.background_test_runs)
        self.assertTrue(self.page.is_not_running())

    def testBackgroundSwirl(self):
        self.page.run_program(set_background('swirl'), 'swirl', run_duration=self.background_test_duration, repeat_runs=self.background_test_runs)
        self.assertTrue(self.page.is_not_running())

    def testBackgroundSnowflakes(self):
        self.page.run_program(set_background('snowflakes'), 'snowflakes', run_duration=self.background_test_duration, repeat_runs=self.background_test_runs)
        self.assertTrue(self.page.is_not_running())

    def testBackgroundSpiral(self):
        self.page.run_program(set_background('spiral'), 'spiral', run_duration=self.background_test_duration, repeat_runs=self.background_test_runs)
        self.assertTrue(self.page.is_not_running())

    def testBackgroundStars(self):
        self.page.run_program(set_background('stars'), 'stars', run_duration=self.background_test_duration, repeat_runs=self.background_test_runs)
        self.assertTrue(self.page.is_not_running())

    def testBackgroundStarspace(self):
        self.page.run_program(set_background('starspace'), 'starspace', run_duration=self.background_test_duration, repeat_runs=self.background_test_runs)
        self.assertTrue(self.page.is_not_running())

    def testBackgroundStrobeLights(self):
        self.page.run_program(set_background('strobe_lights'), 'strobe_lights', run_duration=self.background_test_duration, repeat_runs=self.background_test_runs)
        self.assertTrue(self.page.is_not_running())

    def testBackgroundText(self):
        self.page.run_program(set_background('text'), 'text', run_duration=self.background_test_duration, repeat_runs=self.background_test_runs)
        self.assertTrue(self.page.is_not_running())

    # Foreground tests

    def testForegroundBubbles(self):
        self.page.run_program(set_foreground('bubbles'), 'bubbles',
                              run_duration=self.background_test_duration, repeat_runs=self.background_test_runs)
        self.assertTrue(self.page.is_not_running())

    def testForegroundConfetti(self):
        self.page.run_program(set_foreground('confetti'), 'confetti',
                              run_duration=self.background_test_duration, repeat_runs=self.background_test_runs)
        self.assertTrue(self.page.is_not_running())

    def testForegroundFallingPoop(self):
        self.page.run_program(set_foreground('falling_poop'), 'falling_poop',
                              run_duration=self.background_test_duration, repeat_runs=self.background_test_runs)
        self.assertTrue(self.page.is_not_running())

    def testForegroundFallingRainbows(self):
        self.page.run_program(set_foreground('falling_rainbows'), 'falling_rainbows',
                              run_duration=self.background_test_duration, repeat_runs=self.background_test_runs)
        self.assertTrue(self.page.is_not_running())

    def testForegroundHearts(self):
        self.page.run_program(set_foreground('hearts'), 'hearts',
                              run_duration=self.background_test_duration, repeat_runs=self.background_test_runs)
        self.assertTrue(self.page.is_not_running())

    def testForegroundMusicNotes(self):
        self.page.run_program(set_foreground('music_notes'), 'music_notes',
                              run_duration=self.background_test_duration, repeat_runs=self.background_test_runs)
        self.assertTrue(self.page.is_not_running())

    def testForegroundPineapples(self):
        self.page.run_program(set_foreground('pineapples'), 'pineapples',
                              run_duration=self.background_test_duration, repeat_runs=self.background_test_runs)
        self.assertTrue(self.page.is_not_running())

    def testForegroundPizzas(self):
        self.page.run_program(set_foreground('pizzas'), 'pizzas',
                              run_duration=self.background_test_duration, repeat_runs=self.background_test_runs)
        self.assertTrue(self.page.is_not_running())

    def testForegroundRain(self):
        self.page.run_program(set_foreground('rain'), 'rain', run_duration=self.background_test_duration, repeat_runs=self.background_test_runs)
        self.assertTrue(self.page.is_not_running())

    def testForegroundRainingTacos(self):
        self.page.run_program(set_foreground('raining_tacos'), 'raining_tacos', run_duration=self.background_test_duration, repeat_runs=self.background_test_runs)
        self.assertTrue(self.page.is_not_running())

    def testForegroundSnowflakes(self):
        self.page.run_program(set_foreground('snowflakes'), 'snowflakes', run_duration=self.background_test_duration, repeat_runs=self.background_test_runs)
        self.assertTrue(self.page.is_not_running())

    def testForegroundSpotlight(self):
        self.page.run_program(set_foreground('spotlight'), 'spotlight', run_duration=self.background_test_duration, repeat_runs=self.background_test_runs)
        self.assertTrue(self.page.is_not_running())

    # Very heavy case hitting all background and foreground effects
    # and all animations for one character
    # def testHeavy(self):
    #     self.page.run_program(heavy(), 'heavy', run_duration=15)
    #     self.assertTrue(self.page.is_not_running())

    # Almost the heaviest possible case
    # Hits all background and foreground effects
    # Loads and plays every animation for every character at once
    # Constantly relayouts sprites
    # To add: Burst moves
    # def testHeaviest(self):
    #     self.page.run_program(heaviest(), 'heaviest', run_duration=45)
    #     self.assertTrue(self.page.is_not_running())


# Start of script
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DanceStressTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
