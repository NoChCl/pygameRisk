# Plan for Pygame Risk

Game start: 2 options-
    
    1: Filled in, evenly distriputed, 2 options:
        
        1:Random
        
        2:Color/team alphabetical ordered selection
        
    2: All players start with 3(?) countrys(tbd), all other counteries are "neutral" countries
        def neutral country:
            Neutral player is a country that WILL NOT attack you, but will act as a normal player 
            Neutral player will start with 2(?) defending troops when attacked

Order for turns IN ALL ASPECTS OF GAME will be alphebetical by color/team name

------------------------------------------------------------
Most rules from here out should be normal per a game of risk
------------------------------------------------------------

Game Loop:
    for player in players:
        
        Phase 1: troop placement:
            player is provided with info on number of troops given to them at the begining of a turn
            Player is also provided with info on other countrys current troops
                (maybe also potental troops???? (big maybe))
            Player should, as always, be provided with a number of troops anc countries that player owns.
            With above info in mind, Player may place troops in any country that player owns.
            Player may also choose to retract troops that are in a country, as long as:
                they are troops placed down on this current turn.
            
            Once Player is happy, Player may then select to proceede to the next phase.
            The above is a non revesable thing.
        Phase 2: Attack phase:
            Player may select any of players country that has more than 1 troops in it
            The player may select the country of any oposing player
            said country must be touching either:
                the first selected country of the current player
                or any specal exception
            
            if numb troops in the oposing country is <=2
                notify player 2 that they are being attacked
                show where attack is
                give info on country and other important stats
                give player choice of using 1 or 2 dice
                roll the selected number of dice
            else:
                roll 1 die for opposing player
            
            if player troops >=4:
                give player choice to roll up to 3 dice
                roll that many dice
            elif player troops ==3:
                give player choice to roll up to 2 dice
                roll that many dice
                
            elif player troops ==2:
                roll that one die
            else:
                you did something wrong... look at conditions of starting a war...
                
            list dice rolls for each player in greatest to least order
            get len of smaller list
            
            for i, x in enumarate smaller list:
                if x>big list[i]:
                    take one troop from side with longer list
                elif x<big list[i]:
                    take one troop from side with shorter list
                if x=big list[i]:
                    take one troop from attacking side
            
            if opposing country has 0 troops:
                owner of oposing country no longer has that country
                player now owns oposing country, add it to country list
                add number of dice rolled by player against oposing counrty to opposing country
                    from attacking country
                Ask how many more, must be at least 1 left in attacking country
                
            In any case, player is free to repeat from the top of the attack phase
            Player may also chose to move to next phase, again, like placing phase
                once you move on, you cant move back
            
            Buuuuuuuuuuuuuuuut..... NO. NO NO NO NO NO NO AND N0
            
        Phase 3: Movement:
            Player may select any one country that player owns
            player may select any number of troops, as long as 
                they are in that country
                and there will be one left after movement
            player may select any adjacent country owned by player
            all steps proceding this step are reversable
            
            move selected numb troops from first country, to second country
            
            after this the phase is over, you may only make one troop movement per turn
            
        Players turn is over
            
            
                
                
