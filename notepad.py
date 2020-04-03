from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfile,asksaveasfilename

win = Tk()
win.title("Clone Notepad")

def abrir_arquivo():
	blank.delete("1.0", END)
	arquivo = askopenfile(mode='r', filetypes=[('text files', '*.txt')])
	if(arquivo is not None):
		texto = arquivo.read()
		blank.insert("1.0", texto)

def salvar_arquivo():
	notepad_texto = blank.get("1.0", "end-1c")
	arquivo = asksaveasfilename(title="Salvar", filetypes=[('text files', '*.txt')])
	with open(arquivo, "w") as data:
		data.write(notepad_texto)


barramenu = Menu(win)
win.config(menu=barramenu)

arquivoMenu = Menu(barramenu, tearoff=0)
barramenu.add_cascade(label="Arquivo", menu=arquivoMenu)
arquivoMenu.add_command(label="Abrir", command=abrir_arquivo)
arquivoMenu.add_command(label="Salvar", command=salvar_arquivo)
arquivoMenu.add_command(label="Sair", command=win.destroy)

blank = Text(win, font=("arial", 10))
blank.pack()

win.mainloop()