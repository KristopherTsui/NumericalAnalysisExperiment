function [t, y] = rkf45(odefun, tspan, y0, hmin, hmax, tol)
%RKF45 - Runge-Kutta-Fehlberg 法数值求解常微分方程初值问题.
% Runge-Kutta-Fehlberg 法是一种变步长求解常微分方程初值问题的方法.
% 四阶的 Runge-Kutta-Fehlberg 法采用四阶和五阶的 Runge-Kutta 法.
% 也可以采用更高阶的 Runge-Kutta 法实现高阶的 Runge-Kutta-Fehlberg 法.
%
% 语法 - [t, y] = rkf45(odefun, tspan, y0, hspan, tol)
%
% 输入:
%   odefun - 函数句柄或者匿名函数. odefun 是常微分方程 dy/dt=odefun(t, y) 右端的函数.
%   tspan - 常微分方程的求解区间.
%   y0 - 常微分方程的初值条件 y(t0)=y0.
%   hmin - Runge-Kutta-Fehlberg 法步长允许的最小值, 默认值为 0.00001.
%   hmax - Runge-Kutta-Fehlberg 法步长允许的最大值, 默认值为 0.1.
%   tol - Runge-Kutta-Fehlberg 法迭代的精度, 默认值为 1e-9.
%
% 输出:
%   t - Runge-Kutta-Fehlberg 法求解常微分方程初值问题得到的节点.
%   y - Runge-Kutta-Fehlberg 法求解常微分方程初值问题得到在每个节点处的函数值.
%
% 示例:
% > [t, y] = rkf45(@(t, y) y-t^2+1, [0 1], 0.5, 0.001, 0.25, 1e-5)
% t =
%   0.000000000000000
%   0.250000000000000
%   0.486552202284769
%   0.729333276679330
%   0.979333276679330
%   1.000000000000000
% y =
%   0.500000000000000
%   0.920487049298409
%   1.396487985680925
%   1.953744075203584
%   2.586418983757945
%   2.640858016938946
%
% 另见: rungekutta4, ode45.
%
%
    if nargin < 3
        error("错误! 输入参数不足! 可以使用 help rkf45 命令查看相关文档!")
    end
    if nargin < 4
        hmin = 0.00001;
    end
    if nargin < 5
        hmax = 0.1;
    end
    if nargin < 6
        tol = 1e-9;
    end

    t0 = tspan(1);
    t(1) = t0;
    y(1) = y0;
    h = hmax;
    k = 2;
    while t0 < tspan(2)
        k1 = h * feval(odefun, t0, y0);
        k2 = h * feval(odefun, t0+h/4, y0+k1/4);
        k3 = h * feval(odefun, t0+3*h/8, y0+3*k1/32+9*k2/32);
        k4 = h * feval(odefun, t0+12*h/13, y0+1932*k1/2197-7200*k2/2197+7296*k3/2197);
        k5 = h * feval(odefun, t0+h, y0+439*k1/216-8*k2+3680*k3/513-845*k4/4104);
        k6 = h * feval(odefun, t0+h/2, y0-8*k1/27+2*k2-3544*k3/2565+1859*k4/4104-11*k5/40);
        R = abs(k1/360 - 128*k3/4275 - 2197*k4/75240 + k5/50 + 2*k6/55);
        q = 0.84 * (tol * h / R)^(1/4);
        if R < h * tol
            y0 = y0 + 16*k1/135 + 6656*k3/12825 + 28561*k4/56430 - 9*k5/50 + 2*k6/55;
            t0 = t0 + h;
            t(k) = t0; y(k) = y0; k = k + 1;
        end
        if q <= 0.1
            h = 0.1 * h;
        elseif q >= 4
            h = 4 * h;
        else
            h = q * h;
        end
        if h > hmax
            h = hmax;
        end
        if t0 + h >= tspan(2)
            h = tspan(2) - t0;
        elseif h < hmin
            error("错误! 当前最小步长无法满足要求!")
        end
    end
    t = t'; y = y';
end

