"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().

"""

# Import the required modules
from tkinter import messagebox, simpledialog, Tk
# Create a window object
window = Tk()
# Hide the window, hint: use the withdraw method
window.withdraw()
# Ask the user for the first number   

def is_it_alive(yay,fed,run):
   if yay < 1:
      messagebox.showinfo('Oh no!',name+"'s happiness reached "+str(yay))
   elif fed < 1:
      messagebox.showinfo('Oh no!',name+"'s food reached "+str(fed))
   elif run < 1:
      messagebox.showinfo('Oh no!',name+"'s activity reached "+str(run))
   else:
      messagebox.showinfo(':)','you win')

happy = 3
food = 3
active = 3
pet = simpledialog.askstring('you have a pet CREATURE','write "cat" or "fish" or "bird" to choose your CREATURE')
if pet == 'cat' or pet == 'fish' or pet == 'bird':
   name = simpledialog.askstring('name your '+pet,'what is its name?')
   action = 1
   action1 = simpledialog.askstring('1/5: walk, pet, or feed '+name+'?','choose your first action')
   if action1 == 'walk':
      food = food - 1
      active = active + 1
      if pet == 'fish':
         action2 = simpledialog.askstring('2/5: why are you walking a fish??? but ok??','walk, pet, or feed '+name+'?')
      else:
         action2 = simpledialog.askstring('2/5: you took '+name+' on a walk','walk, pet, or feed?')
   elif action1 == 'pet':
      happy = happy + 1
      active = active - 1
      action2 = simpledialog.askstring('2/5: you pet your '+pet+' good job','walk, pet, or feed '+name+'?')
   elif action1 == 'feed':
      happy = happy - 1
      food = food + 1
      action2 = simpledialog.askstring('2/5: you fed '+name, 'walk, pet, or feed?')
   # action 1 complete
   action = 2
   if action2 == 'walk':
      food = food - 1
      active = active + 1
      if pet == 'fish':
         action3 = simpledialog.askstring('3/5: why are you walking a fish??? but ok??','walk, pet, or feed '+name+'?')
      else:
         action3 = simpledialog.askstring('3/5: you took '+name+' on a walk','walk, pet, or feed?')
   elif action2 == 'pet':
      happy = happy + 1
      active = active - 1
      action3 = simpledialog.askstring('3/5: you pet your '+pet+' good job','walk, pet, or feed '+name+'?')
   elif action2 == 'feed':
      happy = happy - 1
      food = food + 1
      action3 = simpledialog.askstring('3/5: you fed '+name, 'walk, pet, or feed?')
   # action 2 complete
   action = 3
   if action3 == 'walk':
      food = food - 1
      active = active + 1
      if pet == 'fish':
         action4 = simpledialog.askstring('4/5: why are you walking a fish??? but ok??','walk, pet, or feed '+name+'?')
      else:
         action4 = simpledialog.askstring('4/5: you took '+name+' on a walk','walk, pet, or feed?')
   elif action3 == 'pet':
      happy = happy + 1
      active = active - 1
      action4 = simpledialog.askstring('4/5: you pet your '+pet+' good job','walk, pet, or feed '+name+'?')
   elif action3 == 'feed':
      happy = happy - 1
      food = food + 1
      action4 = simpledialog.askstring('4/5: you fed '+name, 'walk, pet, or feed?')
   # action 3 complete
   action = 4
   if action4 == 'walk':
      food = food - 1
      active = active + 1
      if pet == 'fish':
         action5 = simpledialog.askstring('5/5: why are you walking a fish??? but ok??','walk, pet, or feed '+name+'?')
      else:
         action5 = simpledialog.askstring('5/5: you took '+name+' on a walk','walk, pet, or feed?')
   elif action4 == 'pet':
      happy = happy + 1
      active = active - 1
      action5 = simpledialog.askstring('5/5: you pet your '+pet+' good job','walk, pet, or feed '+name+'?')
   elif action4 == 'feed':
      happy = happy - 1
      food = food + 1
      action5 = simpledialog.askstring('5/5: you fed '+name, 'walk, pet, or feed?')
   if action5 == 'walk':
      food = food - 1
      active = active + 1
   elif action5 == 'pet':
      happy = happy + 1
      active = active - 1
   elif action5 == 'feed':
      food = food + 1
      happy = happy - 1
   is_it_alive(happy,food,active)
   
   
else:
   messagebox.showinfo('that is not an option','restart the game to try again')