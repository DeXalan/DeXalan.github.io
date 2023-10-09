from js import document
class GeneradorCongruencial:
    def __init__(self, semilla, a, b, m):
        self.semilla = semilla
        self.a = a
        self.b = b
        self.m = m
        self.valor_actual = semilla

    def generar_numero(self):
        self.valor_actual = (self.a * self.valor_actual + self.b) % self.m
        return self.valor_actual / self.m

def onClickButton():
    # Ejemplo de uso
    semilla = int(document.querySelector("#X0").value)
    a = int(document.querySelector("#A").value)
    b = int(document.querySelector("#B").value)
    m = int(document.querySelector("#M").value)
    n = int(document.querySelector("#N").value)

    generador = GeneradorCongruencial(semilla, a, b, m)


    divTable = document.querySelector("#divTable")
    oldTable = document.querySelector("#dataTable")
    divTable.removeChild(oldTable)

    newTable = document.createElement("table", { id: "dataTable" }) 
    newTable.id = "dataTable"
    
    newTHead = document.createElement("thead")
    newTHeadCell_1 = document.createElement("th")
    newTHeadCell_1.innerText = "n"
    newTHeadCell_2 = document.createElement("th")
    newTHeadCell_2.innerText = "Xn"
    newTHeadCell_3 = document.createElement("th")
    newTHeadCell_3.innerText = "Un"
    newTHeadCell_3 = document.createElement("th")
    newTHeadCell_3.innerText = "Z0"
    newTHeadCell_3 = document.createElement("th")
    newTHeadCell_3.innerText = "Mn"
    newTHead.appendChild(newTHeadCell_1)
    newTHead.appendChild(newTHeadCell_2)
    newTHead.appendChild(newTHeadCell_3)
    
    newTBody = document.createElement("tbody", { id: "tbody" })
    
    newTable.appendChild(newTHead)
    newTable.appendChild(newTBody)

    i = 1
    for _ in range(n):
        numero_aleatorio = generador.generar_numero()
        
        row = document.createElement("tr")
        
        celda1 = document.createElement("td")
        celda1.textContent = i
        
        celda2 = document.createElement("td")
        celda2.textContent = numero_aleatorio * m 

        celda3 = document.createElement("td")
        celda3.textContent = numero_aleatorio

        row.appendChild(celda1)
        row.appendChild(celda2)
        row.appendChild(celda3)

        newTBody.appendChild(row)
        i += 1
    
    divTable.appendChild(newTable)
