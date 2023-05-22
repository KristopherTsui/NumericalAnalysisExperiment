function [x, y] = rungekutta4(dyfun, xspan, y0, h)
%RUNGEKUTTA4 - 四阶 Runge-Kutta 方法求解常微分方程(组).
%
% 语法:
%   [x, y] = rungekutta4(dyfun, xspan, y0, h)
%
% 输入参数:
%   dyfun - 
%   xspan - 
%   y0 - 
%   h - 
% 输出参数:
%   x -
%   y -
%
% 示例:
%
% 相关:
%
%
    x = xspan(1):h:xspan(2);
    y = zeros(length(y0), length(x));
    y(:, 1) = y0(:);
    for n = 1:(length(x)-1)
        k1 = feval(dyfun, x(n), y(:,n));
        k2 = feval(dyfun, x(n)+h/2, y(:,n)+h/2*k1);
        k3 = feval(dyfun, x(n)+h/2, y(:,n)+h/2*k2);
        k4 = feval(dyfun, x(n+1), y(:,n)+h*k3);
        y(:,n+1) = y(:,n) + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6;
    end
    x = x';
    y = y';
end
