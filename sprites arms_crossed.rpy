

###########################################NEUTRAL###########################################



init:
    
    image smile_funny = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_crossed/smile/smile_funny.png",
        )
    
    image gg_neutral_1 = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_crossed/neutral/neutral_1.png",
        (0, 0), "eyes_neutral_1",
        (0, 0), WhileSpeaking("gg", "mouth_neutral", "sprites/arms_crossed/neutral/neutral_mouth_closed.png"),
        )

    image eyes_neutral_1:
        "sprites/arms_crossed/neutral/neutral_1_eyes_open.png"
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

        "sprites/arms_crossed/neutral/neutral_1_eyes_half.png"
        .1
        "sprites/arms_crossed/neutral/neutral_eyes_closed.png"
        .2
        "sprites/arms_crossed/neutral/neutral_1_eyes_half.png"
        .1
        repeat

    image mouth_neutral:
        "sprites/arms_crossed/neutral/neutral_mouth_half.png"
        .1
        "sprites/arms_crossed/neutral/neutral_mouth_full.png"
        .1
        repeat
        
        
        
        
        
    image gg_neutral_2 = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_crossed/neutral/neutral_2.png",
        (0, 0), "eyes_neutral_2",
        (0, 0), WhileSpeaking("gg", "mouth_neutral", "sprites/arms_crossed/neutral/neutral_mouth_closed.png"),
        )

    image eyes_neutral_2:
        "sprites/arms_crossed/neutral/neutral_2_eyes_open.png"
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

        "sprites/arms_crossed/neutral/neutral_2_eyes_half.png"
        .1
        "sprites/arms_crossed/neutral/neutral_eyes_closed.png"
        .2
        "sprites/arms_crossed/neutral/neutral_2_eyes_half.png"
        .1
        repeat

    image mouth_neutral:
        "sprites/arms_crossed/neutral/neutral_mouth_half.png"
        .1
        "sprites/arms_crossed/neutral/neutral_mouth_full.png"
        .1
        repeat  
        
    
    
    
        
    image gg_neutral_3 = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_crossed/neutral/neutral_3.png",
        (0, 0), "eyes_neutral_3",
        (0, 0), WhileSpeaking("gg", "mouth_neutral", "sprites/arms_crossed/neutral/neutral_mouth_closed.png"),
        )

    image eyes_neutral_3:
        "sprites/arms_crossed/neutral/neutral_3_eyes_open.png"
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

        "sprites/arms_crossed/neutral/neutral_3_eyes_half.png"
        .1
        "sprites/arms_crossed/neutral/neutral_eyes_closed.png"
        .2
        "sprites/arms_crossed/neutral/neutral_3_eyes_half.png"
        .1
        repeat

    image mouth_neutral:
        "sprites/arms_crossed/neutral/neutral_mouth_half.png"
        .1
        "sprites/arms_crossed/neutral/neutral_mouth_full.png"
        .1
        repeat 
    
    
    
    
    
    image gg_neutral_4 = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_crossed/neutral/neutral_4.png",
        (0, 0), WhileSpeaking("gg", "mouth_neutral", "sprites/arms_crossed/neutral/neutral_mouth_closed.png"),
        )

    image mouth_neutral:
        "sprites/arms_crossed/neutral/neutral_mouth_half.png"
        .1
        "sprites/arms_crossed/neutral/neutral_mouth_full.png"
        .1
        repeat
        
    
    
    
    
###########################################MAD###########################################    
    
    
    image gg_mad_1 = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_crossed/mad/mad_1.png",
        (0, 0), "eyes_mad_1",
        (0, 0), WhileSpeaking("gg", "mouth_neutral", "sprites/arms_crossed/mad/mad_mouth_closed.png"),
        )

    image eyes_mad_1:
        "sprites/arms_crossed/mad/mad_1_eyes_open.png"
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

        "sprites/arms_crossed/mad/mad_1_eyes_half.png"
        .1
        "sprites/arms_crossed/mad/mad_eyes_closed.png"
        .2
        "sprites/arms_crossed/mad/mad_1_eyes_half.png"
        .1
        repeat

    image mouth_neutral:
        "sprites/arms_crossed/mad/neutral_mouth_half.png"
        .1
        "sprites/arms_crossed/mad/neutral_mouth_full.png"
        .1
        repeat
        
        
        
        
        
    image gg_mad_2 = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_crossed/mad/mad_1.png",
        (0, 0), "eyes_mad_2",
        (0, 0), WhileSpeaking("gg", "mouth_neutral", "sprites/arms_crossed/mad/mad_mouth_closed.png"),
        )

    image eyes_mad_2:
        "sprites/arms_crossed/mad/mad_2_eyes_open.png"
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

        "sprites/arms_crossed/mad/mad_2_eyes_half.png"
        .1
        "sprites/arms_crossed/mad/mad_eyes_closed.png"
        .2
        "sprites/arms_crossed/mad/mad_2_eyes_half.png"
        .1
        repeat

    image mouth_neutral:
        "sprites/arms_crossed/mad/neutral_mouth_half.png"
        .1
        "sprites/arms_crossed/mad/neutral_mouth_full.png"
        .1
        repeat  
        
    
    
    
        
    image gg_mad_3 = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_crossed/mad/mad_3.png",
        (0, 0), WhileSpeaking("gg", "mouth_neutral", "sprites/arms_crossed/mad/mad_mouth_closed.png"),
        )

    image mouth_neutral:
        "sprites/arms_crossed/mad/neutral_mouth_half.png"
        .1
        "sprites/arms_crossed/mad/neutral_mouth_full.png"
        .1
        repeat  
    

    
###########################################SAD###########################################    
    
    
    image gg_sad_1 = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_crossed/sad/sad_1.png",
        (0, 0), "eyes_sad_1",
        (0, 0), WhileSpeaking("gg", "mouth_neutral", "sprites/arms_crossed/sad/sad_mouth_closed.png"),
        )

    image eyes_sad_1:
        "sprites/arms_crossed/sad/sad_1_eyes_open.png"
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

        "sprites/arms_crossed/sad/sad_1_eyes_half.png"
        .1
        "sprites/arms_crossed/sad/sad_eyes_closed.png"
        .2
        "sprites/arms_crossed/sad/sad_1_eyes_half.png"
        .1
        repeat

    image mouth_neutral:
        "sprites/arms_crossed/sad/neutral_mouth_half.png"
        .1
        "sprites/arms_crossed/sad/neutral_mouth_full.png"
        .1
        repeat
        
        
        
        
        
    image gg_sad_2 = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_crossed/sad/sad_1.png",
        (0, 0), "eyes_sad_2",
        (0, 0), WhileSpeaking("gg", "mouth_neutral", "sprites/arms_crossed/sad/sad_mouth_closed.png"),
        )

    image eyes_sad_2:
        "sprites/arms_crossed/sad/sad_2_eyes_open.png"
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

        "sprites/arms_crossed/sad/sad_2_eyes_half.png"
        .1
        "sprites/arms_crossed/sad/sad_eyes_closed.png"
        .2
        "sprites/arms_crossed/sad/sad_2_eyes_half.png"
        .1
        repeat

    image mouth_neutral:
        "sprites/arms_crossed/sad/neutral_mouth_half.png"
        .1
        "sprites/arms_crossed/sad/neutral_mouth_full.png"
        .1
        repeat  
        
    
    
    
        
    image gg_sad_3 = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_crossed/sad/sad_3.png",
        (0, 0), WhileSpeaking("gg", "mouth_neutral", "sprites/arms_crossed/sad/sad_mouth_closed.png"),
        )

    image mouth_neutral:
        "sprites/arms_crossed/sad/neutral_mouth_half.png"
        .1
        "sprites/arms_crossed/sad/neutral_mouth_full.png"
        .1
        repeat      
    
    
###########################################SMILE###########################################    
    
    
    image gg_smile_1 = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_crossed/smile/smile_1.png",
        (0, 0), "eyes_smile_1",
        (0, 0), WhileSpeaking("gg", "mouth_smile", "sprites/arms_crossed/smile/smile_mouth_closed.png"),
        )

    image eyes_smile_1:
        "sprites/arms_crossed/smile/smile_1_eyes_open.png"
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

        "sprites/arms_crossed/smile/smile_1_eyes_half.png"
        .1
        "sprites/arms_crossed/smile/smile_eyes_closed.png"
        .2
        "sprites/arms_crossed/smile/smile_1_eyes_half.png"
        .1
        repeat

    image mouth_smile:
        "sprites/arms_crossed/smile/smile_mouth_half.png"
        .1
        "sprites/arms_crossed/smile/smile_mouth_full.png"
        .1
        repeat
        
        
        
        
        
    image gg_smile_2 = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_crossed/smile/smile_2.png",
        (0, 0), "eyes_smile_2",
        (0, 0), WhileSpeaking("gg", "mouth_smile", "sprites/arms_crossed/smile/smile_mouth_closed.png"),
        )

    image eyes_smile_2:
        "sprites/arms_crossed/smile/smile_2_eyes_open.png"
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

        "sprites/arms_crossed/smile/smile_2_eyes_half.png"
        .1
        "sprites/arms_crossed/smile/smile_eyes_closed.png"
        .2
        "sprites/arms_crossed/smile/smile_2_eyes_half.png"
        .1
        repeat

    image mouth_smile:
        "sprites/arms_crossed/smile/smile_mouth_half.png"
        .1
        "sprites/arms_crossed/smile/smile_mouth_full.png"
        .1
        repeat  
        
    
    
    
        
    image gg_smile_3 = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_crossed/smile/smile_3.png",
        (0, 0), WhileSpeaking("gg", "mouth_smile", "sprites/arms_crossed/smile/smile_mouth_closed.png"),
        )

    image mouth_smile:
        "sprites/arms_crossed/smile/smile_mouth_half.png"
        .1
        "sprites/arms_crossed/smile/smile_mouth_full.png"
        .1
        repeat      
    
  
  
  
###########################################CONF###########################################    
    
    
    image gg_conf_1 = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_crossed/conf/conf_1.png",
        (0, 0), "eyes_conf_1",
        (0, 0), WhileSpeaking("gg", "mouth_conf", "sprites/arms_crossed/conf/conf_mouth_closed.png"),
        )

    image eyes_conf_1:
        "sprites/arms_crossed/conf/conf_1_eyes_open.png"
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

        "sprites/arms_crossed/conf/conf_1_eyes_half.png"
        .1
        "sprites/arms_crossed/conf/conf_eyes_closed.png"
        .2
        "sprites/arms_crossed/conf/conf_1_eyes_half.png"
        .1
        repeat

    image mouth_conf:
        "sprites/arms_crossed/conf/conf_mouth_half.png"
        .1
        "sprites/arms_crossed/conf/conf_mouth_full.png"
        .1
        repeat
        
        
        
        
        
    image gg_conf_2 = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_crossed/conf/conf_2.png",
        (0, 0), "eyes_conf_2",
        (0, 0), WhileSpeaking("gg", "mouth_conf", "sprites/arms_crossed/conf/conf_mouth_closed.png"),
        )

    image eyes_conf_2:
        "sprites/arms_crossed/conf/conf_2_eyes_open.png"
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

        "sprites/arms_crossed/conf/conf_2_eyes_half.png"
        .1
        "sprites/arms_crossed/conf/conf_eyes_closed.png"
        .2
        "sprites/arms_crossed/conf/conf_2_eyes_half.png"
        .1
        repeat

    image mouth_conf:
        "sprites/arms_crossed/conf/conf_mouth_half.png"
        .1
        "sprites/arms_crossed/conf/conf_mouth_full.png"
        .1
        repeat  
        
    
    
    
        
    image gg_conf_3 = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_crossed/conf/conf_3.png",
        (0, 0), WhileSpeaking("gg", "mouth_conf", "sprites/arms_crossed/conf/conf_mouth_closed.png"),
        )

    image mouth_conf:
        "sprites/arms_crossed/conf/conf_mouth_half.png"
        .1
        "sprites/arms_crossed/conf/conf_mouth_full.png"
        .1
        repeat        
  
  
  

###########################################NERV###########################################    
    
    
    image gg_nerv_1 = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_crossed/nerv/nerv_1.png",
        (0, 0), "eyes_nerv_1",
        (0, 0), WhileSpeaking("gg", "mouth_nerv", "sprites/arms_crossed/nerv/nerv_mouth_closed.png"),
        )

    image eyes_nerv_1:
        "sprites/arms_crossed/nerv/nerv_1_eyes_open.png"
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

        "sprites/arms_crossed/nerv/nerv_1_eyes_half.png"
        .1
        "sprites/arms_crossed/nerv/nerv_eyes_closed.png"
        .2
        "sprites/arms_crossed/nerv/nerv_1_eyes_half.png"
        .1
        repeat

    image mouth_nerv:
        "sprites/arms_crossed/nerv/nerv_mouth_half.png"
        .1
        "sprites/arms_crossed/nerv/nerv_mouth_full.png"
        .1
        repeat
        
        
    
        
    image gg_nerv_2 = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_crossed/nerv/nerv_2.png",
        (0, 0), WhileSpeaking("gg", "mouth_nerv", "sprites/arms_crossed/nerv/nerv_mouth_closed.png"),
        )

    image mouth_nerv:
        "sprites/arms_crossed/nerv/nerv_mouth_half.png"
        .1
        "sprites/arms_crossed/nerv/nerv_mouth_full.png"
        .1
        repeat     
  
  
  
  
###########################################ZOUT###########################################    
    
    
    image gg_zout_1 = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_crossed/zout/zout_1.png",
        (0, 0), "eyes_zout_1",
        (0, 0), WhileSpeaking("gg", "mouth_zout", "sprites/arms_crossed/zout/zout_mouth_closed.png"),
        )

    image eyes_zout_1:
        "sprites/arms_crossed/zout/zout_1_eyes_open.png"
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

        "sprites/arms_crossed/zout/zout_1_eyes_half.png"
        .1
        "sprites/arms_crossed/zout/zout_eyes_closed.png"
        .2
        "sprites/arms_crossed/zout/zout_1_eyes_half.png"
        .1
        repeat

    image mouth_zout:
        "sprites/arms_crossed/zout/zout_mouth_half.png"
        .1
        "sprites/arms_crossed/zout/zout_mouth_full.png"
        .1
        repeat
        
        
    
        
    image gg_zout_2 = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_crossed/zout/zout_2.png",
        (0, 0), WhileSpeaking("gg", "mouth_zout", "sprites/arms_crossed/zout/zout_mouth_closed.png"),
        )

    image mouth_zout:
        "sprites/arms_crossed/zout/zout_mouth_half.png"
        .1
        "sprites/arms_crossed/zout/zout_mouth_full.png"
        .1
        repeat       
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
        
        