# dict_instance.update(self, args*, kwargs*)
## Processing the *args parameter
<pre class='mermaid'>
flowchart LR
%% Elements
start([start])
stop([stop])
no_args{no *args or *kwargs}
is_single_arg{"len(args) ==1"}
is_dict{is a dictionary?}
item_loop[loop items]
tuple_loop[loop tuples]
zip_loop[loop zip of alternating values]

%% Execution Paths
start -->   no_args 

no_args --yes--> stop
no_args --no--> is_single_arg 

is_single_arg--yes-->is_dict
is_single_arg--no--> zip_loop

is_dict --yes--> item_loop
is_dict --no--> tuple_loop

</pre>

## args[0] is a dictionary: use .items for loop
``` python
# The single argument is a dictionary.
for key, value in args.items():
    instance[key] = value
```
## args[0] is an iterable of key,value pairs: use tuple unpacking for loop
``` python
for key, value in args:
    instance[key] = value

```
## args is a list of values: use zip of alternating values for loop
```python
# treat *args (length > 1) as a sequence of key-value pairs
for key, value in zip(args[::2], args[1::2]):
    instance[key] = value
```