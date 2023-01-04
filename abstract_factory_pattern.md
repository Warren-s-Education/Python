## Deals with product families

<pre class='mermaid'>
    classDiagram
    direction BT

    %% Class Relationships

        VictorianChair ..|> Chair
        ModernChair ..|> Chair

        VictorianSofa ..|> Sofa
        ModernSofa ..|> Sofa

        VictorianCoffeeTable ..|> CoffeeTable
        ModernCoffeeTable ..|> CoffeeTable

    %% Class Attributes

        class Chair {
            << interface>>
            +hasLegs()
            +sitOn()
        }

        class VictorianChair {
            ...
            +hasLegs()
            +sitOn()
        }

        class ModernChair {
            ...
            +hasLegs()
            +sitOn()
        }
</pre>
## Concrete factories create concrete product families
<pre class='mermaid'>
    classDiagram
    direction BT

    %% Class Relationships

        ModernFurnitureFactory ..|> FurnitureFactory
        VictorianFurnitureFactory ..|> FurnitureFactory

    %% Class Attributes

        class FurnitureFactory {
            << interface>>
            +createChair() Chair
            +createSofa() Sofa
            +createCoffeeTable() CoffeeTable
        }

        class ModernFurnitureFactory {
            << interface>>
            +createChair() Chair
            +createSofa() Sofa
            +createCoffeeTable() CoffeeTable
        }

        class VictorianFurnitureFactory {
            << interface>>
            +createChair() Chair
            +createSofa() Sofa
            +createCoffeeTable() CoffeeTable
        }

</pre>