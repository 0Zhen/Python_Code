namespace WindowsFormsApp1
{
    partial class wheel
    {
        /// <summary>
        /// 設計工具所需的變數。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清除任何使用中的資源。
        /// </summary>
        /// <param name="disposing">如果應該處置受控資源則為 true，否則為 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form 設計工具產生的程式碼

        /// <summary>
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器修改
        /// 這個方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.chris = new System.Windows.Forms.Label();
            this.wheelD_box = new System.Windows.Forms.RichTextBox();
            this.wheellabel = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.handbarwidth = new System.Windows.Forms.Label();
            this.handbarwidth_box = new System.Windows.Forms.RichTextBox();
            this.label5 = new System.Windows.Forms.Label();
            this.hidth_label = new System.Windows.Forms.Label();
            this.hidth_box = new System.Windows.Forms.RichTextBox();
            this.label7 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.bikespeedlabel = new System.Windows.Forms.Label();
            this.BikeSpeed_box = new System.Windows.Forms.RichTextBox();
            this.label6 = new System.Windows.Forms.Label();
            this.label8 = new System.Windows.Forms.Label();
            this.Personweightlabel = new System.Windows.Forms.Label();
            this.personweight_box = new System.Windows.Forms.RichTextBox();
            this.label9 = new System.Windows.Forms.Label();
            this.label10 = new System.Windows.Forms.Label();
            this.bikeweightlabel = new System.Windows.Forms.Label();
            this.bikeweight_box = new System.Windows.Forms.RichTextBox();
            this.label12 = new System.Windows.Forms.Label();
            this.label13 = new System.Windows.Forms.Label();
            this.label15 = new System.Windows.Forms.Label();
            this.slopelabel = new System.Windows.Forms.Label();
            this.slope_box = new System.Windows.Forms.RichTextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.air_density_box = new System.Windows.Forms.RichTextBox();
            this.label4 = new System.Windows.Forms.Label();
            this.label11 = new System.Windows.Forms.Label();
            this.wind_factor_box = new System.Windows.Forms.RichTextBox();
            this.label16 = new System.Windows.Forms.Label();
            this.label17 = new System.Windows.Forms.Label();
            this.wind_area_factor_box = new System.Windows.Forms.RichTextBox();
            this.label18 = new System.Windows.Forms.Label();
            this.friction_factor_box = new System.Windows.Forms.RichTextBox();
            this.wind_load = new System.Windows.Forms.Label();
            this.gravity_load = new System.Windows.Forms.Label();
            this.fraction_load = new System.Windows.Forms.Label();
            this.Torque = new System.Windows.Forms.Label();
            this.motor_speed = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // chris
            // 
            this.chris.AutoSize = true;
            this.chris.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.chris.Location = new System.Drawing.Point(713, 421);
            this.chris.Name = "chris";
            this.chris.Size = new System.Drawing.Size(152, 20);
            this.chris.TabIndex = 1;
            this.chris.Text = "Create by ChrisLee";
            this.chris.Click += new System.EventHandler(this.label1_Click);
            // 
            // wheelD_box
            // 
            this.wheelD_box.Font = new System.Drawing.Font("微軟正黑體", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.wheelD_box.Location = new System.Drawing.Point(121, 180);
            this.wheelD_box.Name = "wheelD_box";
            this.wheelD_box.Size = new System.Drawing.Size(81, 30);
            this.wheelD_box.TabIndex = 2;
            this.wheelD_box.Text = "";
            this.wheelD_box.TextChanged += new System.EventHandler(this.richTextBox1_TextChanged);
            // 
            // wheellabel
            // 
            this.wheellabel.AutoSize = true;
            this.wheellabel.Font = new System.Drawing.Font("微軟正黑體", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.wheellabel.Location = new System.Drawing.Point(122, 162);
            this.wheellabel.Name = "wheellabel";
            this.wheellabel.Size = new System.Drawing.Size(64, 19);
            this.wheellabel.TabIndex = 3;
            this.wheellabel.Text = "輪徑(吋)";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("微軟正黑體", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label3.Location = new System.Drawing.Point(25, 245);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(0, 19);
            this.label3.TabIndex = 7;
            // 
            // handbarwidth
            // 
            this.handbarwidth.AutoSize = true;
            this.handbarwidth.Font = new System.Drawing.Font("微軟正黑體", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.handbarwidth.Location = new System.Drawing.Point(22, 164);
            this.handbarwidth.Name = "handbarwidth";
            this.handbarwidth.Size = new System.Drawing.Size(78, 19);
            this.handbarwidth.TabIndex = 6;
            this.handbarwidth.Text = "把手寬(m)";
            this.handbarwidth.Click += new System.EventHandler(this.label4_Click);
            // 
            // handbarwidth_box
            // 
            this.handbarwidth_box.Font = new System.Drawing.Font("微軟正黑體", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.handbarwidth_box.Location = new System.Drawing.Point(25, 182);
            this.handbarwidth_box.Name = "handbarwidth_box";
            this.handbarwidth_box.Size = new System.Drawing.Size(80, 30);
            this.handbarwidth_box.TabIndex = 5;
            this.handbarwidth_box.Text = "";
            this.handbarwidth_box.TextChanged += new System.EventHandler(this.handbarwidth_box_TextChanged);
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(122, 391);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(0, 15);
            this.label5.TabIndex = 11;
            // 
            // hidth_label
            // 
            this.hidth_label.AutoSize = true;
            this.hidth_label.Font = new System.Drawing.Font("微軟正黑體", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.hidth_label.Location = new System.Drawing.Point(22, 218);
            this.hidth_label.Name = "hidth_label";
            this.hidth_label.Size = new System.Drawing.Size(78, 19);
            this.hidth_label.TabIndex = 10;
            this.hidth_label.Text = "人車高(m)";
            // 
            // hidth_box
            // 
            this.hidth_box.Font = new System.Drawing.Font("微軟正黑體", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.hidth_box.Location = new System.Drawing.Point(25, 236);
            this.hidth_box.Name = "hidth_box";
            this.hidth_box.Size = new System.Drawing.Size(80, 30);
            this.hidth_box.TabIndex = 9;
            this.hidth_box.Text = "";
            this.hidth_box.TextChanged += new System.EventHandler(this.hidth_TextChanged);
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Font = new System.Drawing.Font("微軟正黑體", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label7.Location = new System.Drawing.Point(26, 218);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(0, 19);
            this.label7.TabIndex = 8;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("微軟正黑體", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.Location = new System.Drawing.Point(25, 290);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(0, 19);
            this.label1.TabIndex = 16;
            // 
            // bikespeedlabel
            // 
            this.bikespeedlabel.AutoSize = true;
            this.bikespeedlabel.Font = new System.Drawing.Font("微軟正黑體", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bikespeedlabel.Location = new System.Drawing.Point(22, 269);
            this.bikespeedlabel.Name = "bikespeedlabel";
            this.bikespeedlabel.Size = new System.Drawing.Size(116, 19);
            this.bikespeedlabel.TabIndex = 15;
            this.bikespeedlabel.Text = "車輛速度(km/h)";
            this.bikespeedlabel.Click += new System.EventHandler(this.label4_Click_1);
            // 
            // BikeSpeed_box
            // 
            this.BikeSpeed_box.Font = new System.Drawing.Font("微軟正黑體", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.BikeSpeed_box.Location = new System.Drawing.Point(25, 287);
            this.BikeSpeed_box.Name = "BikeSpeed_box";
            this.BikeSpeed_box.Size = new System.Drawing.Size(80, 30);
            this.BikeSpeed_box.TabIndex = 14;
            this.BikeSpeed_box.Text = "";
            this.BikeSpeed_box.TextChanged += new System.EventHandler(this.richTextBox1_TextChanged_1);
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Font = new System.Drawing.Font("微軟正黑體", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label6.Location = new System.Drawing.Point(25, 290);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(0, 19);
            this.label6.TabIndex = 13;
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Font = new System.Drawing.Font("微軟正黑體", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label8.Location = new System.Drawing.Point(122, 376);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(0, 19);
            this.label8.TabIndex = 12;
            // 
            // Personweightlabel
            // 
            this.Personweightlabel.AutoSize = true;
            this.Personweightlabel.Font = new System.Drawing.Font("微軟正黑體", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.Personweightlabel.Location = new System.Drawing.Point(22, 108);
            this.Personweightlabel.Name = "Personweightlabel";
            this.Personweightlabel.Size = new System.Drawing.Size(68, 19);
            this.Personweightlabel.TabIndex = 29;
            this.Personweightlabel.Text = "人重(Kg)";
            this.Personweightlabel.Click += new System.EventHandler(this.label4_Click_2);
            // 
            // personweight_box
            // 
            this.personweight_box.Font = new System.Drawing.Font("微軟正黑體", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.personweight_box.Location = new System.Drawing.Point(25, 126);
            this.personweight_box.Name = "personweight_box";
            this.personweight_box.Size = new System.Drawing.Size(80, 30);
            this.personweight_box.TabIndex = 28;
            this.personweight_box.Text = "";
            this.personweight_box.TextChanged += new System.EventHandler(this.personweight_box_TextChanged);
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Font = new System.Drawing.Font("微軟正黑體", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label9.Location = new System.Drawing.Point(25, 129);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(0, 19);
            this.label9.TabIndex = 27;
            // 
            // label10
            // 
            this.label10.AutoSize = true;
            this.label10.Font = new System.Drawing.Font("微軟正黑體", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label10.Location = new System.Drawing.Point(28, 159);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(0, 19);
            this.label10.TabIndex = 26;
            // 
            // bikeweightlabel
            // 
            this.bikeweightlabel.AutoSize = true;
            this.bikeweightlabel.Font = new System.Drawing.Font("微軟正黑體", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bikeweightlabel.Location = new System.Drawing.Point(22, 57);
            this.bikeweightlabel.Name = "bikeweightlabel";
            this.bikeweightlabel.Size = new System.Drawing.Size(68, 19);
            this.bikeweightlabel.TabIndex = 25;
            this.bikeweightlabel.Text = "車重(Kg)";
            this.bikeweightlabel.Click += new System.EventHandler(this.wheel_label_Click);
            // 
            // bikeweight_box
            // 
            this.bikeweight_box.Font = new System.Drawing.Font("微軟正黑體", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bikeweight_box.Location = new System.Drawing.Point(25, 75);
            this.bikeweight_box.Name = "bikeweight_box";
            this.bikeweight_box.Size = new System.Drawing.Size(80, 30);
            this.bikeweight_box.TabIndex = 24;
            this.bikeweight_box.Text = "";
            this.bikeweight_box.TextChanged += new System.EventHandler(this.bikeweight_box_TextChanged);
            // 
            // label12
            // 
            this.label12.AutoSize = true;
            this.label12.Font = new System.Drawing.Font("微軟正黑體", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label12.Location = new System.Drawing.Point(25, 54);
            this.label12.Name = "label12";
            this.label12.Size = new System.Drawing.Size(0, 19);
            this.label12.TabIndex = 23;
            // 
            // label13
            // 
            this.label13.AutoSize = true;
            this.label13.Font = new System.Drawing.Font("微軟正黑體", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label13.Location = new System.Drawing.Point(25, 84);
            this.label13.Name = "label13";
            this.label13.Size = new System.Drawing.Size(0, 19);
            this.label13.TabIndex = 22;
            // 
            // label15
            // 
            this.label15.AutoSize = true;
            this.label15.Font = new System.Drawing.Font("微軟正黑體", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label15.Location = new System.Drawing.Point(122, 211);
            this.label15.Name = "label15";
            this.label15.Size = new System.Drawing.Size(0, 19);
            this.label15.TabIndex = 19;
            // 
            // slopelabel
            // 
            this.slopelabel.AutoSize = true;
            this.slopelabel.Font = new System.Drawing.Font("微軟正黑體", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.slopelabel.Location = new System.Drawing.Point(25, 9);
            this.slopelabel.Name = "slopelabel";
            this.slopelabel.Size = new System.Drawing.Size(62, 19);
            this.slopelabel.TabIndex = 18;
            this.slopelabel.Text = "坡度(%)";
            // 
            // slope_box
            // 
            this.slope_box.Font = new System.Drawing.Font("微軟正黑體", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.slope_box.Location = new System.Drawing.Point(25, 24);
            this.slope_box.Name = "slope_box";
            this.slope_box.Size = new System.Drawing.Size(80, 30);
            this.slope_box.TabIndex = 17;
            this.slope_box.Text = "";
            this.slope_box.TextChanged += new System.EventHandler(this.richTextBox4_TextChanged);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("微軟正黑體", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label2.Location = new System.Drawing.Point(25, 320);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(137, 19);
            this.label2.TabIndex = 32;
            this.label2.Text = "空氣密度(kg/m^3)";
            // 
            // air_density_box
            // 
            this.air_density_box.Font = new System.Drawing.Font("微軟正黑體", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.air_density_box.Location = new System.Drawing.Point(25, 343);
            this.air_density_box.Name = "air_density_box";
            this.air_density_box.Size = new System.Drawing.Size(80, 30);
            this.air_density_box.TabIndex = 31;
            this.air_density_box.Text = "";
            this.air_density_box.TextChanged += new System.EventHandler(this.air_density_box_TextChanged);
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Font = new System.Drawing.Font("微軟正黑體", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label4.Location = new System.Drawing.Point(25, 313);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(0, 19);
            this.label4.TabIndex = 30;
            // 
            // label11
            // 
            this.label11.AutoSize = true;
            this.label11.Font = new System.Drawing.Font("微軟正黑體", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label11.Location = new System.Drawing.Point(122, 9);
            this.label11.Name = "label11";
            this.label11.Size = new System.Drawing.Size(69, 19);
            this.label11.TabIndex = 35;
            this.label11.Text = "風阻係數";
            // 
            // wind_factor_box
            // 
            this.wind_factor_box.Font = new System.Drawing.Font("微軟正黑體", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.wind_factor_box.Location = new System.Drawing.Point(125, 27);
            this.wind_factor_box.Name = "wind_factor_box";
            this.wind_factor_box.Size = new System.Drawing.Size(80, 30);
            this.wind_factor_box.TabIndex = 34;
            this.wind_factor_box.Text = "";
            this.wind_factor_box.TextChanged += new System.EventHandler(this.wind_factor_box_TextChanged);
            // 
            // label16
            // 
            this.label16.AutoSize = true;
            this.label16.Font = new System.Drawing.Font("微軟正黑體", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label16.Location = new System.Drawing.Point(136, 2);
            this.label16.Name = "label16";
            this.label16.Size = new System.Drawing.Size(0, 19);
            this.label16.TabIndex = 33;
            // 
            // label17
            // 
            this.label17.AutoSize = true;
            this.label17.Font = new System.Drawing.Font("微軟正黑體", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label17.Location = new System.Drawing.Point(122, 60);
            this.label17.Name = "label17";
            this.label17.Size = new System.Drawing.Size(99, 19);
            this.label17.TabIndex = 37;
            this.label17.Text = "迎風面積係數";
            // 
            // wind_area_factor_box
            // 
            this.wind_area_factor_box.Font = new System.Drawing.Font("微軟正黑體", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.wind_area_factor_box.Location = new System.Drawing.Point(121, 78);
            this.wind_area_factor_box.Name = "wind_area_factor_box";
            this.wind_area_factor_box.Size = new System.Drawing.Size(81, 30);
            this.wind_area_factor_box.TabIndex = 36;
            this.wind_area_factor_box.Text = "";
            this.wind_area_factor_box.TextChanged += new System.EventHandler(this.wind_area_factor_box_TextChanged);
            // 
            // label18
            // 
            this.label18.AutoSize = true;
            this.label18.Font = new System.Drawing.Font("微軟正黑體", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label18.Location = new System.Drawing.Point(122, 111);
            this.label18.Name = "label18";
            this.label18.Size = new System.Drawing.Size(144, 19);
            this.label18.TabIndex = 39;
            this.label18.Text = "接觸面滾動摩擦係數";
            this.label18.Click += new System.EventHandler(this.label18_Click);
            // 
            // friction_factor_box
            // 
            this.friction_factor_box.Font = new System.Drawing.Font("微軟正黑體", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.friction_factor_box.Location = new System.Drawing.Point(121, 129);
            this.friction_factor_box.Name = "friction_factor_box";
            this.friction_factor_box.Size = new System.Drawing.Size(81, 30);
            this.friction_factor_box.TabIndex = 38;
            this.friction_factor_box.Text = "";
            this.friction_factor_box.TextChanged += new System.EventHandler(this.richTextBox1_TextChanged_2);
            // 
            // wind_load
            // 
            this.wind_load.AutoSize = true;
            this.wind_load.Font = new System.Drawing.Font("微軟正黑體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.wind_load.Location = new System.Drawing.Point(454, 55);
            this.wind_load.Name = "wind_load";
            this.wind_load.Size = new System.Drawing.Size(80, 25);
            this.wind_load.TabIndex = 40;
            this.wind_load.Text = "風阻(N)";
            // 
            // gravity_load
            // 
            this.gravity_load.AutoSize = true;
            this.gravity_load.Font = new System.Drawing.Font("微軟正黑體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.gravity_load.Location = new System.Drawing.Point(454, 111);
            this.gravity_load.Name = "gravity_load";
            this.gravity_load.Size = new System.Drawing.Size(80, 25);
            this.gravity_load.TabIndex = 41;
            this.gravity_load.Text = "重力(N)";
            // 
            // fraction_load
            // 
            this.fraction_load.AutoSize = true;
            this.fraction_load.Font = new System.Drawing.Font("微軟正黑體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.fraction_load.Location = new System.Drawing.Point(453, 164);
            this.fraction_load.Name = "fraction_load";
            this.fraction_load.Size = new System.Drawing.Size(100, 25);
            this.fraction_load.TabIndex = 42;
            this.fraction_load.Text = "摩擦力(N)";
            // 
            // Torque
            // 
            this.Torque.AutoSize = true;
            this.Torque.Font = new System.Drawing.Font("微軟正黑體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.Torque.Location = new System.Drawing.Point(453, 224);
            this.Torque.Name = "Torque";
            this.Torque.Size = new System.Drawing.Size(99, 25);
            this.Torque.TabIndex = 43;
            this.Torque.Text = "扭力(Nm)";
            // 
            // motor_speed
            // 
            this.motor_speed.AutoSize = true;
            this.motor_speed.Font = new System.Drawing.Font("微軟正黑體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.motor_speed.Location = new System.Drawing.Point(454, 284);
            this.motor_speed.Name = "motor_speed";
            this.motor_speed.Size = new System.Drawing.Size(188, 25);
            this.motor_speed.TabIndex = 44;
            this.motor_speed.Text = "馬達需求轉速(RPM)";
            // 
            // wheel
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ControlLightLight;
            this.ClientSize = new System.Drawing.Size(883, 450);
            this.Controls.Add(this.motor_speed);
            this.Controls.Add(this.Torque);
            this.Controls.Add(this.fraction_load);
            this.Controls.Add(this.gravity_load);
            this.Controls.Add(this.wind_load);
            this.Controls.Add(this.label18);
            this.Controls.Add(this.friction_factor_box);
            this.Controls.Add(this.label17);
            this.Controls.Add(this.wind_area_factor_box);
            this.Controls.Add(this.label11);
            this.Controls.Add(this.wind_factor_box);
            this.Controls.Add(this.label16);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.air_density_box);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.Personweightlabel);
            this.Controls.Add(this.personweight_box);
            this.Controls.Add(this.label9);
            this.Controls.Add(this.label10);
            this.Controls.Add(this.bikeweightlabel);
            this.Controls.Add(this.bikeweight_box);
            this.Controls.Add(this.label12);
            this.Controls.Add(this.label13);
            this.Controls.Add(this.label15);
            this.Controls.Add(this.slopelabel);
            this.Controls.Add(this.slope_box);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.bikespeedlabel);
            this.Controls.Add(this.BikeSpeed_box);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.label8);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.hidth_label);
            this.Controls.Add(this.hidth_box);
            this.Controls.Add(this.label7);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.handbarwidth);
            this.Controls.Add(this.handbarwidth_box);
            this.Controls.Add(this.wheellabel);
            this.Controls.Add(this.wheelD_box);
            this.Controls.Add(this.chris);
            this.Name = "wheel";
            this.Text = "電輔車附載分析";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.Label chris;
        private System.Windows.Forms.RichTextBox wheelD_box;
        private System.Windows.Forms.Label wheellabel;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label handbarwidth;
        private System.Windows.Forms.RichTextBox handbarwidth_box;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label hidth_label;
        private System.Windows.Forms.RichTextBox hidth_box;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label bikespeedlabel;
        private System.Windows.Forms.RichTextBox BikeSpeed_box;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.Label Personweightlabel;
        private System.Windows.Forms.RichTextBox personweight_box;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.Label label10;
        private System.Windows.Forms.Label bikeweightlabel;
        private System.Windows.Forms.RichTextBox bikeweight_box;
        private System.Windows.Forms.Label label12;
        private System.Windows.Forms.Label label13;
        private System.Windows.Forms.Label label15;
        private System.Windows.Forms.Label slopelabel;
        private System.Windows.Forms.RichTextBox slope_box;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.RichTextBox air_density_box;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label11;
        private System.Windows.Forms.RichTextBox wind_factor_box;
        private System.Windows.Forms.Label label16;
        private System.Windows.Forms.Label label17;
        private System.Windows.Forms.RichTextBox wind_area_factor_box;
        private System.Windows.Forms.Label label18;
        private System.Windows.Forms.RichTextBox friction_factor_box;
        private System.Windows.Forms.Label wind_load;
        private System.Windows.Forms.Label gravity_load;
        private System.Windows.Forms.Label fraction_load;
        private System.Windows.Forms.Label Torque;
        private System.Windows.Forms.Label motor_speed;
    }
}

