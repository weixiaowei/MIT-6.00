def cmp(x, y, z):
##    if x < y:
##        if x < z:
##            print 'x = ' + str(x) + ' is the least'
##        else:
##            print 'z = ' + str(z) + ' is the least'
##    else:
##        if y < z:
##            print 'y = ' + str(y) + ' is the least'
##        else:
##            print 'z = ' + str(z) + ' is the least'


      if x < y and x < z:
          return x
      elif y < z:
          return y
      else:
          return z


x = int(raw_input('x = '))
y = int(raw_input('y = '))
z = int(raw_input('z = '))
print(ctm3(x, y, z))
