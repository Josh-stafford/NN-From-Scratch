mat1 = [[1, 2, 3],
            [3, 4, 5]]

mat2 = [[5, 6],
            [7, 8],
            [9, 10]]


def mult(mat1, mat2):
    nums = []
    finalMat = []

    height = len(mat1)
    width = len(mat2[0])

    # print('Height:', height, '\nWidth:', width)

    lastNums = []

    for row in range(height):

        for column in range(width):

            for num in range(len(mat1[row])):

                #print(mat1[row][num], mat2[num][column])

                number = mat1[row][num] * mat2[num][column]
                
                if num == width-1:
                    # print(num)
                    for i in lastNums:
                        number += i
                    nums.append(number)
                    lastNums = []c

                else:
                    lastNums.append(number)
                    # print(lastNums)

    # print(nums)

    currentRow = 0
    temp = []
    count = 0

    for i in range(len(nums)):

        # print(nums[i])

        count +=1

        temp.append(nums[i])

        if count == width:
            finalMat.append(temp)
            count = 0
            temp = []

    print(finalMat)

if __name__ == '__main__':
    mult(mat1, mat2)
