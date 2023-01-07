# dict_instance.update(*args, **kwargs)
## Processing args
<pre class='mermaid'>
flowchart LR

%%Flowchart Elements
    start([start])
    stop([stop])

    %% Decision Points
        type_check{"is args[0] a dictionary?"}
        length_check{"is len(args) == 1"}
        input_check{"args OR kwargs\nexist?"}

    %% Processes
        %% Processing args
            items_loop["loop dictionary items"]
            tuple_loop["loop existing (key,value) pairs"]
            zip_loop["loop zipped (key, value) pairs"]
        

%% Execution Paths
    %% args paths
        start --> input_check
        input_check --no--> stop
        input_check --yes--> length_check

        length_check --no--> zip_loop
        length_check --yes--> type_check

        type_check --no--> tuple_loop         
        type_check --yes--> items_loop
</pre>
```python
if len(args) == 1:
    other = args[0]
    if isinstance(other, dict):
        # items loop
    else:
        # tuples loop
else:
    # zipped tuples loop
```
## Processing kwargs
<pre class='mermaid'>
    flowchart LR
            %% Processing kwargs
            kwargs_loop["loop kwargs items"]

            kwargs_check --no--> stop
            kwargs_check --yes--> kwargs_loop --> stop
            kwargs_check{"does kwargs exist?"}

</pre>
```python
# kwargs' items loop
```