function [t, y] = impeuler(func, tspan, y0, h)
    t = tspan(1):h:tspan(2);
    y = zeros(size(t));
    y(1) = y0;
    for k = 1:length(t)-1
        k1 = feval(func, t(k), y(k));
        k2 = feval(func, t(k+1), y(k)+h*k1);
        y(k+1) = y(k) + h * (k1 + k2) / 2;
    end
    t = t';
    y = y';
end
