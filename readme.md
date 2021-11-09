# Pacman Framework Documentation
Für diese Dokumentation sind einige Definitionen wichtig. Dafür eine kleine Auflistungen, wobei alles nur Platzhalter sind.
- Wenn eine Klasse mit "()" Klammern steht, handelt es sich um eine Instanz, sonst um die statische Klasse 

## Event
Events sind Objekte aus einem Namen und einem zugehörigen Wert, der jeden Datentyp annehmen kann.
## Events
Die Events Klasse ermöglicht das Versenden eines Events (von theoretisch überall aus) zu allen Objekten, die dieses bestimmte Event abonniert haben.
#### Referenzen 
- ###### Events.subscribe(obj: object, *events: str) -> None
  - Verbindet ein Objekt (i.d.R sich selbst, also "self") zu bestimmten Events
  - Wenn ein abonniertes Event 'fired', wird die Methode obj.receiveEvent() aufgerufen.
  - Das Objekt muss demnach diese Methode beinhalten, sonst wird ein Error ausgegeben.
- ###### Events.dispatch(event: str, value: Any) -> None:
  - Löst ein bestimmtes Event aus. Alle abonnierten Objekte können dieses auf ihre Weise verarbeiten.
- ###### Events.acceptRequest(req: str, func: Callable) -> None:
  - Requests ermöglichen einen Datenaustausch zwischen zwei unabhängig initierten Objekten, wobei beide ihre Aufgabenbereiche nicht verlassen. Im Gegensatz zu Events können Empfänger einer Request eine Antwort zu dem aufrufenden Objekt geben. Ebenfalls kann nur ein Objekt die Request annehmen 
- ###### Events.request(req: str, *args: Any) -> Any:
  - Eine Anfrage wird an einen Empfänger mit Parametern gestellt, dieser gibt eine Antwort zurück. 
## Game
#### Referenzen
- ###### Game().addLevel(level: *Level)
  - Deaktiviert und fügt Level hinzu. Überschreibungen möglich.
- ###### Game().setLevel(id: int)
  - Aktiviert das Level mit zugehöriger
- ###### Game().start()
  - Startet alle wichtige Abhängikeiten
    - pygame.init
    - Dependencies werden geladen
    - "game.start" Event wird versendet
  - Startet den Lifecycle
    - "game.tick" wird versendet
    - "game.controls" wird versendet (deprecated => wird in unabhängige Dependency umgewandelt)
    - .draw Methode aller Objekte im Level wird ausgeführt
- ###### Game.use(dependency: object)
  - Beigefügtes Objekt wird vor dem ersten Frame als Dependency geladen.
  - Damit werden unabhängige Klassen ermöglicht. Bpsw: Sounds
  - Dafür muss der Ort in dem die Funktion aufgerufen wird, bereits durchgeführt sein. 
- ###### Start Game


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

TODO:
needing factory for object id's