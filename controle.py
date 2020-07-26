from PyQt5 import uic,QtWidgets

def funcao_principal():

    campo1 = Projeto_Formulario.lineEdit.text()
    campo2 = Projeto_Formulario.lineEdit.text()
    campo3 = Projeto_Formulario.lineEdit_3.text()

    if Projeto_Formulario.radioButton.isChecked():
        print("Categoria Informática ")
    elif Projeto_Formulario.radioButton_2.isChecked():
        print("Categoria Alimentos")
    else :
        print("Categoria Eletrônicos ")

    


    print("Codigo", campo1)
    print("Descricao", campo2)
    print("Preco", campo3)




app=QtWidgets.QApplication([])
Projeto_Formulario=uic.loadUi("Projeto_Formulario.ui")
Projeto_Formulario.pushButton.clicked.connect(funcao_principal)

Projeto_Formulario.show()
app.exec()