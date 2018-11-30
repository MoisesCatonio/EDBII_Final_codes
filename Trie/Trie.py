from collections import OrderedDict
from copy import deepcopy
alfabeto = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".split(",")
defaultdict = OrderedDict() 

for letter in alfabeto:
		defaultdict[letter] = None
		
class No():

	def __init__(self, char=None):
		self.char = char
		self.filhos = deepcopy(defaultdict)
		self.folha = False

	def print(self, palavra):
		if (self.folha == True):
				print(palavra)
		for letter in alfabeto:
				if (self.filhos[letter] is not None):
						self.filhos[letter].print(deepcopy(palavra+letter))		
	def delete(self):
		self.char = None
		self.filhos = None
		self.folha = None

class Arvore():
	referencia = No(); 

	def filho_nao_unico(self, no):
		contador = 0
		for char in defaultdict:
			if no.filhos[char] != None:
				contador += 1
		if contador > 1:
			return 1
		elif contador == 1:
			return 0
		else:
			return -1

	def Insert(self, palavra, no=referencia):
		palavra = palavra.lower()
		listedPalavra = list(palavra)
		contador = 0
		for char in listedPalavra:
			contador+= 1
			if(no.filhos[char] is not None):
				no = no.filhos[char]
			else:
				no.filhos[char] = No(char)
				no = no.filhos[char]
			if (contador == len(listedPalavra)):
				no.folha = True
	def print(self):
		print("Print:")
		self.referencia.print("")

	def busca(self, palavra, no=referencia):
		palavra = palavra.lower()
		listedPalavra = list(palavra)
		retorno = ""
		contador = 0
		last_char_folha = False
		for char in listedPalavra:
			contador += 1
			if(contador <= len(listedPalavra)):
				if(no.filhos[char] is not None):
					no = no.filhos[char]
					retorno = retorno + str(no.char)
				else:
					retorno = ""
					print("Palavra não encontrada")
					break
			last_char_folha = no.folha
		if(last_char_folha == True):
			print("A seguinte palavra foi encontrada: ")
			return retorno
		else:
			print("A palavra não foi encontrada")
			retorno = ""
			return retorno

	def delete_palavra_interna(self, palavra, no=referencia):
		contador = 0
		palavra = palavra.lower()
		listedPalavra = list(palavra)
		for char in listedPalavra:
			contador += 1
			if(contador == len(listedPalavra)):
				no.filhos[char].folha = False
			elif(no.filhos[char] is not None):
				no = no.filhos[char] 
			
	def delete(self, palavra, no=referencia):
		palavra = palavra.lower()
		listedPalavra = list(palavra)
		impedidor = -1
		contador = 0
		contador_comparador = 0
		ate_o_fim = 0
		for char in listedPalavra:
			contador += 1
			if(self.filho_nao_unico(no) == 1 or no.folha == True):
				impedidor = contador
			if(no.filhos[char] is not None):
				no = no.filhos[char]
		
		if(self.filho_nao_unico(no) >= 0):
			ate_o_fim = 0
		else:
			ate_o_fim = 1

		no = self.referencia
		
		for char in listedPalavra:
			contador_comparador += 1
			if(contador_comparador == impedidor and no.filhos[char] is not None):
				if(ate_o_fim == 1):
					no.filhos[char] = None
					break
				else:
					self.delete_palavra_interna(palavra)
					break
			elif(no.filhos[char] is not None): 
				no = no.filhos[char]

tree = Arvore()
tree.Insert("Cavalo")
tree.Insert("Abelha")
tree.Insert("Abeliano")
tree.Insert("Cava")
tree.Insert("Cavala")
tree.Insert("Caverna")
tree.Insert("Cavernoso")
tree.Insert("Cadete")
tree.Insert("Cacife")
tree.Insert("Cacife")

tree.print()				
print(" ")

print(tree.busca("Abeliano"))
print(tree.busca("Cav"))

tree.delete("Cavalo")
tree.delete("Cava")
tree.delete("Ca")
print(" ")
tree.print()