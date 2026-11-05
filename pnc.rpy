#переменные
default X = 0
default Y = 0
default bp_X = False
default papers_X = False
default clock_Y = False
default laptop_X = False
default notebook_X = False
default pills_X = False
default can_Y = False
default bed_Y = False
default fan_Y = False
default umbrella_Y = False
default tumba_Y = False
default towel_Y = False
default plants_Y = False
default cond_Y = False
default bulbs_Y = False
default vent_Y = False
default posters_Y = False
default smth_X = False
default shkaf_Y = False

#поинт энд клик
screen pnc():
    imagebutton:
        focus_mask True
        idle "images/poc/backpack_idle.png"
        hover "images/poc/backpack_hover.png"
        #звук
        action Jump("backpack")
        xpos 1151 ypos 643
        if bp_X:
            idle "images/poc/backpack_idle.png"
            hover "images/poc/backpack_idle.png"
            xpos 1151 ypos 643
            action NullAction()
    imagebutton:
        focus_mask True
        xpos 550 ypos 851
        idle "images/poc/bed_idle.png"
        hover "images/poc/bed_hover.png"
        #звук
        action Jump("bed")
        if bed_Y:
            xpos 550 ypos 851
            idle "images/poc/bed_idle.png"
            hover "images/poc/bed_idle.png"
            action NullAction()
    imagebutton:
        focus_mask True
        xpos 327 ypos 366
        idle "images/poc/papers_idle.png"
        hover "images/poc/papers_hover.png"
        #звук
        action Jump("papers")
        if papers_X:
            xpos 327 ypos 366
            idle "images/poc/papers_idle.png"
            hover "images/poc/papers_idle.png"
            action NullAction()
    imagebutton:
        focus_mask True
        xpos 594 ypos 301
        idle "images/poc/clock_idle.png"
        hover "images/poc/clock_hover.png"
        #звук
        action Jump("clock")
        if clock_Y:
            xpos 594 ypos 301
            idle "images/poc/clock_idle.png"
            hover "images/poc/clock_idle.png"
            action NullAction()
    imagebutton:
        focus_mask True
        xpos 420 ypos 764
        idle "images/poc/can_idle.png"
        hover "images/poc/can_hover.png"
        #звук
        action Jump("can")
        if can_Y:
            xpos 420 ypos 764
            idle "images/poc/can_idle.png"
            hover "images/poc/can_idle.png"
            action NullAction()
    imagebutton:
        focus_mask True
        xpos 1400 ypos 772
        idle "images/poc/fan_idle.png"
        hover "images/poc/fan_hover.png"
        #звук
        action Jump("fan")
        if fan_Y:
            xpos 1400 ypos 772
            idle "images/poc/fan_idle.png"
            hover "images/poc/fan_idle.png"
            action NullAction()
    imagebutton:
        focus_mask True
        xpos 729 ypos 550
        idle "images/poc/laptop_idle.png"
        hover "images/poc/laptop_hover.png"
        #звук
        action Jump("laptop")
        if laptop_X:
            xpos 729 ypos 550
            idle "images/poc/laptop_idle.png"
            hover "images/poc/laptop_idle.png"
            action NullAction()
    imagebutton:
        focus_mask True
        xpos 1040 ypos 748
        idle "images/poc/notebook_idle.png"
        hover "images/poc/notebook_hover.png"
        #звук
        action Jump("notebook")
        if notebook_X:
            xpos 1040 ypos 748
            idle "images/poc/notebook_idle.png"
            hover "images/poc/notebook_idle.png"
            action NullAction()
    imagebutton:
        focus_mask True
        xpos 140 ypos 581
        idle "images/poc/pills_idle.png"
        hover "images/poc/pills_hover.png"
        #звук
        action Jump("pills")
        if pills_X:
            xpos 140 ypos 581
            idle "images/poc/pills_idle.png"
            hover "images/poc/pills_idle.png"
            action NullAction()
    imagebutton:
        focus_mask True
        xpos 910 ypos 655
        idle "images/poc/umbrella_idle.png"
        hover "images/poc/umbrella_hover.png"
        #звук
        action Jump("umbrella")
        if umbrella_Y:
            xpos 910 ypos 655
            idle "images/poc/umbrella_idle.png"
            hover "images/poc/umbrella_idle.png"
            action NullAction()
    imagebutton:
        focus_mask True
        xpos 654 ypos 618
        idle "images/poc/tumba_idle.png"
        hover "images/poc/tumba_hover.png"
        #звук
        action Jump("tumba")
        if tumba_Y:
            xpos 654 ypos 618
            idle "images/poc/tumba_idle.png"
            hover "images/poc/tumba_idle.png"
            action NullAction()
    imagebutton:
        focus_mask True
        xpos 0 ypos 366
        idle "images/poc/towel_idle.png"
        hover "images/poc/towel_hover.png"
        #звук
        action Jump("towel")
        if towel_Y:
            xpos 0 ypos 366
            idle "images/poc/towel_idle.png"
            hover "images/poc/towel_idle.png"
            action NullAction()
    imagebutton:
        focus_mask True
        xpos 463 ypos 0
        idle "images/poc/plants_idle.png"
        hover "images/poc/plants_hover.png"
        #звук
        action Jump("plants")
        if plants_Y:
            xpos 463 ypos 0
            idle "images/poc/plants_idle.png"
            hover "images/poc/plants_idle.png"
            action NullAction()
    imagebutton:
        focus_mask True
        xpos 1554 ypos 0
        idle "images/poc/cond_idle.png"
        hover "images/poc/cond_hover.png"
        #звук
        action Jump("cond")
        if cond_Y:
            xpos 1554 ypos 0
            idle "images/poc/cond_idle.png"
            hover "images/poc/cond_idle.png"
            action NullAction()
    imagebutton:
        focus_mask True
        xpos 1222 ypos 0
        idle "images/poc/bulbs_idle.png"
        hover "images/poc/bulbs_hover.png"
        #звук
        action Jump("bulbs")
        if bulbs_Y:
            xpos 1222 ypos 0
            idle "images/poc/bulbs_idle.png"
            hover "images/poc/bulbs_idle.png"
            action NullAction()
    imagebutton:
        focus_mask True
        xpos 896 ypos 84
        idle "images/poc/vent_idle.png"
        hover "images/poc/vent_hover.png"
        #звук
        action Jump("vent")
        if vent_Y:
            xpos 896 ypos 84
            idle "images/poc/vent_idle.png"
            hover "images/poc/vent_idle.png"
            action NullAction()
    imagebutton:
        focus_mask True
        xpos 0 ypos 748
        idle "images/poc/milk_idle.png"
        hover "milk_hover"
        hover_sound "audio/milk_hover.ogg"
        action NullAction()
    imagebutton:
        focus_mask True
        xpos 1770 ypos 188
        idle "images/poc/posters_idle.png"
        hover "images/poc/posters_hover.png"
        #звук
        action Jump("posters")
        if posters_Y:
            xpos 1770 ypos 188
            idle "images/poc/posters_idle.png"
            hover "images/poc/posters_idle.png"
            action NullAction()
    imagebutton:
        focus_mask True
        xpos 0 ypos 0
        idle "images/poc/shkaf_idle.png"
        hover "images/poc/shkaf_hover.png"
        #звук
        action Jump("shkaf")
        if shkaf_Y:
            xpos 0 ypos 0
            idle "images/poc/shkaf_idle.png"
            hover "images/poc/shkaf_idle.png"
            action NullAction()            
    imagebutton:
        focus_mask True
        xpos 1666 ypos 1018
        idle "images/poc/smth_idle.png"
        hover "images/poc/smth_hover.png"
        action Jump("smth")
        if smth_X:
            xpos 3000 ypos 1018
            idle "images/poc/smth_idle.png"
            hover "images/poc/smth_idle.png"
            action NullAction()
    
    if renpy.music.is_playing (channel='sound'):
        imagebutton:
            focus_mask True
            xpos 1190 ypos 312
            idle "images/poc/radio1_idle.png"
            hover "images/poc/radio1_hover.png"
            action Stop("sound")
    else:
        imagebutton:
            focus_mask True
            xpos 1190 ypos 312
            idle "images/poc/radio1_idle.png"
            hover "images/poc/radio1_hover.png"
            action Play("sound", renpy.random.choice(radio1)) 
    
    
    if renpy.music.is_playing (channel='sound'):
        imagebutton:
            focus_mask True
            xpos 684 ypos 314
            idle "images/poc/radio2_idle.png"
            hover "images/poc/radio2_hover.png"
            action Stop("sound") 
    else:
        imagebutton:
            focus_mask True
            xpos 684 ypos 314
            idle "images/poc/radio2_idle.png"
            hover "images/poc/radio2_hover.png"
            action Play("sound", renpy.random.choice(radio2)) 
            
      
    if renpy.music.is_playing (channel='sound'):  
        imagebutton:
            focus_mask True
            xpos 1740 ypos 438
            idle "images/poc/radio3_idle.png"
            hover "images/poc/radio3_hover.png"
            action Stop("sound")   
    else:
        imagebutton:
            focus_mask True
            xpos 1740 ypos 438
            idle "images/poc/radio3_idle.png"
            hover "images/poc/radio3_hover.png"
            action Play("sound", renpy.random.choice(radio3)) 
            
            
            
            
            
            
            
            
            
            
            
            
            
    if X >= 3:
        imagebutton:
            focus_mask True
            idle "images/pnc end_idle.png"
            hover "images/pnc end_hover.png"
            action Jump('newscene_check')
                    
            
            
            
            
            
            
            
            
            
