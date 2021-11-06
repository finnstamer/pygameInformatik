

Was für ein Spiel:
- An Pacman angelehntes Spiel
 - mit mehreren Leveln, Gegner, Abwehrmöglichkeiten (zielsuchend), Gegner, Aufsammelbaren   Powerups Skins
 - Zufallsgenerierte Level 
 
 
Welche Art:
 - 2D Arcade Game mit Gegnern

Welches Ziel:
 - verschiedene Modi
    - Survival
    - Alle Gegner erledigen
    - Bossgegner


# Initalization
GameObject
   p: blockingmovment

Level
   content: Dict[str, Group[Any]]
   list of named groups and functions to return objects with specific properties (e.g blockingmovements)

Event
   p: 

static EventDispatcher
   p: subscriber 
      [ [obj, events] ... ]
   f: dispatch (event, *obj)

   // events named G_ADD, G_DEL, G_SETN G_GETN are reserved for Game Class 


Game
   p: levels
      Dict[int, Level]
   p: Level
      Level
   p: notes
      Dict[str, any]
      Notes are global 
   subsribes to all "G_<>" events
   connect all components of currentLevel to Event system
   load level and dispatch "start" event to all comps


# Lifecycle
Game
   Control Event will dispatched to all subscribed Components
   Movement changes will be evaluated
      e.g Player give movement request
   Events from components gets dispatched to each other
   Checks for dispatched Events to run following functions:
   f: addObject (*obj)
      Object(s) will be added to lifecycle
   f: removeObject (obj)
      Object(s) will be removed from lifecycle
   f: setNote (note, value)
      saves a note
   f: getNode(note) -> value
      gets a note

KI
   subscribes to object (e.g player) events 
