#CHARACTERS
define u = Character("[name]", color="#000000")
define b = Character("Betty", color="#FF00FF", what_font="fonts/segoesc.ttf")
define s = Character("Sans", color="#0000FF", what_font="fonts/comic.ttf")
define n = Character("Norf", color="#FF7F27", what_font="fonts/CLARE___.TTF")
define j = Character("Jake Fucking Paul", color="#333333", what_font="fonts/impact.ttf")
define sh = Character("Shane", color="#123456", what_font="fonts/Itali___.ttf")
define f = Character("Ford", color="#653909", what_font="fonts/Pacifico-Regular.ttf")
define fc = Character("Ford", color="#653909", what_font="fonts/Bill_s_Cipher.ttf")
define bd = Character('Belle "Bathwater" Delphine', color="#547466", what_font="fonts/ARLRDBD.TTF")
define su = Character("Steak-Umm", color="983027", what_font="fonts/Autumn__.ttf")
define qe = Character('Queen Elizabeth II', color="#547466", what_font="fonts/ARLRDBD.TTF")
define hp = Character("Hot Pockets", color="983027", what_font="fonts/Autumn__.ttf")
define mc = Character("McCoy", color="003100", what_font="fonts/courbd.ttf")
define mu = Character("Mr. Undertale", color="AA0044", what_font="fonts/FingerPaint-Regular.ttf")
define w = Character("Spouse", color="FF00FF")
define q = Character("???", color="#000000")

#PLOTPOINTVARIABLES
default murderer = False
default murderer2 = False
default weather = False
default politics = False
default sex = False
default sports = False
default uwuwater = False
default atFords = False

#UNLOCKS
default relUnlock = False
default persistent.endUnlock = False

#RELATIONSHIPVARIABLES
default bp = 90
default sp = 65
default np = 50
default jp = 50
default shp = 50
default fp = 50
default bdp = 50
default sup = 50

#POSITIONS
transform veryleft:
    xalign -0.2
    yalign 1.0

transform left:
    xalign 0
    yalign 1.0

transform littleft:
    xalign 0.35
    yalign 1.0

transform slightleft:
    xalign 0.25
    yalign 1.0

transform middle:
    xalign 0.5
    yalign 1.0

transform slightright:
    xalign 0.75
    yalign 1.0

transform littleright:
    xalign 0.85
    yalign 1.0

transform right:
    xalign 1.0
    yalign 1.0

transform veryright:
    xalign 1.2
    yalign 1.0

transform offright:
    xalign 3.0
    yalign 1.0

transform offleft:
    xaligh -3.0
    yalign 1.0
    
#MAINMENUIMAGES
image menu_logo:
    "gui/menu_logo.png"
    logotransform

image menu_particles:
    0.77
    xpos 500
    ypos 104
    ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=20, particleTime=2.0, particleXSpeed=6, particleYSpeed=4).sm
    particle_fadeout

image characters_r3:
    "gui/characters_r3.png"
    char3transform

image characters_r2:
    "gui/characters_r2.png"
    char2transform

image characters_r1:
    "gui/characters_r1.png"
    char1transform

image version:
    "gui/version.png"
    versiontransform

transform logotransform:
    xoffset 325 yoffset -200
    easein_bounce 2.5 xoffset 325 yoffset 100

transform char3transform:
    xoffset 615 yoffset 800
    easein 2.75 xoffset 615 yoffset 425

transform char2transform:
    xoffset 620 yoffset 800
    easein 3.25 xoffset 620 yoffset 255 

transform char1transform:
    xoffset 625 yoffset 800
    easein 3.75 xoffset 625 yoffset 140

transform versiontransform:
    xoffset 300 yoffset 625 alpha 0
    easein 3.0 alpha 1.0

transform particle_fadeout:
    easeout 1.5 alpha 0

init python:
    import math
    import random
    class ParticleBurst(object):
        def __init__(self, theDisplayable, explodeTime=0, numParticles=20, particleTime = 0.500, particleXSpeed = 3, particleYSpeed = 5):
            self.sm = SpriteManager(update=self.update)
            
            self.stars = [ ]
            self.displayable = theDisplayable
            self.explodeTime = explodeTime
            self.numParticles = numParticles
            self.particleTime = particleTime
            self.particleXSpeed = particleXSpeed
            self.particleYSpeed = particleYSpeed
            self.gravity = 3
            self.timePassed = 0
            
            for i in range(self.numParticles):
                self.add(self.displayable, 1)
        
        def add(self, d, speed):
            s = self.sm.create(d)
            ySpeed = (random.random() - 0.5) * self.particleYSpeed
            xSpeed = (random.random() - 0.5) * self.particleXSpeed
            s.x += xSpeed * 40
            s.y += ySpeed * 40
            pTime = self.particleTime
            self.stars.append((s, ySpeed, xSpeed, pTime))
        
        def update(self, st):
            sindex=0
            for s, ySpeed, xSpeed, particleTime in self.stars:
                if (st < particleTime):
                    s.x += xSpeed
                    s.y += (ySpeed + (self.gravity * st))
                else:
                    s.destroy()
                    self.stars.pop(sindex)
                sindex += 1
            return 0

#DISCORDRPC
init -20 python:
    import discord_rpc
    import time

    def readyCallback(current_user):
        print('Our user: {}'.format(current_user))

    def disconnectedCallback(codeno, codemsg):
        print('Disconnected from Discord rich presence RPC. Code {}: {}'.format(
            codeno, codemsg
        ))

    def errorCallback(errno, errmsg):
        print('An error occurred! Error {}: {}'.format(
            errno, errmsg
        ))

init -19 python:
    def rpc_initialize():
            callbacks = {
                'ready': readyCallback,
                'disconnected': disconnectedCallback,
                'error': errorCallback,
            }
            discord_rpc.initialize('604320116100038686', callbacks=callbacks, log=False)
            start = time.time()
            discord_rpc.update_connection()
            discord_rpc.run_callbacks()
            discord_rpc.update_presence(
                **{
                    'large_image_key': 'main',
                    'start_timestamp': start
                }
            )

            discord_rpc.update_connection()
            discord_rpc.run_callbacks()

#SPLASHSCREEN
label splashscreen:

    #RPCSTART
    python:
        # Note: 'event_name': callback
        callbacks = {
            'ready': readyCallback,
            'disconnected': disconnectedCallback,
            'error': errorCallback,
        }
        discord_rpc.initialize('604320116100038686', callbacks=callbacks, log=False)
        start = time.time()
        print(start)
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
        discord_rpc.update_presence(
            **{
                'details': 'Bad Times of Romance',
                'start_timestamp': start,
                'large_image_key': 'main'
            }
        )
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()

    play music "music/placeholder1.mp3"
    scene bg black
    with Pause(2)

    show text "{size=+50}{font=fonts/Comfortaa-Bold.ttf}{color=#FF0055}Buddy{/color}{/font}{/size}\n{size=+10}(regretfully) presents...{/size}" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(2)

    $ rpc_initialize()

    return

#CHAPTERONE
label start:

    scene bg black
    with fade

    python:
        name = renpy.input("I can't fucking remember my name.")
        name = name.strip()

        if not name:
             name = "MISSINGNO"



    stop music fadeout 1.0

    scene bg black
    with Pause(2)

    show text "{size=+10}Chapter 1{/size}" with dissolve
    with Pause(3)

    hide text with dissolve
    with Pause(2)

    play music "music/placeholder2.mp3"
    scene bg exschool

    "Well, it's the first day of school, and you know what that means."
    "Lots of dumb ugly people trying to ask me out on a date, when I do {b}not{/b} want to go on any."

    show betty angry
    with dissolve

    b "What did you say about me, [name]?"

    u "Oh sorry, Betty."

    "Betty is one of the ugliest kids in school, so of course she has a huge crush on me of all people."
    "She can also read minds."

    b "You better be sorry."

    show betty happy

    b "Anyway, how are you?"

    "I really didn't wanna get stuck talking to her for too long, so I came up with the shortest answer possible."

    u "Fine."

    show betty angry

    b "You're so rude!"

    u "What did I do?"

    b "I read your mind! You don't wanna even be near me!"

    show betty sad

    "She wasn't wrong..."

    b "{b}Fine!{/b} I guess I'll be off then."

    hide betty
    with move

    "Ah, peace and quiet."

    scene bg hallway
    with fade

    "The hallway was filled with new people that I have never seen before..."
    "...except for one familiar face."

    show sans happy
    with dissolve

    q "Hey, what's up, [name]!"

    "Sans was my ex lover."

    u "Hey Sans..."

    "I don't like Sans at all anymore. He had sex with my mother when I was a child and forced me to watch. He is actually 62 years old now."
    "The reason he's even still in this school is because he sucks."

    s "I heard you were flirting with Betty earlier!"

    u "No I was not!"

    s "Well that's what she's telling everybody."

    "I could feel my anger building up inside of me."

    u "{b}BETTY{/b}"

    show sans sad at slightright
    with move

    show betty happy at slightleft
    with dissolve

    b "Hi! I heard you call on me!"

    menu:
        "I feel the sudden urge to kill Betty..."

        "Kill her":
            jump kill

        "Spare her":
            jump spare

label kill:

    $ murderer = True
    $ murderer2 = True

    stop music fadeout 1.0
    scene bg black

    "I did what had to be done."
    "Betty was dead."

    $ bp = 0

    jump nextday

label spare:

    "I decided to spare Betty... for now..."

    show betty angry

    b "I heard that!"

    $ bp -= 5

    jump nextday

#CHAPTERTWO
label nextday:

    scene bg black
    with Pause(2)

    show text "{size=+10}Chapter 2{/size}" with dissolve
    with Pause(3)

    hide text with dissolve
    with Pause(2)

    play music "music/placeholder3.mp3"
    scene bg exschool
    with fade

    "I went to school the next day and was greeted by the principal of the school, Mr. Norf."

    if murderer:

        show norf angry
        with dissolve

        n "{b}[name]!{/b}"

        n "Why did you kill Betty yesterday!?"

        $ np -= 5

        u "She was being annoying."

        show norf sad

        n "Oh."

        show norf happy

        n "Fair enough!"

        $ np += 3

    show norf happy

    n "I hope you have a beautiful day!"

    scene bg hallway
    with fade

    "I got inside the school for the second day of hell and guess who was already at my locker?"

    show sans happy
    with dissolve

    s "Hey dude!"

    jump continued

label montinued:

    s "So about what happened yesterday..."

    u "Oh, no need to thank me!"

    show sans sad

    s "I wasn't going to thank you..."

    "..."

    s "Betty was my girlfriend..."

    $ sp -= 20

    "..."

    "I don't know what to say."
    "I'm surprised I didn't know they were dating earlier... they were perfect for each other now that I think about it..."

    u "I..."
    u "I'm sorry you had to put up with her..."

    s "You know what?"

    u "What?"

    show sans happy

    s "I think I know what to do!"

    u "Yeah?"

    s "Yeah."

    show sans angry

    s "I'm gonna give you a taste of your own medicine."
    s "{size=+10}You're gonna have a bad time...{/size}"

    scene bg black
    with fade

    "I need to run as fast as I can"

    scene bg outside1
    with fade

    "I need to find somewhere safe."

    scene bg outside2
    with dissolve

    "It feels like I'm getting nowhere..."

    scene bg outside3

    "Wait a minute... that's because I haven't moved... the world is just zooming in..."
    "Maybe I should turn around..."

    scene bg exschool
    with dissolve

    show sans vangry
    with dissolve

    s "You can't hide from me..."

    "I had two options to get away from him..."

    menu:

        "I could..."

        "Tell on Sans":
            jump tell

        "Keep running":
            jump death1

label tell:

    u "Mr. Norf!!"

    show sans sad at slightright
    with move

    show norf happy at slightleft
    with move

    n "What is it?"

    u "Sans is trying to kill me!"

    show norf angry

    n "Sans! That's not nice!"

    s "But he killed my girlfriend!"

    n "But she was annoying!"
    n "Both of you, inside, now!"

    scene bg hallway
    with fade

    $ murderer = False

    jump continued

label death1:

    scene bg black

    "I can't outrun Sans anymore..."
    "Oh no..."
    "I'm fucking dead now."
    "rip"

    return

label continued:

    if murderer:

        jump montinued

    show sans sad
    with dissolve

    s "..."
    s "I better go..."

    hide sans
    with dissolve

    if murderer2:
        jump good

    "I wonder what that was about..."

    jump day3

label good:

    "Good riddance..."

    jump day3

label day3:

    scene bg exschool
    with fade

    "It's the third day now, and it seems like there are new people at the school."
    "I guess I should probably be polite and say hi..."

    show jake happy at slightleft
    with dissolve

    show shane happy at slightright
    with dissolve

    sh "Hi I'm Shane and this is Jake and he is a sociopath totally true totally not lying. Give me views."

    j "i am a sociopath nice to meet you."
    j "it's everyday bro with that disney channel flow 5 mil on youtube in 6 months never done before."

    u "...what?"

    show shane sad
    show jake sad

    sh "Cmon Jake, let's go. We are obviously not wanted here."

    u "Wait!"

    "They stopped and looked at me confused."

    u "Do you guys want me to show you around the school?"

    show jake happy

    j "sure i guess."

    u "Alright, come follow me!"

    if murderer2:
        jump showingschoolmurder

    jump showingschool

label showingschoolmurder:

    scene bg hallway
    with fade

    show shane happy at slightright
    with dissolve

    show jake happy at slightleft
    with dissolve

    "I've decided to be the good guy here and show them around the school, so that they aren't as lost as me my first time here."

    u "This here is the hallway, where you can socialize for about 2 minutes before being trapped in hell for another 45!"

    j "sounds dope bruh."

    show shane happy at middle
    with move

    show jake happy at left
    with move

    show sans sad at right
    with dissolve

    "Just then Sans showed up and I was suddenly super nervous, considering what had happened yesterday..."

    s "Um, what are you doing here, [name]?"

    u "Giving Jake and Shane a tour of our school."

    s "That was my job..."

    "Well now I'm very confused."

    u "What... what do you mean?"

    show sans angry

    s "Mr. Norf told me yesterday after you had already left that I was supposed to be giving the tour."

    u "Welp, sorry dude. You were too late."

    s "First you kill my girlfriend."

    show shane sad

    sh "Is everything alright?"

    show sans vangry

    s "{b}Then you steal my job...{/b}"

    "This doesn't seem very good..."

    s "{b}What are you gonna do to me next??{/b}"

    "I have to defend myself..."

    u "Well, to be fair, you did bang my mother right in front of me when I was a child."
    u "In fact, why were you dating Betty anyway? You're 62 years old!"

    show jake sad

    j "dude should we leave?"

    s "{b}I was desperate okay??{/b}"

    show jake sad at left
    show shane sad at slightleft
    show sans sad at middle
    with move

    show norf angry at right
    with dissolve

    n "{b}WHAT IS GOING ON HERE???{/b}"

    u "Sans is being a dick again."

    n "Is this true Sans?"

    show sans angry

    s "NO!"

    j "i am a witness and it is very true."

    s "Hey!"

    n "That's it Sans! I didn't want to have to do this... but..."

    show sans sad

    s "But what?"

    n "As your punishment, you will have to die."

    s "What! There must be another way!"

    n "Well I could force you to date Jake Paul, that's a pretty bad thing."

    s "Well now I dunno what I want..."

    "We sat there waiting about 2 hours while Sans thought about what he wanted to do for a punishment... die, or date Jake Paul."

    "Then, the unexpected happened..."

    menu:

        s "Could you choose for me, [name]?"

        "Sans must die":
            jump sansdeath

        "Sans must date Jake":
            jump jakearc


label showingschool:

    scene bg hallway
    with fade

    show shane happy at slightright
    with dissolve

    show jake happy at slightleft
    with dissolve

    "I've decided to be the good guy here and show them around the school, so that they aren't as lost as me my first time here."

    u "This here is the hallway, where you can socialize for about 2 minutes before being trapped in hell for another 45!"

    j "sounds dope bruh."

    $ jp += 3

    show shane happy at middle
    with move

    show jake happy at left
    with move

    show betty happy at right
    with dissolve

    b "Hey guys! What's going on!"

    "Oh no, she's returned."

    show betty sad

    b "Hey!"

    sh "Who's this?"

    u "This is Betty, the ugly slut of the school."

    show betty angry

    b "HEY!"

    show betty sad

    b "I'll have you know that I was in a very happy relationship!"
    b "Well... until yesterday..."

    u "Wait really? With who?"

    "I can't believe what I'm hearing! Betty was in an actual, long relationship with someone?"

    show betty happy

    b "It was Sans!"

    "And suddenly it all made sense. Of course Sans would love Betty."

    show betty sad

    b "What's that supposed to mean?"

    j "i have a question... who the hell is sans?"

    s "That would be me..."

    show jake sad at left
    show shane sad at slightleft
    show betty sad at middle
    with move

    show sans sad at right
    with dissolve

    s "I am the one she was with."

    "Everyone looked confused, especially Betty."

    b "I better go..."

    hide betty
    with dissolve

    u "Is that why you were so sad yesterday, Sans?"

    s "Yes..."
    s "Now tell me..."
    s "Why are you doing my job?"

    "His job?"

    u "What do you mean?"

    s "Mr. Norf told me yesterday after you had already left that I was supposed to be giving the tour."

    u "Welp, sorry dude. You were too late."

    s "Cut me some slack, my girlfriend just broke up with me!"

    sh "Is everything alright here?"

    u "Well Sans, maybe you should look for other people!"

    s "But Betty was the one!"

    u "Well what about Jake?"

    show jake happy

    j "yeah im down you can smash me anytime"

    show sans angry

    s "EW NO!"

    u "Well then I guess you'll have to go with Shane cause nobody else here likes you!"

    sh "I never said I-"

    s "FINE!"

    show sans sad

    s "Shane... will you go out with me..."

    sh "...sure?"

    show sans happy

    s "Yay!"

    $ shp += 5
    $ sp += 5

    "And with that, the day was over, and a new day would bring a new relationship!"

    jump shanearc

label sansdeath:

    u "Sans, I think you need to die."

    s "Alright then, it's settled."
    s "I was probably gonna die soon anyway."

    show sans happy

    s "Welp I hate you all! See ya!"

    $ sp = 0

    scene bg black
    with fade

    "And just like that..."
    "Sans was gone."
    "Mr. Norf drowned him in a bowl of molten caramel."
    "It looked pretty fun to be honest."

    scene bg exschool
    with fade

    "A new day, nothings different."
    "Well except for Sans being dead."

    scene bg hallway
    with fade

    "It's weird not seeing him stalk my locker. I don't miss it, but it's still quite unusual..."
    "Oh well, it's still great to be free from such a weird friend."

    scene bg classroom
    with fade

    "And now for class."
    "Which is now missing Betty AND Sans."
    "Well at least Jake and Shane are here, so I'm not completely alone."

    show jake angry at slightleft
    show shane angry at slightright

    j "[name]! help us NOW!"

    u "What's going on?"

    sh "Jake thinks that Mr. Norf is a prostitute! But I know Mr. Norf would never do such a thing!"
    sh "It makes me so mad that Jake would even THINK such a thing!"

    u "Um..."

    j "but shane won't accept my physical proof!"

    u "What's your proof?"

    show jake happy

    j "i found a used condom in norf's drawer."

    u "EW!"

    "I have no idea what is happening but I need to put an end to it."

    show shane sad

    sh "So? Who's right?"

    show jake angry

    menu:

        j "You better fricking pick me!"

        "Jake is right":
            jump shanedies

        "Shane is right":
            jump jakedies

label shanedies:

    $ shp -= 10
    $ jp += 20

    scene bg black
    with fade

    "Oh no..."
    "I think my choice gave Shane a heartattack..."
    "Shane is..."
    "...dead..."

    $ shp = 0

    scene bg hallway
    with fade

    "Well, {b}another{/b} new day, another person dead!"
    "I'm starting to think I'm just bad luck for everyone."

    show jake happy
    with dissolve

    j "hey dude! thanks for killing shane for me!"

    u "Uh... no problem?"

    j "now we can be best buds!"

    "I don't know how to feel about that."

    show jake angry

    "Before I could even answer however, Jake pulled out a pocket knife."

    j "now listen here boi, i don't wanna die from you like the others have, so im gonna have to kill you first."

    $ jp -= 30

    "Oh no... he makes a good point though."
    "The real question is, should I kill him now with his own knife, or let him kill me and have it all be over with?"

    menu:

        "Let Jake have his ways":
            jump death2

        "Murder Jake":
            jump end1

label death2:

    scene bg black

    "Jake is impaling me now"
    "Goodbye world!"
    "rip."

    return

label end1:

    scene bg end1

    $ jp = 0
    $ shp = 0

    "Well it's better than death....... I think?"

    return

label jakedies:

    $ jp -= 10
    $ shp += 20

    scene bg black
    with fade

    "Oh no..."
    "I think my choice gave Jake a heartattack..."
    "Jake is..."
    "...dead..."

    scene bg hallway
    with fade

    "Well, {b}another{/b} new day, another person dead!"
    "I'm starting to think I'm just bad luck for everyone."

    show shane happy
    with dissolve

    sh "Hey, I'm glad you killed Jake for me but..."

    u "But what?"

    show shane angry

    sh "You're dead meat. I ain't lettin you kill me before I kill you."

    $ shp -= 30

    "Well.. I have two options..."
    "Should I kill him now with his own knife, or let him kill me and have it all be over with?"

    menu:

        "Let Shane have his ways":
            jump death3

        "Kill Shane":
            jump end1

label death3:

    scene bg black

    "Shane is impaling me now"
    "Goodbye world!"
    "rip."

    return

#CHAPTERTHREE
label jakearc:

    u "Sans, you need to date Jake."

    s "Are you sure...?"

    u "Yes."

    s "Well, alright..."

    show jake happy

    j "yes bruh you da best boyfriend ever"

    $ shp -= 5
    $ jp += 5

    show sans angry

    s "Thanks a lot........"

    $ sp -= 10

    scene bg black
    with Pause(2)

    show text "{size=+10}Chapter 3{/size}" with dissolve
    with Pause(3)

    hide text with dissolve
    with Pause(2)

    play music "music/placeholder2.mp3"
    scene bg exschool
    with fade

    "Well, a new day, and a new romance is blooming."
    "I can't wait to see where this ends up leading."

    scene bg classroom
    with dissolve

    "Class was about to start and it turns out Jake and Shane ended up in my class, along with Sans."
    "I guess Sans is lucky he gets to be with his boyfriend, although I'm not sure how much he likes it."

    show jake happy at slightleft
    show sans sad at slightright
    with dissolve

    "I could see the fear in Sans' eyes."

    j "sup dude, thanks for hooking me up with sans, hes a good kisser."

    $ jp += 5

    s "{i}H  e  l  p     m  e  .  .  .{/i}"

    u "I'm glad you two love each other very much!"

    "The bell rang and everyone took their seats."

    hide sans
    hide jake
    with dissolve

    "I started zoning out right away, because Buddy didn't feel like drawing a teacher character so we're just gonna skip the class period."
    "By the time I came back to reality, everyone was leaving the classroom."
    "Except for Sans, Jake, and Shane of course."

    show sans sad at middle
    show jake happy at right
    show shane sad at left
    with dissolve

    sh "I'm glad you two are getting along well..."

    show sans angry

    s "How can you people not see that I am hating this a lot!?"

    j "shhh calm your tits sans, its no biggie. we all know you really do love me, otherwise you wouldn't have givin me a bl-"

    s "OKAY THATS IT!"

    show jake sad

    s "I can't do this anymore, I'd rather die."

    show shane happy

    sh "Yes! Please break up with him!"

    "Why was Shane so excited for them to break up...?"

    j "shane is there a reason that youre happy about this?"

    show shane angry

    sh "No..."

    show shane sad

    sh "I.. I have to go..."

    hide shane
    with dissolve

    "That was odd."
    "I wonder if Shane likes Sans or something..."

    show jake sad at slightright
    show sans sad at slightleft
    with move

    j "so sans, how about we go on a dinner date? maybe after we could go home and you could give me another bl-"

    s "FINE!"
    s "We'll go eat out."
    s "But the only thing I'm doing afterwards is taking you home, then I'll go to my home, and we don't speak for the rest of the night."

    j "um.. i guess that works too. i see you want to take things slow ;)"

    s "Sure..."

    "The bell rang and the day was over... ignore the fact that we only went to one class."

    scene bg exschool
    with dissolve

    "I started to head home when Sans ran up to me."

    s "[name], please! I need your help!"

    show sans sad
    with dissolve

    u "What is it, dude?"

    s "I need you to come with me on the date!"

    u "...why?"

    s "I'm afraid of Jake. What if he tries to come onto me while we're eating?"
    s "What if he whips out his dick onto the table and tells me to eat it?"
    s "I am worried!"

    menu:
        s "So can you please come with?"

        "Go on date":

            u "Alright... fine."
            u "I'll go with."

            show sans happy

            s "Thank you so much! I appreciate it!"

            $ sp += 20

        "Don't go on date":

            u "Sorry Sans but you're on your own."

            s "Well..."
            s "This is awkward..."

            $ sp -= 20

            u "I didn't have a real choice did I?"

            show sans vangry

            s "Nope."
            s "Mr. Norf can't stop me after school hours."

            u "Alright, alright. I'll go."

            show sans happy

            s "Sweet! See ya there baby!"

            "..."

    hide sans
    with dissolve

    "I guess I better head home and get ready..."

    scene bg room
    with fade

    "Ah, my room."
    "I hate it so damn much."
    "{i}...even if it is the best looking place in this game so far... sadly...{/i}"
    "I guess I better find my nice clothes."
    "I wonder how fancy they are gonna be dressing... would a long sleve shirt be good enough, or should I throw on a full tuxedo...?"

    menu:

        "I don't want to look bad for Sans..."

        "Dress casually fancy":
            jump notfancy

        "Dress {b}fancy{/b} fancy.":
            jump fancy

label notfancy:

    "I suppose a long sleeve shirt should be good enough."
    "Alright, guess I'm fine the way I am!"
    "I really hope this goes well for Sans. He really seems to be into Jake."

    scene bg dinner
    with fade

    "Well, I've made it."
    "Seems like I made it early too, nobody else is here..."

    q "Hey, you there!"

    u "Huh?"

    "I turn around and there's a big, thick man with huge shoulders, a sexy collarbone, floofy hair, and broken glasses standing in front of me. He also has a nice suit on... something I don't have..."

    show ford happy
    with dissolve

    "He looked like a hotter version of Mr. Norf... with a nose."
    "I am extremely aroused by this"

    u "Um... hi?"

    q "You're not lookin' very fancy today, are you?"

    $ fp -= 10

    u "No, I didn't think I had to."

    q "Are ya kidding? This is the fanciest place in town!"
    q "Anyway, enough pickin' on ya. The name's Ford."

    f "I have wet dreams about an Illuminati man sometimes."

    u "...fun."

    "Just as the conversation was getting interesting, the others arrived."

    show ford happy at right
    with move

    show sans sadtux at middle
    show jake happytux at left
    with dissolve

    j "sup everyone?"

    s "...hey, [name]. Glad you could make it."

    j "whos the old doofus?"

    "Well that sure was a rude way to refer to Ford, but I guess Jake isn't the nicest person around."

    u "His name is Ford, and you better respect him."

    $ fp += 3

    j "k but why is he here?"

    "That I wasn't able to answer."

    f "I'm your waiter for the evening."
    f "Somehow, unforeseen circumstances led me to your dimension, and it could cost me a lot of money to get materials to make a new portal to get back home."
    f "So in the meantime I am stuck waiting tables."

    "Our dimension? What on earth is he talking about?"
    "Is that why he looks so sexy?"
    "We were all confused, but decided not to question it."

    f "Anyway, please take a seat here."

    "We all sat down at the table he pointed to."

    f "Would any of you care for a drink? We have water, soda, or Mabel Juice."

    "I didn't know what Mabel Juice was, but I needed to try it."

    u "May I have some Mabel Juice?"

    f "Sure thing! How about you two?"

    s "I'll have a water."

    j "soda."

    f "Coming right up!"

    hide ford
    with dissolve

    show sans happytux at slightright
    show jake happytux at slightleft
    with move

    j "you look like a snack today, sans."

    s "Th... thanks..."

    "The sexual tension between the two is astounding."
    "A few minutes pass before Ford comes back with our drinks."

    show ford happy at right
    with dissolve

    show sans sadtux at middle
    show jake happytux at left
    with move

    f "Here you three are, I hope that these drinks have been made to your liking."

    "He hands me a pink substance, which I assume is the Mabel Juice."

    u "What's in this?"

    f "All I know is that it has plastic dinosaurs and plastic ice cubes in it, and that it looks like if coffee and nightmares had a baby."
    f "Enjoy!"

    "I just stared at the drink..."

    f "Is there anything on the menu that would satisfy your appetites?"

    fc "{size=+20}CUDDLES ARE ALWAYS AN OPTION TOO{/size}"

    j "i will have a pizza."

    f "Alright, one pizza, anything else?"

    show sans happytux

    s "I'll have a blue raspberry popsicle, please!"

    f "Great! Good choice if I do say so myself."

    python:
        food = renpy.input("I told Ford what I wanted too...")
        food = food.strip()

        if not food:
             food = "burger"



    u "I'll have a large [food], please!"

    f "One [food] coming right up!"

    hide ford
    with dissolve

    show sans happytux at slightright
    show jake happytux at slightleft
    with move

    "Ford walked away, so I figured now would be a good time to start some awkward small talk that usually happens during dates..."

    menu:

        u "So..."

        "Talk about the weather.":
            jump weather

        "Talk about politics.":
            jump politics

        "Talk about sex.":
            jump sex

        "Talk about sports.":
            jump sports

label weather:

    $ weather = True

    u "So how about that weather right now?"

    show sans sadtux

    s "What?"

    u "You know... the weather..."

    j "why do peeps think talking about the weather is fun?"

    "He has a point..."

    jump awkwardnight

label politics:

    $ politics = True

    u "How about we discuss politics?"

    show sans angrytux

    s "No."

    jump awkwardnight

label sex:

    $ sex = True

    u "Wanna talk about sex?"

    j "my favorite topic >:)"

    show sans sadtux

    s "Oh no..."

    u "You ever have sex, Jake? I know Sans has..."

    j "oh hell yeah all the time, everyday bro."
    j "im hoping sans wont let me break my streak tonight."

    "Sans seems scared, but that's probably just first date jitters."

    u "Is there anyone specific you've had sex with that we might know, Jake?"

    j "Well there's Mr. Norf, that was great."

    u "You had sex with Mr. Norf?"

    j "yeah, he gave me extra credit in class for it."

    u "Oh nice!"

    "Deep down, I'm scarred for life."

    u "Well I'm happy you got to experience it enough that Sans won't be uncomfortable. He's a pro too."

    j "perfect."

    jump goodnight

label sports:

    $ sports = True

    u "So how about the big game last night?"

    show sans sadtux

    s "What big game?"

    u "You know... the... sports thing that people watch."

    j "yOOOOOO YOU SAW IT TOOO???"

    u "Totally!"

    "{i}No I didn't.{/i}"

    j "did you see the part where-"

    s "Jake, we don't watch sports."

    show jake sadtux

    j "...what?"

    $ jp -= 5

    show jake angrytux

    j "why did you lie to me???"

    u "Sorry, Jake! I'm just trying to make small talk!"

    show jake sadtux

    j "oh..."

    show jake happytux

    j "okay."

    $ jp += 3

    jump goodnight

label awkwardnight:

    $ sp -= 10
    $ jp -= 10

    "After a few minutes of silence, due to the awkwardness of our conversation, Ford returned with our food."

    show ford happy at right
    with dissolve

    show sans happytux at middle
    show jake happytux at left
    with move

    f "Here is your pizza, Jake."

    show sans happytux

    f "Here is your blue raspberry popsicle, Sans. Suck on it all you want."
    f "And here is your large [food], [name]."
    f "I hope you all enjoy!"

    hide ford
    with dissolve

    show sans happytux at slightright
    show jake happytux at slightleft
    with move

    "We still sit kinda silent and awkward, I guess the last conversation is still lingering in their heads."

    u "So what do you want to talk about...?"

    if weather:

        show sans sadtux

        s "Not the weather... that's for sure..."

    if politics:

        show jake sadtux

        j "Anything but politics..."

    "He was right..."
    "We sat there silent for a little while longer before we all finished out food."
    "Ford returned to get our plates."

    show ford happy at right
    with dissolve

    show sans sadtux at middle
    show jake sadtux at left
    with move

    f "So, how'd you all like the food?"

    u "I enjoyed it!"

    "I haven't even touched my Mabel Juice."

    f "Well I'm glad!"

    "We left the money at the table and stood up to leave, without even saying a word."

    hide sans
    hide jake
    hide ford
    with dissolve

    "It felt like tonight was pretty unsuccessful."
    "Jake and Sans didn't even have a proper conversation."
    "In fact, Sans barely spoke at all."
    "Oh well, I guess it's time to go home."

    f "Hey!"

    "I heard Ford's voice boom across the diner."

    show ford happy
    with dissolve

    f "I need your assistance with something, [name]."

    u "You need {i}my{/i} assistance?"

    f "Yes, you seem very intelligent compared to most people in this universe, so I think you'd be perfect!"

    menu:
        "Are you willing to do it?"

        "Sure":

            u "Um... sure?"

            f "Great! I'll see you at my house in an hour, here's my address."

            $ fp += 5

            "Ford handed me a card with an address on it."

            u "See ya!"

            jump fordshouse
        
        "No, sorry":

            u "Sorry, but I'm not interested."

            f "Aw, that's too bad."

            $ fp -= 5

            f "Oh well. Maybe I can get back within the week still, even when building solo."

            hide ford

            "Well that was... odd..."

            jump anotherday

label goodnight:

    if sex:

        $ sp += 10
        $ jp += 10

        "After a nice conversation about dinging peoples' dongs, Ford came back with our food."

    if sports:

        $ sp += 10
        $ jp += 10

        "After an interesting conversation about something I didn't even like, because I just play video games all the damn time, Ford came back with our food."

    show ford happy at right
    with dissolve

    show sans happytux at middle
    show jake happytux at left
    with move

    f "Here is your pizza, Jake."

    show sans happytux

    f "Here is your blue raspberry popsicle, Sans. Suck on it all you want."
    f "And here is your large [food], [name]."
    f "I hope you all enjoy!"

    hide ford
    with dissolve

    show sans happytux at slightright
    show jake happytux at slightleft
    with move

    "We continued to talk while we ate our food."

    if sex:

        j "so sans how many babes have you fucked?"

        show sans sadtux

        s "Uh..."

        "We sat for a moment while Sans vocally counted to himself."

        show sans happytux

        s "About 2789 or so!"

        j "daaaaaaaaaaaaaaaamn dude thats nice."
        j "i wish i could be as slick as you. but i guess if you bang me every night i could hit that number eventually."

        show sans sadtux

        s "But these were all different dudes and dudettes."
        s "So you'd have to break up with me..."

        show sans happytux

        "Sans was suddenly smiling a huge smile."

        s "Hey! Why don't you go try to beat that record??"

        j "nah im good, i'd rather be with you."

        show sans sadtux

        s "Oh."

    if sports:

        j "so have you two ever played sports?"

        show sans sadtux

        s "I did once... it was the summer of '72."
        s "I was only 14 years old, and a naive little skeleton."
        s "I had just finished fucking [name]'s mom and had to go play in our local Quidditch tournament."
        s "Little did I know, this would be the last sport I ever played..."

        scene bg fb1
        with fade

        s "I was so excited to play, especially from the sex adreneline I had flowing through my bloodstream."
        s "My mother showed up to support me, but my dad was nowhere to be seen."
        s "That's when I had realized..."
        s "My dad's head was being used for the quaffle ball..."

        scene bg fb2
        with dissolve

        s "This hurt me... I never even got to tell him how much I loved him."
        s "But that's when he called me over, in his dying breath right before the game started."

        scene bg fb3
        with dissolve

        mu "Sans..."

        s "Yes papa?"

        mu "Eating chocolate?"

        s "No papa..."

        mu "Telling....... liess......-"

        scene bg black
        with dissolve

        s "And at that moment, he was dead."
        s "I didn't even get to tell him that I was lying."

        scene bg dinner
        with fade

        show sans sadtux at slightright
        show jake sadtux at slightleft
        with fade

        j "well that sucks dude."

        show jake happytux

        j "anyway old dude be coming back!"

    show ford happy at right
    with dissolve

    show sans sadtux at middle
    show jake sadtux at left
    with move

    f "So, how'd you all like the food?"

    u "I enjoyed it!"

    "I haven't even touched my Mabel Juice."

    f "Well I'm glad!"

    "We left the money at the table and stood up to leave, Jake and Sans were still having their own conversation."

    hide sans
    hide jake
    hide ford
    with dissolve

    "It felt like tonight went pretty well!"
    "Jake and Sans had some beautiful chemistry going on."
    "I guess it's time to go home."

    f "Hey!"

    "I heard Ford's voice boom across the diner."

    show ford happy
    with dissolve

    f "I need your assistance with something, [name]."

    u "You need {i}my{/i} assistance?"

    f "Yes, you seem very intelligent compared to most people in this universe, so I think you'd be perfect!"

    menu:
        "Are you willing to do it?"

        "Sure":

            u "Um... sure?"

            f "Great! I'll see you at my house in an hour, here's my address."

            $ fp += 5

            "Ford handed me a card with an address on it."

            u "See ya!"

            jump fordshouse
        
        "No, sorry":

            u "Sorry, but I'm not interested."

            f "Aw, that's too bad."

            $ fp -= 5

            f "Oh well. Maybe I can get back within the week still, even when building solo."

            hide ford

            "Well that was... odd..."

            jump anotherday

label fancy:

    "I guess I should look as good as possible, since this'll be a big moment for Sans."
    "He's never been on a dinner date."
    "Normally he would just meet someone and take them straight home."

    scene bg dinner
    with fade

    "Well, I've made it."
    "Seems like I made it early too, nobody else is here..."

    q "Hey, you there!"

    u "Huh?"

    "I turn around and there's a big, thick man with huge shoulders, a sexy collarbone, floofy hair, and broken glasses standing in front of me. He also has a nice suit on, looks like that was a good choice."

    show ford happy
    with dissolve

    "He looked like a hotter version of Mr. Norf... with a nose."
    "I am extremely aroused by this"

    u "Um... hi?"

    q "You're lookin' quite sexually attractive today, aren't you?"

    $ fp += 10

    u "Is it because of the suit?"

    q "Yes! You made a good choice wearing that, I woulda had to pick on you a little if you didn't."
    q "Anyway, enough about that. The name's Ford."

    f "I have wet dreams about an Illuminati man sometimes."

    u "...fun."

    "Just as the conversation was getting interesting, the others arrived."

    show ford happy at right
    with move

    show sans sadtux at middle
    show jake happytux at left
    with dissolve

    j "sup everyone?"

    s "...hey, [name]. Glad you could make it."

    j "whos the old doofus?"

    "Well that sure was a rude way to refer to Ford, but I guess Jake isn't the nicest person around."

    u "His name is Ford, and you better respect him."

    j "k but why is he here?"

    "That I wasn't able to answer."

    f "I'm your waiter for the evening."
    f "Somehow, unforeseen circumstances led me to your dimension, and it could cost me a lot of money to get materials to make a new portal to get back home."
    f "So in the meantime I am stuck waiting tables."

    "Our dimension? What on earth is he talking about?"
    "Is that why he looks so sexy?"
    "We were all confused, but decided not to question it."

    f "Anyway, please take a seat here."

    "We all sat down at the table he pointed to."

    f "Would any of you care for a drink? We have water, soda, or Mabel Juice."

    "I didn't know what Mabel Juice was, but I needed to try it."

    u "May I have some Mabel Juice?"

    f "Sure thing! How about you two?"

    s "I'll have a water."

    j "soda."

    f "Coming right up, I'll make sure the Mabel Juice is especially made to perfection!"

    hide ford
    with dissolve

    show sans happytux at slightright
    show jake happytux at slightleft
    with move

    j "you look like a snack today, sans."

    s "Th... thanks..."

    "The sexual tension between the two is astounding."
    "A few minutes pass before Ford comes back with our drinks."

    show ford happy at right
    with dissolve

    show sans sadtux at middle
    show jake happytux at left
    with move

    f "Here you three are, I hope that these drinks have been made to your liking."

    "He hands me a pink substance, which I assume is the Mabel Juice."

    u "What's in this?"

    f "All I know is that it has plastic dinosaurs and plastic ice cubes in it, and that it looks like if coffee and nightmares had a baby."
    f "Enjoy!"

    "I just stared at the drink..."

    f "Is there anything on the menu that would satisfy your appetites?"

    fc "{size=+20}CUDDLES ARE ALWAYS AN OPTION TOO{/size}"

    j "i will have a pizza."

    f "Alright, one pizza, anything else?"

    show sans happytux

    s "I'll have a blue raspberry popsicle, please!"

    f "Great! Good choice if I do say so myself."

    python:
        food = renpy.input("I told Ford what I wanted too...")
        food = food.strip()

        if not food:
             food = "burger"



    u "I'll have a large [food], please!"

    f "One [food] coming right up!"

    hide ford
    with dissolve

    show sans happytux at slightright
    show jake happytux at slightleft
    with move

    "Ford walked away, so I figured now would be a good time to start some awkward small talk that usually happens during dates..."

    menu:

        u "So..."

        "Talk about the weather.":
            jump weather

        "Talk about politics.":
            jump politics

        "Talk about sex.":
            jump sex

        "Talk about sports.":
            jump sports


label fordshouse:

    $ atFords = True

    scene bg fordhouse
    with fade

    "Well I made it."
    "I wonder what Ford even needs help with..."

    scene bg insidefhouse

    "The door was already slightly open so I decided to just walk right in."

    u "Ford?"

    u "You here?"

    show ford happy
    with dissolve

    f "Ah, yes. You made it!"

    u "So what were you wanting help with?"

    f "I want to talk about the dimensional thing that I mentioned earlier."

    u "Oh... right..."

    "Yeah he's crazy."

    u "Alright what about it?"

    f "I think something brought me here, I don't know what... or why... but it was no accident."

    u "And what makes you think that?"

    f "Well, normally when I travel between dimensions, it's my decision where I go, and when I do it."
    f "But this time, I woke up in this place..."
    f "I didn't willingly choose to come here."

    u "You sure you weren't just drunk and confused and you accidentally came here because of it?"

    f "[name], I don't drink."
    f "However I do enjoy coffee, would you like some?"

    u "Yeah, sure!"

    hide ford
    with dissolve

    "This man is truely crazy."
    "How isn't he in a mental hospital?"
    "I mean, he does look very different, so he could be telling the truth..."
    "...nah. He's crazy."
    "Wait a minute... I forgot to tell him what kind of coffee I wanted..."

    show ford happy
    with dissolve

    f "Here you go!"

    if fp <= 48:
        "Ford hands me the coffee and, of course, he got it completely wrong."
        "I can't be rude though... guess I'll try to enjoy it."
    else:
        "Ford hands me the coffee and... wait?"
        "He knew exactly what I wanted?"

    u "Thanks!"

    f "Alright, now."
    f "I have all of the parts that I need for my machine, so how about we get building?"

    u "Um... okay?"

    "I have no idea how to build this thing, but I suppose I'll just do what he says..."

    scene bg insidefhouseportal
    with fade

    "And just like that, as if no time had passed at all, we have... something."
    "It looks like a stereotypical alien portal thing... except like a hunk a junk."

    show ford happy

    f "Perfect!"

    u "...it is?"

    f "Yes! We've done it! Now I can get back home!"

    $ fp += 5

    f "First I just have to switch it on and..."
    f "Hmm?"
    f "OwO, what's this?"

    u "What happened?"

    f "It seems as though I forgot to pick up two AA batteries from the store."

    u "This runs on AA batteries...?"

    f "Indeed!"

    "This could not get any weirder."

    f "I'm out of money so I guess I'll just have to work for another day or two and I'll call you back when I have the batteries."

    u "Oh... uh... okay."

    f "Thanks for the help!"

    fc "{size=+20}YOU CAN STOP BY ANYTIME IF YOU FEEL LONELY{/size}"

    "What the fuck is he saying when he does that?"

    u "No problem! See ya!"

    scene bg fordhouse
    with dissolve

    "What a strange old man..."

    if murderer2:
        jump anotherday
    else:
        jump anotherday2

label anotherday:

    scene bg exschool
    with fade

    "Another day, another dollar... I wish... since I'm poor as hell..."
    "I wonder if Sans took Jake home like he said he would, or if they got it on after the date."

    scene bg hallway
    with dissolve

    "Oh, well look who decided to show up as soon as I mention him."

    show sans sad

    s "[name]! Help!"
    s "He won't leave me alone!"
    s "I decided to have sex with him last night and now it's like he's been on some weird spiritual high and it won't stop!"

    u "What?"

    s "Jake! He's on the move! Quick! Get to the classroom!"

    hide sans

    "I wonder what that was about..."

    scene bg classroom
    with dissolve

    "Class was as boring as ever, though Sans and Jake didn't show up."
    "I guess they were in the band hallway banging some more."

    show shane sad

    sh "Hey, [name]..."

    u "Hey, Shane! What's wrong?"

    sh "I'm sad."

    u "Well no shit... that's why I asked what was wrong."

    sh "It's just..."
    sh "Alright look. I have a huge crush on Sans."
    sh "But it doesn't matter now, because him and Jake seem very happy together."

    u "Well you could still tell Sans, maybe he'll break up with Jake just for you!"

    sh "I highly doubt it..."

    show shane sad at slightleft
    with move

    show sans sad at slightright
    with dissolve

    s "Is this true Shane?"

    sh "Um..."

    s "Why didn't you say anything?"

    sh "I was... scared... and you were forced to date Jake..."
    sh "And I know you're enjoying it..."
    sh "I just didn't want to ruin that for you..."

    s "..."

    show sans angry

    s "{b}That's IT{/b}"
    s "I've had enough of this!"
    s "I do not love Jake!"
    s "I do not like him!"
    s "You are all delusional!"
    s "I have made it fairly obvious that I don't like him, but all of you are too stupid to even notice!"
    s "Shane!"
    s "I love you! Not Jake!"
    s "I didn't ever want to date him!"
    s "I want you..."

    show sans sad

    s "But I guess I can't now, since I'm stuck with Jake."

    u "Why don't you just break up with him?"

    s "Part of the punishment was that {i}he{/i} is the only one that can break us up."
    s "I'm not allowed to..."

    sh "Sans... please..."

    s "I'm sorry Shane..."
    s "I... I have to go..."

    hide sans
    with dissolve

    show shane at middle
    with move

    u "I'm sorry Shane..."

    sh "..."

    $ shp -= 5
    $ sp -= 5

    hide shane

    "Hmm... I hope they'll be okay..."

    scene bg roomnight

    "Today was such a weird day, I can't even think of anything to do besides sleep."
    "At least I know that it can't get any weirder..."

    scene bg black
    with fade

    scene bg droom
    with fade

    "Ah, that was a good sleep, though it did feel kinda quick..."
    "Oh well, I better get to school."

    scene bg dschool
    with fade

    "I wonder if today will be any different from yesterday..."
    "I would hope so anyway..."

    scene bg dhallway
    with dissolve

    "I can't help but feel like something is off..."

    show betty happy
    with dissolve

    b "Hey, [name]!"

    u "Oh, hey Betty!"

    b "Would you mind helping me with something?"

    u "What?"

    b "...do you know how to contact a military general...?"

    "...?"

    u "Excuse me?"

    b "...nevermind..."

    hide betty
    with dissolve

    "That... was very weird..."

    scene bg dclassroom
    with dissolve

    "Well the classroom seems normal at least."

    show norf happy
    with dissolve

    n "Welcome to class!"
    n "Today we'll be joining the military!"

    u "What??"

    n "You have no choice! Everyone is going to war!"

    u "That's..."
    u "..not okay..."

    show norf angry

    n "Nobody asked you!"

    show mcdream
    hide norf
    with dissolve

    u "Um... who the hell are you..."

    q "Heh heh heh..."

    scene bg black
    with fade

    u "Wha-aaAAHAHHH--"

    scene bg room

    "Huh?"
    "What the fuck..."
    "That was unlike any dream or nightmare that I've had before..."
    "What was that demon...?"
    "What was any of that...?"
    "I should do some research on it... maybe Sans will know something too..."
    "I'll ask him tomorrow morning when he stalks me by my locker."

#CHAPTERFOUR
    scene bg black
    with Pause(2)

    show text "{size=+10}Chapter 4{/size}" with dissolve
    with Pause(3)

    hide text with dissolve
    with Pause(2)

    play music "music/placeholder2.mp3"
    scene bg hallway
    with fade

    show shane sad
    with dissolve

    sh "Hey, [name]. Have you seen Sans this morning?"

    u "No... I can't say I have. I've been expecting to see him here by my locker."
    u "Maybe he's in the bathroom fucking Jake or something?"

    sh "Don't put that depressing image into my head..."

    hide shane
    with dissolve

    "Well I guess I should check the bathroom."

    scene bg black
    with fade

    "Outside the restrooms, I knock on the door."

    u "Sans?"
    u "Jake?"
    u "Come on out you dummies..."

    "There's no response."
    "I really didn't want to have to enter the bathroom like this..."
    "Isn't it kind of a breach of privacy?"
    "But they really leave me no choice."
    "I gently open the door."
    "......San-"

    scene s_kill_bg
    show s_kill at slightleft
    with Pause(3)

    "What the hell...?"
    "I think I walked into the fucking girls bathroom!"
    "Whoops."

    scene bg black
    with fade

    "Hopefully nobody saw."
    "Lucky ass girls, they have a nice looking bathroom."
    "Anyways, time to check the {i}boys'{/i} bathroom."

    scene bg bathroom
    with fade

    "Well, they don't seem to be anywhere in here."
    "Oh well... maybe they stayed home together."
    "Guess I better head back to class."

    scene bg black
    with fade

    q "Wait a minute~! Don't leave yet! >w>"

    u "What?"

    scene bg bathroom
    with fade

    u "Who said that?"

    show belle happy
    with dissolve

    q "Me of course! <3"

    u "{size=+10}{b}WHAT THE FUCK!?{/b}{/size}"
    u "This is the boys bathroom... what are you-"

    q "Hush now silly~ You entered the girls' bathroom so you can't call me out! UwO"

    u "That was an accid-"

    q "My name is Belle. Belle Delphine! >w<"

    bd "I've come to this school as a traveling merchant to sell my bathwater to your fellow classmates! :D"

    u "Wha-"

    bd "{size=-5}{i}I'm also undercover for a very important mission, but I'll get into that later. ;){/i}{/size}"
    bd "The point is, you are part of the plan! So I hope you're ready for whatever happens next~ -u-"

    u "Look... all I wanna know right now is, where are Sans and Jake?"

    show belle sad

    bd "Who? ÒnÕ"

    u "Wait... so you have nothing to do with their disappearence?"

    show belle happy

    bd "Nope! But we can investigate that when we need to. For now, follow me! ^u^"

    hide belle
    with dissolve

    u "Wait but-... alright..."

    "Why does this week just keep getting weirder...?"

    scene bg black
    with fade
    with Pause(1)

    scene bg outside1
    with fade

    show belle happy
    with dissolve

    u "So what's going on here?"

    show belle angry

    bd "Hush! I'll be asking the questions for now! ÒnÓ"

    show belle happy

    bd "So... did you happen to have a scary nightmare last night by any chance? OwO"

    u "How did you-"

    bd "{size=+10}PERFECT! OuO{/size}"
    bd "This will help us figure out exactly what's been going on he-"

    show belle sad

    n "{size=+20}{b}[name]!!!{/b}{/size}"

    show belle sad at slightleft
    with move
    show norf angry at slightright
    with dissolve

    n "Where have you been!? I haven't seen you in any of your classes recently!"

    u "I... uh... this girl..."

    n "Oh so you're going to fuck her now huh?"
    n "Instead of getting a good education?"

    show belle angry

    n "Ya know, I think I've fucked every single person in the classroom except for you."
    n "Is this why you're sneaking away to-"

    show belle happy

    bd "Hey~! UwU"

    show norf sad

    bd "Enough yelling. Would you like to buy some of my used bathwater~? ;)"

    show norf happy

    n "Used bathwater you say?"
    n "Well don't mind if I do!"

    bd "That'll be $35 please! ^w^"

    "What on earth?"

    n "Thank you so much!"
    n "Sorry for getting mad at you, [name]. She's a keeper, don't let her down! Go ahead and fuck!"

    hide norf
    with dissolve
    show belle happy at middle
    with move

    u "But we're not- oh nevermind."

    bd "Alrighty then! Let's head over to my house! UuO"

    scene bg black
    with fade

    "Well... I'm in her house... but I can't see a damn thing."

    u "Isn't it kind of dark in here?"

    bd "A lil bit, just feel your way around! :)"

    "What the fuck am I touching right now?"

    u "Uh... Belle? What is this?"

    bd "Hehehe! OuU"

    u "Why is it wet....."

    bd "Don't worry about that~! ;P"
    bd "Hey, here's the lightswitch! :D"

    scene bg bdhouse
    show belle coke

    bd "There we go! >w<"

    u "Why are you holding a Coke?"

    bd "Because I'm thirsty? What'd you think you were touching before I got the lights on? @-@"

    "..."

    show belle coke

    bd "Anyways, this is my house! ^-^"

    show belle coke at left
    with move

    bd "As you can see, people have really been enjoying my bathwater! OwO"

    show belle happy at middle
    with move

    menu:

        bd "Would you care to see how it's made? -w-"

        "No way.":
            u "N.. no... thank you..."

            show belle sad

            bd "Fair enough. UnU"

            $ bdp -= 15

        "Sure!":
            u "Hmmm... yeah sure! Why not!"

            bd "Yaas! >w> I'll let you check it out later tonight when I make more~!"

            $ bdp += 15
            $ uwuwater = True

    show belle happy

    bd "Anyways, I'd like you to meet my co-partner for this mission I'm on!"

    show belle happy at slightleft
    with move

    bd "Steak-Umm! Come on out!"

    show steak umm at slightright
    with dissolve

    su "Hmm, yes. Hello there sir."
    su "The name is Umm. Steak-Umm."

    u "Uh... my name is [name]..."

    su "So, [name], you have a lot to learn about our mission still, is that correct?"

    u "Yeah. I have no fucking clue what is going on anymore... with anything."

    "I just wish they'd help me find out where Sans and Jake are already so I could get the hell out of here."

    bd "Steak-Umm here is another undercover spy helping me out."

    u "Doesn't a walking, talking box of frozen beef sheets seem a bit suspicious?"

    su "This place seems just crazy enough that nobody will even notice."

    "He does have a point here."

    su "Steak-Umm is better than Hot Pockets."

    u "What?"

    bd "He's required to say that every so often."

    su "Anyways, enough chitter chatter. Let us continue with this mission."
    su "You have been having scary nightmares with demons, correct, [name]?"

    u "Just one, but yeah."

    u "Although it was hard to tell if it was a demon or a normal man. There was lots of talk about the military."

    su "Just as I suspected."

    u "What do you mean?"

    bd "We've been monitoring the brain activity of lots of individuals recently! ~w~"

    su "We picked up signals of a demon-like creature hopping from brain to brain throughout the multiverse."
    su "When it arrived here, we knew it would not be hard to catch up with, since everybody in this universe is so slow minded."

    u "Hey!"

    bd "That's why we've come to you for answers! ^w^"
    bd "Your brain is so slow that we managed to catch up within 12 hours of you having the dream! >u<"

    u "Stop saying that!"
    u "And what are you talking about with this whole multiverse thing?"
    u "You mean to tell me that you guys aren't from here?"

    su "Is it not obvious from our appearance?"
    su "Everybody in this universe has a misshapen, blobby form to them."

    u "But... Jake and Shane don't look that way..."

    show belle sad

    bd "You mean Jake Fucking Paul? Is that the Jake you were talking about earlier??? OnO"

    su "Ah, Jake and Shane. They are not from this universe either."
    su "They are from the same universe as us."
    su "Unfortunately."
    su "It seems that the demon-creature brain-hopping around has caused these universes to collide somehow."

    u "So that explains how Ford ended up here as well!"

    su "Another one??"
    su "How many dreams has this demon visited???"
    su "We must gather up everyone from here that is from an alternate universe, that is our first step to defeating this vile creature!"

    u "Yeah... one problem with that plan."
    
    bd "[name] mentioned earlier that Jake and Sans have been missing all morning. >~<"

    u "We can't continue this mission without Jake."
    u "Like you said, we need everybody that's from an outside universe, and that includes him."

    su "Then we must search for them!"
    su "When and where did you last see those two?"

    u "Last time I saw Jake was when I third-wheeled him and Sans's dinner date the other night."
    u "Last time I saw Sans was yesterday morning in class."

    bd "Wait wait wait... ?-?"
    bd "Jake actually had a date? >o<"

    show belle angry

    bd "But the dude is a sociopath! >>O<<"

    su "He is with somebody named Sans. I am certain there is a catch."

    u "Actually, dating Jake was a punishment for Sans."

    show belle sad

    su "See?"
    su "Anyways, let us get going! I have been continuing to monitor the brain activity here all morning, and the demon is still here."
    su "We do not have long until he gets bored with this place and moves on to another universe. We must get going!"

#CHAPTERFIVE
label thehunt:

    scene bg black
    with Pause(2)

    show text "{size=+10}Chapter 5{/size}" with dissolve
    with Pause(3)

    hide text with dissolve
    with Pause(2)

    play music "music/placeholder3.mp3"
    scene bg noutside
    with fade

    show steak umm at slightleft
    show ford happy at littleright
    show belle sad at veryleft
    show shane sad at middle
    show norf sad at veryright
    with dissolve

    u "Sans?"

    n "Jake!"

    sh "Sans!? Can you hear me honey??"

    su "Uh... Shane?"

    sh "Sorry, I just... I really miss him..."
    sh "{b}His bone boner was supposed to MINE!{/b}"

    f "We've been searching all day. I'm afraid it's no use."

    u "We can't just give up!"

    show norf angry

    n "Well what else are we supposed to do? They are nowhere to be found!"

    show norf sad

    su "Wait just a meaty minute!"
    su "I have just picked up some new signals!"
    su "It seems that the creature temporarily left this universe and then returned a few minutes later!"

    show norf happy

    n "Maybe he got horny."

    bd "Do you think it took Jake and Sans with? >->"

    show norf sad

    su "I know it did!"
    su "According to my readings, two unidentified objects exited this universe with the creature."

    show shane happy

    sh "Well then it must be them!"

    f "We gotta get there fast! Do you know what dimension they went to?"

    su "It seems the demon is only able to travel through the multiverse in a linear fashion, so it should be the next universe from here: our universe!"

    show belle happy

    bd "Yes! ^O^"
    bd "I can't wait to finally go home!!! >w<"

    "..."

    show belle sad

    "..."

    bd "And save your friends, of course~ ^u^;"

    show belle angry

    bd "Let me have my moment... -.-"

    show belle happy
    show norf happy

    f "It seems we're only a few blocks away from my house!"

    if atFords:

        f "We can use my portal that [name] and I built a few days ago! I finally got AA batteries!"

    else:

        f "We can use my portal that I built a few days ago! I would've used it sooner but I forgot to buy AA batteries!"

    su "Hmm... Ford... I am not so certain about that..."

    show belle sad

    bd "Yeah, we have our own multiverse-traveling gizmos that we can use! ^u^"

    show belle happy

    bd "And they're rechargable! OwO"

    show belle sad

    su "Not to mention there is no guarantee that your portal device will work."
    su "Am I right to assume it has not been tested yet?"

    f "Well no... but where I'm from, I'm the finest scientist in the world!"

    su "I do not want to take the risk..."

    bd "Neither do I. UnU"

    show belle happy

    bd "I'll be heading with Steak-Umm! >w>"

    sh "Don't worry, Ford! I'll head with you."

    show shane sad
    show belle sad

    sh "I'd rather trust an actual human than a bathwater dispenser and a box of frozen meat."

    show belle happy
    show shane happy

    menu:

        f "Who will you be heading with, [name]?"

        "I'll go with Ford.":
            jump travelford

        "I'll go with Steak-Umm.":
            jump travelsteak

label travelford:

    $ fp += 15
    $ shp += 5
    $ sup -= 10
    $ bdp -= 10

    u "I'll head with you, Ford!"

    show belle sad

    su "Very well then."
    su "We will see you guys there..."
    su "...hopefully..."

    hide steak
    hide belle
    with dissolve

    show shane happy at slightleft
    show ford happy at slightright
    with move

    show norf sad

    n "If it's all the same with you three, I'll just be heading with those two."

    u "See ya there, Norf!"

    hide norf
    with dissolve

    f "Alright you two! We don't have much time."
    f "Follow me to my house and we'll get the portal powered up!"

    scene bg insidefhouseportal with fade
    with Pause(1)

    scene bg portalon with dissolve
    with Pause(1)

    show shane happy at slightleft
    show ford happy at slightright
    with dissolve

    f "Well, it's ready!"

    sh "Let's head through! I need to see my Sansie-poo!"

    "..."

    show shane sad

    sh "...and save Jake..."

    if atFords:

        hide ford
        hide shane
        with dissolve

        "I can't believe I'm about to jump into a portal that leads to a completely new dimension..."
        "Just this morning I accidentally walked into the girls bathroom..."
        "What a weird ass day."

        jump arriveford

    else:

        hide ford
        hide shane
        with dissolve

        "I can't believe I'm about to jump into a portal that leads to a completely new dimension..."
        "I'm surprised Ford was actually able to build this on his own..."
        "Oh well... here goes nothing!"

        jump arriveford

label arriveford:

    scene bg volcano with fade
    with Pause(2)

    "Huh... where is this place...?"
    "This certainly feels just as shitty as my dimension..."
    "And where is everyone??"

    q "Mmph! Mmph mm!"

    "Wait...? Where is that coming from?"

    q "MMPH!!!"

    show tied at middle
    with dissolve

    u "Jake? Sans??"

    s "Mmph! Mm mmphmph mm!"

    u "It would probably help if I got the tape off of your mouths. Lemme-"

    q "Not so fast!"

    show tied at left
    with move

    show mccoy happy at slightright
    with dissolve

    q "Hello there."

    u "Who in the everliving fuck are you?"

    q "Well why don't you allow me to introduce myself?"
    q "My name is General Mccoy."

    mc "I'm generally a general for generalized military purposes."
    mc "I also run a surpisingly successful burrito stand."

    show mccoy angry

    mc "There was a damn taco stand across the street that really got on my nerves."
    mc "The owner was the worst."
    mc "\"Wah!\" this and \"Wah!\" that; just shut up!"

    show mccoy happy

    mc "So I murdered him and his customers."

    j "mph mmph."

    show mccoy angry

    mc "Quiet you!"

    show mccoy happy

    mc "Anyways, I hope you enjoy your visit to Nevada."

    u "This is just a molten volcano."

    mc "Exactly."

    "This dude is a fucking bully."

    $ question1 = False
    $ question2 = False
    $ question3 = False
    $ question3b = False

label mccoytalk:

    if question1 and question2:
        jump endtalk

    menu:

        "I really gotta figure out what's going on."

        "Why did you kidnap Sans and Jake?":
            jump whykidnap

        "What dimension is this?":
            jump whatdimension

        "Are you single?":
            jump aresingle

label whykidnap:

    u "Why did you kidnap Sans and Jake in the first place?"

    if question1:

        show mccoy angry

        mc "Did you listen to anything I just said?"
        mc "I'm not repeating myself."

        jump mccoytalk

    else:

        $ question1 = True

        show mccoy happy

        mc "There are an abundance of problems with Sans and Jake."

        s "Mph!"

        mc "They are both whores who sleep with as many people as they can."

        show mccoy angry

        mc "Jake is a sociopath."
        mc "Sans is a pedophile."

        show mccoy happy

        mc "Need I say more?"

        u "But what are you planning to do to them?"

        mc "Um... kill them, obviously."
        mc "Their love affair needs to be put to rest."
        mc "That's why I will also be killing Shane, to put an end to the entire love triangle."

        j "MMMPH???"

        jump mccoytalk

label whatdimension:

    u "What dimension is this anyways? This doesn't look like what Belle and Steak-umm described."

    if question2:

        show mccoy angry

        mc "I literally just explained everything to you."
        mc "Like... everything."
        mc "What the hell is actually wrong with you."

        jump mccoytalk

    else:

        $ question2 = True

        show mccoy happy

        mc "Ah yes. Belle and Steak-umm."
        mc "They certainly gave you a lot of info, didn't they?"
        mc "I sure hope you took it all with a grain of salt."

        u "What do you mean?"

        mc "Belle! Steak-umm! Come on out!"

        show mccoy at slightleft
        with move

        show belleumm nice behind mccoy at right
        with dissolve

        u "Belle! Steak-umm!"

        show mccoy angry

        mc "Shut up!"

        show mccoy happy

        mc "Go ahead you two. Reveal your true identities."

        show belleumm evil
        with dissolve

        u "What...?"
        u "Hot Pockets...?"
        u "Queen Elizabeth II??"

        "I can't believe it."
        "This whole time I trusted them..."
        "...these two strangers that I had never met before... one an e-thot... the other a box of frozen beef sheets..."
        "...betrayed me???"

        u "So everything you guys said was a lie? The inter-dimensional travel? The dream demon? The bathwater? It was all fake?"

        qe "Of course it was, you fucking idiot."

        u "But what about that dream I had about military generals?"
        u "The one you guys asked me about when we first met?"

        hp "That was just a lucky coincidence. We did not expect you to actually have had the dream."

        mc "Their job was to lure you into this place so I could kill you as well."
        mc "Looks like everything has gone according to plan."

        jump mccoytalk

label aresingle:

    u "Are you, by any chance, single?"

    show mccoy angry

    if question3b:

        mc "..."

        jump mccoykillsyouforcomingontohim

    elif question3:

        mc "Didn't you just... didn't you already ask me that??"

        $ question3b = True

        jump mccoytalk

    else:

        $ question3 = True

        mc "I would murder the entire population of the world before even considering going out with you."

        jump mccoytalk

label mccoykillsyouforcomingontohim:

    scene bg black

    "Oh no McCoy is stabbing me ouch oh God he stabbed me 37 times oh my God I'm fucking dead now."

    show text "{size=+10}{font=fonts/comic.ttf}you horny bitch{/font}{/size}" with dissolve
    with Pause(2)

    return

label endtalk:

    show mccoy angry

    mc "Anyways, I've had enough of your questions!"
    mc "Queen Elizabeth II? Hot Pockets?"
    mc "Take them to the torture chamber..."

    show mccoy happy

    mc "...and kill them."

    scene bg black
    with fade

    "Boy is it dark in here."

    u "Hello? Anyone in here?"

    s "Mm!"

    u "Aside from the people that got us stuck in this mess?"

    if atFords:

        jump fordconvo

    else:

        jump shaneconvo

label fordconvo:

    f "[name]?"

    u "Ford?"

    f "Hey! How are you?"

    u "I'm... is... is that really what you're asking right now?"

    f "I apologize. I just try to be polite to others, even in the most deadly of situations..."
    f "Anyways, I-"

    u "Ford. I need you to tell me this right now."
    u "Are you from another dimension, or was that a bunch of balogna like everything else?"

    f "I can assure you I really am from another dimension."
    f "I know it may be hard to believe, especially after all that's happened today, but rest assured if we make it out of here alive I will prove it to you."

    sh "Hey, guys? Have you found a lightswitch or something in this place?"

    f "Shane, I have a feeling there won't be a lightswitch in-"

    scene bg dungeon

    show shane sad at right
    show tied at left
    show ford happy at middle

    f "...oh."

    u "Hey... uh... where's Norf?"

    f "Well... he chose to go with Belle and Steak- er... Queen Elizabeth II and Hot Pockets..."
    f "Based on that I think that..."

    sh "He fucking died okay they cubified him and he's dead."
    sh "I heard him yelling \"Ah help I'm being turned into a cube ahhh!\" and now he's a paper weight."

    u "Oh."
    u "Oh well, we clearly didn't like him anyways."
    u "Let's get out of here."

    f "Which way is out?"

    j "mmphm mphmmmphm mm mmph mmm mphm mmph."

    sh "Not now Jake, we're trying to figure out how to get out of here."
    sh "Do you know the way out, [name]?"

    u "Why am I always the one making these decisions?"

    s "Mmphm mmm mmph."

    menu:

        "Guess I gotta figure out how to get out of here now. Fuck these people."

        "Leave through the door that Queen Elizabeth II left wide open.":
            jump escape

        "Dig an underground tunnel system when everyone goes to sleep, leave them behind and escape to a different country, change your name to Jerry, and live happily ever after.":
            
            u "How about we just sleep on it and discuss in the morning?"

            f "Sounds like a fine, albeit suspicious, idea!"

            u "Great! Goodnight everyone!"

            scene bg black with dissolve
            with Pause(2)

            show text "{size=+10}5 years later{/size}" with dissolve
            with Pause(3)

            hide text with dissolve
            with Pause(2)

            $ name = 'Jerry'

            scene bg paris 
            with fade

            "Well, I've really been living an amazing life since that fateful day."

            "Everybody in McCoy's dungeon may have died, but..."

            "I got married, had 34 children, and learned how to cook snail!"

            w "Honey! It's time for our daily cloacal opening exchange!"

            u "Yes dear."

            scene bg black with dissolve
            with Pause(2)

            show text "{size=+20}The End{/size}" with dissolve
            with Pause(3)

            hide text with dissolve
            with Pause(2)

            return

        "Kill yourselves.":
            
            u "How about we kill ourselves?"

            sh "Okay."

            scene bg black 
            with dissolve

            "ouch that fucking hurt."

            return

label shaneconvo:

    sh "[name]?"

    u "Shane?"

    sh "Why the fuck didn't you get caught right away?"

    u "I dunno just interdimensional fuck-ups I guess?"
    u "Anyways, who else is in here?"

    sh "I'm not sure... lemme find a lightswitch."

    "As if there'd be a lightswitch in-"

    scene bg dungeon

    show shane sad at right
    show tied at left

    u "...huh."

    u "Hey... uh... where's Norf and Ford?"

    sh "Well Norf fucking died, they cubified him and he's dead."
    sh "I heard him yelling \"Ah help I'm being turned into a cube ahhh!\" and now he's a paper weight."
    sh "As for Ford... since he had to build the portal all on his own, it apparently didn't work as he intended and his physical being got ripped and torn and completely destroyed by space-time and he's also dead."

    u "Oh."
    u "Well shit."
    u "Anyways we gotta get out of here."

    sh "Which way is out?"

    j "mmphm mphmmmphm mm mmph mmm mphm mmph."

    sh "Not now Jake, we're trying to figure out how to get out of here."
    sh "Do you know the way out, [name]?"

    u "Why am I always the one making these decisions?"

    s "Mmphm mmm mmph."

    menu:

        "Guess I gotta figure out how to get out of here now. Fuck these people."

        "Leave through the door that Queen Elizabeth II left wide open.":
            jump escape

        "Dig an underground tunnel system when everyone goes to sleep, leave them behind and escape to a different country, change your name to Jerry, and live happily ever after.":
            
            u "How about we just sleep on it and discuss in the morning?"

            sh "Sounds like a shitty idea."

            u "Great! Goodnight everyone!"

            scene bg black with dissolve
            with Pause(2)

            show text "{size=+10}5 years later{/size}" with dissolve
            with Pause(3)

            hide text with dissolve
            with Pause(2)

            $ name = 'Jerry'

            scene bg paris 
            with fade

            "Well, I've really been living an amazing life since that fateful day."

            "Everybody in McCoy's dungeon may have died, but..."

            "I got married, had 34 children, and learned how to cook snail!"

            w "Honey! It's time for our daily cloacal opening exchange!"

            u "Yes dear."

            scene bg black with dissolve
            with Pause(2)

            show text "{size=+20}The End{/size}" with dissolve
            with Pause(3)

            hide text with dissolve
            with Pause(2)

            return

        "Kill yourselves.":
            
            u "How about we kill ourselves?"

            sh "Okay."

            scene bg black 
            with dissolve

            "ouch that fucking hurt."

            return

label escape:

    u "Let's leave through the door that Queen Elizabeth II left open!"

    j "mph."

    u "Once we get out, I'll create a distraction for you all to escape."
    u "If all goes well I'll run away like a little girl and we'll steal Queen Elizabeth II and Hot Pocket's transporter."

    sh "I like the sound of that."

    u "Alright, let's go!"

    scene bg volcano
    with fade

    show shane sad at right
    with dissolve

    show tied at left
    with dissolve

    if atFords:

        show ford happy at slightright
        with dissolve

    u "Alright, he doesn't seem to be around."

    u "Let's make a run for i-"

    mc "And just what are you all doing out of the McDungeon!?"

    show mccoy angry at middle
    with dissolve

    mc "How did you all get out!?"

    if atFords:

        f "Queen Elizabeth II left the dungeon door wide open."

        mc "I knew it was a mistake hiring her, that hag."

    else:

        j "mmphm mmphmmmph mm mphm mmm mmmmphm mmph mphm mphm."

        mc "I wasn't asking you, sociopath!"

    show mccoy happy

    mc "Nonetheless..."
    mc "I guess this is the part where you all die."
    mc "It came earlier than I was prepared for but, ah well."

    show shane sad at offright
    with move

    mc "I love unpredictability."

    if atFords:
        show ford happy at offright
        with move

    mc "It makes murdering people much more satisfying!"

    show tied at veryright
    with move

    show mccoy angry

    $ idiots = "."

    if atFords:
        $ idiots = " or Ford."

    mc "Hey, wait a minute!"
    mc "Where do you two think you're going?"
    mc "Frankly, I don't give a damn about Shane[idiots]"
    mc "But you two, along with [name] over here, are the reason I started this idiotic plot in the first place!"
    mc "And I won't be done until all three of you are DEAD!!"

    "Mccoy slowly and dramatically pulls out a gun from his pocket."
    "It's so slow and so dramatic, in fact, that it gives me the perfect oppurtunity to save either Jake or Sans."
    
    menu:

        "But who should I save?"

        "Sans":
            
            "I decided it would be best to save Sans."
            "First, McCoy went for Jake."

            show tied jake

            "He pulled the trigger and Jake went down instantly."
            "As soon as McCoy held the gun up to Sans's face, I readied myself to take the bullet."
            "He pulled the trigger as I jumped in front of Sans."

            scene bg black

            "As my chest was bleeding out, I could still faintly hear McCoy say something to me."

            mc "You do realize I have more than 2 bullets, right?"

            "Fuck."
            "I heard Sans fall to the ground in my final breath."
            "oh fuck I'm dead."

            return

        "Jake":

            "I decided it would be best to save Jake."
            "First, McCoy went for Sans."

            show tied sans

            "He pulled the trigger and Sans went down instantly."
            "As soon as McCoy held the gun up to Jake's face, I readied myself to take the bullet."
            "He pulled the trigger as I jumped in front of Jake."

            scene bg black

            "As my chest was bleeding out, I could still faintly hear McCoy say something to me."

            mc "You do realize I have more than 2 bullets, right?"

            "Fuck."
            "I heard Jake fall to the ground in my final breath."
            "oh fuck I'm dead."

            return

        "Neither of them":
            jump jakearcending

label travelsteak:

    $ sup += 15
    $ bdp += 5
    $ fp -= 10
    $ shp -= 10

    u "I'll head with you guys, Steak-Umm!"

    show shane sad

    sh "Fuck you."

    hide shane
    with dissolve

    f "I respect that, [name]! See you there!"

    hide ford
    with dissolve

    show belle happy at slightleft
    show steak umm at slightright
    with move

    show norf sad

    n "If it's all the same with you three, I'll just be heading with those two."

    u "See ya there, Norf!"

    hide norf
    with dissolve

    bd "The inter-dimensional transporter is back at my place! OwO"

    su "Let us head there then."

    scene bg bdhouse
    with fade

    show belle happy at slightleft
    show steak umm at slightright
    with dissolve

    bd "The device is all set up! >w>"

    u "Will it work properly?"

    su "How do you think we got here?"

    u "Good point."

    bd "Alright, boys! Let's go!! >w<"

    scene bg black with fade
    with Pause(2)

    "..."

    u "Hello?"

    "..."

    u "Anybody there?"

    n "Hello??"

    u "Norf? Is that you?"

    q "Shut the hell up!!"

    u "Who's there?"

    n "Wait... who are you??"
    n "Stay away from me!"

    u "Norf, are you okay!?"

    n "Queen Elizabeth II??"

    qe "I said shut the hell up!"

    n "Wait... stop!"
    n "What are you doing??"
    n "Ah!! Help!!" 
    n "I'm being turned into a cube!!" 
    n "Ahhhhh{size=-5}hhh{/size}{size=-10}hhh...{/size}"

    "..."

    u "Norf...?"

    scene bg dungeon

    if uwuwater:

        show belle happy

        bd "Hey [name]~! UwO"

        u "Oh thank God you're here Belle."
        u "Are you sure we're in the right dimension?"
        u "Did you manage to see what was happening to Norf?"

        bd "Shshshsh. Forget about all of that, sweetie~! U3O"

        u "Uh..."

        bd "You said that you'd let me show you how I make my bathwater! -w-"
        bd "So why don't you just sit back, relax, and let the show begin. :)"

        show belle happy at slightleft
        with move

        show bath at slightright
        with dissolve

        show belle queen
        with dissolve

        show belle queen at slightright
        with move

        qe "I hope you don't mind wrinkles!"

        scene bg black
        with dissolve

        "So this is how I spend the rest of my life?"
        "Watching Queen Elizabeth II bathe in a bathtub somewhere deep in a dungeon?"
        "Alright."

        scene bg black with dissolve
        with Pause(2)

        show text "{size=+20}The End{/size}" with dissolve
        with Pause(3)

        hide text with dissolve
        with Pause(2)

        return

    else:

        show belle angry

        u "Oh thank God you're here Belle."
        u "Is everything alright?"

        bd "Shut the hell up."

        u "Uh..."

        bd "You declined my proposal to watch me bathe."

        u "Well of fucking course I did, that's fucking weird!"

        bd "I said shut the hell up!"
        bd "Do you wanna know what happened to Norf?"
        bd "Do you really wanna know??"

        u "Well... yeah, of course."

        show belle happy

        bd "Alright! Hehehe! Let me show you!"

        show belle norfhap

        bd "Here he is!"

        u "WHAT THE FUCK-"

        show belle norfang

        bd "This is what happens when you deny me, [name]!"
        bd "You get turned into a paperweight!"
        bd "And now it's your turn!"

        show belle norfhap

        bd "Come here, sweetie~! :)"

        scene bg black 
        with dissolve

        "Oh god I can feel myself being cubified oh my god the walls are closing in I'm being turned into a paperweight aw fuck I'm dead and useless."

        return

label jakearcending:

    "I decided it would be best to save myself instead of either of them."
    "First, McCoy went for Sans."

    show tied sans
    
    "And secondly, Jake."

    show tied both

    scene bg black
    with dissolve

    "I ran as fast as I could out of that hellhole."
    "I didn't know where I was going, but that didn't matter."
    "As long as I could get as far away as possible from McCoy, that's all that mattered."
    "..."
    "......"
    "........."

    
    scene bg black with dissolve
    with Pause(2)

    show text "{size=+10}Epilogue{/size}" with dissolve
    with Pause(3)

    hide text with dissolve
    with Pause(2)

    if atFords:

        scene bg endford
        with fade

        "Ford went on to finally get back to his own dimension. Turns out he wasn't lying afterall!"
        "Unfortunately, opening the portal caused pieces of our dimension to get through, making his just as ugly as ours was."
        "Hopefully he doesn't mind too much."

    scene bg endshane
    with fade

    "Shane decided to make his next documentary series about everything that had happened since he arrived at the school. Apparently he was secretly recording the whole time."
    "The series got a total of 200M views and he quit YouTube afterwards to pursue his makeup business."
    "The makeup was toxic and caused a global pandemic."

    scene bg exschool
    with fade

    "As for me, I'm still going to school."
    "Nothing is different."
    "Except all of my friends are gone."
    "But that's alright."
    "I literally hated all of them anyways."
    "..."
    "Go away."
    "..."
    "FUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUCK"

    scene bg black with dissolve
    with Pause(2)

    show text "{size=+20}The End{/size}" with dissolve
    with Pause(3)

    hide text with dissolve
    with Pause(2)

    return

#CHAPTERTHREE
label shanearc:

    scene bg black
    with Pause(2)

    show text "{size=+10}Chapter 3{/size}" with dissolve
    with Pause(3)

    hide text with dissolve
    with Pause(2)

    play music "music/placeholder2.mp3"

    "Well, a new day, and a new romance is blooming."
    "I can't wait to see where this ends up leading."

    scene bg classroom
    with dissolve

    "Class was about to start and it turns out Jake and Shane ended up in my class, along with Sans and Betty."
    "I guess Sans is lucky he gets to be with his boyfriend, and he really seems to like it!"

    show shane happy at slightleft
    show sans happy at slightright
    with dissolve

    u "So you guys seem to be a good fit then?"

    s "We had a serious fuck session last night!"

    sh "Yeah he made my dick purple!"
    sh "I love purple dicks!!"

    s "He really does."

    u "Well, I'm glad you two love each other very much!"

    "The bell rang and everyone took their seats."

    hide sans
    hide shane
    with dissolve

    "I started zoning out right away, because Buddy didn't feel like drawing a teacher character so we're just gonna skip the class period."
    "By the time I came back to reality, everyone was leaving the classroom."
    "Except for Sans, Betty, Jake, and Shane of course."

    show sans happy at veryleft
    show betty happy at slightleft
    show jake happy at slightright
    show shane happy at veryright
    with dissolve

    b "I'm glad you two are getting along well..."

    j "you sound jealous."

    show betty angry
    show sans sad
    show shane sad
    show jake sad

    b "I'M NOT JEALOUS!!"

    "..."

    show betty sad

    b "I'm... very happy for you, Sans."

    show sans happy

    s "Well thank you, Betty."

    "She's definitely jealous."

    show betty angry

    b "Shut up, [name]!"

    show sans sad
    show betty sad

    b "I.. I have to go..."

    hide betty
    with dissolve

    "Maybe I was too hard on Betty..."

    u "Hey guys, I'm gonna go see if she's alright."

    show shane happy

    sh "That's fine, do what you gotta do!"

    scene bg hallway
    with dissolve

    u "Betty?"

    show betty sad at middle
    with dissolve

    b "What do you want?"

    u "I'm sorry for being too hard on you... I know it must be hard..."
    u "Do you want me to take you out to dinner, or something?"

    "Wait... what the FUCK am I saying???"

    show betty happy

    b "Despite what you just thought in your head, I'd LOVE to go on a dinner date with you!!"

    u "No not a dinner date just like..."

    b "Let's go!"

    scene bg room
    with fade

    "Ah, my room."
    "I hate it so damn much."
    "{i}...even if it is the best looking place in this game so far... sadly...{/i}"
    "I guess I better find my nice clothes."
    "I wonder how fancy Betty will be dressing... she does think it's a dinner date afterall... would a long sleve shirt be good enough, or should I throw on a full tuxedo...?"

    menu:

        "I don't want to look uglier than her..."

        "Dress casually fancy":
            jump notfancy2

        "Dress {b}fancy{/b} fancy.":
            jump fancy2

label notfancy2:

    "I suppose a long sleeve shirt should be good enough."
    "Alright, guess I'm fine the way I am!"
    "Let's get this over with."

    scene bg dinner
    with fade

    "Well, I've made it."
    "Seems like I made it early too, she isn't even here..."

    q "Hey, you there!"

    u "Huh?"

    "I turn around and there's a big, thick man with huge shoulders, a sexy collarbone, floofy hair, and broken glasses standing in front of me. He also has a nice suit on... something I don't have..."

    show ford happy
    with dissolve

    "He looked like a hotter version of Mr. Norf... with a nose."
    "I am extremely aroused by this"

    u "Um... hi?"

    q "You're not lookin' very fancy today, are you?"

    $ fp -= 10

    u "No, I didn't think I had to."

    q "Are ya kidding? This is the fanciest place in town!"
    q "Anyway, enough pickin' on ya. The name's Ford."

    f "I have wet dreams about an Illuminati man sometimes."

    u "...fun."

    "Just as the conversation was getting interesting, Betty arrived."

    show ford happy at slightright
    with move

    show betty happy at slightleft
    with dissolve

    b "Hey, [name]!"

    u "You didn't dress fancy either, huh?"

    show betty sad

    b "What do you mean...?"

    f "Heh... uh... well... anyways-"
    f "I'm your waiter for the evening."
    f "Somehow, unforeseen circumstances led me to your dimension, and it could cost me a lot of money to get materials to make a new portal to get back home."
    f "So in the meantime I am stuck waiting tables."

    "Our dimension? What on earth is he talking about?"
    "Is that why he looks so sexy?"

    show betty angry
    
    b "HEY WHAT THE FUCK WE'RE ON A DATE HERE!!!"

    "..."

    f "Anyway, please take a seat here."

    "We sat down at the table he pointed to."

    show betty happy

    f "Would either of you care for a drink? We have water, soda, or Mabel Juice."

    "I didn't know what Mabel Juice was, but I needed to try it."

    u "May I have some Mabel Juice?"

    f "Sure thing! How about you?"

    b "I'll have a water!"
    b "Gotta keep the fat to a minimum, don't you think, [name]?"

    u "Yeah, of course."

    show betty angry

    b "Are you implying that I'm fat!??"

    u "No! I... uh..."

    f "Coming right up!"

    hide ford
    with dissolve

    show betty at middle
    with move

    b "I can't believe you're treating me like this on our dinner date!"

    show betty sad

    b "Is that why you asked me out in the first place? Just to shit on me?"

    u "No! Of course not-"

    show ford happy at slightright
    with dissolve

    show betty sad at slightleft
    with move

    f "Here you are, I hope that these drinks have been made to your liking."

    "He hands me a pink substance, which I assume is the Mabel Juice."

    u "What's in this?"

    f "All I know is that it has plastic dinosaurs and plastic ice cubes in it, and that it looks like if coffee and nightmares had a baby."
    f "Enjoy!"

    "I just stared at the drink..."

    f "Is there anything on the menu that would satisfy your appetites?"

    fc "{size=+20}CUDDLES ARE ALWAYS AN OPTION TOO{/size}"

    show betty happy

    b "I'll have a large cheesecake!"

    "I thought she was watching her weight..."

    show betty angry

    b "ONE MORE PEEP OUT OF YOU AND I'M GONNA MURDER YOU!!!"

    "..."

    f "Alright, one cheesecake, anything else?"

    python:
        food = renpy.input("I told Ford what I wanted too...")
        food = food.strip()

        if not food:
             food = "burger"



    u "I'll have a large [food], please!"

    f "One [food] coming right up!"

    hide ford
    with dissolve

    show betty at middle
    with move

    "Ford walked away, so I figured now would be a good time to start some awkward small talk that usually happens during \"dates\"..."

    menu:

        u "So..."

        "Talk about the weather.":
            jump awkwardnight2

        "Talk about politics.":
            jump awkwardnight2

        "Talk about sex.":
            jump awkwardnight2

        "Talk about sports.":
            jump awkwardnight2

label awkwardnight2:

    u "...why don't we discuss-"

    b "Shut up!"
    b "What the hell is wrong with you?"
    b "I thought you were finally going to try and make me happy for once!"
    b "But instead it's just one insult after another!"
    b "Everyone, everyday!"
    b "I thought tonight was finally the night I would get what I wanted, but instead I got more of the same shit I get at school!"

    show ford happy at slightright
    with dissolve

    show betty at slightleft
    with move

    f "Here is your cheesec-"

    b "I'm tired of it, [name]!"
    b "This date sucked!"
    b "Good riddance to you, and I hope I never have to see you again!"

    hide betty
    with dissolve

    show ford at middle
    with move

    f "Um..."
    f "...here is your large [food]."

    u "Thanks."

    hide ford
    with dissolve

    "I sat there silent for a little while to eat my food."
    "Ford returned to get my plates."

    show ford happy at middle
    with dissolve

    f "So, how'd you like the food?"

    u "It was fine."

    "I haven't even touched my Mabel Juice."

    f "Well I'm glad!"

    "I left the money at the table and stood up to leave, without even saying a word."

    hide ford
    with dissolve

    "Tonight was pretty unsuccessful."
    "I made everything even worse for Betty."
    "Oh well, I guess it's time to go home."

    f "Hey!"

    "I heard Ford's voice boom across the diner."

    show ford happy
    with dissolve

    f "I need your assistance with something, [name]."

    u "You need {i}my{/i} assistance?"

    f "Yes, you seem very intelligent compared to most people in this universe, so I think you'd be perfect!"

    menu:
        "Are you willing to do it?"

        "Sure":

            u "Um... sure?"

            f "Great! I'll see you at my house in an hour, here's my address."

            $ fp += 5

            "Ford handed me a card with an address on it."

            u "See ya!"

            jump fordshouse
        
        "No, sorry":

            u "Sorry, but I'm not interested."

            f "Aw, that's too bad."

            $ fp -= 5

            f "Oh well. Maybe I can get back within the week still, even when building solo."

            hide ford

            "Well that was... odd..."

            jump anotherday2

label fancy2:

    "I guess I should look as good as possible, since this'll be a big moment for Betty."
    "She's always wanted to date me."
    "And despite this not being a dinner date, she thinks it is, so I shouldn't ruin that for her."

    scene bg dinner
    with fade

    "Well, I've made it."
    "Seems like I made it early too, she isn't even here..."

    q "Hey, you there!"

    u "Huh?"

    "I turn around and there's a big, thick man with huge shoulders, a sexy collarbone, floofy hair, and broken glasses standing in front of me. He also has a nice suit on... something I don't have..."

    show ford happy
    with dissolve

    "He looked like a hotter version of Mr. Norf... with a nose."
    "I am extremely aroused by this"

    u "Um... hi?"

    q "You're lookin' quite sexually attractive today, aren't you?"

    $ fp += 10

    u "Is it because of the suit?"

    q "Yes! You made a good choice wearing that, I woulda had to pick on you a little if you didn't."
    q "Anyway, enough about that. The name's Ford."

    f "I have wet dreams about an Illuminati man sometimes."

    u "...fun."

    "Just as the conversation was getting interesting, Betty arrived."

    show ford happy at slightright
    with move

    show betty happy at slightleft
    with dissolve

    b "Hey, [name]!"

    u "You didn't dress fancy, huh?"

    show betty sad

    b "What do you mean...?"

    f "Heh... uh... well... anyways-"
    f "I'm your waiter for the evening."
    f "Somehow, unforeseen circumstances led me to your dimension, and it could cost me a lot of money to get materials to make a new portal to get back home."
    f "So in the meantime I am stuck waiting tables."

    "Our dimension? What on earth is he talking about?"
    "Is that why he looks so sexy?"

    show betty angry
    
    b "HEY WHAT THE FUCK WE'RE ON A DATE HERE!!!"

    "..."

    f "Anyway, please take a seat here."

    "We sat down at the table he pointed to."

    show betty happy

    f "Would either of you care for a drink? We have water, soda, or Mabel Juice."

    "I didn't know what Mabel Juice was, but I needed to try it."

    u "May I have some Mabel Juice?"

    f "Sure thing! How about you?"

    b "I'll have a water!"
    b "Gotta keep the fat to a minimum, don't you think, [name]?"

    u "Yeah, of course."

    show betty angry

    b "Are you implying that I'm fat!??"

    u "No! I... uh..."

    f "Coming right up!"

    hide ford
    with dissolve

    show betty at middle
    with move

    b "I can't believe you're treating me like this on our dinner date!"

    show betty sad

    b "Is that why you asked me out in the first place? Just to shit on me?"

    u "No! Of course not-"

    show ford happy at slightright
    with dissolve

    show betty sad at slightleft
    with move

    f "Here you are, I hope that these drinks have been made to your liking."

    "He hands me a pink substance, which I assume is the Mabel Juice."

    u "What's in this?"

    f "All I know is that it has plastic dinosaurs and plastic ice cubes in it, and that it looks like if coffee and nightmares had a baby."
    f "Enjoy!"

    "I just stared at the drink..."

    f "Is there anything on the menu that would satisfy your appetites?"

    fc "{size=+20}CUDDLES ARE ALWAYS AN OPTION TOO{/size}"

    show betty happy

    b "I'll have a large cheesecake!"

    "I thought she was watching her weight..."

    show betty angry

    b "ONE MORE PEEP OUT OF YOU AND I'M GONNA MURDER YOU!!!"

    "..."

    f "Alright, one cheesecake, anything else?"

    python:
        food = renpy.input("I told Ford what I wanted too...")
        food = food.strip()

        if not food:
             food = "burger"



    u "I'll have a large [food], please!"

    f "One [food] coming right up!"

    hide ford
    with dissolve

    show betty at middle
    with move

    "Ford walked away, so I figured now would be a good time to start some awkward small talk that usually happens during \"dates\"..."

    menu:

        u "So..."

        "Talk about the weather.":
            jump awkwardnight2

        "Talk about politics.":
            jump awkwardnight2

        "Talk about sex.":
            jump awkwardnight2

        "Talk about sports.":
            jump awkwardnight2

label anotherday2:

    scene bg exschool
    with fade

    "Another day, another dollar... I wish... since I'm poor as hell..."
    "I wonder how Betty's doing after last night."

    scene bg hallway
    with dissolve

    "Oh, well look who decided to show up."

    show sans sad
    with dissolve

    s "[name]! Help!"
    s "Betty won't leave me alone!"
    s "She came to my house after you ruined your date with her!"

    u "What?"

    s "I may have accidentally had sex with her out of sympathy..."
    s "Like... really hard sex... very rough..."
    s "Like we got complaints from the neighbors because she was screaming so hard."
    s "I don't want Shane to find out but she won't stop talking about it!!!"

    hide sans
    with dissolve

    "What the fuck..."

    scene bg classroom
    with dissolve

    "Class was as boring as ever, though Sans and Betty didn't show up."
    "I guess they were in the band hallway banging some more."

    show shane sad
    with dissolve

    sh "Hey, [name]..."

    u "Hey, Shane! What's wrong?"

    sh "I'm sad."

    u "Well no shit... that's why I asked what was wrong."

    sh "It's just..."
    sh "Alright look. I really love Sans."
    sh "But I think he's cheating on me with Betty... I don't know how to bring it up to him, though..."

    u "Maybe it would be easier to tell him while shoving your cock into his ribcage!!"

    sh "I highly doubt it... he takes viagra before we have sex now..."

    show shane sad at slightleft
    with move

    show sans sad at slightright
    with dissolve

    s "Hey... uh... what are you guys talking about?"

    sh "Um..."

    u "Tell him what you told me this morning, Sans."

    s "..."
    s "I... uh..."
    s "Okay, fine!"
    s "I've been hooking up with Betty..."
    s "But her boobs are just so much bigger than yours!"

    sh "Why do you have to bring my boobs into it??"

    s "Because it's sex!"

    show shane angry

    sh "Well you know what, Sans??"
    sh "Fuck you!"
    sh "In the non-sexual way!"
    sh "Dating you was a mistake, I don't even know why I bothered."
    sh "No wonder Betty broke up with you before."
    sh "You're a shitty fucking pedophile."
    sh "The only thing you're good for is sex, and let's face it."
    sh "YOU AREN'T EVEN GOOD AT THAT!!"

    hide shane
    with dissolve

    show sans at middle
    with move

    u "..."

    show sans angry

    s "..."

    $ shp -= 5
    $ sp -= 5

    hide sans
    with dissolve

    "Well... it was good while it lasted..."

    scene bg roomnight
    with dissolve

    "Today was such a weird day, I can't even think of anything to do besides sleep."
    "At least I know that it can't get any weirder..."

    scene bg black
    with fade

    scene bg droom
    with fade

    "Ah, that was a good sleep, though it did feel kinda quick..."
    "Oh well, I better get to school."

    scene bg dschool
    with fade

    "I wonder if today will be any different from yesterday..."
    "I would hope so anyway..."

    scene bg dhallway
    with dissolve

    "I can't help but feel like something is off..."

    show ford happy
    with dissolve

    f "Hey, [name]!"

    u "Oh, hey Ford!"

    f "Would you mind helping me with something?"

    u "What?"

    f "...do you know how to contact a military general...?"

    "...?"

    u "Excuse me?"

    f "...nevermind..."

    hide ford
    with dissolve

    "That... was very weird..."

    scene bg dclassroom
    with dissolve

    "Well the classroom seems normal at least."

    show norf happy
    with dissolve

    n "Welcome to class!"
    n "Today we'll be joining the military!"

    u "What??"

    n "You have no choice! Everyone is going to war!"

    u "That's..."
    u "..not okay..."

    show norf angry

    n "Nobody asked you!"

    show mcdream
    hide norf
    with dissolve

    u "Um... who the hell are you..."

    q "Heh heh heh..."

    scene bg black
    with fade

    u "Wha-aaAAHAHHH--"

    scene bg room

    "Huh?"
    "What the fuck..."
    "That was unlike any dream or nightmare that I've had before..."
    "What was that demon...?"
    "What was any of that...?"
    "I should do some research on it... maybe Sans will know something too..."
    "I'll ask him tomorrow morning when he stalks me by my locker."

#CHAPTERFOUR
    scene bg black
    with Pause(2)

    show text "{size=+10}Chapter 4{/size}" with dissolve
    with Pause(3)

    hide text with dissolve
    with Pause(2)

    play music "music/placeholder2.mp3"
    scene bg hallway
    with fade

    show betty sad
    with dissolve

    b "Hey, [name]. Have you seen Sans this morning?"

    u "No... I can't say I have. I've been expecting to see him here by my locker."
    u "Maybe he's in the bathroom fucking Shane or something?"

    b "Oh please, after what happened yesterday? I'm sure Sans chose me over Shane..."
    b "...I hope..."

    hide betty
    with dissolve

    "Well I guess I should check the bathroom."

    scene bg black
    with fade

    "Outside the restrooms, I knock on the door."

    u "Sans?"
    u "Shane?"

    scene bg bathroom
    with fade

    "Well, they don't seem to be anywhere in here."
    "Oh well... maybe they stayed home together."
    "Guess I better head back to class."

    scene bg black
    with fade

    q "Wait a minute~! Don't leave yet! >w>"

    u "What?"

    scene bg bathroom
    with fade

    u "Who said that?"

    show belle happy
    with dissolve

    q "Me of course! <3"

    u "{size=+10}{b}WHAT THE FUCK!?{/b}{/size}"
    u "This is the boys bathroom... what are you-"

    q "Hush now silly~ UwO"

    q "My name is Belle. Belle Delphine! >w<"

    bd "I've come to this school as a traveling merchant to sell my bathwater to your fellow classmates! :D"

    u "Wha-"

    bd "{size=-5}{i}I'm also undercover for a very important mission, but I'll get into that later. ;){/i}{/size}"
    bd "The point is, you are part of the plan! So I hope you're ready for whatever happens next~ -u-"

    u "Look... all I wanna know right now is, where are Sans and Shane?"

    show belle sad

    bd "Who? ÒnÕ"

    u "Wait... so you have nothing to do with their disappearence?"

    show belle happy

    bd "Nope! But we can investigate that when we need to. For now, follow me! ^u^"

    hide belle
    with dissolve

    u "Wait but-... alright..."

    "Why does this week just keep getting weirder...?"

    scene bg black
    with fade
    with Pause(1)

    scene bg outside1
    with fade

    show belle happy
    with dissolve

    u "So what's going on here?"

    show belle angry

    bd "Hush! I'll be asking the questions for now! ÒnÓ"

    show belle happy

    bd "So... did you happen to have a scary nightmare last night by any chance? OwO"

    u "How did you-"

    bd "{size=+10}PERFECT! OuO{/size}"
    bd "This will help us figure out exactly what's been going on he-"

    show belle sad

    n "{size=+20}{b}[name]!!!{/b}{/size}"

    show belle sad at slightleft
    with move
    show norf angry at slightright
    with dissolve

    n "Where have you been!? I haven't seen you in any of your classes recently!"

    u "I... uh... this girl..."

    n "Oh so you're going to fuck her now huh?"
    n "Instead of getting a good education?"

    show belle angry

    n "Ya know, I think I've fucked every single person in the classroom except for you."
    n "Is this why you're sneaking away to-"

    show belle happy

    bd "Hey~! UwU"

    show norf sad

    bd "Enough yelling. Would you like to buy some of my used bathwater~? ;)"

    show norf happy

    n "Used bathwater you say?"
    n "Well don't mind if I do!"

    bd "That'll be $35 please! ^w^"

    "What on earth?"

    n "Thank you so much!"
    n "Sorry for getting mad at you, [name]. She's a keeper, don't let her down! Go ahead and fuck!"

    hide norf
    with dissolve
    show belle happy at middle
    with move

    u "But we're not- oh nevermind."

    bd "Alrighty then! Let's head over to my house! UuO"

    scene bg black
    with fade

    "Well... I'm in her house... but I can't see a damn thing."

    u "Isn't it kind of dark in here?"

    bd "A lil bit, just feel your way around! :)"

    "What the fuck am I touching right now?"

    u "Uh... Belle? What is this?"

    bd "Hehehe! OuU"

    u "Why is it wet....."

    bd "Don't worry about that~! ;P"
    bd "Hey, here's the lightswitch! :D"

    scene bg bdhouse
    show belle coke

    bd "There we go! >w<"

    u "Why are you holding a Coke?"

    bd "Because I'm thirsty? What'd you think you were touching before I got the lights on? @-@"

    "..."

    show belle coke

    bd "Anyways, this is my house! ^-^"

    show belle coke at left
    with move

    bd "As you can see, people have really been enjoying my bathwater! OwO"

    show belle happy at middle
    with move

    menu:

        bd "Would you care to see how it's made? -w-"

        "No way.":
            u "N.. no... thank you..."

            show belle sad

            bd "Fair enough. UnU"

            $ bdp -= 15

        "Sure!":
            u "Hmmm... yeah sure! Why not!"

            bd "Yaas! >w> I'll let you check it out later tonight when I make more~!"

            $ bdp += 15
            $ uwuwater = True

    show belle happy

    bd "Anyways, I'd like you to meet my co-partner for this mission I'm on!"

    show belle happy at slightleft
    with move

    bd "Steak-Umm! Come on out!"

    show steak umm at slightright
    with dissolve

    su "Hmm, yes. Hello there sir."
    su "The name is Umm. Steak-Umm."

    u "Uh... my name is [name]..."

    su "So, [name], you have a lot to learn about our mission still, is that correct?"

    u "Yeah. I have no fucking clue what is going on anymore... with anything."

    "I just wish they'd help me find out where Sans and Shane are already so I could get the hell out of here."

    bd "Steak-Umm here is another undercover spy helping me out."

    u "Doesn't a walking, talking box of frozen beef sheets seem a bit suspicious?"

    su "This place seems just crazy enough that nobody will even notice."

    "He does have a point here."

    su "Steak-Umm is better than Hot Pockets."

    u "What?"

    bd "He's required to say that every so often."

    su "Anyways, enough chitter chatter. Let us continue with this mission."
    su "You have been having scary nightmares with demons, correct, [name]?"

    u "Just one, but yeah."

    u "Although it was hard to tell if it was a demon or a normal man. There was lots of talk about the military."

    su "Just as I suspected."

    u "What do you mean?"

    bd "We've been monitoring the brain activity of lots of individuals recently! ~w~"

    su "We picked up signals of a demon-like creature hopping from brain to brain throughout the multiverse."
    su "When it arrived here, we knew it would not be hard to catch up with, since everybody in this universe is so slow minded."

    u "Hey!"

    bd "That's why we've come to you for answers! ^w^"
    bd "Your brain is so slow that we managed to catch up within 12 hours of you having the dream! >u<"

    u "Stop saying that!"
    u "And what are you talking about with this whole multiverse thing?"
    u "You mean to tell me that you guys aren't from here?"

    su "Is it not obvious from our appearance?"
    su "Everybody in this universe has a misshapen, blobby form to them."

    u "But... Jake and Shane don't look that way..."

    show belle sad

    bd "You mean Jake Fucking Paul? OnO"

    su "Ah, Jake and Shane. They are not from this universe either."
    su "They are from the same universe as us."
    su "Unfortunately."
    su "It seems that the demon-creature brain-hopping around has caused these universes to collide somehow."

    u "So that explains how Ford ended up here as well!"

    su "Another one??"
    su "How many dreams has this demon visited???"
    su "We must gather up everyone from here that is from an alternate universe, that is our first step to defeating this vile creature!"

    u "Yeah... one problem with that plan."
    
    bd "[name] mentioned earlier that Shane and Sans have been missing all morning. >~<"

    u "We can't continue this mission without Shane."
    u "Like you said, we need everybody that's from an outside universe, and that includes him."

    su "Then we must search for them!"
    su "When and where did you last see those two?"

    u "Last time I saw Shane was when he and Sans had a major fight in class."
    u "The same goes for Sans."

    bd "What about Jake... ?-?"
    bd "Does he have a girlfriend? >o<"

    u "Not that I know of..."

    bd "Good!"

    show belle angry

    bd "The dude is a sociopath! >>O<<"

    su "Anyways, let us get going! I have been continuing to monitor the brain activity here all morning, and the demon is still here."
    su "We do not have long until he gets bored with this place and moves on to another universe. We must get going!"

#CHAPTERFIVE
label thehunt2:

    scene bg black
    with Pause(2)

    show text "{size=+10}Chapter 5{/size}" with dissolve
    with Pause(3)

    hide text with dissolve
    with Pause(2)

    play music "music/placeholder3.mp3"
    scene bg noutside
    with fade

    show steak umm at slightleft
    show ford happy at littleright
    show belle sad at veryleft
    show jake sad at middle
    show betty sad at slightright
    show norf sad at veryright
    with dissolve

    u "Sans?"

    n "Shane!"

    b "Sans!? Can you hear me honey??"

    show jake angry

    j "oh would you shut the fuck up he wants to be with shane you whore."

    b "..."

    show jake sad

    f "We've been searching all day. I'm afraid it's no use."

    u "We can't just give up!"

    show norf angry

    n "Well what else are we supposed to do? They are nowhere to be found!"

    show norf sad

    su "Wait just a meaty minute!"
    su "I have just picked up some new signals!"
    su "It seems that the creature temporarily left this universe and then returned a few minutes later!"

    show norf happy

    n "Maybe he got horny."

    bd "Do you think it took Shane and Sans with? >->"

    show norf sad

    su "I know it did!"
    su "According to my readings, two unidentified objects exited this universe with the creature."

    show jake happy

    j "well that must be them"

    f "We gotta get there fast! Do you know what dimension they went to?"

    su "It seems the demon is only able to travel through the multiverse in a linear fashion, so it should be the next universe from here: our universe!"

    show belle happy

    bd "Yes! ^O^"
    bd "I can't wait to finally go home!!! >w<"

    "..."

    show belle sad

    "..."

    bd "And save your friends, of course~ ^u^;"

    show belle angry

    bd "Let me have my moment... -.-"

    show belle happy
    show norf happy

    f "It seems we're only a few blocks away from my house!"

    if atFords:

        f "We can use my portal that [name] and I built a few days ago! I finally got AA batteries!"

    else:

        f "We can use my portal that I built a few days ago! I would've used it sooner but I forgot to buy AA batteries!"

    su "Hmm... Ford... I am not so certain about that..."

    show belle sad

    bd "Yeah, we have our own multiverse-traveling gizmos that we can use! ^u^"

    show belle happy

    bd "And they're rechargable! OwO"

    show belle sad

    su "Not to mention there is no guarantee that your portal device will work."
    su "Am I right to assume it has not been tested yet?"

    f "Well no... but where I'm from, I'm the finest scientist in the world!"

    su "I do not want to take the risk..."

    bd "Neither do I. UnU"

    show belle happy

    bd "I'll be heading with Steak-Umm! >w>"

    show betty happy

    b "Don't worry, Ford! I'll head with you."

    j "me too you seem like a cool bro."

    show jake sad
    show belle sad

    j "i'd rather go with people i know than some random cosplayers."

    show belle happy
    show jake happy

    menu:

        f "Who will you be heading with, [name]?"

        "I'll go with Ford.":
            jump travelford2

        "I'll go with Steak-Umm.":
            jump travelsteak2

label travelford2:

    $ fp += 15
    $ jp += 5
    $ sup -= 10
    $ bdp -= 10

    u "I'll head with you, Ford!"

    show belle sad

    su "Very well then."
    su "We will see you guys there..."
    su "...hopefully..."

    hide steak
    hide belle
    with dissolve

    show jake happy at left
    show ford happy at right
    show betty happy at middle
    with move

    show norf sad

    n "If it's all the same with you four, I'll just be heading with those two."

    u "See ya there, Norf!"

    hide norf
    with dissolve

    f "Alright you three! We don't have much time."
    f "Follow me to my house and we'll get the portal powered up!"

    scene bg insidefhouseportal with fade
    with Pause(1)

    scene bg portalon with dissolve
    with Pause(1)

    show jake happy at left
    show ford happy at right
    show betty happy at middle
    with dissolve

    f "Well, it's ready!"

    b "Let's head through! I need to see Sans's cock! GOD I'm so horny!!"

    "..."

    show betty sad

    b "...and save Shane..."

    if atFords:

        hide ford
        hide jake
        hide betty
        with dissolve

        "I can't believe I'm about to jump into a portal that leads to a completely new dimension..."
        "This morning seemed so normal at first...aside from the nightmare..."
        "What a weird ass day."

        jump arriveford2

    else:

        hide ford
        hide jake
        hide betty
        with dissolve

        "I can't believe I'm about to jump into a portal that leads to a completely new dimension..."
        "I'm surprised Ford was actually able to build this on his own..."
        "Oh well... here goes nothing!"

        jump arriveford2

label arriveford2:

    scene bg volcano with fade
    with Pause(2)

    "Huh... where is this place...?"
    "This certainly feels just as shitty as my dimension..."
    "And where is everyone??"

    q "Mmph! Mmph mm!"

    "Wait...? Where is that coming from?"

    q "MMPH!!!"

    show tied2 at middle
    with dissolve

    u "Shane? Sans??"

    s "Mmph! Mm mmphmph mm!"

    u "It would probably help if I got the tape off of your mouths. Lemme-"

    q "Not so fast!"

    show tied2 at left
    with move

    show mccoy happy at slightright
    with dissolve

    q "Hello there."

    u "Who in the everliving fuck are you?"

    q "Well why don't you allow me to introduce myself?"
    q "My name is General Mccoy."

    mc "I'm generally a general for generalized military purposes."
    mc "I also run a surpisingly successful burrito stand."

    show mccoy angry

    mc "There was a damn taco stand across the street that really got on my nerves."
    mc "The owner was the worst."
    mc "\"Wah!\" this and \"Wah!\" that; just shut up!"

    show mccoy happy

    mc "So I murdered him and his customers."

    sh "Mph mmph."

    show mccoy angry

    mc "Quiet you!"

    show mccoy happy

    mc "Anyways, I hope you enjoy your visit to Nevada."

    u "This is just a molten volcano."

    mc "Exactly."

    "This dude is a fucking bully."

    $ question1 = False
    $ question2 = False
    $ question3 = False
    $ question3b = False

label mccoytalk2:

    if question1 and question2:
        jump endtalk2

    menu:

        "I really gotta figure out what's going on."

        "Why did you kidnap Sans and Shane?":
            jump whykidnap2

        "What dimension is this?":
            jump whatdimension2

        "Are you single?":
            jump aresingle2

label whykidnap2:

    u "Why did you kidnap Sans and Shane in the first place?"

    if question1:

        show mccoy angry

        mc "Did you listen to anything I just said?"
        mc "I'm not repeating myself."

        jump mccoytalk2

    else:

        $ question1 = True

        show mccoy happy

        mc "There are an abundance of problems with Sans and Shane as a couple."

        s "Mph!"

        mc "They both don't get along despite the fact that they both love each other!"

        show mccoy angry

        mc "Shane is MADLY in love with Sans but Sans keeps hooking up with Betty."
        mc "Sans is a pedophile."

        show mccoy happy

        mc "Need I say more?"

        u "But what are you planning to do to them?"

        mc "Um... kill them, obviously."
        mc "Their love affair needs to be put to rest."
        mc "That's why I will also be killing Betty, to put an end to the entire love triangle."

        sh "MMMPH???"

        jump mccoytalk2

label whatdimension2:

    u "What dimension is this anyways? This doesn't look like what Belle and Steak-umm described."

    if question2:

        show mccoy angry

        mc "I literally just explained everything to you."
        mc "Like... everything."
        mc "What the hell is actually wrong with you."

        jump mccoytalk2

    else:

        $ question2 = True

        show mccoy happy

        mc "Ah yes. Belle and Steak-umm."
        mc "They certainly gave you a lot of info, didn't they?"
        mc "I sure hope you took it all with a grain of salt."

        u "What do you mean?"

        mc "Belle! Steak-umm! Come on out!"

        show mccoy at slightleft
        with move

        show belleumm nice behind mccoy at right
        with dissolve

        u "Belle! Steak-umm!"

        show mccoy angry

        mc "Shut up!"

        show mccoy happy

        mc "Go ahead you two. Reveal your true identities."

        show belleumm evil
        with dissolve

        u "What...?"
        u "Hot Pockets...?"
        u "Queen Elizabeth II??"

        "I can't believe it."
        "This whole time I trusted them..."
        "...these two strangers that I had never met before... one an e-thot... the other a box of frozen beef sheets..."
        "...betrayed me???"

        u "So everything you guys said was a lie? The inter-dimensional travel? The dream demon? The bathwater? It was all fake?"

        qe "Of course it was, you fucking idiot."

        u "But what about that dream I had about military generals?"
        u "The one you guys asked me about when we first met?"

        hp "That was just a lucky coincidence. We did not expect you to actually have had the dream."

        mc "Their job was to lure you into this place so I could kill you as well."
        mc "Looks like everything has gone according to plan."

        jump mccoytalk2

label aresingle2:

    u "Are you, by any chance, single?"

    show mccoy angry

    if question3b:

        mc "..."

        jump mccoykillsyouforcomingontohim2

    elif question3:

        mc "Didn't you just... didn't you already ask me that??"

        $ question3b = True

        jump mccoytalk2

    else:

        $ question3 = True

        mc "I would murder the entire population of the world before even considering going out with you."

        jump mccoytalk2

label mccoykillsyouforcomingontohim2:

    scene bg black

    "Oh no McCoy is stabbing me ouch oh God he stabbed me 37 times oh my God I'm fucking dead now."

    show text "{size=+10}{font=fonts/comic.ttf}you horny bitch{/font}{/size}" with dissolve
    with Pause(2)

    return

label endtalk2:

    show mccoy angry

    mc "Anyways, I've had enough of your questions!"
    mc "Queen Elizabeth II? Hot Pockets?"
    mc "Take them to the torture chamber..."

    show mccoy happy

    mc "...and kill them."

    scene bg black
    with fade

    "Boy is it dark in here."

    u "Hello? Anyone in here?"

    s "Mm!"

    u "Aside from the people that got us stuck in this mess?"

    if atFords:

        jump fordconvo2

    else:

        jump jakeconvo

label fordconvo2:

    f "[name]?"

    u "Ford?"

    f "Hey! How are you?"

    u "I'm... is... is that really what you're asking right now?"

    f "I apologize. I just try to be polite to others, even in the most deadly of situations..."
    f "Anyways, I-"

    u "Ford. I need you to tell me this right now."
    u "Are you from another dimension, or was that a bunch of balogna like everything else?"

    f "I can assure you I really am from another dimension."
    f "I know it may be hard to believe, especially after all that's happened today, but rest assured if we make it out of here alive I will prove it to you."

    b "Hey, guys? Have you found a lightswitch or something in this place?"

    f "Betty, I have a feeling there won't be a lightswitch in-"

    scene bg dungeon

    show jake sad at veryright
    show betty sad at littleright
    show tied2 at veryleft
    show ford happy at middle

    f "...oh."

    u "Hey... uh... where's Norf?"

    f "Well... he chose to go with Belle and Steak- er... Queen Elizabeth II and Hot Pockets..."
    f "Based on that I think that..."

    j "he fucking died okay they cubified him and he's dead."
    j "i heard him screaming shit like \"Ah help I'm being turned into a cube ahhh!\" and now he's a fucking paper weight."

    u "Oh."
    u "Oh well, we clearly didn't like him anyways."
    u "Let's get out of here."

    f "Which way is out?"

    sh "Mmphm mphmmmphm MM mmph mmm mphm mmph."

    show betty angry

    b "Shut it Shane! We're trying to figure out how to get out of here!"

    show betty sad 

    b "Do you know the way out, [name]?"

    u "Why am I always the one making these decisions?"

    s "Mmphm mmm mmph."

    menu:

        "Guess I gotta figure out how to get out of here now. Fuck these people."

        "Leave through the door that Queen Elizabeth II left wide open.":
            jump escape2

        "Dig an underground tunnel system when everyone goes to sleep, leave them behind and escape to a different country, change your name to Jerry, and live happily ever after.":
            
            u "How about we just sleep on it and discuss in the morning?"

            f "Sounds like a fine, albeit suspicious, idea!"

            u "Great! Goodnight everyone!"

            scene bg black with dissolve
            with Pause(2)

            show text "{size=+10}5 years later{/size}" with dissolve
            with Pause(3)

            hide text with dissolve
            with Pause(2)

            $ name = 'Jerry'

            scene bg paris 
            with fade

            "Well, I've really been living an amazing life since that fateful day."

            "Everybody in McCoy's dungeon may have died, but..."

            "I got married, had 34 children, and learned how to cook snail!"

            w "Honey! It's time for our daily cloacal opening exchange!"

            u "Yes dear."

            scene bg black with dissolve
            with Pause(2)

            show text "{size=+20}The End{/size}" with dissolve
            with Pause(3)

            hide text with dissolve
            with Pause(2)

            return

        "Kill yourselves.":
            
            u "How about we kill ourselves?"

            j "okay."

            scene bg black 
            with dissolve

            "ouch that fucking hurt."

            return

label jakeconvo:

    j "[name]?"

    u "Jake?"

    j "why didn't they fucking take you in right away?"
    j "this is fucking BULLSHIT!!!"

    u "I dunno just interdimensional fuck-ups I guess?"
    u "Anyways, who else is in here?"

    j "i dunno lemme turn on the lights."

    "As if there'd be a lightswitch in-"

    scene bg dungeon

    show jake sad at veryright
    show betty sad at littleright
    show tied2 at veryleft

    u "...huh."

    u "Hey... uh... where's Norf and Ford?"

    j "norf fucking died they cubified him and he's dead."
    j "i heard him yelling \"Ah help I'm being turned into a cube ahhh!\" and now he's a fucking paper weight or some shit."
    j "ford died in his portal because apparently he was too stupid to build it right and it tore him apart or some shit."

    u "Oh."
    u "Well shit."
    u "Anyways we gotta get out of here."

    j "but which way is out?"

    sh "Mmphm mphmmmphm MM mmph mmm mphm mmph."

    show betty angry

    b "Shut it Shane! We're trying to figure out how to get out of here!"

    show betty sad 

    b "Do you know the way out, [name]?"

    u "Why am I always the one making these decisions?"

    s "Mmphm mmm mmph."

    menu:

        "Guess I gotta figure out how to get out of here now. Fuck these people."

        "Leave through the door that Queen Elizabeth II left wide open.":
            jump escape2

        "Dig an underground tunnel system when everyone goes to sleep, leave them behind and escape to a different country, change your name to Jerry, and live happily ever after.":
            
            u "How about we just sleep on it and discuss in the morning?"

            sh "Sounds like a shitty idea."

            u "Great! Goodnight everyone!"

            scene bg black with dissolve
            with Pause(2)

            show text "{size=+10}5 years later{/size}" with dissolve
            with Pause(3)

            hide text with dissolve
            with Pause(2)

            $ name = 'Jerry'

            scene bg paris 
            with fade

            "Well, I've really been living an amazing life since that fateful day."

            "Everybody in McCoy's dungeon may have died, but..."

            "I got married, had 34 children, and learned how to cook snail!"

            w "Honey! It's time for our daily cloacal opening exchange!"

            u "Yes dear."

            scene bg black with dissolve
            with Pause(2)

            show text "{size=+20}The End{/size}" with dissolve
            with Pause(3)

            hide text with dissolve
            with Pause(2)

            return

        "Kill yourselves.":
            
            u "How about we kill ourselves?"

            j "okay."

            scene bg black 
            with dissolve

            "ouch that fucking hurt."

            return

label escape2:

    u "Let's leave through the door that Queen Elizabeth II left open!"

    sh "Mph."

    u "Once we get out, I'll create a distraction for you all to escape."
    u "If all goes well I'll run away like a little girl and we'll steal Queen Elizabeth II and Hot Pocket's transporter."

    show betty happy

    b "I like the sound of that!"

    u "Alright, let's go!"

    scene bg volcano
    with fade

    show jake sad at right
    with dissolve

    show betty sad at veryright
    with dissolve

    show tied2 at left
    with dissolve

    if atFords:

        show ford happy at slightright
        with dissolve

    u "Alright, he doesn't seem to be around."

    u "Let's make a run for i-"

    mc "And just what are you all doing out of the McDungeon!?"

    show mccoy angry at middle
    with dissolve

    mc "How did you all get out!?"

    if atFords:

        f "Queen Elizabeth II left the dungeon door wide open."

        mc "I knew it was a mistake hiring her, that hag."

    else:

        s "Mmphm mmphmmmph MM mphm mmm mmmmphm mmph mphm mphm."

        mc "I wasn't asking you, creep!"

    show mccoy happy

    mc "Nonetheless..."
    mc "I guess this is the part where you all die."
    mc "It came earlier than I was prepared for but, ah well."

    show jake sad at offright
    with move

    mc "I love unpredictability."

    if atFords:
        show ford happy at offright
        with move

    mc "It makes murdering people much more satisfying!"

    show betty sad at offright
    with move

    mc "Of course, cleaning up the blood is always a chore..."

    show tied2 at veryright
    with move

    show mccoy angry

    $ idiots = "."

    if atFords:
        $ idiots = " or Ford"

    mc "Hey, wait a minute!"
    mc "Where do you two think you're going?"
    mc "Frankly, I don't give a damn about any of them anymore!"
    mc "But you two, along with [name] over here, are the reason I started this idiotic plot in the first place!"
    mc "And I won't be done until all three of you are DEAD!!"

    "Mccoy slowly and dramatically pulls out a gun from his pocket."
    "It's so slow and so dramatic, in fact, that it gives me the perfect oppurtunity to save either Shane or Sans."
    
    menu:

        "But who should I save?"

        "Sans":
            
            "I decided it would be best to save Sans."
            "First, McCoy went for Shane."

            show tied2 shane

            "He pulled the trigger and Shane went down instantly."
            "As soon as McCoy held the gun up to Sans's face, I readied myself to take the bullet."
            "He pulled the trigger as I jumped in front of Sans."

            scene bg black

            "As my chest was bleeding out, I could still faintly hear McCoy say something to me."

            mc "You do realize I have more than 2 bullets, right?"

            "Fuck."
            "I heard Sans fall to the ground in my final breath."
            "oh fuck I'm dead."

            return

        "Shane":

            "I decided it would be best to save Shane."
            "First, McCoy went for Sans."

            show tied2 sans

            "He pulled the trigger and Sans went down instantly."
            "As soon as McCoy held the gun up to Shane's face, I readied myself to take the bullet."
            "He pulled the trigger as I jumped in front of Shane."

            scene bg black

            "As my chest was bleeding out, I could still faintly hear McCoy say something to me."

            mc "You do realize I have more than 2 bullets, right?"

            "Fuck."
            "I heard Shane fall to the ground in my final breath."
            "oh fuck I'm dead."

            return

        "Neither of them":
            jump shanearcending

label travelsteak2:

    $ sup += 15
    $ bdp += 5
    $ fp -= 10
    $ shp -= 10

    u "I'll head with you guys, Steak-Umm!"

    show jake sad

    sh "fuck you."

    hide jake
    with dissolve

    f "I respect that, [name]! See you there!"

    hide ford
    with dissolve

    hide betty
    with dissolve

    show belle happy at slightleft
    show steak umm at slightright
    with move

    show norf sad

    n "If it's all the same with you three, I'll just be heading with those three."

    u "See ya there, Norf!"

    hide norf
    with dissolve

    bd "The inter-dimensional transporter is back at my place! OwO"

    su "Let us head there then."

    scene bg bdhouse
    with fade

    show belle happy at slightleft
    show steak umm at slightright
    with dissolve

    bd "The device is all set up! >w>"

    u "Will it work properly?"

    su "How do you think we got here?"

    u "Good point."

    bd "Alright, boys! Let's go!! >w<"

    scene bg black with fade
    with Pause(2)

    "..."

    u "Hello?"

    "..."

    u "Anybody there?"

    n "Hello??"

    u "Norf? Is that you?"

    q "Shut the hell up!!"

    u "Who's there?"

    n "Wait... who are you??"
    n "Stay away from me!"

    u "Norf, are you okay!?"

    n "Queen Elizabeth II??"

    qe "I said shut the hell up!"

    n "Wait... stop!"
    n "What are you doing??"
    n "Ah!! Help!!" 
    n "I'm being turned into a cube!!" 
    n "Ahhhhh{size=-5}hhh{/size}{size=-10}hhh...{/size}"

    "..."

    u "Norf...?"

    scene bg dungeon

    if uwuwater:

        show belle happy

        bd "Hey [name]~! UwO"

        u "Oh thank God you're here Belle."
        u "Are you sure we're in the right dimension?"
        u "Did you manage to see what was happening to Norf?"

        bd "Shshshsh. Forget about all of that, sweetie~! U3O"

        u "Uh..."

        bd "You said that you'd let me show you how I make my bathwater! -w-"
        bd "So why don't you just sit back, relax, and let the show begin. :)"

        show belle happy at slightleft
        with move

        show bath at slightright
        with dissolve

        show belle queen
        with dissolve

        show belle queen at slightright
        with move

        qe "I hope you don't mind wrinkles!"

        scene bg black
        with dissolve

        "So this is how I spend the rest of my life?"
        "Watching Queen Elizabeth II bathe in a bathtub somewhere deep in a dungeon?"
        "Alright."

        scene bg black with dissolve
        with Pause(2)

        show text "{size=+20}The End{/size}" with dissolve
        with Pause(3)

        hide text with dissolve
        with Pause(2)

        return

    else:

        show belle angry

        u "Oh thank God you're here Belle."
        u "Is everything alright?"

        bd "Shut the hell up."

        u "Uh..."

        bd "You declined my proposal to watch me bathe."

        u "Well of fucking course I did, that's fucking weird!"

        bd "I said shut the hell up!"
        bd "Do you wanna know what happened to Norf?"
        bd "Do you really wanna know??"

        u "Well... yeah, of course."

        show belle happy

        bd "Alright! Hehehe! Let me show you!"

        show belle norfhap

        bd "Here he is!"

        u "WHAT THE FUCK-"

        show belle norfang

        bd "This is what happens when you deny me, [name]!"
        bd "You get turned into a paperweight!"
        bd "And now it's your turn!"

        show belle norfhap

        bd "Come here, sweetie~! :)"

        scene bg black 
        with dissolve

        "Oh god I can feel myself being cubified oh my god the walls are closing in I'm being turned into a paperweight aw fuck I'm dead and useless."

        return

label shanearcending:

    "I decided it would be best to save myself instead of either of them."
    "First, McCoy went for Sans."

    show tied2 sans
    
    "And secondly, Shane."

    show tied2 both

    scene bg black
    with dissolve

    "I ran as fast as I could out of that hellhole."
    "I didn't know where I was going, but that didn't matter."
    "As long as I could get as far away as possible from McCoy, that's all that mattered."
    "..."
    "......"
    "........."

    
    scene bg black with dissolve
    with Pause(2)

    show text "{size=+10}Epilogue{/size}" with dissolve
    with Pause(3)

    hide text with dissolve
    with Pause(2)

    if atFords:

        scene bg endford
        with fade

        "Ford went on to finally get back to his own dimension. Turns out he wasn't lying afterall!"
        "Unfortunately, opening the portal caused pieces of our dimension to get through, making his just as ugly as ours was."
        "Hopefully he doesn't mind too much."

    scene bg endjake
    with fade

    "Jake decided to stop being a sociopath. He thought it was the perfect time to take on his passion of rocket science!"
    "He worked with NASA to design the worlds first solar powered rocket, and they launched 50 of them into orbit."
    "Jake's design was responsible for the deaths of 109842 people that day."

    scene bg endbetty
    with fade

    "As for me, I'm dating Betty now."
    "Sounds crazy, huh?"
    "Bet you weren't expecting that when I talked shit about her at the beginning of the game."
    "Or when I ruined our dinner date."
    "You probably didn't even want this to be an ending, and assumed your choices would have lead you to be with literally anyone else."
    "But nope!"
    "She has a very VERY tight pussy."
    "Like... don't even get me started."
    "She's so damn hot."
    "I just wanna inhale her nostral hairs right here, right now."
    "This is what happens when you let me speak for you instead of giving you a say in the matter."
    "Except there were other endings which were arguably better, but nonetheless this is the one you got so you'll have to deal with it..."
    "FUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUCK"

    scene bg black with dissolve
    with Pause(2)

    show text "{size=+20}The End{/size}" with dissolve
    with Pause(3)

    hide text with dissolve
    with Pause(2)

    return