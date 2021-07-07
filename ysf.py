#tugas python

tanya = 'y'
while(tanya == 'y'):
    class Node(object):
        def __init__(self,value):
            self.value=Value
            self.left=None
            self.right=None

    class BinaryTree(object):
        def __init__(self,root):
            self.root=None(root)
        
        def print_tree(self,travelsal_type):
            if traversal_type=='preorder':
                return self.preorder_print(tree.root,'[')
            else:
                print('traversal type' +
                       str(traversal_type),+'is not supported.')
                return False
        def preorder_print(self,start,trevelsal):
            if start:
                travelsal +=(str(start.value)+'] [')
                traversal =self.preorder_print(star.left,traversal)
                traversal =self.preorder_print(star.right,traversal)
            return traversal
        
        root=input(str('input akar;'))
        simbol_kiri=input(str('input simbol_kiri='))
        simpul_kanan=input(str('input simbul_kanan='))
        ranting_kiri_kanan=input(str('input ranting_kiri_kanan='))
        ranting_kiri_kiri=input(str('input ranting_kiri_kiri='))
        ranting_kanan_kanan=input(str('input ranting_kaknan_kanan='))
        ranting_kanan_kiri=input(str('input ranting_kanan_kiri='))

        tree=binary_tree(root)
        tree.root.left=Node(simbol_kiri)
        tree.root.right=Node(simbol_kanan)
        tree.root.lift.right=(ranting_kiri_kanan)
        tree.root.left.left=(ranting_kiri_kiri)
        tree.root.right.right=(ranting_kanan_kanan)
        tree.root.right.left=(ranting_kanan_kiri)
        print()
        print(tree.print_tree('preorder'))
        print()
        tanya=input(str('apakah anda ingin mengulangnya? [Y/N]:'))
        print()





