clc
close all
clear all
x1 = 10.724295;
y1 = 99.376935;
x2 = 10.724324;
y2 = 99.376843;
m = (y1-y2)/(x1-x2);
c = -m*x1+y1; % y = (m*x2)+c;

u = 10.7243;
v = 99.3769;

d = abs(u-(m*v)-c)/sqrt(1+m^2)

w = (m*u)+c;
if x2>u & y2>w
    e = sqrt((x2^2-u^2)+(y2^2-w^2))
elseif x2>u & y2<w
    e = sqrt((x2^2-u^2)+(w^2-y2^2))
elseif x2<u & y2>w
    e = sqrt((u^2-x2^2)+(y2^2-w^2))
else   % x2<u & w>y2
    e = sqrt((u^2-x2^2)+(w^2-y2^2))
end
zeta = atan(d/e)*180/3.14;  % degree
