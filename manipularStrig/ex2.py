file = open('c:/Users/home/Desktop/PYTON/manipularStrig/valor.csv','w+')

x = [1,2,3,4,5,6]
y = 0



for i in range(len(x)) :
    
    y = 2 * x[i] + 6 
    file.writelines(str(x[i]) + ", " + str(y) + '\n' )




file.close()