import tkinter as tk
from tkinter import filedialog
import zlib
import subprocess

def get_user_input():
    variables = []
    for i in range(1, 17):
        var = entry_widgets[i-1].get()
        variables.append(var)
    return variables

def show_variables():
    user_input = get_user_input()
    result_label.config(text="您輸入的變數為：" + str(user_input))
    sw_version = user_input[0]
    hw_version = user_input[1]
    kernel_version = user_input[2]
    parameter_version = user_input[3]
    bootloader_version = user_input[4]
    project_name = user_input[5]
    project_code = user_input[6]
    date = user_input[7]
    part_number = user_input[8]
    customer = user_input[9]
    kernel_hash256 = user_input[10]
    kernel_project_hash256 = user_input[11]
    codebase_hash256 = user_input[12]
    owner = user_input[13]
    code_path = user_input[14]

    note = user_input[15]

    text = ('\documentclass[12pt,a4paper]{article}\n\
            \\setcounter{tocdepth}{3}\n\
            \\usepackage{wordlike}\n\
            \\usepackage{listings}\n\
            \\lstset{\n\
                rulesepcolor= \color{gray},\n\
                breaklines=true,  %程式碼過長則換行\n\
                numbers=left, %行號在左側顯示\n\
                numberstyle= \small,%行號字型\n\
                commentstyle=\color{gray}, %註釋顏色\n\
                frame=shadowbox,%用方框框住程式碼塊\n\
                basicstyle=\fontsize{8}{12}\ttfamily\n\
                }\n\
            \\usepackage{indentfirst}\n\
            \\usepackage{multirow}\n\
            \\usepackage{booktabs}\n\
            \\usepackage{xltabular}\n\
            \\usepackage{xcolor}\n\
            \\usepackage{colortbl}\n\
            \\usepackage{tabularx}\n\
            \\usepackage{multicol}\n\
            \\usepackage{lipsum}\n\
            \\usepackage{tabularray}\n\
            \\usepackage{array}\n\
            \\usepackage{comment}\n\
            \\usepackage[hidelinks]{hyperref}\n\
            \\usepackage{geometry}\n\
            \\usepackage{etoolbox}\n\
            \\newcommand{\protocal}{Battery1}\n\
            \\geometry{\n\
              a4paper,\n\
              left=1.5cm,\n\
              right=1.5cm,\n\
              top=2cm,\n\
              bottom=2cm\n\
            }\n\
            \\usepackage[document]{ragged2e}\n\
            \\usepackage{ulem}\n\
            \\usepackage{makecell}\n\
            \\usepackage{xcolor}\n\
            \\usepackage{graphicx}\n\
            \\usepackage{hhline}\n\
            \\usepackage{newtxtext,newtxmath}\n\
            \\usepackage{draftwatermark}\n\
            \\usepackage{csvsimple}\n\
            \\newcommand{\head}[1]{\\textnormal{\\textbf{#1}}}\n\
            \\newcommand{\website}{\color{blue}\\uline}\n\
            \\newcommand{\ct}{\centering} %置中\n\
            \\newcommand{\cth}[1]{\centering{\\textbf{#1}}} %置中粗體\n\
            \\newcommand{\mct}[1]{\centering\\arraybackslash{#1}} %表個字體置中\n\
            \\newcommand{\mcth}[1]{\makecell{\centering{\\textbf{#1}}}} %表格粗體最右邊\n\
            \\newcommand{\\ul}[1]{\\texorpdfstring{\\uline{#1}}{{#1}}} % 斜體\n\
            \\newcommand{\\bct}[1]{\centering{\\textbf{\\textit{#1}}}} %斜粗體\n\
            \\newcommand{\mbcth}[1]{\makecell{\centering{\\textbf{\\textit{#1}}}}} %斜粗體\n\
            \\SetWatermarkText{HYENA Confidential}\n\
            \\SetWatermarkLightness{0.9}\n\
            \\SetWatermarkScale{0.5}\n\
            \\begin{document}\n\
            \\title{Hyena Release Note}\n\
            \\author{Hyena System Integration Team}\n\
            \\date{}\n\
            \\maketitle\n\
            \\begin{table}[h!]\n\
        \\centering\n\
        \\large\n\
        \\resizebox{\\textwidth}{!}{\n\
        \\begin{tabular}[c]{|m{4cm}|m{4cm}|m{4cm}|m{4cm}|}\n\
        \\hline\n\
        \\rowcolor{black}\multicolumn{4}{|l|}{\color{white}\\textbf{General Information}}\\\\\n\
        \\hline\n\
        \\textbf {Project Name} & \ct{DP-TR19A} & \\textbf{Project Type} & \mct{Controller}\\\\\n\
        \\hline\n\
        \\textbf {Project Code} & \ct{D0027} & \\textbf{Part Number} & \mct{40021D20A-1}\\\\\n\
        \\hline\n\
        \\textbf {Release Date} & \ct{2022/10/31} & \\textbf{Owner} & \mct{person}\\\\\n\
        \\hline\n\
        \\textbf {Customer} & \ct{Trek} & \multicolumn{2}{c|}{} \\\\\n\
        \\hline\n\
        \\end{tabular}}\n\
    \\end{table}\n\
    \\begin{table}[h!]\n\
        \\centering\n\
        \\large\n\
        \\resizebox{\\textwidth}{!}{\n\
        \\begin{tabular}[c]{|m{4cm}|m{4cm}|m{4cm}|m{4cm}|}\n\
            \\hline\n\
            \\rowcolor{black}\multicolumn{4}{|l|}{\color{white}\\textbf{Version}}\\\\\n\
            \\hline\n\
            \\textbf {SW version } & \ct{swv} & \\textbf{HW version} & \mct{hv}\\\\\n\
            \\hline\n\
            \\textbf {Kernel version } & \ct{kv} & \\textbf{BTL version} & \mct{bv}\\\\\n\
            \\hline\n\
            \\textbf {Parameter version } & \ct{pv} & \multicolumn{2}{c|}{} \\\\\n\
            \\hline\n\
        \\end{tabular}}\n\
    \\end{table}\n\
    \\begin{table}[h!]\n\
        \\centering\n\
        \\large\n\
        \\resizebox{\\textwidth}{!}{\n\
        \\begin{tabular}[c]{|m{3cm}|m{12cm}|m{3cm}|}\n\
            \\hline\n\
            \\rowcolor{black}\multicolumn{3}{|l|}{\color{white}\\textbf{Files Location }}\\\\\n\
            \\hline\n\
            \\textbf {HEX path} & \ct{Refer to SharePoint project list} & \mcth{CRC32}\\\\\n\
            \\hline\n\
            \\textbf {APP} & \ct{40021D20A-1\_Driver\_APP\_swv\_kv\_hv\_pv.hex } & \mct{app_crc32 }\\\\\n\
            \\hline\n\
            \\textbf {Bootloader} & \ct{40021D20A-1\_Driver\_BTL\_swv\_kv\_hv\_pv.hex } & \mct{btl_crc32}\\\\\n\
            \\hline\n\
            \\textbf {Merge} & \ct{40021D20A-1\_Driver\_MRG\_swv\_kv\_hv\_pv.hex } & \mct{mrg_crc32}\\\\\n\
            \\hline\n\
            \\textbf {Bin} & \ct{40021D20A-1\_Driver\_APP\_swv\_kv\_hv\_pv.bin } & \mct{bin_crc32}\\\\\n\
            \\hline\n\
            \\textbf {APP Zip} & \ct{} & \mcth{}\\\\\n\
            \\hline\n\
            \\textbf {Code path} & \multicolumn{2}{l|}{code_path}\\\\\n\
            \\hline\n\
            \\textbf {Test Plan} & \multicolumn{2}{l|}{}\\\\\n\
            \\hline\n\
        \\end{tabular}}\n\
    \\end{table}\n\
    \\begin{table}[h!]\n\
        \\centering\n\
        \\large\n\
        \\resizebox{\\textwidth}{!}{\n\
        \\begin{tabular}[c]{|m{4cm}|m{12cm}|}\n\
            \\hline\n\
            \\rowcolor{black}\multicolumn{2}{|l|}{\color{white}\\textbf{Note }}\\\\\n\
            \\hline\n\
            \\textbf{Requirement} & \mct{Release swv version FW.}\\\\\n\
            \\hline\n\
            \\textbf{Kerenl} & \mct{KERNEL}\\\\\n\
            \\hline\n\
            \\textbf{kernel Project} & \mct{KP}\\\\\n\
            \\hline\n\
            \\textbf{Code Base} & \mct{CODEBASE}\\\\\n\
            \\hline\n\
            \\multicolumn{2}{|l|}{\makecell[l]{NOTE}}\\\\\n\
            \\hline\n\
        \\end{tabular}}\n\
    \\end{table}\n\
        \\end{document}')

    text = text.replace('DP-TR19A', project_name)
    text = text.replace('D0027', project_code)
    text = text.replace('2022/10/31', date)
    text = text.replace('40021D20A-1', part_number)
    text = text.replace('Trek', customer)

    text = text.replace('swv', sw_version)
    text = text.replace('hv', hw_version)
    text = text.replace('kv', kernel_version)
    text = text.replace('pv', parameter_version)
    text = text.replace('bv', bootloader_version)

    text = text.replace('person', owner)

    text = text.replace('KERNEL', kernel_hash256)
    text = text.replace('KP', kernel_project_hash256)
    text = text.replace('CODEBASE', codebase_hash256)

    text = text.replace('app_crc32', app_crc32)
    text = text.replace('btl_crc32', btl_crc32)
    text = text.replace('mrg_crc32', mrg_crc32)
    text = text.replace('bin_crc32', bin_crc32)

    text = text.replace('code_path', code_path)

    text = text.replace('NOTE',note)

    # 開啟文本檔，'w' 表示以寫入（write）模式打開
    with open('ReleaseNote.tex', 'w') as file:
        # 將字符串寫入文本檔
        file.write(text)

    print("Text has been written to output.txt.")




def app_open_file():
    file_paths = filedialog.askopenfilenames()
    global app_crc32
    if file_paths:
        app_crc32 = calculate_crc32(' '.join(file_paths))
        app_file_path.config(text="path：" + ' '.join(file_paths))

def btl_open_file():
    file_paths = filedialog.askopenfilenames()
    global btl_crc32
    if file_paths:
        btl_crc32 = calculate_crc32(' '.join(file_paths))
        btl_file_path.config(text="path：" + ' '.join(file_paths))


def mrg_open_file():
    file_paths = filedialog.askopenfilenames()
    global mrg_crc32
    if file_paths:
        mrg_crc32 = calculate_crc32(' '.join(file_paths))
        mrg_file_path.config(text="path：" + ' '.join(file_paths))

def bin_open_file():
    file_paths = filedialog.askopenfilenames()
    global bin_crc32
    if file_paths:
        bin_crc32 = calculate_crc32(' '.join(file_paths))
        bin_file_path.config(text="path：" + ' '.join(file_paths))


def calculate_crc32(file_path):
    # 使用 'rb' 模式以二進制讀取檔案
    with open(file_path, 'rb') as file:
        # 建立一個 CRC32 值的初始值
        crc32_value = 0

        # 以一小部分為單位計算 CRC32 值，適用於大檔案
        while True:
            data = file.read(8192)
            if not data:
                break
            crc32_value = zlib.crc32(data, crc32_value)

    # 將計算後的 CRC32 值轉換為正確的格式
    crc32_value = format(crc32_value & 0xFFFFFFFF, '08x')
    return crc32_value

def compile_tex():

    try:
        pdf_gen.config(text='LaTex is Building......')
        root.update()  # 强制刷新界面

        # 使用 pdflatex 编译 .tex 文件
        subprocess.run(["pdflatex", "ReleaseNote.tex"], check=True)
        pdf_gen.config(text='LaTeX compilation successful.')
        root.update()  # 强制刷新界面
        print("LaTeX compilation successful.")
    except subprocess.CalledProcessError as e:
        pdf_gen.config(text="LaTeX compilation failed. Error:")
        print("LaTeX compilation failed. Error:", e)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Build Release Note for Controller")
    entry_widgets = []
    app_crc32 = ''
    btl_crc32 = ''
    mrg_crc32 = ''
    bin_crc32 = ''
    label = tk.Label(root, text="FW Version")
    label.grid(row=1, column=0, padx=5, pady=5)

    entry = tk.Entry(root)
    entry.grid(row=1, column=1, padx=5, pady=5)
    entry_widgets.append(entry)


    label = tk.Label(root, text="HW Version")
    label.grid(row=2, column=0, padx=5, pady=5)

    entry = tk.Entry(root)
    entry.grid(row=2, column=1, padx=5, pady=5)
    entry_widgets.append(entry)

    label = tk.Label(root, text="Kernel Version")
    label.grid(row=3, column=0, padx=5, pady=5)

    entry = tk.Entry(root)
    entry.grid(row=3, column=1, padx=5, pady=5)
    entry_widgets.append(entry)

    label = tk.Label(root, text="Parameter Version")
    label.grid(row=4, column=0, padx=5, pady=5)

    entry = tk.Entry(root)
    entry.grid(row=4, column=1, padx=5, pady=5)
    entry_widgets.append(entry)

    label = tk.Label(root, text="Bootloader Version")
    label.grid(row=5, column=0, padx=5, pady=5)

    entry = tk.Entry(root)
    entry.grid(row=5, column=1, padx=5, pady=5)
    entry_widgets.append(entry)

    label = tk.Label(root, text="Project Name")
    label.grid(row=6, column=0, padx=5, pady=5)

    entry = tk.Entry(root)
    entry.grid(row=6, column=1, padx=5, pady=5)
    entry_widgets.append(entry)

    label = tk.Label(root, text="Project Code")
    label.grid(row=7, column=0, padx=5, pady=5)

    entry = tk.Entry(root)
    entry.grid(row=7, column=1, padx=5, pady=5)
    entry_widgets.append(entry)


    label = tk.Label(root, text="Date")
    label.grid(row=2, column=2, padx=5, pady=5)

    entry = tk.Entry(root)
    entry.grid(row=2, column=3, padx=5, pady=5)
    entry_widgets.append(entry)


    label = tk.Label(root, text="Part Number")
    label.grid(row=3, column=2, padx=5, pady=5)

    entry = tk.Entry(root)
    entry.grid(row=3, column=3, padx=5, pady=5)
    entry_widgets.append(entry)


    label = tk.Label(root, text="Customer")
    label.grid(row=4, column=2, padx=5, pady=5)

    entry = tk.Entry(root)
    entry.grid(row=4, column=3, padx=5, pady=5)
    entry_widgets.append(entry)


    label = tk.Label(root, text="kernel_hash256")
    label.grid(row=5, column=2, padx=5, pady=5)

    entry = tk.Entry(root)
    entry.grid(row=5, column=3, padx=5, pady=5)
    entry_widgets.append(entry)

    label = tk.Label(root, text="kernel_project_hash256")
    label.grid(row=6, column=2, padx=5, pady=5)

    entry = tk.Entry(root)
    entry.grid(row=6, column=3, padx=5, pady=5)
    entry_widgets.append(entry)

    label = tk.Label(root, text="code_base_hash256")
    label.grid(row=7, column=2, padx=5, pady=5)

    entry = tk.Entry(root)
    entry.grid(row=7, column=3, padx=5, pady=5)
    entry_widgets.append(entry)

    label = tk.Label(root, text="Owner")
    label.grid(row=8, column=0, padx=5, pady=5)

    entry = tk.Entry(root)
    entry.grid(row=8, column=1, padx=5, pady=5)
    entry_widgets.append(entry)

    label = tk.Label(root, text="Code Path")
    label.grid(row=8, column=2, padx=5, pady=5)

    entry = tk.Entry(root)
    entry.grid(row=8, column=3, padx=5, pady=5)
    entry_widgets.append(entry)


    label = tk.Label(root, text="Note\n(換行打兩個 '\\\\' 反斜線)")
    label.grid(row=1, column=2, padx=5, pady=5)

    entry = tk.Entry(root)
    entry.grid(row=1, column=3, padx=5, pady=5)
    entry_widgets.append(entry)




    submit_button = tk.Button(root, text="產出tex檔", command=show_variables)
    submit_button.grid(row=15, column=0, columnspan=2, padx=5, pady=10)

    result_label = tk.Label(root, text="")
    result_label.grid(row=16, column=0, columnspan=2, padx=5, pady=5)


    file_button = tk.Button(root, text="APP.hex", command=app_open_file)
    file_button.grid(row=17,column=0, padx=5, pady=5)

    app_file_path = tk.Label(root,text="")
    app_file_path.grid(row=17,column=1, padx=5, pady=5)

    file_button = tk.Button(root, text="BTL.hex", command=btl_open_file)
    file_button.grid(row=18,column=0, padx=5, pady=5)

    btl_file_path = tk.Label(root,text="")
    btl_file_path.grid(row=18,column=1, padx=5, pady=5)

    file_button = tk.Button(root, text="MRG.hex", command=mrg_open_file)
    file_button.grid(row=19,column=0, padx=5, pady=5)

    mrg_file_path = tk.Label(root,text="")
    mrg_file_path.grid(row=19,column=1, padx=5, pady=5)

    file_button = tk.Button(root, text="APP.bin", command=bin_open_file)
    file_button.grid(row=20,column=0, padx=5, pady=5)

    bin_file_path = tk.Label(root,text="")
    bin_file_path.grid(row=20,column=1, padx=5, pady=5)

    pdf_gen = tk.Label(root, text="")
    pdf_gen.grid(row=21, column=1, padx=5, pady=5)


    file_button = tk.Button(root, text="產出PDF", command=compile_tex)
    file_button.grid(row=15,column=1, padx=5, pady=10)




    root.mainloop()

