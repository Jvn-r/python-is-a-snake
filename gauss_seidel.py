#this is a code to simulate The Gauss Seidel iterative method in math 

x = 0
y = 0
z = 0

def diag_dom(a11,a12,a13,a21,a22,a23,a31,a32,a33):
    di_dom_1 = a12 + a13
    di_dom_2 = a21 + a23
    di_dom_3 = a31 + a32

    if(a11>di_dom_1 and a22>di_dom_2 and a33>di_dom_3) :
        print("The Set of equations is correct!!Thank you")
    else :
        print("The equations are not Diagnolly Dominant!!Try Again ")
        exit()

def Calc_Iteration(a11,a12,a13,a21,a22,a23,a31,a32,a33,b1,b2,b3,x,y,z,n):
    if(n<=4):
        x_calc = (b1-(a12*y)-(a13*z))/a11
        y_calc = (b2-(a21 * x_calc)-(a23 * z))/a22
        z_calc = (b3-(a31 * x_calc)-(a32 * y_calc))/a33

        print(f"The {n}th iteration Has values of X={x_calc} , Y={y_calc} , Z={z_calc}")

        return Calc_Iteration(a11,a12,a13,a21,a22,a23,a31,a32,a33,b1,b2,b3,x_calc,y_calc,z_calc,n+1)
    else:
        print("4 iterations are done!!!! Thanks")
        return x , y , z
    
print("The Format Of 3 Equations is shown below please follow it while entering the values \n >>a11 x + a12 y + a13 z \n >>a21 x + a22 y + a23 z \n >>a31 x + a32 y + a33 z")
print("Please note the set of equations must be Diagnolly Dominant")

a11 = float(input("Enter value of a11: "))
a12 = float(input("Enter value of a12: "))
a13 = float(input("Enter value of a13: "))
a21 = float(input("Enter value of a21: "))
a22 = float(input("Enter value of a22: "))
a23 = float(input("Enter value of a23: "))
a31 = float(input("Enter value of a31: "))
a32 = float(input("Enter value of a32: "))
a33 = float(input("Enter value of a33: "))
b1 = float(input("Enter value of b1: "))
b2 = float(input("Enter value of b2: "))
b3 = float(input("Enter value of b3: "))

diag_dom(a11,a12,a13,a21,a22,a23,a31,a32,a33)

print("The answers are: ")

x_final, y_final, z_final = Calc_Iteration(a11, a12, a13, a21, a22, a23, a31, a32, a33, b1, b2, b3, x, y, z, 1)  
