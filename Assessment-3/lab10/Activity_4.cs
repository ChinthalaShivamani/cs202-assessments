using System;

class Student
{
    // Properties
    public string Name { get; set; }
    public string ID { get; set; }
    public double Marks { get; set; }

    // Constructor
    public Student(string name, string id, double marks)
    {
        Name = name;
        ID = id;
        Marks = marks;
    }

    // Copy constructor
    public Student(Student other)
    {
        Name = other.Name;
        ID = other.ID;
        Marks = other.Marks;
    }

    // Method to get grade
    public char GetGrade()
    {
        if (Marks >= 90) return 'A';
        else if (Marks >= 80) return 'B';
        else if (Marks >= 70) return 'C';
        else if (Marks >= 60) return 'D';
        else return 'F';
    }

    // Main method
    public static void Main()
    {
        Student student1 = new Student("Alice", "S001", 85.5);
        Console.WriteLine($"Student: {student1.Name}, ID: {student1.ID}, Marks: {student1.Marks}, Grade: {student1.GetGrade()}");

        // Using copy constructor
        Student student2 = new Student(student1);
        student2.Name = "Bob";
        Console.WriteLine($"Student: {student2.Name}, ID: {student2.ID}, Marks: {student2.Marks}, Grade: {student2.GetGrade()}");
    }
}

class StudentIIIGN : Student
{
    // Additional property
    public string Hostel_Name_IIIGN { get; set; }

    // Constructor
    public StudentIIIGN(string name, string id, double marks, string hostel) 
        : base(name, id, marks)
    {
        Hostel_Name_IIIGN = hostel;
    }

    // Main method in derived class
    public static new void Main()
    {
        StudentIIIGN iiignStudent = new StudentIIIGN("Charlie", "S002", 92.0, "Gandhi Hostel");
        Console.WriteLine($"IIIGN Student: {iiignStudent.Name}, Hostel: {iiignStudent.Hostel_Name_IIIGN}, Grade: {iiignStudent.GetGrade()}");
    }
}