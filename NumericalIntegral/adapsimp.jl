"""

    adapsimp(func::Function, a::Real, b::Real, tol::Float64=eps())

Numerically approximate the integral of func from `a` to `b` using Simpson's adaptive rule.

See also [`simpson`], [`comsimp`].

# Arguments

* `func::Function`: `func` is the integrand.
* `a::Real`: `a` is the lower limit of integration by default.
* `b::Real`: `b` is the upper limit of integration by default.

If `a = b`, throw a Warning and return 0; if `a > b`, swap `a` and `b` to ensure `h = (b - a)/2 > 0`.

* `tol::Float64=eps()`: `tol` is the accuracy of integral approximation. The default value is `eps()=2.220446049250313e-16`.

# Outputs

* `s::Float64`: `s` is the approximation of integral.

# Examples

```julia-relp
julia> adapsimp(sin, 0, 0)
Warning: The limits of integration are equal!
0

julia> adapsimp(x->exp(-x^2), 1, 0)
0.746824132812427

julia> adapsimp(x->exp(-x^2), 0, 1, 1e-6)
0.7468242574357303
```
"""
function adapsimp(func::Function, a::Real, b::Real, tol::Float64=eps())
    if a == b
        @warn "The limits of integration are equal!"
        return 0
    elseif a > b
        a, b = b, a
    end

    c = (a + b) / 2;
    s0 = (b - a) * (func(a) + 4 * func(c) + func(b)) / 6;
    s1 = (c - a) * (func(a) + 4 * func((a+c)/2) + func(c)) / 6;
    s2 = (b - c) * (func(c) + 4 * func((c+b)/2) + func(b)) / 6;
    if abs(s1+s2-s0) < 15 * tol
        s = s1 + s2
    else
        s1 = adapsimp(func, a, c, tol/2)
        s2 = adapsimp(func, c, b, tol/2)
        s = s1 + s2
    end
    return s
end
