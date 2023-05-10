"""
    simpson(func::Function, a::Real, b::Real)

Numerically approximate the integral of func from `a` to `b` using Simpson's rule.

See also [`comsimp`], [`adapsimp`].

# Arguments

* `func::Function`: `func` is the integrand.
* `a::Real`: `a` is the lower limit of integration by default.
* `b::Real`: `b` is the supper limit of integration by defautlt.

If `a = b`, throw a Warning and return 0; if `a > b`, swap `a` and `b` to ensure `h = (b - a)/2 > 0`.

# Outputs

* `s::Float64`: s is the approximation of integral.

# Examples

```julia-repl
julia> simpson(cos, 0, 0)
Warning: The limits of integration are equal!
0

julia> simpson(sin, 0, pi/2)
1.0022798774922104

julia> simpson(x->exp(-x^2), 1, 0)
0.7471804289095104
```
"""
function simpson(func::Function, a::T, b::T) where T<:Real
    if a == b
        @warn "The limits of integration are equal!"
        return 0
    elseif a > b
        a, b = b, a
    end
    h = (b - a) / 2;
    s = h * (func(a) + 4 * func(a+h) + func(b)) / 3
    return s
end
