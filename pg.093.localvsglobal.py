def spam():
  eggs = 'spam local'
print(eggs) # prints 'spam local'
def bacon():
  eggs = 'bacon local'
  print(eggs) # prints 'bacon local'
  spam()
  print(eggs) # prints 'bacon local'

eggs = 'global'
bacon()
print(eggs) # prints 'global'

'''
When you run this program, it outputs the following:
bacon local
spam local
bacon local
global
'''
