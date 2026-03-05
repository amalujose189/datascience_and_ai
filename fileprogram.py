#writing the data into a file
#read the date from the file
#append the data into a file


'''f=open('sample1.txt','x')
f.write("hello ,this is new file")'''


'''f=open('test1.txt','w')
f.write("good")
f.close()
print('file saved')'''

'''f=open('sample1.txt','x')
f.write("hello ,this is new file")
'''

'''f=open('test1.txt','w')
f.writelines(["good\n","how\n","are you"])
f.close()
print("file saved")
'''

#read method
#while using read method file should exist . if there is no file it will shows error
'''f=open('test1.txt','r')
result=f.read()
print(result)
f.close()'''


'''f=open('test1.txt','r')
result=f.readline() #only print first line
print(result)
f.close()'''
#readline while read lines line by line
'''f=open('test1.txt','r')
result=f.readline()
result2=f.readline()  #only print first line
print(result)
print(result2)
f.close()'''

'''f=open('test1.txt','r')
result=f.readlines()
 #only print first line
print(result)
f.close()'''

#append

#if we use write will rewrite the content
f=open('test1.txt','a')
f.writelines("\n amalu")
f.close()
print("file saved")