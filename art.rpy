    ##############################MINI-CG##############################
    
    
    image mini_cg_1_1 = Animation("mini_cg_1/1.png", 0.1, "mini_cg_1/2.png", 0.1, "mini_cg_1/3.png", 0.1, "mini_cg_1/4.png", 0.1, "mini_cg_1/5.png", 0.1, "mini_cg_1/6.png", 0.1,  
                         "mini_cg_1/7.png", 0.1, "mini_cg_1/8.png", 0.1, "mini_cg_1/9.png", 0.1, "mini_cg_1/10.png", 0.1, "mini_cg_1/11.png", 0.1, "mini_cg_1/12.png", 0.1,
                          "mini_cg_1/13.png", 0.1, "mini_cg_1/14.png", 0.1, "mini_cg_1/15.png", 0.1, "mini_cg_1/16.png", 4)
    image mini_cg_1_2 = Animation("mini_cg_1/17.png", 0.1, "mini_cg_1/18.png", 0.1, "mini_cg_1/19.png", 0.1, "mini_cg_1/20.png", 0.1, "mini_cg_1/21.png", 0.1,)
    
    image mini_cg_mom_1:
        "mini_cg_mom/1.png"
        choice:
            8
        choice:
            6
        choice:
            4

        "mini_cg_mom/1.png"
        .1
        "mini_cg_mom/2.png"
        .1
        "mini_cg_mom/1.png"
        .1
        repeat
    
    image mini_cg_door = Animation("mini_cg_door/1.png", 0.1, "mini_cg_door/2.png", 0.1, "mini_cg_door/3.png", 0.1, "mini_cg_door/4.png", 0.1, "mini_cg_door/5.png", 0.1)  
    
    image mini_cg_run = Animation("mini_cg_run/1.png", 0.1, "mini_cg_run/2.png", 0.1, "mini_cg_run/3.png", 0.1, "mini_cg_run/4.png", 0.1, "mini_cg_run/5.png", 0.1, "mini_cg_run/6.png", 0.1)  

    image eyes_fear = Animation ("mini_cg_eyes/eyes_fear/center1.png", 4, "mini_cg_eyes/eyes_fear/center2.png", 0.1, "mini_cg_eyes/eyes_fear/center3.png", 0.1, "mini_cg_eyes/eyes_fear/center2.png", 0.1, "mini_cg_eyes/eyes_fear/center1.png", 3, 
         "mini_cg_eyes/eyes_fear/center2.png", 0.1, "mini_cg_eyes/eyes_fear/center3.png", 0.1, "mini_cg_eyes/eyes_fear/center2.png", 0.1, "mini_cg_eyes/eyes_fear/center1.png", 11,
         "mini_cg_eyes/eyes_fear/center2.png", 0.1, "mini_cg_eyes/eyes_fear/center3.png", 0.1, "mini_cg_eyes/eyes_fear/center2.png", 0.1, "mini_cg_eyes/eyes_fear/center1.png", 2,
         "mini_cg_eyes/eyes_fear/center2.png", 0.1, "mini_cg_eyes/eyes_fear/center3.png", 0.1, "mini_cg_eyes/eyes_fear/left2.png", 0.1, "mini_cg_eyes/eyes_fear/left1.png", 2,
         "mini_cg_eyes/eyes_fear/trans.png", 0.1, "mini_cg_eyes/eyes_fear/right1.png", 1, "mini_cg_eyes/eyes_fear/trans.png", 0.1, "mini_cg_eyes/eyes_fear/left1.png", 1,
         "mini_cg_eyes/eyes_fear/left2.png", 0.1, "mini_cg_eyes/eyes_fear/left3.png", 0.1, "mini_cg_eyes/eyes_fear/center2.png", 0.1)
    
    image mini_cg_momp_1 = "mini_cg_momp/1.png"
    image mini_cg_momp_2 = "mini_cg_momp/11.png"
    image mini_cg_momp_22 = Animation("mini_cg_momp/11.png", 0.05, "mini_cg_momp/12.png", 0.05, "mini_cg_momp/13.png", 0.05, "mini_cg_momp/14.png", 0.05,"mini_cg_momp/15.png", 0.05)  
    
    
    ##############################CG##############################
    
    image cg_balcony = "cg_balcony/1.png"
    
    image cg_mirror_idle = LiveComposite(
        (1920, 1080),
        (0, 0), "cg_mirror/1.png",
        (0, 0), "eyes_mirror",
        (0, 0), WhileSpeaking("gg", "mouth_mirror", "cg_mirror/1_mouth_closed.png"),
        )
    
    image cg_eyelash = Animation("cg_eyelash/1.png", 6, "cg_eyelash/2.png", 0.05, "cg_eyelash/3.png", 0.05, "cg_eyelash/4.png", 0.05)
    
    image eyes_mirror:
        "cg_mirror/1_eyes_open.png"
        choice:
            6
        choice:
            5
        choice:
            4
        choice:
            3
        choice:
            2

        "cg_mirror/1_eyes_half.png"
        .1
        "cg_mirror/1_eyes_closed.png"
        .2
        "cg_mirror/1_eyes_half.png"
        .1
        repeat

    image mouth_mirror:
        "cg_mirror/1_mouth_half.png"
        .1
        "cg_mirror/1_mouth_full.png"
        .1
        repeat
        
    
    
    image cg_mirror_brush = LiveComposite(
        (1920, 1080),
        (0, 0), "cg_mirror/2.png",
        (0, 0), "eyes_mirror",
        (0, 0), WhileSpeaking("gg", "cg_mirror/1_mouth_closed.png"),
        )

    image eyes_mirror:
        "cg_mirror/1_eyes_open.png"
        choice:
            6
        choice:
            5
        choice:
            4
        choice:
            3
        choice:
            2

        "cg_mirror/1_eyes_half.png"
        .1
        "cg_mirror/1_eyes_closed.png"
        .2
        "cg_mirror/1_eyes_half.png"
        .1
        repeat



    image cg_floor = LiveComposite(
        (1920, 1080),
        (0, 0), "cg_floor/1.png",
        (0, 0), "eyes_floor",
        (0, 0), WhileSpeaking("gg", "mouth_floor", "cg_floor/mouth_closed.png"),
        )

    image eyes_floor:
        "cg_floor/eyes_open.png"
        choice:
            6
        choice:
            5
        choice:
            4
        choice:
            3
        choice:
            2

        "cg_floor/eyes_half.png"
        .1
        "cg_floor/eyes_closed.png"
        .2
        "cg_floor/eyes_half.png"
        .1
        repeat

    image mouth_floor:
        "cg_floor/mouth_half.png"
        .1
        "cg_floor/mouth_full.png"
        .1
        repeat
        
        
    
    
    image cg_dream_s = LiveComposite(
        (1920, 1080),
        (0, 0), "cg_dream/2.png",
        (0, 0), "eyes_dream",
        (0, 0), WhileSpeaking("gg", "mouth_dream", "cg_dream/mouth_closed.png"),
        )
    
    image cg_dream = LiveComposite(
        (1920, 1080),
        (0, 0), "cg_dream/1.png",
        (0, 0), WhileSpeaking("gg", "mouth_dream", "cg_dream/mouth_closed.png"),
        )

    image eyes_dream:
        "cg_dream/eyes_open.png"
        choice:
            6
        choice:
            5
        choice:
            4
        choice:
            3
        choice:
            2

        "cg_dream/eyes_half.png"
        .1
        "cg_dream/eyes_closed.png"
        .2
        "cg_dream/eyes_half.png"
        .1
        repeat

    image mouth_dream:
        "cg_dream/mouth_half.png"
        .1
        "cg_dream/mouth_closed.png"
        .1
        "cg_dream/mouth_open.png"
        .1
        "cg_dream/mouth_closed.png"
        .1
        repeat
        
    
    image cg_pills = "cg_pills/1.png"
    
    image cg_firefly = "cg_firefly/1.png"
    
    image cg_ceiling = "cg_ceiling/1.png"
    
    image fireflies_anim = Animation("cg_ceiling/ff1.png", 0.1, "cg_ceiling/ff2.png", 0.1,  "cg_ceiling/ff3.png", 0.1,  "cg_ceiling/ff4.png", 0.1,  "cg_ceiling/ff5.png", 0.1,
         "cg_ceiling/ff6.png", 0.1, "cg_ceiling/ff7.png", 0.1, "cg_ceiling/ff8.png", 0.1, "cg_ceiling/ff9.png", 0.1, "cg_ceiling/ff10.png", 0.1,
          "cg_ceiling/ff11.png", 0.1, "cg_ceiling/ff12.png", 0.1, "cg_ceiling/ff13.png", 0.1, "cg_ceiling/ff14.png", 0.1, "cg_ceiling/ff15.png", 0.1,)  
    
    image cg_fall_close = Animation("cg_fall_close/1.png", 0.1, "cg_fall_close/2.png", 0.1, "cg_fall_close/3.png", 0.1, "cg_fall_close/4.png", 0.1, 
        "cg_fall_close/5.png", 0.1, "cg_fall_close/6.png", 0.1, "cg_fall_close/7.png", 0.1, "cg_fall_close/8.png", 0.1, "cg_fall_close/9.png", 0.1, 
        "cg_fall_close/10.png", 0.1) 
    
    image cg_fall_far = Animation("cg_fall_far/1.png", 0.1, "cg_fall_far/2.png", 0.1, "cg_fall_far/3.png", 0.1, "cg_fall_far/4.png", 0.1, 
        "cg_fall_far/5.png", 0.1, "cg_fall_far/6.png", 0.1)
    
    
    ##############################BGS##############################
    
    image eyebox:
        choice:
            "images/eyebox/1.png"
        choice:
            "images/eyebox/2.png"
        choice:
            "images/eyebox/3.png"
        choice:
            "images/eyebox/4.png"
        choice:
            "images/eyebox/5.png"
        choice:
            "images/eyebox/6.png"
        choice:
            "images/eyebox/7.png"
        choice:
            "images/eyebox/8.png"
        choice:
            "images/eyebox/9.png"
        choice:
            "images/eyebox/10.png"
        choice:
            "images/eyebox/11.png"
        choice:
            "images/eyebox/12.png"
        choice:
            "images/eyebox/13.png"
        choice:
            "images/eyebox/14.png"
        choice:
            "images/eyebox/15.png"
        choice:
            "images/eyebox/16.png"
        choice:
            "images/eyebox/17.png"
        choice:
            "images/eyebox/18.png"
        choice:
            "images/eyebox/19.png"
        choice:
            "images/eyebox/20.png"
    
    image cg_mirror_gg1:
        choice:
            "images/cg_mirror/cg_mirror_gg/1.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/2.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/3.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/4.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/5.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/6.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/7.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/8.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/9.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/10.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/11.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/12.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/13.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/14.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/15.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/19.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/20.png"
            
    image cg_mirror_gg2:
        choice:
            "images/cg_mirror/cg_mirror_gg/21.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/22.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/23.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/24.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/26.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/27.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/28.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/29.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/30.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/31.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/32.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/33.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/34.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/35.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/36.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/37.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/38.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/39.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/40.png"
    
    image cg_mirror_gg3:
        choice:
            "images/cg_mirror/cg_mirror_gg/41.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/42.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/43.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/44.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/45.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/46.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/47.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/48.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/49.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/50.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/51.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/52.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/53.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/54.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/55.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/56.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/57.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/58.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/59.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/60.png"
            
    image cg_mirror_gg4:
        choice:
            "images/cg_mirror/cg_mirror_gg/61.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/62.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/63.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/64.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/65.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/65.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/66.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/67.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/68.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/69.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/70.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/71.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/72.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/73.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/74.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/75.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/76.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/77.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/78.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/79.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/80.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/81.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/82.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/83.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/84.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/85.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/86.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/87.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/88.png"
        choice:
            "images/cg_mirror/cg_mirror_gg/89.png"

    image sky1:
        choice:
            "images/skybox/1.png"
        choice:
            "images/skybox/2.png"
        choice:
            "images/skybox/3.png"
        choice:
            "images/skybox/4.png"
        choice:
            "images/skybox/5.png"
        choice:
            "images/skybox/6.png"
        choice:
            "images/skybox/7.png"
        choice:
            "images/skybox/8.png"
        choice:
            "images/skybox/9.png"
        choice:
            "images/skybox/10.png"
        choice:
            "images/skybox/11.png"
        choice:
            "images/skybox/12.png"
        choice:
            "images/skybox/13.png"
        choice:
            "images/skybox/14.png"
        choice:
            "images/skybox/15.png"
        choice:
            "images/skybox/19.png"
        choice:
            "images/skybox/20.png"
                
    image sky2:
        choice:
            "images/skybox/21.png"
        choice:
            "images/skybox/22.png"
        choice:
            "images/skybox/23.png"
        choice:
            "images/skybox/24.png"
        choice:
            "images/skybox/26.png"
        choice:
            "images/skybox/27.png"
        choice:
            "images/skybox/28.png"
        choice:
            "images/skybox/29.png"
        choice:
            "images/skybox/30.png"
        choice:
            "images/skybox/31.png"
        choice:
            "images/skybox/32.png"
        choice:
            "images/skybox/33.png"
        choice:
            "images/skybox/34.png"
        choice:
            "images/skybox/35.png"
        choice:
            "images/skybox/36.png"
        choice:
            "images/skybox/37.png"
        choice:
            "images/skybox/38.png"
        choice:
            "images/skybox/39.png"
        choice:
            "images/skybox/40.png"
            
    image sky3:
        choice:
            "images/skybox/41.png"
        choice:
            "images/skybox/42.png"
        choice:
            "images/skybox/43.png"
        choice:
            "images/skybox/44.png"
        choice:
            "images/skybox/45.png"
        choice:
            "images/skybox/46.png"
        choice:
            "images/skybox/47.png"
        choice:
            "images/skybox/48.png"
        choice:
            "images/skybox/49.png"
        choice:
            "images/skybox/50.png"
        choice:
            "images/skybox/51.png"
        choice:
            "images/skybox/52.png"
        choice:
            "images/skybox/53.png"
        choice:
            "images/skybox/54.png"
        choice:
            "images/skybox/55.png"
        choice:
            "images/skybox/56.png"
        choice:
            "images/skybox/57.png"
        choice:
            "images/skybox/58.png"
        choice:
            "images/skybox/59.png"
        choice:
            "images/skybox/60.png"
            
    image sky4:
        choice:
            "images/skybox/61.png"
        choice:
            "images/skybox/62.png"
        choice:
            "images/skybox/63.png"
        choice:
            "images/skybox/64.png"
        choice:
            "images/skybox/65.png"
        choice:
            "images/skybox/66.png"
        choice:
            "images/skybox/67.png"
        choice:
            "images/skybox/68.png"
        choice:
            "images/skybox/69.png"
        choice:
            "images/skybox/70.png"
        choice:
            "images/skybox/71.png"
        choice:
            "images/skybox/72.png"
        choice:
            "images/skybox/73.png"
        choice:
            "images/skybox/74.png"
        choice:
            "images/skybox/75.png"
        choice:
            "images/skybox/76.png"
        choice:
            "images/skybox/77.png"
        choice:
            "images/skybox/78.png"
        choice:
            "images/skybox/79.png"
        choice:
            "images/skybox/80.png"
        choice:
            "images/skybox/81.png"
        choice:
            "images/skybox/82.png"
        choice:
            "images/skybox/83.png"
        choice:
            "images/skybox/84.png"
        choice:
            "images/skybox/85.png"
        choice:
            "images/skybox/86.png"
        choice:
            "images/skybox/87.png"
        choice:
            "images/skybox/88.png"
        choice:
            "images/skybox/89.png"
    
    image skyseizure = Animation("images/skybox/1.png", 0.05, "images/skybox/2.png", 0.05, "images/skybox/3.png", 0.05, "images/skybox/4.png", 0.05, 
        "images/skybox/5.png", 0.05, "images/skybox/6.png", 0.05, "images/skybox/7.png", 0.05, "images/skybox/8.png", 0.05, 
        "images/skybox/9.png", 0.05, "images/skybox/10.png", 0.05, "images/skybox/11.png", 0.05, "images/skybox/12.png", 0.05, "images/skybox/13.png", 0.05, 
        "images/skybox/14.png", 0.05, "images/skybox/15.png", 0.05, "images/skybox/19.png", 0.05, "images/skybox/20.png", 0.05, "images/skybox/21.png", 0.05, 
        "images/skybox/22.png", 0.05, "images/skybox/23.png", 0.05, "images/skybox/24.png", 0.05, "images/skybox/26.png", 0.05, "images/skybox/27.png", 0.05, "images/skybox/28.png")
    
            
    define gui.main_menu_background = renpy.random.choice(["images/skybox/1.png", "images/skybox/2.png", "images/skybox/3.png", "images/skybox/4.png", 
            "images/skybox/5.png", "images/skybox/6.png", "images/skybox/7.png", "images/skybox/8.png", "images/skybox/9.png", "images/skybox/10.png", "images/skybox/11.png", "images/skybox/12.png", 
            "images/skybox/13.png", "images/skybox/14.png", "images/skybox/15.png", "images/skybox/19.png", "images/skybox/20.png", 
            "images/skybox/21.png", "images/skybox/22.png", "images/skybox/23.png", "images/skybox/24.png"])
            
        
            
        
            
        
    image nk = "credits/nk.png"        
    image creditroll = "credits/credits.png"
    image controls = "controls.png"  
    image dsclmr = "dsclmr.png"  
        
            
        
            
        
            
        
            
        
            
        
            
        
            
        
            
        
            
        
            
        
            
        
            
        
            
        
            
            