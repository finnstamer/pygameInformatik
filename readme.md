# Pacman Framework Documentation
Für diese Dokumentation sind einige Definitionen wichtig. Dafür eine kleine Auflistungen, wobei alles nur Platzhalter sind.
- Wenn eine Klasse mit "()" Klammern steht, handelt es sich um eine Instanz, sonst um die statische Klasse 
  - Der Unterschied liegt ist, dass eine Instanz eigenständig und unabhängig zu anderen Instanzen (auch Objekten von mir genannt) ist; Die statische Klasse ist global identisch. Verschieden Wände beispielsweise, die alle dieselbe Klasse sind, müssen demnach alle eine Instanz sein. Bei einer statischen Wand Klasse wären alle Wände identisch - das wäre sehr unpraktisch. Wichtig ist auch, dass statische Klasse nicht von Instanzen erben können, denn ihnen fehlt eine __init__ Funktion um erben zu können => logischerweise, da init nämlich eine Instanz erstellt.
- "Deprecated" heißt, dass dies nicht mehr lange in dieser Weise funktioniert, da es optimiert wird. Möglichst umgehen!
- Ich verwende öfters "Parameter" statt "Argument", da dass m.M.n besser verständlich ist, eine Variabel, die Einfluss auf eine Funktion, Parameter zu benennen.

## Events
Die Events Klasse ermöglicht das Versenden eines Events (von theoretisch überall aus) zu allen Objekten, die dieses bestimmte Event abonniert haben.
### Referenzen 
#### Events
- ###### Events.subscribe(obj: object, *events: str) -> None
  - Verbindet ein Objekt (i.d.R sich selbst, also "self") zu bestimmten Events
  - Wenn ein abonniertes Event 'fired', wird die Methode obj.receiveEvent() mit einem Event als Parameter aufgerufen.
  - Das Objekt muss demnach diese Methode beinhalten, sonst wird ein Error ausgegeben.
- ###### Events.dispatch(event: str, value: Any) -> None:
  - Löst ein bestimmtes Event aus. Alle abonnierten Objekte können dieses auf ihre Weise verarbeiten.
#### Requests
Requests ermöglichen einen Datenaustausch zwischen zwei unabhängig initierten Objekten, wobei beide ihre Aufgabenbereiche nicht verlassen. Im Gegensatz zu Events können Empfänger einer Request eine Antwort zu dem aufrufenden Objekt geben. Ebenfalls kann nur ein Objekt die Request annehmen 
- ###### Events.acceptRequest(req: str, func: Callable) -> None:
  - Gibt dem System Bescheid, dass eine bestimme Request mit dem Namen jeweiligen Namen für req einer bestimmten Funktion (func) zugeordnet ist.
- ###### Events.request(req: str, *args: Any) -> Any:
  - Eine Anfrage wird an einen Empfänger mit Parametern gestellt, dieser gibt eine Antwort zurück. 
#### Event
Das Event hält Informationen, die dem Abonnent übergeben werden.
- ###### Event().name -> str:
  - Name des Events
- ###### Event().value -> Any:
  - Mitgelieferter Wert des Events
## Game
### Referenzen
- ###### Game().addLevel(level: *Level) -> None
  - Deaktiviert und fügt Level hinzu. Überschreibungen möglich.
- ###### Game().setLevel(id: int) -> None
  - Aktiviert das Level mit zugehöriger
- ###### Game().start() -> None
  - Startet alle wichtige Abhängikeiten
    - pygame.init
    - Dependencies werden geladen
    - "game.start" Event wird versendet
  - Startet den Lifecycle
    - "game.dependency.tick" wird versendet, damit alle Dependencies vor dem ersten globalen Tick neue Daten verarbeiten können.
    - "game.tick" wird versendet
    - .draw Methode aller Objekte im Level wird ausgeführt
- ###### Game.use(dependency: object) -> None
  - Beigefügtes Objekt wird vor dem ersten Frame als Dependency geladen.
  - Damit werden unabhängige Klassen ermöglicht. Bpsw: Sounds
  - Dafür muss der Ort in dem die Funktion aufgerufen wird, bereits durchgeführt sein. 


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