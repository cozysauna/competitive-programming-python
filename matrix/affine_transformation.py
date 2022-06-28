class Affine:
    def __init__(self):
        self.mat = [[1 if i == j else 0 for i in range(3)] for j in range(3)]

    @staticmethod
    def get(A, x, y):
        M = mat_mul(
            A, 
            [
                [x],
                [y],
                [1]
            ]
        )

        return (M[0][0], M[1][0])

    # clock wise
    def rot90(self):
        self.mat = mat_mul(
            [
                [0, 1, 0],
                [-1, 0, 0],
                [0, 0, 1]
            ],
            self.mat
            )

    # counter clock wise
    def rot90_rev(self):
        self.mat = mat_mul(
            [
                [0, -1, 0],
                [1, 0, 0],
                [0, 0, 1]
            ],
            self.mat
            )

    # x += t
    def add_x(self, t):
        self.mat = mat_mul(
            [
                [1, 0, t],
                [0, 1, 0],
                [0, 0, 1]
            ],
            self.mat
            )
    
    # y += t
    def add_y(self, t):
        self.mat = mat_mul(
            [
                [1, 0, 0],
                [0, 1, t],
                [0, 0, 1]
            ],
            self.mat
            )

    # x -> -x
    def rev_x(self):
        self.mat = mat_mul(
            [
                [-1, 0, 0],
                [0, 1, 0],
                [0, 0, 1]
            ],
            self.mat
            )

    # y -> -y
    def rev_y(self):
        self.mat = mat_mul(
            [
                [1, 0, 0],
                [0, -1, 0],
                [0, 0, 1]
            ],
            self.mat
        )
