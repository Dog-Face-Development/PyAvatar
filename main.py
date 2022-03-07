"""
PyAvatar - sort and display avatars by website. 
Copyright (C) 2020-2022 @willtheorangeguy

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

# Import Statements
from tkinter import *

# Build Window
window = Tk()
window.title("Online Account Avatar and Banners")

# Window Title 
title = Label(window, text = "Online Account Avatar and Banners")

# Account Avatars
account1 = Frame(window)
img_account1 = PhotoImage(file = "PyAvatar/images/placeholder.gif") # needs to be a GIF
title_account1 = Label(account1, image = img_account1)
text_account1 = Label(account1, text = "Account #1")

account2 = Frame(window)
img_account2 = PhotoImage(file = "PyAvatar/images/placeholder.gif") # needs to be a GIF
title_account2 = Label(account2, image = img_account2)
text_account2 = Label(account2, text = "Account #2")

account3 = Frame(window)
img_account3 = PhotoImage(file = "PyAvatar/images/placeholder.gif") # needs to be a GIF
title_account3 = Label(account3, image = img_account3)
text_account3 = Label(account3, text = "Account #1")

account4 = Frame(window)
img_account4 = PhotoImage(file = "PyAvatar/images/placeholder.gif") # needs to be a GIF
title_account4 = Label(account4, image = img_account4)
text_account4 = Label(account4, text = "Account #1")

account5 = Frame(window)
img_account5 = PhotoImage(file = "PyAvatar/images/placeholder.gif") # needs to be a GIF
title_account5 = Label(account5, image = img_account5)
text_account5 = Label(account5, text = "Account #1")

# Window Layout
title.grid(row = 1, column = 1, columnspan = 5)

# Sustain Window
window.mainloop()
