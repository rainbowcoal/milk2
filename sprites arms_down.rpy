

###########################################NEUTRAL###########################################



init:
    image gg_neutral_1_ad = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_down/neutral/neutral_1.png",
        (0, 0), "eyes_neutral_1_ad",
        (0, 0), WhileSpeaking("gg", "mouth_neutral_ad", "sprites/arms_down/neutral/neutral_mouth_closed.png"),
        )

    image eyes_neutral_1_ad:
        "sprites/arms_down/neutral/neutral_1_eyes_open.png"
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

        "sprites/arms_down/neutral/neutral_1_eyes_half.png"
        .1
        "sprites/arms_down/neutral/neutral_eyes_closed.png"
        .2
        "sprites/arms_down/neutral/neutral_1_eyes_half.png"
        .1
        repeat

    image mouth_neutral_ad:
        "sprites/arms_down/neutral/neutral_mouth_half.png"
        .1
        "sprites/arms_down/neutral/neutral_mouth_full.png"
        .1
        repeat
        
        
        
        
        
    image gg_neutral_2_ad = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_down/neutral/neutral_2.png",
        (0, 0), "eyes_neutral_2_ad",
        (0, 0), WhileSpeaking("gg", "mouth_neutral_ad", "sprites/arms_down/neutral/neutral_mouth_closed.png"),
        )

    image eyes_neutral_2_ad:
        "sprites/arms_down/neutral/neutral_2_eyes_open.png"
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

        "sprites/arms_down/neutral/neutral_2_eyes_half.png"
        .1
        "sprites/arms_down/neutral/neutral_eyes_closed.png"
        .2
        "sprites/arms_down/neutral/neutral_2_eyes_half.png"
        .1
        repeat

    image mouth_neutral_ad:
        "sprites/arms_down/neutral/neutral_mouth_half.png"
        .1
        "sprites/arms_down/neutral/neutral_mouth_full.png"
        .1
        repeat 
        
    
    
    
        
    image gg_neutral_3_ad = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_down/neutral/neutral_1.png",
        (0, 0), "eyes_neutral_3_ad",
        (0, 0), WhileSpeaking("gg", "mouth_neutral_ad", "sprites/arms_down/neutral/neutral_mouth_closed.png"),
        )

    image eyes_neutral_3_ad:
        "sprites/arms_down/neutral/neutral_3_eyes_open.png"
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

        "sprites/arms_down/neutral/neutral_3_eyes_half.png"
        .1
        "sprites/arms_down/neutral/neutral_eyes_closed.png"
        .2
        "sprites/arms_down/neutral/neutral_3_eyes_half.png"
        .1
        repeat

    image mouth_neutral_ad:
        "sprites/arms_down/neutral/neutral_mouth_half.png"
        .1
        "sprites/arms_down/neutral/neutral_mouth_full.png"
        .1
        repeat 
        
        
    
    image gg_neutral_4_ad = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_down/neutral/neutral_4.png",
        (0, 0), WhileSpeaking("gg", "mouth_neutral_ad", "sprites/arms_down/neutral/neutral_mouth_closed.png"),
        )

    image mouth_neutral_ad:
        "sprites/arms_down/neutral/neutral_mouth_half.png"
        .1
        "sprites/arms_down/neutral/neutral_mouth_full.png"
        .1
        repeat
    
    
    

    
    
    
    
###########################################MAD###########################################    
    
    
    image gg_mad_1_ad = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_down/mad/mad_1.png",
        (0, 0), "eyes_mad_1_ad",
        (0, 0), WhileSpeaking("gg", "mouth_mad_ad", "sprites/arms_down/mad/mad_mouth_closed.png"),
        )

    image eyes_mad_1_ad:
        "sprites/arms_down/mad/mad_1_eyes_open.png"
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

        "sprites/arms_down/mad/mad_1_eyes_half.png"
        .1
        "sprites/arms_down/mad/mad_eyes_closed.png"
        .2
        "sprites/arms_down/mad/mad_1_eyes_half.png"
        .1
        repeat

    image mouth_mad_ad:
        "sprites/arms_down/mad/mad_mouth_half.png"
        .1
        "sprites/arms_down/mad/mad_mouth_full.png"
        .1
        repeat
        
        
        
        
        
    image gg_mad_2_ad = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_down/mad/mad_2.png",
        (0, 0), "eyes_mad_2_ad",
        (0, 0), WhileSpeaking("gg", "mouth_mad_ad", "sprites/arms_down/mad/mad_mouth_closed.png"),
        )

    image eyes_mad_2_ad:
        "sprites/arms_down/mad/mad_2_eyes_open.png"
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

        "sprites/arms_down/mad/mad_2_eyes_half.png"
        .1
        "sprites/arms_down/mad/mad_eyes_closed.png"
        .2
        "sprites/arms_down/mad/mad_2_eyes_half.png"
        .1
        repeat

    image mouth_mad_ad:
        "sprites/arms_down/mad/mad_mouth_half.png"
        .1
        "sprites/arms_down/mad/mad_mouth_full.png"
        .1
        repeat  
        
    
    
    image gg_mad_3_ad = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_down/mad/mad_1.png",
        (0, 0), "eyes_mad_3_ad",
        (0, 0), WhileSpeaking("gg", "mouth_mad_ad", "sprites/arms_down/mad/mad_mouth_closed.png"),
        )

    image eyes_mad_3_ad:
        "sprites/arms_down/mad/mad_3_eyes_open.png"
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

        "sprites/arms_down/mad/mad_3_eyes_half.png"
        .1
        "sprites/arms_down/mad/mad_eyes_closed.png"
        .2
        "sprites/arms_down/mad/mad_3_eyes_half.png"
        .1
        repeat

    image mouth_mad_ad:
        "sprites/arms_down/mad/mad_mouth_half.png"
        .1
        "sprites/arms_down/mad/mad_mouth_full.png"
        .1
        repeat
        
        
        
    image gg_mad_4_ad = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_down/mad/mad_4.png",
        (0, 0), WhileSpeaking("gg", "mouth_mad_ad", "sprites/arms_down/mad/mad_mouth_closed.png"),
        )

    image mouth_mad_ad:
        "sprites/arms_down/mad/mad_mouth_half.png"
        .1
        "sprites/arms_down/mad/mad_mouth_full.png"
        .1
        repeat  
    

    
###########################################SAD###########################################    
    
    
    image gg_sad_1_ad = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_down/sad/sad_1.png",
        (0, 0), "eyes_sad_1_ad",
        (0, 0), WhileSpeaking("gg", "mouth_neutral_ad", "sprites/arms_down/sad/sad_mouth_closed.png"),
        )

    image eyes_sad_1_ad:
        "sprites/arms_down/sad/sad_1_eyes_open.png"
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

        "sprites/arms_down/sad/sad_1_eyes_half.png"
        .1
        "sprites/arms_down/sad/sad_eyes_closed.png"
        .2
        "sprites/arms_down/sad/sad_1_eyes_half.png"
        .1
        repeat

    image mouth_neutral_ad:
        "sprites/arms_down/neutral/neutral_mouth_half.png"
        .1
        "sprites/arms_down/neutral/neutral_mouth_full.png"
        .1
        repeat
        
        
        
        
        
    image gg_sad_2_ad = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_down/sad/sad_2.png",
        (0, 0), "eyes_sad_2_ad",
        (0, 0), WhileSpeaking("gg", "mouth_neutral_ad", "sprites/arms_down/sad/sad_mouth_closed.png"),
        )

    image eyes_sad_2_ad:
        "sprites/arms_down/sad/sad_2_eyes_open.png"
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

        "sprites/arms_down/sad/sad_2_eyes_half.png"
        .1
        "sprites/arms_down/sad/sad_eyes_closed.png"
        .2
        "sprites/arms_down/sad/sad_2_eyes_half.png"
        .1
        repeat

    image mouth_neutral_ad:
        "sprites/arms_down/neutral/neutral_mouth_half.png"
        .1
        "sprites/arms_down/neutral/neutral_mouth_full.png"
        .1
        repeat  
        
    
    
    
        
    image gg_sad_3_ad = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_down/sad/sad_3.png",
        (0, 0), "eyes_sad_3_ad",
        (0, 0), WhileSpeaking("gg", "mouth_neutral_ad", "sprites/arms_down/sad/sad_mouth_closed.png"),
        )

    image eyes_sad_3_ad:
        "sprites/arms_down/sad/sad_3_eyes_open.png"
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

        "sprites/arms_down/sad/sad_3_eyes_half.png"
        .1
        "sprites/arms_down/sad/sad_eyes_closed.png"
        .2
        "sprites/arms_down/sad/sad_3_eyes_half.png"
        .1
        repeat

    image mouth_neutral_ad:
        "sprites/arms_down/neutral/neutral_mouth_half.png"
        .1
        "sprites/arms_down/neutral/neutral_mouth_full.png"
        .1
        repeat      
    
    
###########################################SMILE###########################################    
    
    
    image gg_smile_1_ad = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_down/smile/smile_1.png",
        (0, 0), "eyes_smile_1_ad",
        (0, 0), WhileSpeaking("gg", "mouth_smile_ad", "sprites/arms_down/smile/smile_mouth_closed.png"),
        )

    image eyes_smile_1_ad:
        "sprites/arms_down/smile/smile_1_eyes_open.png"
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

        "sprites/arms_down/smile/smile_1_eyes_half.png"
        .1
        "sprites/arms_down/smile/smile_eyes_closed.png"
        .2
        "sprites/arms_down/smile/smile_1_eyes_half.png"
        .1
        repeat

    image mouth_smile_ad:
        "sprites/arms_down/smile/smile_mouth_half.png"
        .1
        "sprites/arms_down/smile/smile_mouth_full.png"
        .1
        repeat
        
        
        
        
        
    image gg_smile_2_ad = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_down/smile/smile_2.png",
        (0, 0), "eyes_smile_2_ad",
        (0, 0), WhileSpeaking("gg", "mouth_smile_ad", "sprites/arms_down/smile/smile_mouth_closed.png"),
        )

    image eyes_smile_2_ad:
        "sprites/arms_down/smile/smile_2_eyes_open.png"
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

        "sprites/arms_down/smile/smile_2_eyes_half.png"
        .1
        "sprites/arms_down/smile/smile_eyes_closed.png"
        .2
        "sprites/arms_down/smile/smile_2_eyes_half.png"
        .1
        repeat

    image mouth_smile_ad:
        "sprites/arms_down/smile/smile_mouth_half.png"
        .1
        "sprites/arms_down/smile/smile_mouth_full.png"
        .1
        repeat  
        
    
    
    
        
    image gg_smile_3_ad = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_down/smile/smile_3.png",
        (0, 0), "eyes_smile_3_ad",
        (0, 0), WhileSpeaking("gg", "mouth_smile_ad", "sprites/arms_down/smile/smile_mouth_closed.png"),
        )

    image eyes_smile_3_ad:
        "sprites/arms_down/smile/smile_3_eyes_open.png"
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

        "sprites/arms_down/smile/smile_3_eyes_half.png"
        .1
        "sprites/arms_down/smile/smile_eyes_closed.png"
        .2
        "sprites/arms_down/smile/smile_3_eyes_half.png"
        .1
        repeat

    image mouth_smile_ad:
        "sprites/arms_down/smile/smile_mouth_half.png"
        .1
        "sprites/arms_down/smile/smile_mouth_full.png"
        .1
        repeat      
    
  
  
  
###########################################CONF###########################################    
    
    
    image gg_conf_1_ad = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_down/conf/conf_1.png",
        (0, 0), "eyes_conf_1_ad",
        (0, 0), WhileSpeaking("gg", "mouth_conf_ad", "sprites/arms_down/conf/conf_mouth_closed.png"),
        )

    image eyes_conf_1_ad:
        "sprites/arms_down/conf/conf_1_eyes_open.png"
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

        "sprites/arms_down/conf/conf_1_eyes_half.png"
        .1
        "sprites/arms_down/conf/conf_eyes_closed.png"
        .2
        "sprites/arms_down/conf/conf_1_eyes_half.png"
        .1
        repeat

    image mouth_conf_ad:
        "sprites/arms_down/conf/conf_mouth_half.png"
        .1
        "sprites/arms_down/conf/conf_mouth_full.png"
        .1
        repeat
        
        
        
        
        
    image gg_conf_2_ad = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_down/conf/conf_2.png",
        (0, 0), "eyes_conf_2_ad",
        (0, 0), WhileSpeaking("gg", "mouth_conf_ad", "sprites/arms_down/conf/conf_mouth_closed.png"),
        )

    image eyes_conf_2_ad:
        "sprites/arms_down/conf/conf_2_eyes_open.png"
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

        "sprites/arms_down/conf/conf_2_eyes_half.png"
        .1
        "sprites/arms_down/conf/conf_eyes_closed.png"
        .2
        "sprites/arms_down/conf/conf_2_eyes_half.png"
        .1
        repeat

    image mouth_conf_ad:
        "sprites/arms_down/conf/conf_mouth_half.png"
        .1
        "sprites/arms_down/conf/conf_mouth_full.png"
        .1
        repeat  
        
    
    image gg_conf_3_ad = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_down/conf/conf_3.png",
        (0, 0), "eyes_conf_3_ad",
        (0, 0), WhileSpeaking("gg", "mouth_conf_ad", "sprites/arms_down/conf/conf_mouth_closed.png"),
        )

    image eyes_conf_3_ad:
        "sprites/arms_down/conf/conf_3_eyes_open.png"
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

        "sprites/arms_down/conf/conf_3_eyes_half.png"
        .1
        "sprites/arms_down/conf/conf_eyes_closed.png"
        .2
        "sprites/arms_down/conf/conf_3_eyes_half.png"
        .1
        repeat

    image mouth_conf_ad:
        "sprites/arms_down/conf/conf_mouth_half.png"
        .1
        "sprites/arms_down/conf/conf_mouth_full.png"
        .1
        repeat
    
    
        
    image gg_conf_4_ad = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_down/conf/conf_4.png",
        (0, 0), WhileSpeaking("gg", "mouth_conf_ad", "sprites/arms_down/conf/conf_mouth_closed.png"),
        )

    image mouth_conf_ad:
        "sprites/arms_down/conf/conf_mouth_half.png"
        .1
        "sprites/arms_down/conf/conf_mouth_full.png"
        .1
        repeat        
  
  
  

###########################################NERV###########################################    
    
    
    image gg_nerv_1_ad = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_down/nerv/nerv_1.png",
        (0, 0), "eyes_nerv_1_ad",
        (0, 0), WhileSpeaking("gg", "mouth_nerv_ad", "sprites/arms_down/nerv/nerv_mouth_closed.png"),
        )

    image eyes_nerv_1_ad:
        "sprites/arms_down/nerv/nerv_1_eyes_open.png"
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

        "sprites/arms_down/nerv/nerv_1_eyes_half.png"
        .1
        "sprites/arms_down/nerv/nerv_eyes_closed.png"
        .2
        "sprites/arms_down/nerv/nerv_1_eyes_half.png"
        .1
        repeat

    image mouth_nerv_ad:
        "sprites/arms_down/nerv/nerv_mouth_closed.png"
        .1
        "sprites/arms_down/nerv/nerv_mouth_full.png"
        .1
        repeat
        
    
    image gg_nerv_2_ad = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_down/nerv/nerv_2.png",
        (0, 0), "eyes_nerv_2_ad",
        (0, 0), WhileSpeaking("gg", "mouth_nerv_ad", "sprites/arms_down/nerv/nerv_mouth_closed.png"),
        )

    image eyes_nerv_2_ad:
        "sprites/arms_down/nerv/nerv_2_eyes_open.png"
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

        "sprites/arms_down/nerv/nerv_2_eyes_half.png"
        .1
        "sprites/arms_down/nerv/nerv_eyes_closed.png"
        .2
        "sprites/arms_down/nerv/nerv_2_eyes_half.png"
        .1
        repeat

    image mouth_nerv_ad:
        "sprites/arms_down/nerv/nerv_mouth_closed.png"
        .1
        "sprites/arms_down/nerv/nerv_mouth_full.png"
        .1
        repeat
    
     
     
    image gg_nerv_3_ad = LiveComposite(
        (1959, 1027),
        (0, 0), "sprites/arms_down/nerv/nerv_3.png",
        (0, 0), WhileSpeaking("gg", "mouth_nerv_ad", "sprites/arms_down/nerv/nerv_mouth_closed.png"),
        )

    image mouth_nerv_ad:
        "sprites/arms_down/nerv/nerv_mouth_closed.png"
        .1
        "sprites/arms_down/nerv/nerv_mouth_full.png"
        .1
        repeat     
  
  
  
  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
        
        