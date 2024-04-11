using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    public partial class wheel : Form
    {
        struct input
        {
            public double slope;
            public double bike_weight;
            public double person_weight;
            public double handbar_width;
            public double bike_height;
            public double bike_speed;
            public double air_density;
            public double wind_factor;
            public double wind_area_factor;
            public double friction_factor;
            public double wheel_diameter;
            public double temperature;

        }

        struct output
        {
            public double wheel_diameter_km;
            public double slope_degree;
            public double total_weight;
            public double gravity;
            public double area;
            public double wheel_radius;
            public double bike_speed_ms;
            public double wind_N;
            public double gravity_N;
            public double friction_N;
            public double total_N;
            public double Torque;
            public double require_rpm;
            public double require_motor_speed;
        }

        input input_info = new input();
        output output_info = new output { gravity = 9.8 };
        public wheel()
        {
            InitializeComponent();
            //this.Icon = new Icon("D:\\ChrisLee\\personal\\Chris\\Personal Git\\Code\\python_personal\\WindowsFormsApp1\\Logo_black.ico");
        }
        private void show()
        {

            double angle = Math.Atan((double)input_info.slope / 100);
            // 將弧度轉換為度

            output_info.wheel_radius = input_info.wheel_diameter * ((25.4 / 2 )/ 1000);
            output_info.wheel_diameter_km = output_info.wheel_radius * 2 * Math.PI / 1000;
            output_info.total_weight = input_info.bike_weight + input_info.person_weight;
            output_info.gravity = 9.8;
            output_info.area = input_info.handbar_width * input_info.bike_height * input_info.wind_area_factor;
            output_info.bike_speed_ms = input_info.bike_speed * 1000 / 60 / 60;
            output_info.wind_N = 0.5 * output_info.area * input_info.air_density * Math.Pow(output_info.bike_speed_ms, 2) * input_info.wind_factor; 
            output_info.slope_degree = angle * 180 / Math.PI;
            output_info.gravity_N = output_info.total_weight * output_info.gravity * Math.Sin(angle);
            output_info.friction_N = input_info.friction_factor * output_info.total_weight * output_info.gravity * Math.Cos(angle);
            output_info.total_N = output_info.wind_N + output_info.gravity_N + output_info.friction_N;
            output_info.Torque = output_info.total_N * output_info.wheel_radius;
            output_info.require_motor_speed = input_info.bike_speed / output_info.wheel_diameter_km / 60;
            chris.Text = String.Format("Created by ChrisLee ", "");
            wind_load.Text = String.Format("風阻力: {0} N", output_info.wind_N.ToString("F2")); 
            gravity_load.Text = String.Format("重力: {0}N", output_info.gravity_N.ToString("F2"));
            fraction_load.Text = String.Format("摩擦力: {0}N", output_info.friction_N.ToString("F2"));
            Torque.Text = String.Format("扭力: {0}Nm", output_info.Torque.ToString("F2"));
            motor_speed.Text = String.Format("馬達需求轉速: {0} RPM", output_info.require_motor_speed.ToString("F2"));

        }
        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void ClickThis_Click(object sender, EventArgs e)
        {
            chris.Text = "Hello World";
        }

        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {
            bool test = double.TryParse(wheelD_box.Text, out input_info.wheel_diameter);
            if (test)
            {
                show();
            }
            else
            {
                chris.Text = "Please Inupt number";
            }
        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void label4_Click(object sender, EventArgs e)
        {

        }

        private void hidth_TextChanged(object sender, EventArgs e)
        {
            bool test = double.TryParse(hidth_box.Text, out input_info.bike_height);
            if (test)
            {
                show();
            }
            else
            {
                chris.Text = "Please Inupt number";
            }
        }

        private void label4_Click_1(object sender, EventArgs e)
        {

        }

        private void richTextBox1_TextChanged_1(object sender, EventArgs e)
        {
            bool test = double.TryParse(BikeSpeed_box.Text, out input_info.bike_speed);
            if (test)
            {
                output_info.bike_speed_ms = input_info.bike_speed *1000 / 60 / 60;
                show();
            }
            else
            {
                chris.Text = "Please Inupt number";
            }

        }

        private void label14_Click(object sender, EventArgs e)
        {

        }

        private void wheel_label_Click(object sender, EventArgs e)
        {

        }

        private void label4_Click_2(object sender, EventArgs e)
        {

        }

        private void label18_Click(object sender, EventArgs e)
        {

        }

        private void richTextBox1_TextChanged_2(object sender, EventArgs e)
        {
            bool test = double.TryParse(friction_factor_box.Text, out input_info.friction_factor);
            if (test)
            {
                show();
            }
            else
            {
                chris.Text = "Please Inupt number";
            }
        }

        private void richTextBox4_TextChanged(object sender, EventArgs e)
        {
            bool test = double.TryParse(slope_box.Text, out input_info.slope);
            if (test)
            {

                show();
            }
            else
            {
                chris.Text = "Please Inupt number";
            }
        }

        private void bikeweight_box_TextChanged(object sender, EventArgs e)
        {
            bool test = double.TryParse(bikeweight_box.Text, out input_info.bike_weight);
            if (test)
            {
                show();
            }
            else
            {
                chris.Text = "Please Inupt number";
            }
        }

        private void personweight_box_TextChanged(object sender, EventArgs e)
        {
            bool test = double.TryParse(personweight_box.Text, out input_info.person_weight);
            if (test)
            {
                show();
            }
            else
            {
                chris.Text = "Please Inupt number";
            }
        }

        private void handbarwidth_box_TextChanged(object sender, EventArgs e)
        {
            bool test = double.TryParse(handbarwidth_box.Text, out input_info.handbar_width);
            if (test)
            {
                show();
            }
            else
            {
                chris.Text = "Please Inupt number";
            }
        }

        private void air_density_box_TextChanged(object sender, EventArgs e)
        {
            bool test = double.TryParse(air_density_box.Text, out input_info.air_density);
            if (test)
            {
                show();
            }
            else
            {
                chris.Text = "Please Inupt number";
            }
        }

        private void wind_factor_box_TextChanged(object sender, EventArgs e)
        {
            bool test = double.TryParse(wind_factor_box.Text, out input_info.wind_factor);
            if (test)
            {
                show();
            }
            else
            {
                chris.Text = "Please Inupt number";
            }
        }

        private void wind_area_factor_box_TextChanged(object sender, EventArgs e)
        {
            bool test = double.TryParse(wind_area_factor_box.Text, out input_info.wind_area_factor);
            if (test)
            {
                show();
            }
            else
            {
                chris.Text = "Please Inupt number";
            }
        }


    }
}
