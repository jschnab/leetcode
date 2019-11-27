# leetcode 836
# determine if two rectangles overlap
# input is two lists [x1,y1,x2,y2] coordinates
# where x1,y1 are coordinates of bottom left corner
# and x2,y2 are coordinates of top right corner

def overlap_rect(rec1, rec2):
    """Determine if rectangles overlap."""
    # true if rec2 is left of rec1
    a = rec2[2] <= rec1[0]
    
    # true if rec2 is right of rec1
    b = rec1[2] <= rec2[0]

    # true if rec2 is below rec1
    c = rec2[3] <= rec1[1]

    # true if rec2 is above rec1
    d = rec1[3] <= rec2[1]

    return not (a or b or c or d)
