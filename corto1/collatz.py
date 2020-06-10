#SERGIO ESTUARDO RUANO NAJARRO 
#201612203




def collatz(num):
    #agregar para obtener secuencia completa
    #yield num
    while(num != 1):
        if(num %2> 0):
            num = 3*num +1
            yield num
        else:
            num = num/2
            yield num

            

n=203
for i in range(2,n):
    print(list(collatz(i)))
  
#Funcionamiento:        30/40 no guarda las secuencias en un archivo
#Uso de Funciones       20/20
#Manejo de archivos     0/10
#Manejo de Listas       10/10
#Uso de git             20/20
#*****************************
#Total                  80/100

