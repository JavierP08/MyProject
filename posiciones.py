import json
with open("C:/Users/PC/Documents/Escuela/Agentes/agentData.json", "r") as file:
        data = json.load(file)
with open("C:/Users/PC/Documents/Escuela/Agentes/agent_positions.json", "r") as file:
        data2 = json.load(file)

def posX(i):
    agente = data[i]
    x = agente['x']
    x = 50 + (x * 100)
    return x

def posY(i):
    agente = data[i]
    y = agente['y']
    y = 50 + (y * 100)
    return y

def direccion(i):
    agente = data[i]
    x = agente['x']
    y = agente['y']
    meta = agente['goal']
    if meta[0] == x:
         direccion = 1
         if meta[1] < y:
              direccion = 2
    elif meta[1] == y:
         direccion = 3
         if meta[0] < x:
              direccion = 4
    return direccion

def numAgentes():
    numero = len(data)
    return numero - 1

def agenteId(i):
     agente = data[i]
     id_a = agente["id"]
     return id_a

def obtener_posicion_por_id_x(agent_id, step,prevX):
    for agente_info in data2[step]:
        if agente_info["agent_id"] == agent_id:
            x = agente_info["x"]
            newX = (50 + (x*100))
            suma = newX - prevX
            return prevX + suma
        
def obtener_posicion_por_id_y(agent_id, step,prevY):
    for agente_info in data2[step]:
        if agente_info["agent_id"] == agent_id:
            y = agente_info["y"]
            newY = (50 + (y*100))
            suma = newY - prevY
            return prevY + suma