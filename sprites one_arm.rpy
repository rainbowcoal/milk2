
###########################################NEUTRAL###########################################



init:
    image gg_neutral_1_oa = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/one_arm/neutral/neutral_1.png",
        (0, 0), "eyes_neutral_1_oa",
        (0, 0), WhileSpeaking("gg", "mouth_neutral_oa", "sprites/one_arm/neutral/neutral_mouth_closed.png"),
        )

    image eyes_neutral_1_oa:
        "sprites/one_arm/neutral/neutral_1_eyes_open.png"
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

        "sprites/one_arm/neutral/neutral_1_eyes_half.png"
        .1
        "sprites/one_arm/neutral/neutral_eyes_closed.png"
        .2
        "sprites/one_arm/neutral/neutral_1_eyes_half.png"
        .1
        repeat

    image mouth_neutral_oa:
        "sprites/one_arm/neutral/neutral_mouth_half.png"
        .1
        "sprites/one_arm/neutral/neutral_mouth_full.png"
        .1
        repeat
        
        
        
        
        
    image gg_neutral_2_oa = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/one_arm/neutral/neutral_2.png",
        (0, 0), "eyes_neutral_2_oa",
        (0, 0), WhileSpeaking("gg", "mouth_neutral_oa", "sprites/one_arm/neutral/neutral_mouth_closed.png"),
        )

    image eyes_neutral_2_oa:
        "sprites/one_arm/neutral/neutral_2_eyes_open.png"
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

        "sprites/one_arm/neutral/neutral_2_eyes_half.png"
        .1
        "sprites/one_arm/neutral/neutral_eyes_closed.png"
        .2
        "sprites/one_arm/neutral/neutral_2_eyes_half.png"
        .1
        repeat

    image mouth_neutral_oa:
        "sprites/one_arm/neutral/neutral_mouth_half.png"
        .1
        "sprites/one_arm/neutral/neutral_mouth_full.png"
        .1
        repeat 
        
    
    
    
        
    image gg_neutral_3_oa = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/one_arm/neutral/neutral_1.png",
        (0, 0), "eyes_neutral_3_oa",
        (0, 0), WhileSpeaking("gg", "mouth_neutral_oa", "sprites/one_arm/neutral/neutral_mouth_closed.png"),
        )

    image eyes_neutral_3_oa:
        "sprites/one_arm/neutral/neutral_3_eyes_open.png"
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

        "sprites/one_arm/neutral/neutral_3_eyes_half.png"
        .1
        "sprites/one_arm/neutral/neutral_eyes_closed.png"
        .2
        "sprites/one_arm/neutral/neutral_3_eyes_half.png"
        .1
        repeat

    image mouth_neutral_oa:
        "sprites/one_arm/neutral/neutral_mouth_half.png"
        .1
        "sprites/one_arm/neutral/neutral_mouth_full.png"
        .1
        repeat 
    
    
    
    

    
    
    
    
###########################################MAD###########################################    
    
    
    image gg_mad_1_oa = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/one_arm/mad/mad_1.png",
        (0, 0), "eyes_mad_1_oa",
        (0, 0), WhileSpeaking("gg", "mouth_mad_oa", "sprites/one_arm/mad/mad_mouth_closed.png"),
        )

    image eyes_mad_1_oa:
        "sprites/one_arm/mad/mad_1_eyes_open.png"
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

        "sprites/one_arm/mad/mad_1_eyes_half.png"
        .1
        "sprites/one_arm/mad/mad_eyes_closed.png"
        .2
        "sprites/one_arm/mad/mad_1_eyes_half.png"
        .1
        repeat

    image mouth_mad_oa:
        "sprites/one_arm/mad/mad_mouth_half.png"
        .1
        "sprites/one_arm/mad/mad_mouth_full.png"
        .1
        repeat
        
        
        
        
        
    image gg_mad_2_oa = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/one_arm/mad/mad_2.png",
        (0, 0), "eyes_mad_2_oa",
        (0, 0), WhileSpeaking("gg", "mouth_mad_oa", "sprites/one_arm/mad/mad_mouth_closed.png"),
        )

    image eyes_mad_2_oa:
        "sprites/one_arm/mad/mad_2_eyes_open.png"
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

        "sprites/one_arm/mad/mad_2_eyes_half.png"
        .1
        "sprites/one_arm/mad/mad_eyes_closed.png"
        .2
        "sprites/one_arm/mad/mad_2_eyes_half.png"
        .1
        repeat

    image mouth_mad_oa:
        "sprites/one_arm/mad/mad_mouth_half.png"
        .1
        "sprites/one_arm/mad/mad_mouth_full.png"
        .1
        repeat  
        
    
    
    image gg_mad_3_oa = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/one_arm/mad/mad_1.png",
        (0, 0), "eyes_mad_3_oa",
        (0, 0), WhileSpeaking("gg", "mouth_mad_oa", "sprites/one_arm/mad/mad_mouth_closed.png"),
        )

    image eyes_mad_3_oa:
        "sprites/one_arm/mad/mad_3_eyes_open.png"
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

        "sprites/one_arm/mad/mad_3_eyes_half.png"
        .1
        "sprites/one_arm/mad/mad_eyes_closed.png"
        .2
        "sprites/one_arm/mad/mad_3_eyes_half.png"
        .1
        repeat

    image mouth_mad_oa:
        "sprites/one_arm/mad/mad_mouth_half.png"
        .1
        "sprites/one_arm/mad/mad_mouth_full.png"
        .1
        repeat
        
        
        
    image gg_mad_4_oa = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/one_arm/mad/mad_4.png",
        (0, 0), WhileSpeaking("gg", "mouth_mad_oa", "sprites/one_arm/mad/mad_mouth_closed.png"),
        )

    image mouth_mad_oa:
        "sprites/one_arm/mad/mad_mouth_half.png"
        .1
        "sprites/one_arm/mad/mad_mouth_full.png"
        .1
        repeat  
    

    
###########################################SAD###########################################    
    
    
    image gg_sad_1_oa = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/one_arm/sad/sad_1.png",
        (0, 0), "eyes_sad_1_oa",
        (0, 0), WhileSpeaking("gg", "mouth_neutral_oa", "sprites/one_arm/sad/sad_mouth_closed.png"),
        )

    image eyes_sad_1_oa:
        "sprites/one_arm/sad/sad_1_eyes_open.png"
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

        "sprites/one_arm/sad/sad_1_eyes_half.png"
        .1
        "sprites/one_arm/sad/sad_eyes_closed.png"
        .2
        "sprites/one_arm/sad/sad_1_eyes_half.png"
        .1
        repeat

    image mouth_neutral_oa:
        "sprites/one_arm/neutral/neutral_mouth_half.png"
        .1
        "sprites/one_arm/neutral/neutral_mouth_full.png"
        .1
        repeat
        
        
        
        
        
    image gg_sad_2_oa = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/one_arm/sad/sad_2.png",
        (0, 0), "eyes_sad_2_oa",
        (0, 0), WhileSpeaking("gg", "mouth_neutral_oa", "sprites/one_arm/sad/sad_mouth_closed.png"),
        )

    image eyes_sad_2_oa:
        "sprites/one_arm/sad/sad_2_eyes_open.png"
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

        "sprites/one_arm/sad/sad_2_eyes_half.png"
        .1
        "sprites/one_arm/sad/sad_eyes_closed.png"
        .2
        "sprites/one_arm/sad/sad_2_eyes_half.png"
        .1
        repeat

    image mouth_neutral_oa:
        "sprites/one_arm/neutral/neutral_mouth_half.png"
        .1
        "sprites/one_arm/neutral/neutral_mouth_full.png"
        .1
        repeat  
        
    
    
    
        
    image gg_sad_3_oa = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/one_arm/sad/sad_3.png",
        (0, 0), "eyes_sad_3_oa",
        (0, 0), WhileSpeaking("gg", "mouth_neutral_oa", "sprites/one_arm/sad/sad_mouth_closed.png"),
        )

    image eyes_sad_3_oa:
        "sprites/one_arm/sad/sad_3_eyes_open.png"
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

        "sprites/one_arm/sad/sad_3_eyes_half.png"
        .1
        "sprites/one_arm/sad/sad_eyes_closed.png"
        .2
        "sprites/one_arm/sad/sad_3_eyes_half.png"
        .1
        repeat

    image mouth_neutral_oa:
        "sprites/one_arm/neutral/neutral_mouth_half.png"
        .1
        "sprites/one_arm/neutral/neutral_mouth_full.png"
        .1
        repeat      
    
    
###########################################SMILE###########################################    
    
    
    image gg_smile_1_oa = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/one_arm/smile/smile_1.png",
        (0, 0), "eyes_smile_1_oa",
        (0, 0), WhileSpeaking("gg", "mouth_smile_oa", "sprites/one_arm/smile/smile_mouth_closed.png"),
        )

    image eyes_smile_1_oa:
        "sprites/one_arm/smile/smile_1_eyes_open.png"
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

        "sprites/one_arm/smile/smile_1_eyes_half.png"
        .1
        "sprites/one_arm/smile/smile_eyes_closed.png"
        .2
        "sprites/one_arm/smile/smile_1_eyes_half.png"
        .1
        repeat

    image mouth_smile_oa:
        "sprites/one_arm/smile/smile_mouth_half.png"
        .1
        "sprites/one_arm/smile/smile_mouth_full.png"
        .1
        repeat
        
        
        
        
        
    image gg_smile_2_oa = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/one_arm/smile/smile_2.png",
        (0, 0), "eyes_smile_2_oa",
        (0, 0), WhileSpeaking("gg", "mouth_smile_oa", "sprites/one_arm/smile/smile_mouth_closed.png"),
        )

    image eyes_smile_2_oa:
        "sprites/one_arm/smile/smile_2_eyes_open.png"
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

        "sprites/one_arm/smile/smile_2_eyes_half.png"
        .1
        "sprites/one_arm/smile/smile_eyes_closed.png"
        .2
        "sprites/one_arm/smile/smile_2_eyes_half.png"
        .1
        repeat

    image mouth_smile_oa:
        "sprites/one_arm/smile/smile_mouth_half.png"
        .1
        "sprites/one_arm/smile/smile_mouth_full.png"
        .1
        repeat  
        
    
    
    
        
    image gg_smile_3_oa = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/one_arm/smile/smile_3.png",
        (0, 0), "eyes_smile_3_oa",
        (0, 0), WhileSpeaking("gg", "mouth_smile_oa", "sprites/one_arm/smile/smile_mouth_closed.png"),
        )

    image eyes_smile_3_oa:
        "sprites/one_arm/smile/smile_3_eyes_open.png"
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

        "sprites/one_arm/smile/smile_3_eyes_half.png"
        .1
        "sprites/one_arm/smile/smile_eyes_closed.png"
        .2
        "sprites/one_arm/smile/smile_3_eyes_half.png"
        .1
        repeat

    image mouth_smile_oa:
        "sprites/one_arm/smile/smile_mouth_half.png"
        .1
        "sprites/one_arm/smile/smile_mouth_full.png"
        .1
        repeat      
    
  
  
  
###########################################CONF###########################################    
    
    
    image gg_conf_1_oa = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/one_arm/conf/conf_1.png",
        (0, 0), "eyes_conf_1_oa",
        (0, 0), WhileSpeaking("gg", "mouth_conf_oa", "sprites/one_arm/conf/conf_mouth_closed.png"),
        )

    image eyes_conf_1_oa:
        "sprites/one_arm/conf/conf_1_eyes_open.png"
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

        "sprites/one_arm/conf/conf_1_eyes_half.png"
        .1
        "sprites/one_arm/conf/conf_eyes_closed.png"
        .2
        "sprites/one_arm/conf/conf_1_eyes_half.png"
        .1
        repeat

    image mouth_conf_oa:
        "sprites/one_arm/conf/conf_mouth_half.png"
        .1
        "sprites/one_arm/conf/conf_mouth_full.png"
        .1
        repeat
        
        
        
        
        
    image gg_conf_2_oa = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/one_arm/conf/conf_2.png",
        (0, 0), "eyes_conf_2_oa",
        (0, 0), WhileSpeaking("gg", "mouth_conf_oa", "sprites/one_arm/conf/conf_mouth_closed.png"),
        )

    image eyes_conf_2_oa:
        "sprites/one_arm/conf/conf_2_eyes_open.png"
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

        "sprites/one_arm/conf/conf_2_eyes_half.png"
        .1
        "sprites/one_arm/conf/conf_eyes_closed.png"
        .2
        "sprites/one_arm/conf/conf_2_eyes_half.png"
        .1
        repeat

    image mouth_conf_oa:
        "sprites/one_arm/conf/conf_mouth_half.png"
        .1
        "sprites/one_arm/conf/conf_mouth_full.png"
        .1
        repeat  
        
    
    
    image gg_conf_3_oa = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/one_arm/conf/conf_3.png",
        (0, 0), "eyes_conf_3_oa",
        (0, 0), WhileSpeaking("gg", "mouth_conf_oa", "sprites/one_arm/conf/conf_mouth_closed.png"),
        )

    image eyes_conf_3_oa:
        "sprites/one_arm/conf/conf_3_eyes_open.png"
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

        "sprites/one_arm/conf/conf_3_eyes_half.png"
        .1
        "sprites/one_arm/conf/conf_eyes_closed.png"
        .2
        "sprites/one_arm/conf/conf_3_eyes_half.png"
        .1
        repeat

    image mouth_conf_oa:
        "sprites/one_arm/conf/conf_mouth_half.png"
        .1
        "sprites/one_arm/conf/conf_mouth_full.png"
        .1
        repeat
    
    
        
    image gg_conf_4_oa = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/one_arm/conf/conf_4.png",
        (0, 0), WhileSpeaking("gg", "mouth_conf_oa", "sprites/one_arm/conf/conf_mouth_closed.png"),
        )

    image mouth_conf_oa:
        "sprites/one_arm/conf/conf_mouth_half.png"
        .1
        "sprites/one_arm/conf/conf_mouth_full.png"
        .1
        repeat        
  
  
  

###########################################NERV###########################################    
    
    
    image gg_nerv_1_oa = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/one_arm/nerv/nerv_1.png",
        (0, 0), "eyes_nerv_1_oa",
        (0, 0), WhileSpeaking("gg", "mouth_nerv_oa", "sprites/one_arm/nerv/nerv_mouth_closed.png"),
        )

    image eyes_nerv_1_oa:
        "sprites/one_arm/nerv/nerv_1_eyes_open.png"
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

        "sprites/one_arm/nerv/nerv_1_eyes_half.png"
        .1
        "sprites/one_arm/nerv/nerv_eyes_closed.png"
        .2
        "sprites/one_arm/nerv/nerv_1_eyes_half.png"
        .1
        repeat

    image mouth_nerv_oa:
        "sprites/one_arm/nerv/nerv_mouth_closed.png"
        .1
        "sprites/one_arm/nerv/nerv_mouth_full.png"
        .1
        repeat
        
    
    image gg_nerv_2_oa = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/one_arm/nerv/nerv_2.png",
        (0, 0), "eyes_nerv_2_oa",
        (0, 0), WhileSpeaking("gg", "mouth_nerv_oa", "sprites/one_arm/nerv/nerv_mouth_closed.png"),
        )

    image eyes_nerv_2_oa:
        "sprites/one_arm/nerv/nerv_2_eyes_open.png"
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

        "sprites/one_arm/nerv/nerv_2_eyes_half.png"
        .1
        "sprites/one_arm/nerv/nerv_eyes_closed.png"
        .2
        "sprites/one_arm/nerv/nerv_2_eyes_half.png"
        .1
        repeat

    image mouth_nerv_oa:
        "sprites/one_arm/nerv/nerv_mouth_closed.png"
        .1
        "sprites/one_arm/nerv/nerv_mouth_full.png"
        .1
        repeat
    
     
     
    image gg_nerv_3_oa = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/one_arm/nerv/nerv_3.png",
        (0, 0), WhileSpeaking("gg", "mouth_nerv_oa", "sprites/one_arm/nerv/nerv_mouth_closed.png"),
        )

    image mouth_nerv_oa:
        "sprites/one_arm/nerv/nerv_mouth_closed.png"
        .1
        "sprites/one_arm/nerv/nerv_mouth_full.png"
        .1
        repeat     