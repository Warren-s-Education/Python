<pre class='mermaid'>
classDiagram
direction BT

    %% Class Relationships
    Laptop --|> Computer
    Square --|> Figure
    Hovercraft --|> Vehicle

    %% Class Definitions

</pre>
# Inheritance Tree - beware explosion antipattern

<pre class='mermaid'>
classDiagram
direction BT

    %% Class Relationships
    Land --|> Vehicle
    Water --|> Vehicle
    Air --|> Vehicle
    Space --|> Vehicle

    Wheeled --|> Land
    Tracked --|> Land
    Hovercraft --|> Land

    %% Class Definitions
    class Vehicle {
        mileage
        start()
        stop()
        tank()
    }

</pre>

# Inheritance Tree - beware explosion antipattern

<pre class='mermaid'>
classDiagram
direction BT

    %% Class Relationships
    Laptop "1" o-- "*" NetworkCard
    Hovercraft o-- Engine

    %% Class Definitions


</pre>

# Composition - other objects perform a part of a desired behaviour

<pre class='mermaid'>
classDiagram
direction BT

    %% Class Relationships
    Laptop "1" o-- "*" NetworkCard
    Hovercraft o-- Engine

    %% Class Definitions

</pre>

# Car Example

<pre class='mermaid'>
classDiagram
direction BT

    %% Class Relationships
    Car o-- Engine
    Engine <|-- Gas
    Engine <|-- Diesel

    %% Class Definitions
    class Car {
        +engine
    }

    class Engine {
        +horsepower
        +start()
    }

</pre>

# Computer Example

<pre class='mermaid'>
classDiagram
direction BT

    %% Class Relationships
    PersonalComputer --|> BaseComputer

    DialUp --|> Connection
    ADSL --|> Connection
    Ethernet --|> Connection

    PersonalComputer o-- Connection

    %% Class Definitions
    class Connection {
        speed
        download()
    }
    
    BaseComputer: serial_number
    PersonalComputer: connection
</pre>

# Automotive Example

<pre class='mermaid'>
classDiagram
direction BT

    %% Class Relationships
    PetrolEngine --|> Engine
    ElectricEngine --|> Engine

    Vehicle "1" o-- "1" Engine
    Vehicle "1" o-- "4" Tyres

    CityTyres --|> Tyres
    OffRoadTyres --|> Tyres



    %% Class Definitions

    class Vehicle {
        VIN
        engine
        tyres
    }
    class Tyres {
        size
        pressure
        get_pressure()
        pump()
    }


    class Engine {
        state
        fuel_type
        start()
        stop()
        get_state()
    }
</pre>