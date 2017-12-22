# Character Sheet
Holy guacamole did I bite off more than I can chew! Well, at least in my given time frame, that is. Here's how it went down:

My first attempt to dummy code the program revolved around trying to break up the pieces of the potential program and put them into functions. This seemed simple enough-- I knew Races and Classes would need to be attended to separately, and tried to think ahead to more fiddly bits like armor class and weapons, but then assumed it wouldn't be THAT fiddly and put it aside to focus on the ability scores, which I KNEW would be difficult to think through.

When I next went in to attack the code, I realized that my thinking process is mostly top-down, so I kind of ignored my previously made functions and just started writing the code introduction, thinking about what information I'd need to make that part of the code and creating that information, then continuing on down. So that was a process to learn about my workflow. If I try to jump all over the place, I'll forget what needs to connect where and get confused. Ah, coding.

In class we mostly used dictionaries to tally the number of times a word appeared in a chunk of text. In this code I realized that it could be used to hold all kinds of information on one subject, so I used it to hold information on each race and class. 
What I haven't yet explored is a dictionary within a dictionary, which might be needed when I hit the spellcasting properly. 

My output looks simple and is mostly made of standalone print statements. This way a user can easily fill out sections on their printout character sheet without squinting at a weird ASCII table, haha. I'm extremely pleased with my ability score table, though. I'm really proud that I managed to look up how to organize nested lists, /and/ use those same lists to grab the ability modifiers when I needed them for other parts of the sheet!!

The ability dicerolling, adding, and editing with race modifiers was the biggest chunk of work. I got carried away putting in every race when I didn't need to for a proof of concept, but it looks RAD and works well! As noted in the code commentary, I took pointers from another character creator to get the input-on-where-you-want-your-rolls-to-go section, but I figured out the exception-throwing myself, which is pretty cool. Of course, my focusing on the race section took up all the time I had, so the class section, while similar, is much smaller. Adding the class stuff to the race stuff in the final printable variable was also interesting.

My original stat modifier was also a great big table, but after looking at the stackOverflow about it my professor showed me, I changed it to the simple math problem it actually was, haha. I also checked to make sure Python rounded correctly, as D&D always rounds down.

Missing:

-Skill proficiency

-Armor class that isn't just the default

-Subraces -> other than human, halforc, dragonborn and tiefling, the races are missing some ability points due to subraces or other customization.

-Weapons

-A zillion classes!

-Who knows?! Turns out there's a lot to character sheets that I hardly realized even after a year of using them, haha.


Overall, though, I'm extremely happy with what I have done and I'm excited to keep going in my own time. I really want to make this good!!!

# Spell Lookup
 I super dropped the ball on this one due to focusing too hard on the character sheet. But I'm confident that with the help of this Excel sheet it'll be relatively simple to make the info searchable in Python prompts once I extract it into Pythonese. http://thezohar.tumblr.com/post/161327175208/spells
  
