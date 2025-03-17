# Hướng Dẫn Sử Dụng Script Sinh Test

## Bước 1: Tạo Folder Chứa Bài Tập
Tạo một folder mới bên trong thư mục `problems`, đặt tên theo mã bài tập. Ví dụ:
```
problems/
    bai1/
    bai2/
    ...
```

## Bước 2: Thêm File Code Bài Tập
Thêm file code **C++ hoặc Python** vào folder vừa tạo.
- **Tên file phải trùng với tên folder**.
- Nếu viết bằng **C++**, đặt tên file là `<problemName>.cpp`.
- Nếu viết bằng **Python**, đặt tên file là `<problemName>.py`.

Ví dụ với bài `bonghong`:
```
problems/
    bonghong/
        bonghong.cpp  (hoặc bonghong.py)
```

## Bước 3: Cấu Hình File `config.py`
- **Copy file** `config_sample.py` vào thư mục bài tập.
- **Đổi tên file** thành `config.py`.
- **Chỉnh sửa các tham số** bên trong `config.py` như sau:

```python
# Tên bài toán (trùng với tên folder và file code)
problemName = "bonghong"

# Số lượng test case cần sinh
totalOfTests = 20

# Phân chia điểm theo subtask
subtasks = [50, 50]  # Subtask 1: 50%, Subtask 2: 50%. Đoạn này có bao nhiêu subtask thì ta sẽ thêm và ghi ra số lượng % tương ứng

# Giới hạn đầu vào của bài toán
minN = 1
maxN = [1000, 1000000]  # Subtask 1: tối đa 1000, Subtask 2: tối đa 1.000.000. Nếu nhiều subtask thì ta lần lượt thêm 
```

**Giải thích:**
- `problemName`: Tên bài toán, phải khớp với tên folder và file code.
- `totalOfTests`: Số lượng test case cần tạo.
- `subtasks`: Chia điểm theo các subtask. Ví dụ `[50, 50]` nghĩa là mỗi subtask chiếm 50% tổng điểm.
- `minN`: Giá trị nhỏ nhất của đầu vào.
- `maxN`: Giá trị lớn nhất của đầu vào, có thể là một số hoặc một danh sách tương ứng với các subtask.

- Hàm `genInputContent(testID, curSubtask)` chịu trách nhiệm sinh dữ liệu đầu vào cho từng test case. Chỉnh sửa hàm sao cho phù hợp với dữ liệu từng đề bài. File `genUltils.py` chứa các hàm hỗ trợ sinh dữ liệu ngẫu nhiên và xử lý định dạng. Để hiểu rõ hơn, hãy mở genUltils.py để xem các hàm tiện ích.

## Bước 4: Chạy Script Sinh Test
Chạy file `genTest.py` để tạo bộ test tự động:
```sh
python genTest.py
```

Sau khi chạy xong, test cases sẽ được tạo trong thư mục bài tập. Bạn có thể kiểm tra output trong các file `*.out` tương ứng.

# Guide to Using Test Generation Script

## Step 1: Create a Problem Folder
Create a new folder inside the `problems` directory, named after your problem code. For example:
```
problems/
    bai1/
    bai2/
    ...
```

## Step 2: Add the Problem Code File
Add a **C++ or Python** code file to the folder you just created.
- **The filename must match the folder name**.
- If writing in **C++**, name the file `<problemName>.cpp`.
- If writing in **Python**, name the file `<problemName>.py`.

Example for problem `bonghong`:
```
problems/
    bonghong/
        bonghong.cpp  (or bonghong.py)
```

## Step 3: Configure the `config.py` File
- **Copy** the `config_sample.py` file into your problem folder.
- **Rename** it to `config.py`.
- **Edit the parameters** inside `config.py` as follows:

```python
# Problem name (matching the folder and code file name)
problemName = "bonghong"

# Number of test cases to generate
totalOfTests = 20

# Point distribution by subtask
subtasks = [50, 50]  # Subtask 1: 50%, Subtask 2: 50%. Add more entries for additional subtasks with their percentage points

# Input constraints
minN = 1
maxN = [1000, 1000000]  # Subtask 1: maximum 1000, Subtask 2: maximum 1,000,000. Add more entries for additional subtasks
```

**Explanation:**
- `problemName`: The problem name, must match the folder and code file name.
- `totalOfTests`: Number of test cases to generate.
- `subtasks`: Point distribution across subtasks. For example, `[50, 50]` means each subtask is worth 50% of the total points.
- `minN`: The minimum input value.
- `maxN`: The maximum input value, can be a single number or a list corresponding to each subtask.

- The `genInputContent(testID, curSubtask)` function is responsible for generating input data for each test case. Modify this function according to your problem's requirements. The `genUltils.py` file contains utility functions for random data generation and formatting. For a better understanding, open genUltils.py to see the available utility functions.

## Step 4: Run the Test Generation Script
Run the `genTest.py` file to automatically generate the test suite:
```sh
python genTest.py
```

After running, test cases will be created in your problem folder. You can check the output in the corresponding `*.out` files.