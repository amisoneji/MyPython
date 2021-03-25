**FUNCTION:**
a function is named block that contains reusable logic.

**Parameter v/s Argument:**
parameter:defination time created variable is called parameter.
outer level variables define as parameter.

**Argument**:
when calling the function used varible define as arguments.
argumnents can be value,variable,expressions.

**Positional arguments**:

Positional arguments are arguments that can be called by their position in the function definition.

**Keyword arguments**:

Keyword arguments are arguments that can be called by their name. Required arguments are arguments that must passed to the function. 
we can put parameter in any sequence.

**Default argumnets**:

Default values indicate that the function argument will take that value if no argument value is passed during the function call. The default value is assigned by using the assignment(=) operator of the form keywordname=value.

**Keywords Arbitary Parameters**:
If the number of keyword arguments is unknown, add a double ** as parameter.
internally it becomes dictionary.

**Positional Arbitary Parameter:**
Sometimes, we do not know in advance the number of arguments that will be passed into a function. Python allows us to handle this kind of situation through function calls with an arbitrary number of arguments.

In the function definition, we use an asterisk (*) before the parameter name.
we can't pass keywords as arguments.

**Positional only Parameters:**
To specify arguments as positional only, a / marker should be added after all those arguments in the function definition.
All parameters to the left of / can only be passed positionally. 

**Keyword Only Parameter:**
We use * parameter ,all parameters after * become keyword only parameters.

