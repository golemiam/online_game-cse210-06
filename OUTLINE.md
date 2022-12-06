# Final Project Outline

## Game Ideas
### The following Ideas are ranked from 1-3 in importance, based on how easy it is to implement and how long it takes to implement.
1. (2) Zelda screen movement
2. (3) races: 
    - snow people 
    - fire people
3. (3) classes 
    - Christians 
    - Muslims
4. (2) Abilities 
    - snow people: cold stare preaching: 10 fps
    - fire people: fiery indignation: 15 faith points hit, with 15 second cooldown
5. For Health FP (faith points)
6. (2) Sprites with radius impact around
7. (1) frame selection (draw_scene(s))
8. (1) possible sprite implementation?
9. (2) Faith points
    - Total amount (health)
    - healing or gaining faith (leveling?)
10. (2) implement tiles for scene drawing (see #7)
11. (2) enemy/npc ideas
    - NPC = anti faith pamphlets
    - temptations (glowing orbs)
    - damage amounts
    - health amounts
    - Bosses (p2 can be exchanged for additional boss)
12. (2) Buffs
    - scripture page
    - Shop items
    - artifacts
13. (1) Level grid (map)
14. (2) main menu
15. (3) possible gamemodes/singleplayer or multiplayer (ai controls p2 if no p2 is present)
16. (3) Animation for faith lost
17. (2) See if we can implement animated sprites or swap model parts.
    - like head is a separate sprite from body
18. (2) importing sprites? 
19. (3) light sources?

## Roles
- Robbie: Art, Idea/outlines
- Marc: Logic, Organization, Tilemapping?
- Helaman: Logic/functions

## Scripting Ideas
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
        pass
