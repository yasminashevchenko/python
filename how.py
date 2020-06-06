inputTextOne="Привет!Сколько тебе лет? "
i=int(input(inputTextOne))
type(range(i+1))
while type(i)==int:
  
  if i in range(0, 5):
          print("Тебе пора в детский сад")
  if i in range(6, 17):
          print("Тебе пора в школу")  
  if i in range(18, 23):
          print("Тебе пора в институт")
  if i in range(23, i+1):
          print("Тебе пора на работу")

  i=int(input(inputTextOne))