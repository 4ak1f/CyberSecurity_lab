S = {0, 1, 2}
add_op = lambda x, y: (x + y) % 3
mul_op = lambda x, y: (x * y) % 3

# Group check
is_group = all(add_op(x, add_op(y, z)) == add_op(add_op(x, y), z) for x in S for y in S for z in S)

# Ring check
is_ring = is_group and all(mul_op(x, mul_op(y, z)) == mul_op(mul_op(x, y), z) for x in S for y in S for z in S)

# Field check
is_field = is_ring and all(any(mul_op(x, y) == 1 for y in S if y != 0) for x in S if x != 0)

print(f"Group: {is_group}, Ring: {is_ring}, Field: {is_field}")