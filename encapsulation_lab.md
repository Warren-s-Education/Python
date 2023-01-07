# Class Diagram
<pre class='mermaid'>
classDiagram
direction LR

%% Class Relationships
    AccountException --|> Exception
    BankAccount --> AccountException : raises

%% Class Definitions
    class AccountException
    class Exception
    class BankAccount {
        -account_number: str
        -balance: float
        +get_account_number(): str
        +deposit()
        +withdraw()
    }
</pre>

# Deposit Logic
<pre class='mermaid'>
flowchart LR
    start([start])
        deposit[deposit money]
        decision1{money > $100?}
        audit[audit]

        start --> deposit --> decision1
        decision1 -- yes --> audit --> stop
        decision1 -- no --> stop


    stop([stop])
</pre>

# Withdrawal Logic
<pre class='mermaid'>
flowchart LR
    start([start])

        start --> input[/input: withdrawal/] --> decision1{withdrawal > balance}
        decision1 -- yes --> exception --> stop
        decision1 -- no --> decision2{withdrawal > 100}
        
        
        subgraph "insufficient funds"
            exception
        end

        subgraph "sufficient funds"
            decision2 --yes--> audit --> output
            output[\output\]
           decision2 -- no --> output
        end

        output --> stop

    stop([stop])
</pre>

# Account Number behaviour
<pre class='mermaid'>
flowchart LR
    start([start])
    stop([stop])

    get[get_account_number]
    set[set_account_number]
    
    output[\account number\]
    
    exception[exception]

    start --> get
    start --> set
    
    subgraph get 
        get --> output
    end

    
    subgraph set 
        set --> exception
    end

    exception --> stop
    output --> stop
    
</pre>