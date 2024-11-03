def mad_libs():
     template=(
         "once upon a time {their}"
         " {adjective}  lived in a {color} house,"
     )
     their =input("enter their")
     adjective = input("enter adjective")
     color=input("enter color")
     story = template.format(their=their,adjective=adjective,color=color)
     print(story)
     
     
     
mad_libs()
     