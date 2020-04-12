# Báo cáo bài tập môn Nguyên lý và phương pháp lập trình

## Giảng viên: Trịnh Quốc Sơn

## CS 111. K21. KHTN

### Thành viên nhóm: 	

| MSSV              | Họ và tên |
|-------------------|-----------|
| Lưu Hoàng Sơn     | 18521348  |
| Nguyễn Trần Trung | 18521555  |

### Đề tài: 14. Nghiên cứu cài đặt trình phiên dịch intepretercho ngôn ngữ lập trình Barebone

#### Mục tiêu tìm hiểu:

1. Ngôn ngữ lập trình Barebone và Cách intepreter hoạt động 

    1.1 Barebone và cú pháp của barebone

    1.2 Lexer

        Quá trình tách cách kí tự vào trong các tokens được gọi là lexing và được thực hiện
        bởi Lexer.
        Tokens là những đối tượng có kiểu dữ liện kèm theo nó là giá trị

    1.3 Parser

        Parser sẽ sắp xếp lại cấu trúc của tokens thu được từ Lexer và xây dựng một AST

    1.4 AST (Abstract syntax tree)

        Cấu trúc cây đại diện cho sự trừu tượng về cấu trúc cú pháp của một source code được viết 
        bằng một ngôn ngữ lập trình. 

    1.5 Bytecode

        Bytecode là một chuỗi các chỉ dẫn cho máy tính 

    1.6 Interpreter

    1.7 Tài liệu tham khảo 

        Sách viết về barebone : Computer Science: An Overview by Glenn Brookshear, Dennis Brylow 
        Sách viết về intepreter: https://craftinginterpreters.com/contents.html


2. Xây dựng chương trình cho phép biên dịch chương trình viết bằng Barebone để có thể thực thi được cho các phép toán : +, -,*, / 2 số nguyên ; phép toán so sánh <, < =, >=, >, # giữa 2 số nguyên

    2.1 Mục tiêu phát triển barebone:

        Phát triển từ một chương trình đã có ở sau: https://github.com/shirkey/barebones
        dựa trên source code này tụi em sẽ phát triển thêm bằng python
        toán tử + - * / 
        toán tử so sánh
        câu lệnh điều kiện

    2.2 Tài liệu tham khảo:

    https://en.wikipedia.org/wiki/Operator_(computer_programming)

3. Giao diện chương trình biên dịch ở dạng đồ họa hoặc giao diện dòng lệnh command line

    3.1 Tài liệu tham khảo 

        https://www.guru99.com/introduction-to-shell-scripting.html

4. Chương trình có hỗ trợ chức năng biên soạn chương trình barebone được khuyến khích

    4.1 Tài liệu tham khảo

    Tạm thời em chưa tìm được ra tài liệu phần này, mong thầy cho tụi em xin ạ 

