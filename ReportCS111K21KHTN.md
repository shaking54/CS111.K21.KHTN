Báo cáo bài tập môn Nguyên lý và phương pháp lập trình
CS111.K21.KHTN
Giảng viên: Trịnh Quốc Sơn
Thành viên nhóm: 	Lưu Hoàng Sơn		18521348
				    Nguyễn Trần Trung	18521555

Báo cáo về nội dung cần tìm hiểu để xây dựng một interpreter cho ngôn ngữ barebone
bằng Python

1. Các vấn đề cần tìm hiểu:
1.1 Lexer
    Quá trình tách cách kí tự vào trong các tokens được gọi là lexing và được thực hiện
    bởi Lexer.
    Tokens là những đối tượng có kiểu dữ liện kèm theo nó là giá trị
1.2 Parser
    Parser sẽ sắp xếp lại cấu trúc của tokens thu được từ Lexer và xây dựng một AST
1.3 AST (Abstract syntax tree)
    Cấu trúc cây đại diện cho sự trừu tượng về cấu trúc cú pháp của một source code được viết 
    bằng một ngôn ngữ lập trình. 
1.4 Bytecode
    Bytecode là một chuỗi các chỉ dẫn cho máy tính 
1.5 Interpreter
2. Các tài liệu tham khảo:
https://ruslanspivak.com/lsbasi-part1/
https://www.youtube.com/watch?v=LCslqgM48D4
https://craftinginterpreters.com/contents.html