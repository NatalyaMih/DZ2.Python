#Напишите программу, которая принимает на вход вещественное число и показывает 
# сумму его цифр.
#Пример:
#- 6782 -> 23
#- 0,56 -> 11

#n=int(input('Введите число:'))
#sum=0
#while (n>0):
 #num=n%10
 #sum=sum+num
 #n=n//10
#print ('Сумма цифр равна:', sum)





#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел 
# от 1 до N.
#Пример:
#Пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

#n=int(input('Введите число:'))
#f=1
#for i in range(n):
    #i=i+1
    #f=i*f
    #print(f, end= " ")



#Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

n=int(input('Введите число:'))
sum=0
i=1
for i in range(1,n+1):
    result=(1+1/i)**i
    sum=sum+result
    i+=1
    print(sum)

