Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: D:\mphill Study material\3rd semester\stat 701\assignment1Stat\Assigmnt2StatExample2.py 
X1= [0, 0, 10, 10, 20, 20]
Total Sum of X1 values is: 60
X2= [0, 0, 100, 100, 400, 400]
Total Sum of X2 values is: 1000
Y= [5, 7, 15, 17, 9, 11]
Total Sum of Y values is: 64
value of X1_bar is: 10
value of X1_bar^2 is: 100
value of X2_bar is: 166.66666666666666
value of X2_bar^2 is: 27777.777777777774
value of Y_bar is: 10.666666666666666
Value of x1=X1-X_bar is:
[-10]
[-10, -10]
[-10, -10, 0]
[-10, -10, 0, 0]
[-10, -10, 0, 0, 10]
[-10, -10, 0, 0, 10, 10]
Value of x2=X2-X2_bar is:
[-166.66666666666666]
[-166.66666666666666, -166.66666666666666]
[-166.66666666666666, -166.66666666666666, -66.66666666666666]
[-166.66666666666666, -166.66666666666666, -66.66666666666666, -66.66666666666666]
[-166.66666666666666, -166.66666666666666, -66.66666666666666, -66.66666666666666, 233.33333333333334]
[-166.66666666666666, -166.66666666666666, -66.66666666666666, -66.66666666666666, 233.33333333333334, 233.33333333333334]
Value of y=Y-Y_bar is:
[-5.666666666666666]
[-5.666666666666666, -3.666666666666666]
[-5.666666666666666, -3.666666666666666, 4.333333333333334]
[-5.666666666666666, -3.666666666666666, 4.333333333333334, 6.333333333333334]
[-5.666666666666666, -3.666666666666666, 4.333333333333334, 6.333333333333334, -1.666666666666666]
[-5.666666666666666, -3.666666666666666, 4.333333333333334, 6.333333333333334, -1.666666666666666, 0.3333333333333339]
B1^=(sigmax1.y.sigmax2^2)-(sigmax2.y.sigmax1.x2)/(sigmax1^2.sigmax2^2)-(sigma(x1x2))^2
firstly calculate sigmax1.y.sigmax2^2
value of x1.y is: [56.66666666666666, 36.66666666666666, 0.0, 0.0, -16.66666666666666, 3.3333333333333393]
sigma(x1.y) is: 80.0
value of (x2)^2 is: [27777.777777777774, 27777.777777777774, 4444.444444444443, 4444.444444444443, 54444.444444444445, 54444.444444444445]
sigma(x2)^2 is: 173333.3333333333
value of (sigmax1.y.sigmax2^2) is: 13866666.666666664
 2ndly calculate sigmax2.y.sigmax1.x2
value of x2.y is: [944.4444444444443, 611.111111111111, -288.8888888888889, -422.22222222222223, -388.88888888888874, 77.77777777777791]
sigma(x2.y) is: 533.3333333333333
value of (x1)(x2) is: [1666.6666666666665, 1666.6666666666665, -0.0, -0.0, 2333.3333333333335, 2333.3333333333335]
sigma(x1)(x2) is: 8000.0
value of (sigmax2.y.sigmax1.x2) is: 4266666.666666666
value of (sigmax1.y.sigmax2^2)-(sigmax2.y.sigmax1.x2) is: 9599999.999999998
value of (x1)^2 is: [100, 100, 0, 0, 100, 100]
sigma(x1)^2 is: 400
sigma(x2)^2 is(solved above is): 173333.3333333333
value of (sigmax1^2.sigmax2^2) is: 69333333.33333333
value of (sigma(x1x2)^2 is: 64000000.0
value of (sigmax1^2.sigmax2^2)-(sigma(x1x2))^2 is: 5333333.333333328
value of B1^ is: 1.8000000000000014
B2^=(sigmax2.y.sigmax1^2)-(sigmax1.y.sigmax1.x2)/(sigmax1^2.sigmax2^2)-(sigma(x1x2))^2
firstly calculate (sigmax2.y.sigmax1^2)
value 0f (sigmax2.y.sigmax1^2) is: 213333.3333333333
3rdly calculate (sigmax1.y.sigmax1.x2)
value 0f (sigmax1.y.sigmax1.x2) is: 640000.0
value of (sigmax1.y.sigmax2^2)-(sigmax2.y.sigmax1.x2) is: -426666.6666666667
value of B2^ is: -0.08000000000000008
B0^=(Y_bar)-(B1^.X1_bar)-(B2^.X2_bar)
value of B0^ is: 5.999999999999998
Y^=B1^*X1+B2^*X2
1stly calculate B1^*X1
value of B1^*X is: [0.0, 0.0, 18.000000000000014, 18.000000000000014, 36.00000000000003, 36.00000000000003]
2ndly calculate B2^*X2
value of B2^*X2 is: [-0.0, -0.0, -8.000000000000009, -8.000000000000009, -32.000000000000036, -32.000000000000036]
value of (B1^*X1)+(B2^*X2) is: [0.0, 0.0, 10.000000000000005, 10.000000000000005, 3.999999999999993, 3.999999999999993]
value of Y^ is: [5.999999999999998, 5.999999999999998, 16.000000000000004, 16.000000000000004, 9.999999999999991, 9.999999999999991]
TSS=sigma(Y-Y_bar)^2
calculate value of (Y-Y_bar)^2
value of (Y-Y_bar)^2 is:
[32.11111111111111, 13.44444444444444, 18.777777777777782, 40.11111111111112, 2.777777777777776, 0.11111111111111151]
value of TSS is : 107.33333333333334
MSS=sigma(Y^-Y_bar)^2
1stly calculate value of (Y^-Y_bar)
Value of Y(i)^-Y_bar is:
[-4.666666666666668]
[-4.666666666666668, -4.666666666666668]
[-4.666666666666668, -4.666666666666668, 5.3333333333333375]
[-4.666666666666668, -4.666666666666668, 5.3333333333333375, 5.3333333333333375]
[-4.666666666666668, -4.666666666666668, 5.3333333333333375, 5.3333333333333375, -0.666666666666675]
[-4.666666666666668, -4.666666666666668, 5.3333333333333375, 5.3333333333333375, -0.666666666666675, -0.666666666666675]
value of (Y_hat-Y_bar)^2 is: [21.77777777777779, 21.77777777777779, 28.44444444444449, 28.44444444444449, 0.4444444444444555, 0.4444444444444555]
MSS=Sigma(Y^-Y_bar)^2 is: 101.33333333333347
RSS=sigma(Y-Y^)^2
1stly calculate value of (Y-Y^)
value of (Y-Y^) is: [-0.9999999999999982, 1.0000000000000018, -1.0000000000000036, 0.9999999999999964, -0.9999999999999911, 1.0000000000000089]
value of (Y-Y^)^2 is: [0.9999999999999964, 1.0000000000000036, 1.000000000000007, 0.9999999999999929, 0.9999999999999822, 1.0000000000000178]
RSS=Sigma(Y-Y^)^2 is: 6.0
<^2=RSS/n-k
k=no. of parameters=3 i.e(B1,B2,B0) and n=7
n-k= 4
value of <^2 is: 1.5
V(B1^)=<^2. sigmax2^2)/ (sigmax1^2.sigmax2^2)-(sigma(x1x2))^2
vaue of V(B1^) is: 0.04875000000000004
V(B2^)=<^2. sigmax1^2)/ (sigmax1^2.sigmax2^2)-(sigma(x1x2))^2
vaue of V(B2^) is: 0.0001125000000000001
V(B0^)=<^2. 1/n+[X1_bar^2.sigmax2^2+X2_bar^2.sigmax1^2+2X1_bar.X2_bar.sigmax1x2]/ (sigmax1^2.sigmax2^2)-(sigma(x1x2))^2
for [X1_bar^2.sigmax2^2+X2_bar^2.sigmax1^2+2X1_bar.X2_bar.sigmax1x2]
1stly calculate X1_bar^2.sigmax2^2
value of X1_bar^2.sigmax2^2 is: 17333333.333333332
2ndly calculate X2_bar^2.sigmax1^2
value of X2_bar^2.sigmax1^2 is: 11111111.11111111
3rdly calculate 2X1_bar.X2_bar.sigmax1x2
value of 2X1_bar.X2_bar.sigmax1x2 is: 26666666.666666664
so value of [X1_bar^2.sigmax2^2+X2_bar^2.sigmax1^2+2X1_bar.X2_bar.sigmax1x2] is: 55111111.111111104
value of VB0_hat : 15.714285714285726
This is the 2nd Assignment(example.2)of Stat701 in python.Thanku for watching :)
>>> 
