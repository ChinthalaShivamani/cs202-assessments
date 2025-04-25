using System;
using System.Drawing;
using System.Windows.Forms;

namespace Lab12_windowsapp
{
    public partial class Form1 : Form
    {
        private TextBox timeInput;
        private Button startButton;
        private Timer checkTimer;
        private Timer colorTimer;
        private TimeSpan targetTime;
        private Random rand;

        public Form1()
        {
            InitializeComponent();
            
            timeInput = new TextBox { Location = new Point(39, 30), Width = 200 };
            startButton = new Button { Text = "Start", Location = new Point(250, 30) };
            startButton.Click += StartButton_Click;
            
            this.Controls.Add(timeInput);
            this.Controls.Add(startButton);
            
            checkTimer = new Timer { Interval = 1000 };
            checkTimer.Tick += CheckTimer_Tick;
            
            colorTimer = new Timer { Interval = 1000 };
            colorTimer.Tick += ColorTimer_Tick;
            
            rand = new Random();
        }
                private void StartButton_Click(object sender, EventArgs e)
        {
            if (TimeSpan.TryParse(timeInput.Text, out targetTime))
            {
                checkTimer.Start();
                colorTimer.Start();
            }
            else
            {
                MessageBox.Show("Invalid time format. Use HH:MM:SS");
            }
        }

        private void CheckTimer_Tick(object sender, EventArgs e)
        {
            TimeSpan current = DateTime.Now.TimeOfDay;
            if (current.Hours == targetTime.Hours &&
                current.Minutes == targetTime.Minutes &&
                current.Seconds == targetTime.Seconds)
            {
                checkTimer.Stop();
                colorTimer.Stop();
                MessageBox.Show($"Alarm! Time is up: {targetTime.ToString(@"hh\:mm\:ss")}");
            }
        }

        private void ColorTimer_Tick(object sender, EventArgs e)
        {
            this.BackColor = Color.FromArgb(rand.Next(256), rand.Next(256), rand.Next(256));
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // Optional: Any actions you want on form load
        }
    }
}