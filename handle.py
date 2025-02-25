# Thư viện
import pandas as pd

# Các Mô-dun
from func.createData import PGLangs, GetCodeLevel

# Chương trình chính
df = pd.read_excel(
    pd.ExcelFile("./input/data.xlsx"), 
    sheet_name="Form Responses 1")

Heard_PGLangs, Use_PGLang = PGLangs(df)
Code_Level = GetCodeLevel(df)

# Tạo file output
Heard_PGLangs_Table = pd.DataFrame(
    {
        "Tên ngôn ngữ lập trình" : Heard_PGLangs.keys(),
        "Số lượng sinh viên đã nghe qua" : Heard_PGLangs.values()
    }
)

Use_PGLang_Table = pd.DataFrame(
    {
        "Tên ngôn ngữ lập trình" : Use_PGLang.keys(),
        "Số lượng sinh viên đã sử dụng" : Use_PGLang.values()
    }
)

Code_Level_Table = pd.DataFrame(
    {
        "Trình độ code": Code_Level.keys(),
        "Số lượng": Code_Level.values()
    }
)

outputFileName = "./output/output.xlsx"

with pd.ExcelWriter(outputFileName, engine="xlsxwriter") as writer:
    Heard_PGLangs_Table.to_excel(writer, sheet_name="Thống kê đơn giản", index=False, startrow=0, startcol=0)  # Ghi vào A1
    Use_PGLang_Table.to_excel(writer, sheet_name="Thống kê đơn giản", index=False, startrow=0, startcol=5)  # Ghi vào C6
    Code_Level_Table.to_excel(writer, sheet_name="Thống kê đơn giản", index=False, startrow=0, startcol=8) # Ghi vào E11

print("Kiểm tra thư mục output của source code")