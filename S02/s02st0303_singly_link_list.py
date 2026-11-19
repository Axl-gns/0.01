#importando clase node
from s02t0107_linked_list import Node 
#creando la clase de una lista enlazada
class Singly_Linked_List:
  #cosntructor
  def  __init__(self):
    self.head=None
    self.tail = None
    self.size = 0 
    #metodo de insercion de nodo en lista
  def append(self,data):
    #creo el nodo
    new_node = Node(data)

    # si hay teal, en nuevo nodo 
    #pasa a ser el nuevo tail 
    if self.tail:
        self.tail.next = new_node 
        self.tail = new_node

        #si no hay tail
    else: 
        self.tail = new_node 
        self.head = new_node
    self.size += 1 

  #insertando en posicion intermedia
  #[a->b->c] -1 2
  #si[1 2 3]
  def append_at_location(self, data, index):
     if index < 1 or index > self.size + 1:
        raise IndexError(f"Indice {index} fuera de rango NENE")
     #crea un nuevo nodo
     new_node = Node(data) 
     
     #insertar al incio 
     if index == 1:
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
         # incremento en el 1 tamaño 
        self.size += 1
 
     current = self.head
     prev = None 
     position = 1
     #transversal 
     while current is not None and position < index:
       prev = current 
       current = current.next
       position += 1
       #llegando a la posicion
       #estoy al final?
       if current is None:
          prev.next = new_node
          self.tail = new_node
          self.size += 1
          return


def main():
  my_list = Singly_Linked_List()
  #agregar elementos a la lista
  my_list.append(30)
  my_list.append(59)
  my_list.append(80)
  my_list.append(100)
  #recorrer la lista
  for value in my_list.head.iter():
    print(f" {value}, ",end=" ")

#1 creo funcion principal
# def main():
#  #2coloco el codigo ejecutable
#  test_node = Node("prueba")
#  print(f"valor del nodo: {test_node.data}")

 #evaluo el valor name __name__
if __name__ == "__main__":
   main()