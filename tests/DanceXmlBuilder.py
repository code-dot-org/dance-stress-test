def set_background(effect_name):
    return set_effect('Background', effect_name)


def set_foreground(effect_name):
    return set_effect('Foreground', effect_name)


def set_effect(effect_type, effect_name):
    return """
     <xml>
      <block type="Dancelab_whenSetup" movable="false">
       <statement name="DO">
        <block type="Dancelab_set{effect_type}Effect">
         <title name="EFFECT">"{effect_name}"</title>
        </block>
       </statement>
      </block>
     </xml>
    """.format(effect_type=effect_type, effect_name=effect_name)


def heavy():
    return (
        'heavy',
        """
        <xml>
         <block type="Dancelab_whenSetup" movable="false"></block>
        """ +
        SET_FOREGROUND_EVERY_SECONDS +
        SET_BACKGROUND_EVERY_SECONDS +
        LAYOUT_SPRITES_EVERY_SECONDS +
        xml_add_dancer(CHARACTERS[0]) +
        """
        </xml>
        """
    )


def heaviest():
    return (
        'heaviest',
        """
        <xml>
         <block type="Dancelab_whenSetup" movable="false"></block>
        """ +
        SET_FOREGROUND_EVERY_SECONDS +
        SET_BACKGROUND_EVERY_SECONDS +
        LAYOUT_SPRITES_EVERY_SECONDS +
        xml_add_all_dancers() +
        """
        </xml>
        """
    )


CHARACTERS = ['ALIEN', 'BEAR', 'CAT', 'DOG', 'DUCK', 'FROG', 'MOOSE', 'PINEAPPLE', 'ROBOT', 'SHARK', 'UNICORN']

MOVES = ['Rest', 'ClapHigh', 'Clown', 'Dab', 'DoubleJam', 'Drop', 'Floss', 'Fresh', 'Roll', 'Kick', 'ThisOrThat',
         'Thriller']


def xml_add_move(costume, time, move):
    var_name = "{}_{}_{:d}".format(costume, move, int(time))
    return """
     <block type="Dancelab_atTimestamp">
      <title name="TIMESTAMP">{time}</title>
      <title name="UNIT">"seconds"</title>
      <next>
       <block type="Dancelab_makeNewDanceSprite">
        <title name="COSTUME">"{costume}"</title>
        <title name="NAME">{var_name}</title>
        <title name="LOCATION">{{x: 200, y: 100}}</title>
        <next>
         <block type="Dancelab_changeMoveLR">
          <title name="SPRITE">{var_name}</title>
          <title name="MOVE">MOVES.{move}</title>
          <title name="DIR">-1</title>
         </block>
        </next>
       </block>
      </next>
     </block>
    """.format(costume=costume, time=time, var_name=var_name, move=move)


def xml_add_dancer(costume):
    xml = ""
    time = 1
    for move in MOVES:
        xml += xml_add_move(costume, time, move)
        time += 0.25
    return xml


def xml_add_all_dancers():
    xml = ""
    time = 1
    for costume in CHARACTERS:
        for move in MOVES:
            xml += xml_add_move(costume, time, move)
            time += 0.25
    return xml


SET_FOREGROUND_EVERY_SECONDS = """
<block type="Dancelab_everySeconds">
 <title name="N">3.02</title>
 <title name="UNIT">"seconds"</title>
 <statement name="DO">
  <block type="Dancelab_setForegroundEffect">
   <title name="EFFECT">['spotlight', 'rain', 'raining_tacos'][randomInt(0,2)]</title>
  </block>
 </statement>
</block>
"""

SET_BACKGROUND_EVERY_SECONDS = """
<block type="Dancelab_everySeconds">
 <title name="N">4.03</title>
 <title name="UNIT">"seconds"</title>
 <statement name="DO">
  <block type="Dancelab_setBackgroundEffect">
   <title name="EFFECT">['disco', 'color_cycle', 'rainbow', 'text',
    'diamonds','splatter','swirl','spiral'][randomInt(0,7)]
   </title>
  </block>
 </statement>
</block>
"""

LAYOUT_SPRITES_EVERY_SECONDS = """
<block type="Dancelab_everySeconds">
 <title name="N">0.125</title>
 <title name="UNIT">"seconds"</title>
 <statement name="DO">
  <block type="Dancelab_layoutSprites">
   <title name="GROUP">sprites</title>
   <title name="FORMAT">"grid"</title>
  </block>
 </statement>
</block>
"""
