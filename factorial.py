i = int(input("Привет!Я посчитаю для тебя фактораил, введи число "))
while i>1:
 factorial = 1

 for i in range(1, i+1):
  factorial *= i
 print("факториал=",factorial)
 i = int(input("Введи число "))
 if i<1:
  print("Фактораил не может быть меньше 1!")