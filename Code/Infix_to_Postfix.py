class myStack:
  def __init__(self):
    self.lst=[]

  def push(self, data):
    self.lst.append(data)

  def pop(self):
    if self.lst:
        return self.lst.pop()
    else:
        return 'None'

  def is_empty(self):
    return self.lst==[]

  def peek(self):
    return self.lst[-1]
  



def InfixToPostfix(exp):
  s = myStack()
  p = {'+' : 1 , '-':1 , '*':2 , '/': 2}
  output = ''
  for i in exp:
    if i.isalpha():
      output += i
    elif i == '(':
      s.push('(')
    elif i == ')':
      while not s.is_empty() and s.peek() != '(':
        output += s.pop()
      s.pop()
    else:
      while not s.is_empty()  and s.peek() != '('  and p[i] <= p[s.peek()]:
        output += s.pop()
      s.push(i)
    
  while not s.is_empty():
    output += s.pop()
  return output


print(InfixToPostfix('a*b+c*d'))
