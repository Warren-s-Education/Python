# IntegerList example

<pre class='mermaid'>
classDiagram
direction BT

    %% Class Relationships
    IntegerList --|> List

    %% Class Definitions
    class IntegerList {
        +check_value_type()$
        +set_item(index, value)
        +append(value)
        +extend(iterable: Iterable[any]) void
        ...
    }

    class List {
        __getitem__(index:int) Any
        __setitem__(index:int, value:any) void
        extend(iterable:Iterable[any]) void
        __mul__(n:int) List
        __delitem__(index:int) void
        __add__(other: List) List
    }
</pre>

# MonitoredDict example
```Python
"""A dictionary that logs the times for operations.

Specifically, it logs for the following operations:
    1.  class instantiation
    2. read access
    3. new element creation 
    4. element update.
"""
```
<pre class='mermaid'>
classDiagram
direction BT

%% Class Relationships
    MonitoredDict --|> Dict

%% Class Definitions 
    class Dict {
        ...
    }
    class MonitoredDict {
        log: List
        __setitem__(key: Hashable, value: Any) void
        __getitem__(key: Hashable) void
        __init__(*args, **kwargs) MonitoredDict
        log_timestamp(message:str) void
    }
</pre>