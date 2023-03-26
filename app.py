clients = ["John", "Marry", "Kate"]

clientsHighPriority = ["Tob", "Pete"]
clientsLowPriority = ["Vicky", "Lessly"]

clients = clientsHighPriority + clients + clientsLowPriority

def showClients():
    for i in range(len(clients)):
        print(f"{i+1}. {clients[i]}")

showClients()

while True:
    name = input("Introduceti numele clientului: ")
    if name == "":
        break
    else:
        priority = input("Prioritate (inalta/normala): ")
        if priority == "inalta":
            clients.insert(0, name)
        else:
            clients.append(name)
        showClients()