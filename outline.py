Game_ideas = """
1. Zelda screen movement
2. races: 
    a. snow people 
    b. fire people
3. classes 
    a. Christians 
    b. Muslims
4. Abilities 
    a. snow people: cold stare preaching: 10 fps
    b. fire people: fiery indignation: 15 faith points hit, with 15 second cooldown
5. For Health FP (faith points)
6. Sprites with radius impact around
7. frame selection (draw_scene(s))
8. possible sprite implementation?
9. Faith points
    a. Total amount (health)
    b. healing or gaining faith (leveling?)
10. implement tiles for scene drawing (see #7)
11. enemy/npc ideas
    a. NPC = anti faith pamphlets
    b. temptations (glowing orbs)
    c. damage amounts
    d. health amounts
    e. Bosses (p2 can be exchanged for additional boss)
12. Buffs
    a. scripture page
    b. Shop items
    c. artifacts
13. Level grid (map)
14. main menu
15. possible gamemodes/singleplayer or multiplayer (ai controls p2 if no p2 is present)
16. Animation for faith lost
17. See if we can implement animated sprites or swap model parts.
    a. like head is a separate sprite from body
18. 
def draw_head_one():

if player_choice == "1":
    draw_head_one()
19. importing sprites? 
20. light sources?

Robbie: Art, Idea/outlines
Marc: Logic, Tilemapping?
Helaman: Logic

"""



def main(scale):
    """
    Usage: Choose the output

    """
    _t = turtle.Turtle()
    _s = turtle.getscreen()
    _s.update()
    head_east = ""
    if character_pos > max_x:
        condition = head_east

    scene_list[x_0, x_1, x_2, x_3]
    draw_scene_east = scene_list[i+1]
    try:
        condition = (sys.argv[1]).lower() # Draw peace time
        if condition == "head_east":
            draw_scene_east(_t) #Draw Scuffle
            print("Our supplies are well stocked")
        elif condition == "2":
            print("A mild skirmish")
            draw_scuffle(_t, 1, "red")
        elif condition == "3": #Draw Ganon
            draw_ganon_battle(_t, 100, 100, "yellow")
            print("Defeating Ganon is no easy task")
        elif condition != 1 or condition != 2 or condition != 3:
            print("Error. Usage is Python <Program name> <condition> where condition = '1' for peace, '2' for scuffle or '3' for ganon")
    except IndexError:
