Set
   i candidates / v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12 /
   j our company's work plans / p1, p2, p3, p4, p5, p6, p7, p8, p9, p10 /
   k rival company's work plans / r1, r2, r3, r4, r5, r6, r7, r8, r9, r10 /
;

Parameter
   Qp(j) our company's quality per plan j
         / p1 0.8
           p2 0.9
           p3 0.8
           p4 1
           p5 0.8
           p6 0.7
           p7 0.6
           p8 1
           p9 0.6
           p10 0.7 /

   Rq(k) rival company's quality per plan k
         / r1 0.8
           r2 0.5
           r3 0.8
           r4 0.8
           r5 1
           r6 0.6
           r7 1
           r8 0.6
           r9 0.9
           r10 0.7 /


   Pq(k) rival company's salary per plan k
         / r1 24
           r2 20
           r3 24
           r4 24
           r5 28
           r6 20
           r7 28
           r8 20
           r9 26
           r10 22 /

   Vp(j) variable cost per paln j
         / p1 5.5
           p2 5.5
           p3 3.5
           p4 2.5
           p5 2
           p6 1
           p7 5.5
           p8 0
           p9 1
           p10 2 /

   d(i) candidates' total desired employment ratio
        / v1 0.8
          v2 0.8
          v3 0.8
          v4 1
          v5 0.9
          v6 0.7
          v7 1
          v8 0.6
          v9 0.9
          v10 0.9
          v11 0.6
          v12 0.9 /

   Sp(j) salary provided by our company per plan j
         / p1 0
           p2 0
           p3 0
           p4 0
           p5 0
           p6 0
           p7 0
           p8 23.6
           p9 23.6
           p10 0 /
;

Table X(i , j) required salary by candidate i in plan j in our company
               p1  p2  p3  p4  p5  p6  p7  p8  p9  p10
      v1       34  45  25  39  40  35  45  39  26  34
      v2       25  43  31  45  29  33  38  30  43  40
      v3       39  44  35  39  38  27  36  34  25  35
      v4       38  37  30  34  39  33  35  30  29  42
      v5       37  30  38  29  40  33  32  26  39  38
      v6       30  42  39  32  41  35  42  31  35  36
      v7       25  34  34  38  29  44  26  42  42  43
      v8       39  36  44  26  33  27  27  39  25  40
      v9       29  39  38  27  37  34  43  32  28  27
      v10      36  32  37  37  27  30  25  35  43  32
      v11      40  34  34  25  28  29  40  36  43  40
      v12      28  40  29  39  45  31  34  35  33  35
;

Table Y(i , k) required salary by candidate i in plan k in rival's company
               r1  r2  r3  r4  r5  r6  r7  r8  r9  r10
      v1       33  33  38  42  45  31  36  39  39  28
      v2       43  28  32  34  33  37  27  45  39  26
      v3       40  32  39  26  33  32  26  38  40  26
      v4       35  26  40  33  31  44  42  36  28  25
      v5       26  34  31  40  39  29  44  34  41  38
      v6       38  36  36  30  27  44  45  36  41  39
      v7       44  34  25  34  42  41  34  29  25  37
      v8       37  34  39  31  43  37  31  29  43  32
      v9       45  40  30  43  33  41  43  25  34  40
      v10      30  43  29  41  27  38  44  35  44  30
      v11      45  31  42  36  34  30  45  35  41  39
      v12      42  34  29  26  33  31  44  32  30  36
;

Table gamma(i , j) employing candidate i for plan j in our company
                   p1  p2  p3  p4  p5  p6  p7  p8  p9  p10
      v1           0   0   0   0   0   0   0   1   0    0
      v2           0   0   0   0   0   0   0   1   0    0
      v3           0   0   0   0   0   0   0   0   1    0
      v4           0   0   0   0   0   0   0   1   0    0
      v5           0   0   0   0   0   0   0   1   0    0
      v6           0   0   0   0   0   0   0   0   1    0
      v7           0   0   0   0   0   0   0   0   1    0
      v8           0   0   0   0   0   0   0   0   1    0
      v9           0   0   0   0   0   0   0   0   0    0
      v10          0   0   0   0   0   0   0   1   0    0
      v11          0   0   0   0   0   0   0   0   1    0
      v12          0   0   0   0   0   0   0   1   0    0
;

Variable
   z     gap between salary recieved and advantages provided
;

Positive variable
   alpha(i , j) candidates' desired employment ratio in our company
   beta(i , k) candidates' desired employment ratio in rival's company
;

Equation
   gap         define objective function
   constraint1(i) employment ratio
;

gap             .. z =e= sum((i,j), alpha(i,j)*(X(i,j)-(Qp(j)*(Vp(j)*gamma(i,j)+Sp(j)))))+sum((i,k), beta(i,k)*(Y(i,k)-(Rq(k)*Pq(k))));


constraint1(i)  .. sum(j,alpha(i,j))+sum(k,beta(i,k)) =e= d(i);

model bi_level /all/;

solve bi_level using LP minimizing z;

display z.l , alpha.l , beta.l;
