function [t, y] = euler(func, tspan, y0, h)
    t = tspan(1):h:tspan(2);
    y = zeros(size(t));
    y(1) = y0;
    for k = 1:length(t)-1
        y(k+1) = y(k) + h * feval(func, t(k), y(k));
    end
    t = t'; y = y';
end
