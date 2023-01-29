import linearset as ls

smith = ls.Set()
smith.add( "CSCI-112" )
smith.add( "MATH-121" )
smith.add( "HIST-340" )
smith.add( "ECON-101" )

roberts = ls.Set()
roberts.add( "POL-101" )
roberts.add( "ANTH-230" )
roberts.add( "CSCI-112" )
roberts.add( "ECON-101" )

sameCourses = ls.Set()
print("%50s"%('-'*50))
print('Smith is taking courses:')
for course in smith:
    print(course,end=', ')
print("\n%50s" % ('-' * 50))
print('Roberts is taking courses:')
for course in roberts:
    print(course,end=', ')
#print("\n%50s"%('-'*50))

if smith == roberts :
    print( "Smith and Roberts are taking the same courses." )
else :
    sameCourses = smith.intersection(roberts )
print("\n%50s"%('-'*50))
if len(sameCourses)==0 :
    print( "Smith and Roberts are not taking any of "\
    + "the same courses." )
else :
    print( "Smith and Roberts are taking some of the "\
    + "same courses:" )
for course in sameCourses :
    print( course )
print("\n%50s"%('-'*50))
print('Smith is taking courses different from Roberts.')
uniqueCourses = smith.difference( roberts )
for course in uniqueCourses :
    print( course )