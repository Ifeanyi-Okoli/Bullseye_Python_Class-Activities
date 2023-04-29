def quadrant_segment(A, B):
    if A[0] < 0 and A[1] < 0:
        quadA = 3
    elif A[0] > 0 and A[1] > 0:
        quadA = 2
    elif A[0] < 0 and A[1] > 0:
        quadA = 1
    else:
        quadA = 4
    
    if B[0] < 0 and B[1] < 0:
        quadB = 3
    elif B[0] > 0 and B[1] > 0:
        quadB = 2
    elif B[0] < 0 and B[1] > 0:
        quadB = 1
    else:
        quadB = 4
    return False if quadA == quadB else True

print(quadrant_segment(( 1, 2), ( 3, 4)))
print(quadrant_segment(( 9, 3), (-1, 6)))
print(quadrant_segment((-1, 6), (-9, 1)))