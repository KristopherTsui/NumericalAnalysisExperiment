function [I] = gausslegendre(func, a, b, n)
%GAUSSLEGENDRE - Gauss-Legendre 求积公式.
%
% 输入:
%   func - 被积函数. func 是一个函数句柄或者匿名函数.
%   a - double. a 默认为积分下限.
%   b - double. b 默认为积分上限.
%       如果 a = b, 抛出积分上下限相等的警告并赋 s = 0.
%       如果 a > b, 交换 a 和 b 的值保证 h = (b - a) / 2 > 0.
%   n - integer. Gauss-Legendre 求积公式所使用节点个数或 n 次 Legendre 多项式, 默认值为 5.
%
% 输出:
%   I - double. I 是积分的近似值.
%
% 示例:
% > gausslegendre(@(x) 50*exp(-x.^2), 0, 1, 16)
% ans =
%   29.9072
% > gausslegendre(@(x) x.*exp(-x.^2), -1, 1)
% ans =
%   3.9135e-15
%
    if nargin < 4
        n = 5;
    end
    if n <= 0
        error("错误! n 必须为正整数!");
    end

    if a == b
        disp("警告! 积分上下限相等!");
        s = 0;
        return;
    elseif a > b
        c = a;
        a = b;
        b = c;
    end

    % 获取 n 次 Legendre 多项式的系数
    p = legendpoly(n);
    % 获取 n 次 Legendre 多项式的根
    r = roots(p);
    % 计算 Gauss-Legendre 求积公式的系数
    A = 2 ./ polyval(legendpoly(n-1), r) ./ polyval(polyder(p), r) / n;
    % 将积分区间 [a, b] 转化为 [-1, 1]
    x = ((b - a) * r + (b + a)) / 2;
    % Gauss-Legendre 求积公式
    I = dot(A, func(x)) * (b - a) / 2;
end

function [p] = legendpoly(n)
%LEGENDPOLY - n 次 Legendre 多项式.
% Legendre 多项式是区间 [-1, 1] 上带权函数 rho(x) = 1 的正交多项式.
% 利用递推公式求 n 次 Legendre 多项式的系数.
% Legendre 多项式可用于函数逼近, Gauss-Legendre 积分公式也有应用.
%
% 输入:
%   n - integer. n 为 Legendre 多项式的次数, 非负值.
%
% 输出:
%   p - vector. n 次 Legendre 多项式的系数向量.
%
% 示例:
% > p = legendpoly(3)   % 3 次 Legendre 多项式
% p =
%   2.5000  0.0000  -1.5000  0.0000
% > r = roots(p)        % 3 次 Legendre 多项式的零点
% r =
%   0.0000
%  -0.7746
%   0.7746
%
    if n < 0
        error("错误! n 必须为非负整数!");
    elseif n == 0
        p = [1];        % L0(x) = 1;
    elseif n == 1
        p = [1, 0];     % L1(x) = x;
    else
        p1 = legendpoly(n - 1);
        p2 = legendpoly(n - 2);
        % Ln(x) = (2-1/n)L_{n-1}(x) - (1-1/n)L_{n-2}(x)
        p1 = cat(2, p1, 0);
        p2 = cat(2, [0, 0], p2);
        p = (2 - 1 / n) * p1 - (1 - 1 / n) * p2;
    end
end
