from PyQt5 import uic,QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    port="3307",
    user="root",
    passwd="123456",
    database="cadastro_python"
)

print(banco)


def funcao_principal():

    campo1 = Projeto_Formulario.lineEdit.text()
    campo2 = Projeto_Formulario.lineEdit_2.text()
    campo3 = Projeto_Formulario.lineEdit_3.text()

    categoria = ""

    if Projeto_Formulario.radioButton.isChecked():
        print("Categoria Informática ")
        categoria = "Informática"
    elif Projeto_Formulario.radioButton_2.isChecked():
        print("Categoria Alimentos")
        categoria = "Alimentos"
    else :
        print("Categoria Eletrônicos ")
        categoria = "Eletrônicos"

    print("Codigo", campo1)
    print("Descricao", campo2)
    print("Preco", campo3)
    
    cursor = banco.cursor()
    comando_SQL = "INSERT INTO produtos (codigo,descriçao,preco,categoria) VALUES (%s,%s,%s,%s)"
    dados = (str(campo1),str(campo2),str(campo3),categoria)
    cursor.execute(comando_SQL,dados)
    banco.commit()
    Projeto_Formulario.lineEdit.setText("")
    Projeto_Formulario.lineEdit_2.setText("")
    Projeto_Formulario.lineEdit_3.setText("")

def Chama_segundatela():
    Projeto_Formulario2.show()
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM produtos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

########exibi as colunas######################

    Projeto_Formulario2.tableWidget.setRowCount(len(dados_lidos))
    Projeto_Formulario2.tableWidget.setColumnCount(5)

    for i in range(0, len(dados_lidos)):
        for j in range(0,5):
            Projeto_Formulario2.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


app=QtWidgets.QApplication([])
Projeto_Formulario=uic.loadUi("Projeto_Formulario.ui")
Projeto_Formulario2=uic.loadUi("Projeto_Formulario2.ui")

Projeto_Formulario.pushButton.clicked.connect(funcao_principal)
Projeto_Formulario.pushButton_2.clicked.connect(Chama_segundatela)

Projeto_Formulario.show()
app.exec()
