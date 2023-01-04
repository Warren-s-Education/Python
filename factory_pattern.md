# Factory Pattern (virtual constructor)
<pre class='mermaid'>
classDiagram
    direction BT

    %% Class Relationships
        ConcreteProductA ..|> Product: implements
        ConcreteProductB ..|> Product: implements

        ConcreteCreatorA --|> Creator
        ConcreteCreatorB --|> Creator

        Creator ..> Product: uses

    %% Class Attributes
    class Creator {
        ...
        createProduct()* Product
    }

    class ConcreteCreatorA {
        ...
        createProduct(): Product
    }

    class ConcreteCreatorB {
        ...
        createProduct(): Product
    }

    class Product {
        << interface>>
        doStuff()
    }

    %% Example Code

    note for Creator "Product p = createProduct()\np.doStuff()"
    note for ConcreteCreatorA "ConcreteCreators do not have to create. can return existing"

</pre>


# Example of Factory Pattern
<pre class='mermaid'>
classDiagram
    direction BT

    %% Define class relationships

        RoadLogistics --|> Logistics
        SeaLogistics --|> Logistics

        Truck ..|> Transport
        Ship ..|> Transport

        Logistics ..> Transport
        
    %% Define class attributes 

        class Logistics {
            businessLogic(Transport) 
            createTransport()*Transport
        }

        class RoadLogistics {
            businessLogic(Transport) 
            createTransport()*Transport
        }

        class SeaLogistics {
            businessLogic(Transport) 
            createTransport()*Transport
        }
          
        class Transport {
            << interface>>
            deliver()
        }
</pre>

# Cross-platform UI elements
<pre class='mermaid'>
classDiagram
direction BT

%% Core Classes

    class Button { 
        << interface>>
        onClick()*
        render()*
    }

    class Dialog { 
        createButton()* Button
        render()
    }

%% Implementation Classes

    class WindowsButton {
        onClick()
        render()
    }

    class HTML_Button {
        onClick()
        render()
    }

    class WindowsDialog {
        createButton()
    }

    class WebDialog {
        createButton()
    }

%% Relationships

    WindowsButton ..|> Button
    HTML_Button ..|> Button

    WindowsDialog --|> Dialog
    WebDialog --|> Dialog

    Dialog ..> Button: uses

</pre>

``` python
class Dialog(ABC):

    @abstractmethod
    def create_button(self):
        pass

    def render(self):
        """Create and render the button.
        
        This function performs the class' primary responsibility. To achieve 
        this, it calls the factory method 'create_button()'.
        """
        # Call factory method
        button = createButton()
        # Use the product
        button.on_click(close_dialog)
        button.render()

class WindowsDialog(Dialog):
    """A Windows-based implementation of the Dialog superclass that implements 
    the abstract 'create_button()' method.
    """

    def createButton(self):
        return WindowsButton()

class WebDialog(Dialog):
    """A web-based implementation of the Dialog superclass."""

    def createButton(self):
        return WebButton()

class Button(ABC):

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def onClick(self, command):
        pass


class WebButton(Button):
    """Web-based implementation of the Button interface."""

class WindowsButton(Button):
    """Windows-based implementation of the Button interface."""


class Application:

    def __init__(self):
        self.dialog = None
        
    def initialise(self):
        config = read_config_file()

        if config.os == 'Windows':
            dialog = WindowsDialog()
        elif config.os == 'Web':
            dialog = WebDialog()
        else:
            raise Exception("Unknown OS.")

    def main(self):
        self.initialise()
        self.dialog.render()

```