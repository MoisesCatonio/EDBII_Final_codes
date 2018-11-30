from math import log
class node:
	def __init__(self, value):
		self.value = value
		self.left_child = None
		self.right_child = None
		self.h_left = 0
		self.h_right = 0

	def print(self):
		if (self.left_child is not None): 
			self.left_child.print()
		print(self.value)
		if (self.right_child is not None): 
			self.right_child.print()
	
	def isleaf(self):
		return (self.left_child is None) and (self.right_child is None)

	def fator_balanceamento(self):
		return self.h_left - self.h_right	

class Tree:
	def __init__(self):
		self.root = None
		self.number_elements = 0
	
	def add(self, value, root_subtree = None):
		if (root_subtree is None):
			root_subtree = self.root
			if (root_subtree is None):
				self.number_elements += 1
				self.root = node(value)
				return

		if (value < root_subtree.value):
			if (root_subtree.left_child is None):
				root_subtree.left_child = node(value)
				self.number_elements += 1
				root_subtree.h_left = 1
			else:
				root_subtree.left_child = self.add(value, root_subtree.left_child)
				root_subtree.h_left = max(root_subtree.left_child.h_left, root_subtree.left_child.h_right) + 1
		else:
			if (root_subtree.right_child is None):
				root_subtree.right_child = node(value)
				self.number_elements += 1
				root_subtree.h_right = 1
			else:
				root_subtree.right_child = self.add(value, root_subtree.right_child)
				root_subtree.h_right = max(root_subtree.right_child.h_left, root_subtree.right_child.h_right) + 1

		#balanceamento
		fator_balanceamento = root_subtree.fator_balanceamento()
		if (fator_balanceamento == -2):
			#rotaciona para a esquerda e atualiza a raiz da árvore se for o caso
			if (root_subtree.right_child.fator_balanceamento()) == -1:
				temp = self.rotation_RR(root_subtree)
				if (root_subtree is self.root):
					self.root = temp
			else:
				root_subtree.right_child = self.rotation_LL(root_subtree.right_child)
				temp = self.rotation_RR(root_subtree)
				if (root_subtree is self.root):
					self.root = temp
			return temp
		if (fator_balanceamento == 2):
			if (root_subtree.left_child.fator_balanceamento() == 1):
				#rotaciona para a direita e atualiza a raiz da árvore se for o caso
				temp = self.rotation_LL(root_subtree)
				if (root_subtree is self.root):
					self.root = temp	
			else:
				#rotaciona o filho esquerdo para a esquerda
				root_subtree.left_child = self.rotation_RR(root_subtree.left_child)
				#rotaciona para a direita e atualiza a root se for o caso
				temp = self.rotation_LL(root_subtree)
				if (root_subtree is self.root):
					self.root = temp
			return temp

		return root_subtree

	def remove(self, value, root_subtree = None):
		if (root_subtree is None):
			root_subtree = self.root
		#se o valor que procuro é menor, procure a esquerda
		if (value < root_subtree.value):
			if (root_subtree.left_child is None):
				return root_subtree
			else:
				root_subtree.left_child = self.remove(value, root_subtree.left_child)
				if (root_subtree.left_child is None):
					root_subtree.h_left = 0
				else:
					root_subtree.h_left = max(root_subtree.left_child.h_left, root_subtree.left_child.h_right)+ 1	
		#se o valor que procuro é maior, procure a direita 
		if (value > root_subtree.value):
			if (root_subtree.right_child is None):
				return root_subtree
			else:
				root_subtree.right_child = self.remove(value, root_subtree.right_child)
				if (root_subtree.right_child is None):
					root_subtree.h_right = 0
				else:
					root_subtree.h_right = max(root_subtree.right_child.h_left, root_subtree.right_child.h_right)+ 1

		#se for igual, verifique se é folha, se sim, só remova retornando None
		#Se tiver apenas filho esquerdo, retorne o filho esquerdo. Se tiver só direito, retorne o filho direito
		#Se for nó interno, pegue o maior dos menores filhos, troque o valor do pai por o valor dele e delete a folha
		if (root_subtree.value == value):
			if (root_subtree.isleaf()):
				self.number_elements -= 1
				return None
			if (root_subtree.left_child is None):
				self.number_elements -= 1
				return root_subtree.right_child
			if (root_subtree.right_child is None):
				self.number_elements -= 1
				return root_subtree.left_child

			temp = root_subtree.left_child
			if (temp.isleaf()):
				root_subtree.value = temp.value
				root_subtree.left_child = None
				root_subtree.h_left = 0
			else:
				while (temp.right_child):
					temp = temp.right_child
				root_subtree.value = temp.value
				root_subtree.left_child = self.remove(root_subtree.value, root_subtree.left_child)
				root_subtree.h_left = max(root_subtree.left_child.h_left, root_subtree.left_child.h_right)+ 1
					
		#balanceamento
		fator_balanceamento = root_subtree.fator_balanceamento()
		if (fator_balanceamento == -2):
			#rotaciona para a esquerda e atualiza a raiz da árvore se for o caso
			if (root_subtree.right_child.fator_balanceamento()) == -1:
				temp = self.rotation_RR(root_subtree)
				if (root_subtree is self.root):
					self.root = temp
			else:
				root_subtree.right_child = self.rotation_LL(root_subtree.right_child)
				temp = self.rotation_RR(root_subtree)
				if (root_subtree is self.root):
					self.root = temp
			return temp

		if (fator_balanceamento == 2):
			if (root_subtree.left_child.fator_balanceamento() == 1):
				#rotaciona para a direita e atualiza a raiz da árvore se for o caso
				temp = self.rotation_LL(root_subtree)
				if (root_subtree is self.root):
					self.root = temp	
			else:
				#rotaciona o filho esquerdo para a esquerda
				root_subtree.left_child = self.rotation_RR(root_subtree.left_child)
				#rotaciona para a direita e atualiza a root se for o caso
				temp = self.rotation_LL(root_subtree)
				if (root_subtree is self.root):
					self.root = temp
			return temp
		return root_subtree	

	def rotation_RR(self, root_subtree):
		temp = root_subtree.right_child
		root_subtree.right_child = temp.left_child
		root_subtree.h_right = 0 if temp.left_child is None else temp.h_left
		temp.left_child = root_subtree
		temp.h_left = max(root_subtree.h_left, root_subtree.h_right) + 1
		return temp

	def rotation_LL(self, root_subtree):
		temp = root_subtree.left_child
		root_subtree.left_child = temp.right_child
		root_subtree.h_left = 0 if temp.right_child is None else temp.h_right
		temp.right_child = root_subtree
		temp.h_right = max(root_subtree.h_left, root_subtree.h_right) + 1
		return temp

	def search(self, value):
		temp = self.root
		achou = False
		while (achou == False) and (temp is not None):
			if (value < temp.value):
				temp = temp.left_child
			elif (value > temp.value):
				temp = temp.right_child
			else:
				achou = True
		if (achou == True):
			print("Valor Encontrado \n")
		else:
			print("Valor Não Encontrado \n")					

	def height(self):
		return int(log(self.number_elements, 2))

	def print(self):
		self.root.print()
		print("\n")