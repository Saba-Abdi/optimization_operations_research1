Set
   i candidates / v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12 /
   j our company's work plans / p1, p2, p3, p4, p5, p6, p7, p8, p9, p10 /
;

Parameters
   C(i) fixed cost per candidate i
        / v1 14
          v2 10
          v3 20
          v4 12
          v5 10
          v6 14
          v7 16
          v8 18
          v9 18
          v10 18
          v11 14
          v12 18 /

   n(i) expected income per candidate i
        / v1 40
          v2 56
          v3 50
          v4 48
          v5 48
          v6 42
          v7 48
          v8 50
          v9 40
          v10 50
          v11 60
          v12 58 /

   Mp(j) fixed cost per paln j
         / p1 2
           p2 2.5
           p3 2
           p4 3
           p5 2
           p6 1.5
           p7 1
           p8 3
           p9 1
           p10 1.5 /

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

    MinSalary the average of rival's company's salary as our company's minimum salary
              / 23.6 /
;

Table edu(i , j) training cost of candidate i in plan j in our company
               p1   p2  p3  p4  p5   p6    p7   p8   p9     p10
      v1       5    4   5   1    2    1    4    1.1   3     1.2
      v2       2    3   1   4    1    5    3.8  3     4     4
      v3       2.1  4   3   3    1.6  2    3    3     1     3
      v4       1.5  3   3   3    4    3    3    3     2.9   2
      v5       4    3   3   2    4    3    3    2     3.9   2.8
      v6       6    2   3   2    4.1  5    4    20      3    3
      v7       1.5  3   4   3    2.9  4    1.2  4.2    0.5    3
      v8       1.5  3   4   2    3.3  2.7  2    20     2.2    2.3
      v9       2    3   1   2.1  3.7  3    3    2     2.8   2.7
      v10      3    2   2   3    2.7  3    2    3      3     2
      v11      4    3   3   1.2  2.8  2    4    3      1     4
      v12      2    4   2   3    1    1    2     3     3     1
;


Positive variable
   Sp(i , j) salary provided by our company
;

Binary variables
   Op(j) plan j provided by our company
   gamma(i , j) employing candidate i for plan j in our company
;

Variable
   z      total profit gained by our company
;

Equation
   profit           define objective function
   constraint1(i)   the quantity of plans recommended to each candidate i is at most 1
   constraint2      the quantity of candidates required by our company in each plan j in at least 5
   constraint3(j)   relation between plans and candidates
   constraint4(i,j) Sp should be greater than a minimum value
;

profit           .. z =e=  sum((i,j),gamma(i,j)*n(i))-sum((i,j),Sp(i,j)+gamma(i,j)*(C(i)+Vp(j)))-sum(j,Op(j)*Mp(j))-sum((i,j),gamma(i,j)*edu(i,j));

constraint1(i)   .. sum(j, gamma(i,j)) =l= 1;
constraint2      .. sum((i,j), gamma(i,j)) =g= 5;
constraint3(j)   .. sum(i,gamma(i,j)) =l= 12*Op(j);
constraint4(i,j) .. Sp(i,j) =g= MinSalary*gamma(i,j);

model bi_level /all/;

solve bi_level using MIP maximizing z;

display Sp.l , z.l , gamma.l;
