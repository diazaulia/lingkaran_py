from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def initFun():
    glClearColor(1.0,1.0,1.0,0.0)
    glColor3f(128.0,0.0, 0.0)
    glPointSize(5.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0,640.0,0.0,480.0)
    
def AlgLingkaran():
    #tentukan titik pusat dan jari-jari
    r = 150
    xc = 300
    yc = 300

    #hitung p awal dan set nilai awal untuk x dan y
    p = 1-r;
    x = 0;
    y = r;

    glBegin(GL_POINTS);

    #perulangan untuk menggambar titik
    while (x <= y):
        x = x+1 #tambah nilai x
        if (p < 0): 
            p += 2 * x + 1 #hitung p selanjutnya jika p < 0
        else:
            y = y - 1 #kurangi nilai y
            p += 2 * (x - y) + 1 #hitung p selanjutnya jika p > 0 atau p = 0

        #translasi terhadap titik pusat dan cerminkan
        glVertex2i(xc + x, yc + y)
        glVertex2i(xc - x, yc + y)
        glVertex2i(xc + x, yc - y)
        glVertex2i(xc - x, yc - y)
        glVertex2i(xc + y, yc + x)
        glVertex2i(xc - y, yc + x)
        glVertex2i(xc + y, yc - x)
        glVertex2i(xc - y, yc - x)
    glEnd()
    glFlush()

if __name__ == '__main__':
    glutInit()
    glutInitWindowSize(640,480)
    glutCreateWindow("Komputer Grafik - Algoritma Lingkaran")
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutDisplayFunc(AlgLingkaran)
    initFun()
    glutMainLoop()