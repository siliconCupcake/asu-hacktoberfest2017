 def countingsort( aList, k ): # k is max element in aList
    counter = [0] * ( k + 1 ) # array with number of occurrences of each value initialized to 0
    for i in aList:
      counter[i] += 1 # calculate number of occurrences of each value
 
    ndx = 0;
    for i in range( len( counter ) ): # place value at its correct position in the array
      while 0 < counter[i]:
        aList[ndx] = i
        ndx += 1
        counter[i] -= 1