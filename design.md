<pre class='mermaid'>
flowchart LR

condition{{condition\ncounter < 1000\ntotal_weight + 0.5 < 300}} 
add[Apple]


start([start])
stop([stop])

start --> condition
condition -- yes --> add --> condition
condition -- no --> stop
</pre>

<pre class='mermaid'>
classDiagram 
class Apple {
    _counter
    _total_weight
    Apple()
}
note for Apple "Apple( ) increments 'counter' by 1 and 'total_weight' by [0.2, 0.5]"

</pre>


<pre class='mermaid'>
classDiagram 
class Person {
    age
    salary
    weight
}

class Elevator {
    _total_weight
    add(Person)
    remove(Person)
}

</pre>


<pre class='mermaid'>
classDiagram
  class Vehicle {
  }
  class LandVehicle {
  }
  class TrackedVehicle {
  }
  Vehicle <|-- LandVehicle
  LandVehicle <|-- TrackedVehicle
</pre>

<pre class='mermaid'>
classDiagram
 class A {info()}
 class B {info()}
 class C {info()}
 class D

 B --|> A
 C --|> A
 D --|> B
 D --|> C
</pre>

<pre class='mermaid'>
classDiagram 

class Scanner {
    scan()
}

class Printer {
    print()
}

class Fax {
    send()
    print()
}

class MFD_SPF 

class MFD_SFP 

MFD_SPF --|> Scanner
MFD_SPF --|> Printer
MFD_SPF --|> Fax

MFD_SFP --|> Scanner
MFD_SFP --|> Fax
MFD_SFP --|> Printer
</pre>


<pre class='mermaid'>
classDiagram

class Device { turn_on(): std_out} 
class Radio 
class TvSet { turn_on(): std_out}
class PortableRadio { turn_on(): std_out}

Radio --|> Device
PortableRadio --|> Device
TvSet --|> Device
</pre>

<pre class='mermaid'>
classDiagram

class Wax {melt()}
class Cheese {fire()}
class Wood {melt()}

</pre>


<pre class='mermaid'>
classDiagram
class LuxuryWatch {
    int watches_created$
    +String engraving
    +get_number_of_watches_created(): Int
    +with_engraving(String text)$ LuxuryWatch
}



</pre>


<pre class='mermaid'>
flowchart TB

A[mammogram]
B[ultrasound]
C[have a lump ASAP]
D[have a referral]
E[both breasts]
F[doctor is away]

</pre>




<pre class='mermaid'>
classDiagram

class Logistics {
    ...
    +planDelivery()
    +createTransport() Transport
}

class RoadLogistics {
    ...
    +createTransport():Transport
}

class SeaLogistics {
    ...
    +createTransport(): Transport
}

RoadLogistics --|> Logistics
SeaLogistics --|> Logistics


class Transport {
    ...
    +deliver()*
}

class Truck {
    ...
    + deliver()
}


class Ship {
    ...
    + deliver()
}

<< interface >> Transport

Truck ..|> Transport : implements
Ship ..|> Transport : implements


Logistics ..> Transport: creates and invokes

</pre>
