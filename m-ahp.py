class MAHP():
    def __init__(self):
        self.n = None
        self.max_parameter_scores = []
        self.instantaneous_parameter_scores = []
        
    
    def getValues(self):
    
        self.n = int(input("Enter number of parameters:"))
        print("Enter maximum paramater scores:")
        for i in range(self.n):
            value = int(input(str(i+1)+". parameter:"))
            self.max_parameter_scores.append(value)
        print("Enter instantaneous paramater scores:")
        for i in range(self.n):
            value = int(input(str(i+1)+". parameter:"))
            while(value > max(self.max_parameter_scores)):
                print("Value should be less than or equal maximum value of maximum paramater scores")
                value = int(input(str(i+1)+". parameter:"))
            self.instantaneous_parameter_scores.append(value)
    
    
    def create_diff_matrix(self):
        diff_matrix = []
        for i in range(self.n):
            row = []
            for j in range(self.n):
                value = self.instantaneous_parameter_scores[i] - self.instantaneous_parameter_scores[j]
                row.append(value)
            diff_matrix.append(row)
        return diff_matrix
        
    def create_normalised_diff_matrix(self,matrix):
        normalised_diff_matrix = []
        max_value = max(self.max_parameter_scores)
        for i in range(self.n):
            row = []
            for j in range(self.n):
                value = matrix[i][j] / max_value
                row.append(value)
            normalised_diff_matrix.append(row)
        return normalised_diff_matrix
    
    def create_comparison_matrix(self,matrix):
        comparison_matrix = []
        score_diff_interval = [0, 0.125, 0.250, 0.375, 0.500, 0.625, 0.750, 0.875, 1]
        importance_value_positive = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        importance_value_negative = [1, 0.5, 0.33, 0.25, 0.2, 0.167, 0.143, 0.125, 0.111]
        for i in range(self.n):
            row = []
            for j in range(self.n):
                if(matrix[i][j] > 0):
                    for k in range(1,len(score_diff_interval)):
                        if(score_diff_interval[k-1] < matrix[i][j] <= score_diff_interval[k]):
                            row.append(importance_value_positive[k])
                elif(matrix[i][j] < 0):
                    for k in range(1,len(score_diff_interval)):
                        if(score_diff_interval[k-1] < abs(matrix[i][j]) <= score_diff_interval[k]):
                            row.append(importance_value_negative[k])
                else:
                    row.append(1)
            comparison_matrix.append(row)
        return comparison_matrix
        
    def calculate_weight_vector(self,matrix):
        matrix_B_columns = []
        matrix_C = []
        vector_W = []

        for j in range(self.n):
            col_B = []
            div = 0
            for i in range(self.n):
                div = div + matrix[i][j]
            for i in range(self.n):
                item = matrix[i][j] / div
                item = item - (item % 0.01)
                col_B.append(item)
            matrix_B_columns.append(col_B)

        for i in range(self.n):
            row = []
            for j in range(self.n):
                row.append(matrix_B_columns[j][i])
            matrix_C.append(row)

        for i in range(self.n):
            w = 0
            up = 0
            for j in range(self.n):
                up = up + matrix_C[i][j]
            w = up / self.n
            vector_W.append(round(w,2))
        return vector_W

mahp_object = MAHP()
mahp_object.getValues()
diff_matrix = mahp_object.create_diff_matrix()
normalised_diff_matrix = mahp_object.create_normalised_diff_matrix(diff_matrix)
comparison_matrix = mahp_object.create_comparison_matrix(normalised_diff_matrix)
weight_vector = mahp_object.calculate_weight_vector(comparison_matrix)
print("Weight Vector --> ",weight_vector)
input()
        
    
