defmodule NumericalIntegration do
  @doc """
  Calculates the area under the curve of function `f` from `a` to `b` 
  using the Trapezoidal Rule with `n` subintervals.
  """
  def trapezoidal_rule(f, a, b, n) do
    dx = (b - a) / n
    
    # Sum the values of the function at the boundaries of each trapezoid
    sum = Enum.reduce(1..(n - 1), 0.5 * (f.(a) + f.(b)), fn i, acc ->
      x = a + i * dx
      acc + f.(x)
    end)

    sum * dx
  end
end

# 1. Define the curve/function: f(x) = x^2
curve = fn x -> :math.pow(x, 2) end

# 2. Define integration boundaries and intervals
start_x = 0.0
end_x = 4.0
intervals = 1000 # Higher number = more accuracy

# 3. Calculate the area
area = NumericalIntegration.trapezoidal_rule(curve, start_x, end_x, intervals)

# 4. Output the result
IO.puts("The approximate area under the curve is: #{area}")
# Calculus exact answer for x^2 from 0 to 4 is 64/3 ≈ 21.3333
