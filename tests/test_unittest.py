import unittest
from DancePage import DancePage
from DanceXmlBuilder import heavy, heaviest


class DanceStressTest(unittest.TestCase):

    def setUp(self):
        self.page = DancePage()
        self.page.setup()

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

    # So many background changes in this one discovered in the wild,
    # so it seemed like a good candidate for stress testing.
    # https://studio.code.org/projects/dance/o26gc1LPkpQ9yYL1Z3UQi_vDsnqO3RqozM3jr6zswp0
    def testSoFastClappign(self):
        self.page.run_fixture('soFastClapping.xml', run_duration=30)
        self.assertTrue(self.page.is_not_running())

    # Test cycling through many backgrounds and foregrounds to see if they
    # have memory leaks
    def testBackgrouds(self):
        self.page.run_fixture('backgrounds.xml', run_duration=30)
        self.assertTrue(self.page.is_not_running())

    # This next block tests all backgrounds and foregrounds individually
    # in an effort to isolate performance problems to the particular effects
    # causing them.

    def testEffect_bubbles(self):
        self.page.test_foreground('bubbles')

    def testEffect_circles(self):
        self.page.test_background('circles')

    def testEffect_color_cycle(self):
        self.page.test_background('color_cycle')

    def testEffect_color_lights(self):
        self.page.test_foreground('color_lights')

    def testEffect_confetti(self):
        self.page.test_foreground('confetti')

    def testEffect_diamonds(self):
        self.page.test_background('diamonds')

    def testEffect_disco(self):
        self.page.test_background('disco')

    def testEffect_disco_ball(self):
        self.page.test_background('disco_ball')

    def testEffect_emojis(self):
        self.page.test_foreground('emojis')

    def testEffect_exploding_stars(self):
        self.page.test_foreground('exploding_stars')

    def testEffect_fireworks(self):
        self.page.test_background('fireworks')

    def testEffect_floating_rainbows(self):
        self.page.test_foreground('floating_rainbows')

    def testEffect_flowers(self):
        self.page.test_background('flowers')

    def testEffect_galaxy(self):
        self.page.test_background('galaxy')

    def testEffect_growing_stars(self):
        self.page.test_background('growing_stars')

    def testEffect_hearts_colorful(self):
        self.page.test_foreground('hearts_colorful')

    def testEffect_hearts_red(self):
        self.page.test_foreground('hearts_red')

    def testEffect_kaleidoscope(self):
        self.page.test_background('kaleidoscope')

    def testEffect_lasers(self):
        self.page.test_background('lasers')

    def testEffect_music_notes(self):
        self.page.test_foreground('music_notes')

    def testEffect_pineapples(self):
        self.page.test_foreground('pineapples')

    def testEffect_pizzas(self):
        self.page.test_foreground('pizzas')

    def testEffect_quads(self):
        self.page.test_background('quads')

    def testEffect_rain(self):
        self.page.test_foreground('rain')

    def testEffectRainbow(self):
        self.page.test_background('rainbow')

    def testEffect_raining_tacos(self):
        self.page.test_foreground('raining_tacos')

    def testEffect_ripples(self):
        self.page.test_background('ripples')

    def testEffect_ripples_random(self):
        self.page.test_background('ripples_random')

    def testEffect_snowflakes(self):
        self.page.test_background('snowflakes')

    def testEffect_smile_face(self):
        self.page.test_foreground('smile_face')

    def testEffect_smiling_poop(self):
        self.page.test_foreground('smiling_poop')

    def testEffect_sparkles(self):
        self.page.test_background('sparkles')

    def testEffect_spiral(self):
        self.page.test_background('spiral')

    def testEffect_splatter(self):
        self.page.test_background('splatter')

    def testEffect_spotlight(self):
        self.page.test_foreground('spotlight')

    def testEffect_squiggles(self):
        self.page.test_background('squiggles')

    def testEffect_stars(self):
        self.page.test_background('stars')

    def testEffect_swirl(self):
        self.page.test_background('swirl')

    def testEffect_text(self):
        self.page.test_background('text')


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
