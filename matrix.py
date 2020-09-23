class Matrix:
    """
    A class used to represent a Matrix

    ...

    Attributes
    ----------
    matrix_string : str
        string with embedded newlines like:
        "9 8 7\n5 3 2\n6 6 7"

    Methods
    -------
    row(index)
        returns the number "index" row as a list of integers
    column(index)
        return the number "index" column as a list of integers
    """

    def __init__(self, matrix_string):
        """
        Parameters
        ----------
        matrix_string : str
            The string rappresentig a matrix
        """

        # splitting the string in double-levelled lists of string
        self.matrix_string = [row.split() for row in matrix_string.strip().split("\n")]

    def row(self, index):
        """
        Parameters
        ----------
        index : int
            The row number to be returned (1 --> first row)
        """

        # converting each element of "index"th row to "int" and returning it as list
        return [int(j) for j in self.matrix_string[index - 1]]

    def column(self, index):
        """
        Parameters
        ----------
        index : int
            The column number to be returned (1 --> first column)
        """

        # converting each "index"th element of each row in int and returning as list
        return [int(k[index - 1]) for k in self.matrix_string]
