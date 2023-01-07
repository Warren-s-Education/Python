<pre class='mermaid'>
    classDiagram
    direction BT
        %% Class Definitions
            class TankError
            class Exception  
            class Tank {
                capacity: int 
                -level: int
                +set_level(amount:int) None
                +remove_level() None
            }

        %% Class Relationships
            TankError --|> Exception
            Tank --> TankError : raises 
</pre>