A = Matrix(GF(257),[[102, 108, 97, 103, 123], [97, 114, 101, 95, 121], [111, 117, 95, 115, 117], [114, 101, 95, 102, 114], [105, 101, 110, 100, 125]])

encode =  Matrix(GF(257),[[ 56 109  75  75 185], [138 249 138 187  92],[138 154 186 107 210],[198 187   5 144  86],[147 230  18 189  79]])

flag = encode*A.inverse()