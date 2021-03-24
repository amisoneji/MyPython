It is technique to avoid abnormal program termination by executing alternative statements.

**Try & Except**:

it contains those set of statements whose execution may genrate exception.
often try block use either except or finally block.
Exception can not handle keyboard & stop iteration error but default Except can handle any exception.
Default except must be last handler.

**Else & Finally**

Genrally we use finally block to free the resources (like file/database/network etc)taken in try block.
if in try block,there is no excepltion then else will executes
if if try block execution occure or not finally block always executed


**Raise keyword**

It is used to genrate exception explicity.
Sometimes need of genrate exception base custom requiremnet and for such requirement interpreter does not genrate exception hence we use raise keyword.

**Assert keyword**

Already include condition loop
it is also used to genrate exception explicity.
