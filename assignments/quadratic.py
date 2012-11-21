def quadratic(a,b,c):
	try:
		discriminant = (b**2)-(4*a*c)

		if discriminant < 0:
			print "The quadratic {0}x^2 {1:+}x {2:+} has no roots".format(a,b,c)
			return None
		elif discriminant == 0:
			print "The quadratic {0}x^2 {1:+}x {2:+} only has 1 root".format(a,b,c)
			return (-b)/(2*a)
			
		else:
			x1 = (-b + (discriminant**0.5))/(2*a)
			x2 = (-b - (discriminant**0.5))/(2*a)
			print "The quadratic {0}x^2 {1:+}x {2:+} has 2 roots".format(a,b,c)
			return (x1,x2)
	
	except TypeError:
		print "[Error] Invalid arguments types, must provide a numeric argument"
	except ZeroDivisionError:
		print "[Error] A must be > 0, invalid argument of A"



print quadratic(2,1,2)#No roots
print quadratic(1,12,36)#One roots
print quadratic(1,4,-21)#Two roots