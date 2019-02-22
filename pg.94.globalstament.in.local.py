def spam():
  global eggs
  eggs = 'spam'
eggs = 'global'
spam()
print(eggs)

'''
When you run this program, the final print() call will output this:
spam
'''
