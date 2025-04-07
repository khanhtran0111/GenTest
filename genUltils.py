import random
import string
import datetime

#### Example Random
# random.random()  # Số thực ngẫu nhiên trong khoảng [0.0, 1.0)
# random.uniform(10, 20)  # Số thực trong khoảng [10, 20]
# random.randint(1, 100)  # Số nguyên trong khoảng [1, 100]
# random.randrange(1, 100, 2)  # Số nguyên lẻ từ 1 đến 99
# random.shuffle(numbers) # Xáo trộn danh sách

############## RANDOM 1 GIÁ TRỊ ##############

def randomInList(items, numberOfItems=1, duplicate=0):  
    """
    Hàm chọn ngẫu nhiên một hoặc nhiều phần tử từ danh sách cho trước.

    Tham số:
    - items: Danh sách các phần tử có thể chọn.
    - numberOfItems: Số lượng phần tử cần lấy (mặc định là 1).
    - duplicate: 
        + Nếu duplicate = 0 (mặc định): Không cho phép trùng lặp (sử dụng random.sample).
        + Nếu duplicate ≠ 0: Cho phép trùng lặp (sử dụng random.choices).

    Ví dụ:
    items = ["A", "B", "C", "D"]
    randomInList(items, 2, 0)  # Lấy 2 phần tử không trùng
    randomInList(items, 3, 1)  # Lấy 3 phần tử có thể trùng lặp
    """
    
    if duplicate == 0:  
        # Sử dụng random.sample để lấy các phần tử không trùng lặp
        return random.sample(items, numberOfItems)
    else:  
        # Sử dụng random.choices để lấy các phần tử có thể trùng lặp
        return random.choices(items, k=numberOfItems)
    
def randomDate(minYear, maxYear):
    """
    Sinh một ngày ngẫu nhiên trong khoảng minYear đến maxYear.
    """
    year = random.randint(minYear, maxYear)
    month = random.randint(1, 12)
    
    # Chọn ngày hợp lệ theo tháng/năm
    maxDay = (datetime.date(year, month % 12 + 1, 1) - datetime.timedelta(days=1)).day
    day = random.randint(1, maxDay)

    return (day, month, year)

def randomString(length, useSpace=True, useUpper=True, useLower=True, useSpecial=False):
    """
    Hàm randomString sinh chuỗi ngẫu nhiên với các tùy chọn:

    - length (int): Độ dài chuỗi cần sinh.
    - useSpace (bool, mặc định=True): Cho phép dấu cách hay không.
    - useUpper (bool, mặc định=True): Cho phép chữ hoa hay không.
    - useLower (bool, mặc định=True): Cho phép chữ thường hay không.
    - useSpecial (bool, mặc định=False): Cho phép ký tự đặc biệt (!@#$%^&*...) hay không.

    Returns:
    - str: Chuỗi ngẫu nhiên theo yêu cầu.

    Ví dụ:
    randomString(10)                 # Chuỗi 10 ký tự có khoảng trắng, chữ hoa, chữ thường.
    randomString(8, useSpace=False)   # Chuỗi 8 ký tự không có dấu cách.
    randomString(12, useSpecial=True) # Chuỗi 12 ký tự có ký tự đặc biệt.
    randomString(15, useLower=False)  # Chuỗi 15 ký tự chỉ có chữ hoa và khoảng trắng.
    """

    charPool = ""
    
    if useLower:
        charPool += string.ascii_lowercase  # a-z
    if useUpper:
        charPool += string.ascii_uppercase  # A-Z
    if useSpecial:
        charPool += string.punctuation      # !@#$%^&*()_+...
    if useSpace:
        charPool += " "                     # Dấu cách
    
    if not charPool:
        raise ValueError("Phải chọn ít nhất một loại ký tự!")

    return "".join(random.choices(charPool, k=length))

def randomStringFromChars(length, options, allowDuplicates=True):
    """
    Sinh một chuỗi ngẫu nhiên với các ký tự thuộc danh sách options.
    
    - length: Độ dài chuỗi cần tạo.
    - options: Danh sách các ký tự hợp lệ.
    - allowDuplicates: Cho phép trùng lặp ký tự hay không.
    
    Nếu allowDuplicates=False và length > len(options), sẽ báo lỗi.
    """
    if not allowDuplicates and length > len(options):
        raise ValueError("Không thể tạo chuỗi không trùng với số lượng lớn hơn danh sách ký tự")

    return "".join(random.choices(options, k=length)) if allowDuplicates else "".join(random.sample(options, length))



############## RANDOM 1 LIST ##############

def randomIntList(size, minVal, maxVal, allowDuplicates=True, sortOrder=None):
    """
    Hàm randomList sinh list số nguyên có đầy đủ các tùy chọn:
    - size: Số lượng phần tử trong danh sách.
    - minVal, maxVal: Giá trị nhỏ nhất và lớn nhất.
    - allowDuplicates (bool, mặc định=True): Cho phép trùng lặp hay không.
    - sortOrder: Kiểu sắp xếp (None - không sắp xếp, "asc" - tăng dần, "desc" - giảm dần).
    
    Returns:
    - List[int]: Danh sách số nguyên ngẫu nhiên theo yêu cầu.

    Ví dụ:
    randomList(5, 1, 10) # Ngẫu nhiên, có thể trùng
    randomList(5, 1, 10, False) # Ngẫu nhiên, không trùng
    randomList(5, 1, 10, allowDuplicates=False, sortOrder="desc") # Ngẫu nhiên, không trùng, giảm dần
    randomList(5, 1, 10, sort_order="asc") # Ngẫu nhiên, có thể trùng, tăng dần
    """
    if allowDuplicates:
        lst = [random.randint(minVal, maxVal) for _ in range(size)]
    else:
        if maxVal - minVal + 1 < size:
            raise ValueError("Khoảng giá trị không đủ để tạo danh sách không trùng lặp")
        lst = random.sample(range(minVal, maxVal + 1), size)

    # Sắp xếp nếu cần
    if sortOrder == "asc":
        lst.sort()
    elif sortOrder == "desc":
        lst.sort(reverse=True)

    return lst


def randomFloatList(size, minVal, maxVal, allowDuplicates=True, sortOrder=None, precision=2):
    """
    Hàm randomFloatList sinh list số thực có đầy đủ các tùy chọn:
    
    - size (int): Số lượng phần tử trong danh sách.
    - minVal, maxVal: Giá trị nhỏ nhất và lớn nhất.
    - allowDuplicates (bool, mặc định=True): Cho phép trùng lặp hay không.
    - sortOrder (str, mặc định=None): Kiểu sắp xếp kết quả ("asc" - tăng dần, "desc" - giảm dần, None - không sắp xếp).
    - precision (int, mặc định=2): Số chữ số sau dấu thập phân.

    Returns:
    - List[float]: Danh sách số thực ngẫu nhiên theo yêu cầu.

    Ví dụ:
    randomFloatList(5, 1.0, 10.0) # Ngẫu nhiên, có thể trùng
    randomFloatList(5, 1.0, 10.0, False) # Ngẫu nhiên, không trùng
    randomFloatList(5, 1.0, 10.0, allowDuplicates=False, sortOrder="desc") # Ngẫu nhiên, không trùng, giảm dần
    randomFloatList(5, 1.0, 10.0, sortOrder="asc", precision=3) # Ngẫu nhiên, có thể trùng, tăng dần, 3 chữ số thập phân
    """
    
    if allowDuplicates:
        # Nếu cho phép trùng lặp, chọn ngẫu nhiên số thực với số chữ số thập phân được chỉ định
        lst = [round(random.uniform(minVal, maxVal), precision) for _ in range(size)]
    else:
        # Nếu không cho phép trùng lặp, cần sinh các giá trị không trùng
        uniqueValues = set()
        while len(uniqueValues) < size:
            uniqueValues.add(round(random.uniform(minVal, maxVal), precision))
        lst = list(uniqueValues)

    # Sắp xếp danh sách nếu cần
    if sortOrder == "asc":
        lst.sort()
    elif sortOrder == "desc":
        lst.sort(reverse=True)

    return lst

def randomStringList(size, maxLen, useSpace=True, useUpper=True, useLower=True, useSpecial=False, minStrLen=1):
    """
    Sinh danh sách `size` chuỗi ngẫu nhiên sao cho tổng độ dài <= `maxLen`.

    - size (int): Số lượng phần tử trong danh sách.
    - maxLen (int): Tổng độ dài tối đa của tất cả chuỗi trong danh sách.
    - minStrLen (int, mặc định=1): Độ dài tối thiểu của mỗi chuỗi.
    - Các tùy chọn khác giống như `randomString`.

    Returns:
    - list: Danh sách `size` chuỗi ngẫu nhiên.
    """
    
    if minStrLen * size > maxLen:
        raise ValueError("Không thể tạo danh sách thỏa mãn điều kiện (tối thiểu quá lớn so với maxLen)")

    remainingLen = maxLen  # Tổng số ký tự còn lại có thể sử dụng
    result = []

    for i in range(size):
        maxStrLen = remainingLen - (size - len(result) - 1) * minStrLen  # Giữ đủ ký tự cho phần còn lại
        strLen = random.randint(minStrLen, maxStrLen)  # Chọn độ dài hợp lệ
        result.append(randomString(strLen, useSpace, useUpper, useLower, useSpecial))
        remainingLen -= strLen  # Giảm phần còn lại

    return result

def randomListDate(size, minYear, maxYear, allowDuplicates=True, sortOrder=None):
    """
    Sinh danh sách các ngày ngẫu nhiên.
    
    - size: Số lượng phần tử.
    - minYear, maxYear: Khoảng năm hợp lệ.
    - allowDuplicates: Cho phép trùng lặp hay không.
    - sortOrder: None (ngẫu nhiên), "asc" (tăng dần), "desc" (giảm dần).
    """
    if not allowDuplicates and (maxYear - minYear + 1) * 365 < size:
        raise ValueError("Khoảng ngày không đủ để tạo danh sách không trùng lặp!")

    dateSet = set()
    result = []

    while len(result) < size:
        newDate = randomDate(minYear, maxYear)
        if allowDuplicates or newDate not in dateSet:
            result.append(newDate)
            dateSet.add(newDate)

    # Sắp xếp danh sách nếu cần
    if sortOrder == "asc":
        result.sort(key=lambda d: (d[2], d[1], d[0]))  # Sắp xếp theo (năm, tháng, ngày)
    elif sortOrder == "desc":
        result.sort(key=lambda d: (d[2], d[1], d[0]), reverse=True)

    return result


############## ĐỊNH DẠNG ĐẦU RA CỦA DANH SÁCH ##############

def toStringLines(lst):
    """
    Tạo một chuỗi từ danh sách lst, mỗi phần tử cách nhau một dòng.
    - Nếu phần tử là số hoặc chuỗi, chuyển thành chuỗi và giữ nguyên.
    - Nếu phần tử là danh sách con, các phần tử trong đó được ghép lại thành một dòng (cách nhau dấu cách).
    - Toàn bộ danh sách được nối lại bằng dấu xuống dòng ("\n").

    Ví dụ:
    >>> toStringLines([1, [2, 3, 4], 5])
    '1\n2 3 4\n5'
    """
    result = []
    for item in lst:
        if isinstance(item, list):  # Nếu phần tử là danh sách con
            result.append(" ".join(map(str, item)))  # Ghép thành một dòng
        else:
            result.append(str(item))  # Chuyển thành chuỗi
    return "\n".join(result)  # Ghép toàn bộ danh sách thành chuỗi với dấu xuống dòng

def toStringLinesAll(lst):
    """
    Chuyển danh sách lst thành một chuỗi, mỗi phần tử cách nhau một dòng.
    - Nếu phần tử là số hoặc chuỗi, giữ nguyên.
    - Nếu phần tử là danh sách con, mỗi phần tử trong đó cũng xuống dòng riêng (đệ quy).
    - Toàn bộ danh sách được nối lại bằng dấu xuống dòng ("\n").

    Ví dụ:
    >>> toStringLinesAll([1, [2, 3], 4, [5, [6, 7], 8]])
    '1\n2\n3\n4\n5\n6\n7\n8'
    """
    result = []
    for item in lst:
        if isinstance(item, list):  # Nếu phần tử là danh sách con, xử lý đệ quy
            result.append(toStringLinesAll(item))  # Gọi lại chính hàm này
        else:
            result.append(str(item))  # Chuyển thành chuỗi

    return "\n".join(result)  # Ghép tất cả phần tử thành chuỗi với dấu xuống dòng

def toStringSpace(lst):
    """
    Tạo một chuỗi từ danh sách lst, mỗi phần tử cách nhau một dấu cách.
    - Nếu phần tử là số hoặc chuỗi, giữ nguyên.
    - Nếu phần tử là danh sách con, các phần tử bên trong được nối lại bằng dấu cách.
    - Toàn bộ danh sách được nối lại thành một chuỗi trên một dòng.

    Ví dụ:
    >>> toStringSpace([1, [2, 3, 4], 5])
    '1 2 3 4 5'
    """
    result = []
    for item in lst:
        if isinstance(item, list):  # Nếu phần tử là danh sách con
            result.append(" ".join(map(str, item)))  # Ghép tất cả phần tử con thành một chuỗi
        else:
            result.append(str(item))  # Chuyển thành chuỗi
    return " ".join(result)  # Ghép toàn bộ danh sách thành chuỗi với dấu cách