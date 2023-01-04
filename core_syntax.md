<pre class='mermaid'>
classDiagram
class TimeInterval {
    +add(other: TimeInterval)
    +subtract(TimeInterval other): TimeInterval
    +multiply(Integer value) TimeInterval
    +to_string(): string
}
%% This is a comment.
</pre>

```python
def to_string() --> str
""""Return HH:MM:SS format."""
    pass

add, subtract, multiply
"""Check argument type."""

def __init__()
"""Based on keywords: hour, minute, seconds."""




```

<pre class='mermaid'>
classDiagram
A --|> B: inheritance
C "1" --* "1" D: composition
E --o F: aggregation
G ..|> H: realisation
I ..> J: dependence 
K --> L: association 


</pre>


<pre class='mermaid'>
classDiagram
  class timedelta {
    -days: int
    -seconds: int
    -microseconds: int
    +__init__(days: int = 0, seconds: int = 0, microseconds: int = 0, milliseconds: int = 0, minutes: int = 0, hours: int = 0, weeks: int = 0)
    +__repr__() -> str
    +__str__() -> str
    +__format__(format: str) -> str
    +__neg__() -> timedelta
    +__abs__() -> timedelta
    +__add__(other: timedelta) -> timedelta
    +__sub__(other: timedelta) -> timedelta
    +__mul__(other: int) -> timedelta
    +__truediv__(other: int) -> timedelta
    +__floordiv__(other: int) -> timedelta
    +__mod__(other: timedelta) -> timedelta
    +__divmod__(other: timedelta) -> Tuple[timedelta, timedelta]
    +__eq__(other: object) -> bool
    +__ne__(other: object) -> bool
    +__lt__(other: timedelta) -> bool
    +__le__(other: timedelta) -> bool
    +__gt__(other: timedelta) -> bool
    +__ge__(other: timedelta) -> bool
    +total_seconds() -> float
    +resolution() -> timedelta
    +max() -> timedelta
    +min() -> timedelta
    +__reduce__() -> Tuple[Type[timedelta], Tuple[int, int, int]]
  }

</pre>
