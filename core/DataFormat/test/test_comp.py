import ROOT,sys
import matplotlib.pyplot as plt

def print_mat(mat):

    img_array=ROOT.larcv.as_ndarray(mat)
    for row in range(mat.meta().rows()):
        for col in range(mat.meta().cols()):
            print(int(mat.pixel(row,col)), end=' ')
        print()
    print()

def main():

    print()
    ncols=24
    nrows=24

    img=ROOT.larcv.Image2D(nrows,ncols)
    img.paint(0)
    for row in range(nrows):
        for col in range(ncols):
            v=0
            if row==col: v+=1
            if (row+col - nrows) % 4==0: v+=1
            img.set_pixel(row,col,v)

    print_mat(img)
    
    img.compress(12,12)
    
    print_mat(img)

    img.compress(4,4)

    print_mat(img)

if __name__ == '__main__':
    main()
