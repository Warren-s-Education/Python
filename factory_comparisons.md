# Overview
This document explores the different ways factories are discussed.

## 1. Factory

**What is it?**
        
        A function, method or class that produces something.

**What does it do?**

        Typically creates objects. But can create files, database records, etc.

**How might it do it?**


## 2. Creation Method

## 3. Static creation method
**What is it?**
A creation method declared as static. 
``` python
class LuxuryWatch:
    # Constructor creation method.
    def __init__(self):
        self.text = ''
    
    # Example of a static creation method.  
    @classmethod
    def with_engraving(cls, text):
        _watch = cls()
        _watch.text = text
        return _watch
```
**Why use it?**

1. To have an option to return an existing object
2. Overload constructor signatures: `Random(int max)` and `Random(int min)`
3. Use a method that more clearly declares your intention

## 4. *Simple factory* pattern

**What is it?**
One creation method with a large conditional based on method parameters which choose which product class to instantiate and then return.

```python
class Dog:
    ...

class Cat:
    ...

def get_animal(animal:str) -> Union[Cat, Dog]:
    """Simple factory."""
    match animal:
        case 'dog':
            return Dog()
        case 'cat':
            return Cat()
```

## *Factory Method* pattern
**How do I spot it?**

If there is a creation method in a base class and subclasses extend it.

## *Abstract Factory* pattern