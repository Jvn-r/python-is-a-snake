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

#print("this is bullshit im typing to fake me doing something so yeah hows it goin todays smoge did hit like 1 a day is like the best for both health and pleasure same formula goes for masturbation too like 1 a day will feel nice and your dick wont hurt or sumn like dat like just make sure youre edging and allat and youll be fine youll have a good time since we're on good times lets talka bout the fact" \
#"that we are never gonna be sleeping like thats all we are never gonna sleep sleep is a bitch and you should assert your high ground over sleep man idefk like what is this bull shiet tspmo all the time like its actually crazy how far under my skin he can get in such a small amount of time like just drills down and starts being a fuckin psycho bitch " \
#"idk man like what is even going on i wanna like just go on and skip the next two years get away for masters somewhere and like chill out again like the 3 months in the room were the best months ive had in a long time like man fuck my stupid baka life")