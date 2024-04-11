using System;
using System.Drawing;
public Size ClientSize { get; set; }
using System.Windows.Forms;
using static System.Net.Mime.MediaTypeNames;

public class ExampleForm : Form
{
    public ExampleForm()
    {
        // 設定表單的標題
        this.Text = "範例程式";

        // 設定表單的大小
        this.ClientSize = new Size(300, 200);

        // 建立一個按鈕
        Button button = new Button();
        button.Text = "顯示訊息方塊";
        button.Location = new Point(100, 100);
        button.Click += new EventHandler(this.Button_Click);

        // 將按鈕新增到表單上
        this.Controls.Add(button);
    }

    private void Button_Click(object sender, EventArgs e)
    {
        // 顯示一個訊息方塊
        MessageBox.Show("Hello, world!");
    }

    public static void Main(string[] args)
    {
        // 建立一個表單的執行個體
        Application.Run(new ExampleForm());
    }
}
