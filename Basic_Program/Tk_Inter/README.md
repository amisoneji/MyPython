**Tkinter:**

> It is one of the GUI library to create desktop based GUI application using python.

> This library was the part of tcl language with name Tk.

> Python borrowed it from tcl and renamed Tkinter.


**Widget:**

> A graphical component that has visible interface and rectangular in shape.

> In coding,each widget is represented by object.

**Container Widgets:**

	
        > Top Level(Tk)
	      > Child Level(Frame)


**Basic Widgets:**
 
	   
        > Label,Entry,Text,Button,Combobox(drop down),etc.


**Layout Manager:**
  
	
    > Pack(side,anchor,padx,pady,ipadx,ipady,fill)
		side:left,right,top(default),bottom
		anchor:e,w,n,s,ne,se,nw,sw,center(default)
		fill=X,Y,BOTH

	 > Place(x,y,relx,rely,width,height,relwidth,relheight)

	 > Grid(row,column,padx,pady,ipadx,ipady,sticky)
		here sticky=anchor

**How to get width & height of widget:**

> widget.update()

> w=widget.winfo_width()

> h=widget.winfo_height()


**Event Handling:**

**Event:**

  Change of state of an object is called event 
                      
                 OR

  Any user interaction with any widget ,called event

**EventHandling:**

  Executing logic on an event,called eventhandling.

**Types of Event:**

> Button
	whenever a mouse button is clicked on any widget.

> Motion
	Whenever mouse is moved over any widget.

> Enter
	Whenever mouse is entered to a widget.

> Leave
	Whenever mouse is exited from a widget.
etc.

**How to Handle Event:**

> first identify type of event
> call bind() on the widget
	widget.bind('<EventType>',callback)

  Note:here callback represents a function or method

> format of callback:
	def callback(event): 
		logic

  Note:Button widget also provides command arg to pass this callback and in this case callback function does not take event arg.

	b=Button(....,command=callback)

**messagebox:**

> messagebox.showinfo(title=None, message=None)

> messagebox.showwarning(title=None, message=None)

> messagebox.showerror(title=None, message=None)

> messagebox.askquestion(title=None,message=None)

> messagebox.askokcancel(title=None, message=None)

> messagebox.askretrycancel(title=None, message=None)

> messagebox.askyesno(title=None, message=None)

> messagebox.askyesnocancel(title=None, message=None)

**filedialog:**

> filedialog.askopenfile()

> filedialog.askopenfiles()

> filedialog.askopenfilename()

> filedialog.askopenfilenames()

> filedialog.askdirectory()

> filedialog.asksaveasfile()

**simpledialog**

> simpledialog.askstring()

**ScrolledText:**	

Text+Scrollbar

st=scrolledtext.ScrolledText(parent,width,height)

st.insert(END,'msg')

st.delete('1.0',END)	

**drop-down list:**
 

from tkinter import ttk

comboExample = ttk.Combobox(app, 
                            values=[
                                    "January", 
                                    "February",
                                    "March",
                                    "April"])

comboExample.current(1)

comboExample.get()
