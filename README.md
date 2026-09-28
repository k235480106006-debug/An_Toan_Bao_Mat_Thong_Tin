\# BÀI TẬP VỀ NHÀ MÔN AN TOÀN VÀ BẢO MẬT THÔNG TIN



\- \*\*Họ và tên:\*\* NGUYỄN VĂN CƯƠNG

\- \*\*Mã sinh viên:\*\* K235480106006

\- \*\*Lớp:\*\* K59KMT

\- \*\*Mô tả:\*\* Bài tập tìm hiểu về các thuật toán mã hóa đối xứng (DES, AES), mã hóa bất đối xứng (RSA) và mô hình mã hóa kết hợp.



\---



\## 1. Thuật toán mã hóa hiện đại DES và AES



\### a. Thuật toán DES (Data Encryption Standard)

\- \*\*Tổng quan:\*\* DES là thuật toán mã hóa đối xứng theo khối (Block cipher). Kích thước khối dữ liệu là 64-bit và độ dài khóa thực tế là 56-bit (8-bit còn lại dùng kiểm tra lỗi parity).

\- \*\*Cấu trúc:\*\* Sử dụng cấu trúc mạng Feistel gồm 16 vòng biến đổi liên tiếp.

\- \*\*Quy trình mã hóa:\*\*

&#x20; 1. Khối văn bản rõ 64-bit đầu vào được đưa qua phép Hoán vị ban đầu (Initial Permutation - IP).

&#x20; 2. Khối dữ liệu được tách thành 2 nửa 32-bit là Trái L0 và Phải R0.

&#x20; 3. Trải qua 16 vòng biến đổi Feistel theo công thức:

&#x20;    - L(i) = R(i-1)

&#x20;    - R(i) = L(i-1) XOR F(R(i-1), K\_i)

&#x20;    - Trong đó: K\_i là khóa vòng 48-bit được tạo ra từ khóa chính, F là hàm biến đổi Feistel thực hiện mở rộng R(i-1) từ 32-bit lên 48-bit, XOR với K\_i, nén qua 8 hộp S-Box về 32-bit và hoán vị qua P-Box.

&#x20; 4. Sau 16 vòng, ghép hai nửa (R16, L16) lại và cho qua phép Hoán vị ngược IP^(-1) để thu được bản mã 64-bit.

\- \*\*Quy trình giải mã:\*\* Sử dụng cùng thuật toán và sơ đồ như mã hóa, nhưng thứ tự khóa vòng được đưa vào ngược lại (từ K16 về K1).



\---



\### b. Thuật toán AES (Advanced Encryption Standard)

\- \*\*Tổng quan:\*\* AES là thuật toán mã hóa đối xứng mã hóa theo từng khối 128-bit. Thuật toán hỗ trợ các độ dài khóa 128-bit (10 vòng), 192-bit (12 vòng) và 256-bit (14 vòng).

\- \*\*Quy trình mã hóa (với khóa 128-bit - 10 vòng):\*\*

&#x20; 1. \*\*Khởi tạo:\*\* Cộng khóa vòng đầu tiên (AddRoundKey) giữa khối dữ liệu và K0.

&#x20; 2. \*\*Vòng 1 đến Vòng 9:\*\* Lặp lại 4 bước biến đổi:

&#x20;    - \*\*SubBytes:\*\* Thay thế phi tuyến từng byte qua bảng S-Box cố định.

&#x20;    - \*\*ShiftRows:\*\* Dịch chuyển vòng các hàng của ma trận trạng thái (Hàng 0 giữ nguyên, Hàng 1 dịch trái 1 byte, Hàng 2 dịch 2 byte, Hàng 3 dịch 3 byte).

&#x20;    - \*\*MixColumns:\*\* Trộn các cột bằng phép nhân ma trận trên trường Galois GF(2^8).

&#x20;    - \*\*AddRoundKey:\*\* XOR dữ liệu với khóa vòng K\_i tương ứng.

&#x20; 3. \*\*Vòng 10 (Vòng cuối):\*\* Thực hiện 3 bước SubBytes -> ShiftRows -> AddRoundKey (bỏ qua bước MixColumns).

\- \*\*Quy trình giải mã:\*\* Thực hiện các bước biến đổi ngược (InvShiftRows -> InvSubBytes -> AddRoundKey -> InvMixColumns) theo thứ tự ngược lại từ vòng cuối về vòng đầu.

\- \*\*Cài đặt chương trình:\*\* Em đã cài đặt demo thuật toán AES chế độ CBC bằng ngôn ngữ Python trong file `aes\_demo.py` kèm theo repository này.



\---



\## 2. Thuật toán mã hóa bất đối xứng RSA



RSA là thuật toán mã hóa khóa công khai dựa trên độ khó của bài toán phân tích một số nguyên cực lớn thành các thừa số nguyên tố.



\### Nguyên lý sinh cặp khóa (Public Key \& Private Key):

1\. Chọn 2 số nguyên tố ngẫu nhiên rất lớn là p và q (với p khác q).

2\. Tính n = p \* q. Giá trị n gọi là kích thước không gian khóa (modulus).

3\. Tính hàm số Euler Phi(n) = (p - 1) \* (q - 1).

4\. Chọn một số nguyên e làm khóa công khai sao cho 1 < e < Phi(n) và ước chung lớn nhất ucln(e, Phi(n)) = 1 (thông thường chọn e = 65537).

5\. Tính khóa bí mật d là nghịch đảo nhân modular của e theo Phi(n), thỏa mãn phương trình: (d \* e) mod Phi(n) = 1.

6\. Cặp khóa thu được:

&#x20;  - \*\*Khóa công khai (Public Key):\*\* PU = (e, n) dùng để mã hóa hoặc xác minh chữ ký.

&#x20;  - \*\*Khóa bí mật (Private Key):\*\* PR = (d, n) dùng để giải mã hoặc tạo chữ ký số.



\### Công thức thực hiện:

\- \*\*Mã hóa thông điệp M (với M < n):\*\* Bản mã C = (M ^ e) mod n

\- \*\*Giải mã bản mã C:\*\* Thông điệp gốc M = (C ^ d) mod n



\---



\## 3. Các mô hình áp dụng RSA, So sánh và Mô hình kết hợp



\### a. Các mô hình áp dụng thuật toán RSA

\- \*\*Mô hình 1: Xác thực người nhận (Bảo mật thông điệp)\*\*

&#x20; - Người gửi A lấy Khóa công khai của người nhận B (PU\_B) để mã hóa văn bản.

&#x20; - Chỉ có người nhận B sở hữu Khóa bí mật (PR\_B) tương ứng mới có thể giải mã. Mô hình này đảm bảo tính bảo mật dữ liệu.

\- \*\*Mô hình 2: Xác thực người gửi (Chữ ký số)\*\*

&#x20; - Người gửi A dùng Khóa bí mật của mình (PR\_A) để mã hóa/ký vào thông điệp. Người nhận B dùng Khóa công khai của A (PU\_A) để giải mã xác minh.

&#x20; - Nếu giải mã thành công, chứng minh thông điệp đúng do A gửi và A không thể chối bỏ trách nhiệm.

\- \*\*Mô hình 3: Kết hợp cả hai (Vừa bảo mật vừa xác thực)\*\*

&#x20; - Người gửi A dùng Khóa bí mật của mình (PR\_A) để ký trước, sau đó dùng tiếp Khóa công khai của B (PU\_B) để mã hóa toàn bộ.

&#x20; - Người nhận B dùng Khóa bí mật (PR\_B) để mở lớp bảo mật, sau đó dùng Khóa công khai (PU\_A) để xác minh người gửi.



\### b. So sánh thời gian mã hóa/giải mã giữa RSA và AES

\- \*\*AES (Mã hóa đối xứng):\*\* Dựa trên các phép toán XOR, dịch bit và tra bảng ma trận đơn giản nên tốc độ xử lý rất nhanh (hàng trăm MB/s đến GB/s). Rất thích hợp để mã hóa các file và dữ liệu dung lượng lớn.

\- \*\*RSA (Mã hóa bất đối xứng):\*\* Dựa trên phép tính lũy thừa trên các số nguyên khổng lồ (2048 đến 4096 bit) nên tốn nhiều tài nguyên tính toán. Tốc độ mã hóa/ giải mã của RSA chậm hơn AES từ 100 đến 1000 lần.



\### c. Mô hình kết hợp sức mạnh giữa RSA và AES (Mã hóa lai - Hybrid Encryption)

Để tận dụng \*\*tốc độ mã hóa nhanh của AES\*\* và \*\*khả năng quản lý khóa an toàn của RSA\*\*, mô hình mã hóa kết hợp được thực hiện như sau:



1\. \*\*Phía người gửi:\*\*

&#x20;  - Tạo ra một khóa AES ngẫu nhiên dùng 1 lần (gọi là Khóa phiên - Session Key K\_AES).

&#x20;  - Dùng K\_AES mã hóa toàn bộ dữ liệu gốc bằng thuật toán AES -> thu được bản mã dữ liệu C\_data (thực hiện rất nhanh).

&#x20;  - Dùng Khóa công khai RSA của người nhận (PU\_B) để mã hóa khóa K\_AES -> thu được C\_key = (K\_AES ^ e\_B) mod n\_B.

&#x20;  - Gửi gói dữ liệu gồm (C\_data, C\_key) cho người nhận.

2\. \*\*Phía người nhận:\*\*

&#x20;  - Dùng Khóa bí mật RSA của mình (PR\_B) giải mã C\_key để lấy lại khóa K\_AES.

&#x20;  - Dùng khóa K\_AES thu được để giải mã C\_data bằng thuật toán AES thu lại dữ liệu gốc ban đầu.

