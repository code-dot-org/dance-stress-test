import os
import unittest
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from time import sleep

# Six dancers of each character, cycling through the repeat animations
HEAVY_LOAD = """
<xml>
 <block type="Dancelab_whenSetup" movable="false">
  <statement name="DO">
   <block type="Dancelab_makeNewDanceSpriteGroup">
    <title name="N">6</title>
    <title name="COSTUME">"ALIEN"</title>
    <title name="LAYOUT">"circle"</title>
    <next>
     <block type="Dancelab_makeNewDanceSpriteGroup">
      <title name="N">6</title>
      <title name="COSTUME">"BEAR"</title>
      <title name="LAYOUT">"circle"</title>
      <next>
       <block type="Dancelab_makeNewDanceSpriteGroup">
        <title name="N">6</title>
        <title name="COSTUME">"CAT"</title>
        <title name="LAYOUT">"circle"</title>
        <next>
         <block type="Dancelab_makeNewDanceSpriteGroup">
          <title name="N">6</title>
          <title name="COSTUME">"DOG"</title>
          <title name="LAYOUT">"circle"</title>
          <next>
           <block type="Dancelab_makeNewDanceSpriteGroup">
            <title name="N">6</title>
            <title name="COSTUME">"DUCK"</title>
            <title name="LAYOUT">"circle"</title>
            <next>
             <block type="Dancelab_makeNewDanceSpriteGroup">
              <title name="N">6</title>
              <title name="COSTUME">"FROG"</title>
              <title name="LAYOUT">"circle"</title>
              <next>
               <block type="Dancelab_makeNewDanceSpriteGroup">
                <title name="N">6</title>
                <title name="COSTUME">"MOOSE"</title>
                <title name="LAYOUT">"circle"</title>
                <next>
                 <block type="Dancelab_makeNewDanceSpriteGroup">
                  <title name="N">6</title>
                  <title name="COSTUME">"PINEAPPLE"</title>
                  <title name="LAYOUT">"circle"</title>
                  <next>
                   <block type="Dancelab_makeNewDanceSpriteGroup">
                    <title name="N">6</title>
                    <title name="COSTUME">"ROBOT"</title>
                    <title name="LAYOUT">"circle"</title>
                    <next>
                     <block type="Dancelab_makeNewDanceSpriteGroup">
                      <title name="N">6</title>
                      <title name="COSTUME">"SHARK"
                      </title>
                      <title name="LAYOUT">"circle"
                      </title>
                      <next>
                       <block type="Dancelab_makeNewDanceSpriteGroup">
                        <title name="N">6
                        </title>
                        <title name="COSTUME">
                         "UNICORN"
                        </title>
                        <title name="LAYOUT">
                         "circle"
                        </title>
                       </block>
                      </next>
                     </block>
                    </next>
                   </block>
                  </next>
                 </block>
                </next>
               </block>
              </next>
             </block>
            </next>
           </block>
          </next>
         </block>
        </next>
       </block>
      </next>
     </block>
    </next>
   </block>
  </statement>
 </block>
 <block type="Dancelab_everySeconds">
  <title name="N">1</title>
  <title name="UNIT">"measures"</title>
  <statement name="DO">
   <block type="Dancelab_setBackgroundEffect">
    <title name="EFFECT">['disco', 'color_cycle', 'rainbow', 'text',
     'diamonds','splatter','swirl','spiral'][randomInt(0,7)]
    </title>
    <next>
     <block type="Dancelab_setForegroundEffect">
      <title name="EFFECT">['spotlight', 'rain', 'raining_tacos'][randomInt(0,2)]</title>
      <next>
       <block type="Dancelab_changeMoveEachLR">
        <title name="GROUP">sprites</title>
        <title name="MOVE">"next"</title>
        <title name="DIR">-1</title>
       </block>
      </next>
     </block>
    </next>
   </block>
  </statement>
 </block>
</xml>
"""


class DanceStressTest(unittest.TestCase):

    def setUp(self):
        # desired_caps = {
        #     'platformName': 'Android',
        #     # 'platformVersion': '8.0',
        #     'avd': 'Nexus_4_API_22',
        #     'deviceName': 'Android Emulator',
        #     'browserName': 'Browser',
        #     'automationName': 'UiAutomator2'
        # }
        # self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', {})
        self.driver.orientation = "LANDSCAPE"
        self.screenshot_folder = os.getenv('SCREENSHOT_PATH', '/tmp')

    def tearDown(self):
        self.driver.quit()

    def testStress(self):
        # Load dance party free-play level
        self.driver.get('https://test-studio.code.org/s/dance/stage/1/puzzle/13')

        # Enter age and dismiss dialog, which causes a page reload
        self.bypassAgeDialog()

        # Wait for the page to load again
        self.waitToSee('runButton')

        self.screenshot('loaded')

        # svgFlyoutGroup
        # Then I open the topmost blockly category "Brushes"
        #   And I drag block matching selector "#draw-color" to block matching selector "#when_run"
        self.setBlocks(HEAVY_LOAD)
        self.screenshot('blocks_loaded')

        # Run basic dance party for 30 seconds
        self.clickRun()
        sleep(30)
        self.clickReset()
        sleep(1)
        self.assertTrue(self.isNotRunning())

        self.screenshot('test_over')

        # TODO: Play short burst dances
        # TODO: Run/reset several times to catch memory leaks
        # TODO: Force out-of-memory to see what happens

    def bypassAgeDialog(self):
        self.waitToSee('uitest-age-selector')
        selector = Select(self.driver.find_element_by_id('uitest-age-selector'))
        selector.select_by_visible_text('10')
        submit = self.driver.find_element_by_id('uitest-submit-age')
        submit.click()
        sleep(3)  # Enough time for reload to start

    def setBlocks(self, block_xml):
        self.driver.execute_script("""
            var blocksXml = arguments[0];
            Blockly.mainBlockSpace.clear();
            var arrangedBlocksXml = __TestInterface.arrangeBlockPosition(blocksXml, {});
            __TestInterface.loadBlocks(arrangedBlocksXml);
        """, block_xml)

    def clickRun(self):
        el = self.driver.find_element_by_id('runButton')
        el.click()

    def clickReset(self):
        el = self.driver.find_element_by_id('resetButton')
        el.click()

    def isNotRunning(self):
        el = self.driver.find_element_by_id('runButton')
        return el.is_displayed() and el.is_enabled()

    def waitToSee(self, element_id):
        element = None
        attempt_count = 0
        while element is None:
            try:
                attempt_count += 1
                element = self.driver.find_element_by_id(element_id)
            except NoSuchElementException:
                if attempt_count > 30:
                    print('Could not locate element #{} in 30 attempts'.format(element_id))
                    raise
                else:
                    sleep(1)  # Wait one second then check again

    def screenshot(self, name):
        self.driver.save_screenshot(self.screenshot_folder + '/' + name + '.png')


# Start of script
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DanceStressTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
