from Gestion_Datos import Pendientes, Completados
i=0
h=0
Pendientes = Pendientes()
Completados = Completados()
print("**********************")
print("******Bienvenido******") 
print("**********************")

while(i==0):
   print("¿que desea hacer?\n1. digitar nuevo pedido\n2. marcar pedido como competado\n3. ver pedidos pendientes \n4.ver pedidos completados \n5. salir")
   op1 = int(input())
   if(op1 == 1):
      Pendientes.add_Data()
   else:
      if(op1 == 2):
         Completados.add_Data()
      else:
         if(op1==3):
            Pendientes.show_Data()
         else:
            if(op1 == 4):
               Completados.show_Data
            else:
               if(op1== 5):
                     print("¡Hasta la proxima! :)") 
                     i = 1
               else:
                     print("Opcion invalida")  
