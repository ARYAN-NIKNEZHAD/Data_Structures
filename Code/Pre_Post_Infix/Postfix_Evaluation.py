from pythonds.basic import Stack



def f(op, a, b):
  if op == '*':
    return a * b
  elif op == '/':
    return a / b
  elif op == '+':
    return a + b
  else:
    return a - b




def postEval(exp):
  s = Stack()
  lst = exp.split()
  for t in lst:
    if t in '0123456789':
      s.push(int(t))
    else:
      x = s.pop()
      y = s.pop()
      r = f(t,y,x)
      s.push(r)
  return s.pop()


print(postEval('7 8 + 3 2 + /'))
