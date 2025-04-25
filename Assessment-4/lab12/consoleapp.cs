using System;
using System.Threading;

public class AlarmClock
{
    public delegate void AlarmHandler();
    public event AlarmHandler raiseAlarm;

    private TimeSpan targetTime;

    public void SetTime(string inputTime)
    {
        if (TimeSpan.TryParse(inputTime, out targetTime))
        {
            Console.WriteLine("Alarm set for: " + targetTime);
            StartChecking();
        }
        else
        {
            Console.WriteLine("Invalid time format.");
        }
    }

    private void StartChecking()
    {
        while (true)
        {
            TimeSpan currentTime = DateTime.Now.TimeOfDay;
            Console.WriteLine("Current Time: " + currentTime.ToString(@"hh\:mm\:ss"));
            if (currentTime.Hours == targetTime.Hours &&
                currentTime.Minutes == targetTime.Minutes &&
                currentTime.Seconds == targetTime.Seconds)
            {
                raiseAlarm?.Invoke();
                break;
            }
            Thread.Sleep(1000);
        }
    }

    public void RingAlarm()
    {
        Console.WriteLine("Alarm! It's now " + targetTime);
    }
}

public static class Program
{
    public static void Main()
    {
        AlarmClock alarm = new AlarmClock();
        alarm.raiseAlarm += alarm.RingAlarm;

        Console.Write("Enter time (HH:MM:SS): ");
        string input = Console.ReadLine();
        alarm.SetTime(input);
    }
}
