#include<iostream>
#include<string>
using namespace std;
int total_lectures = 0; //global variable to count total lectures
class Lecture_details
{
    private:
        string lecturer_name;
        string subject_name;
        string course_name;
    public:
        Lecture_details(){ //constructor to add initial values
        lecturer_name="Priyanka";
        subject_name="C++";
        course_name="Backend Programming";
        total_lectures++;
    }
    void add_lecture_details(){ //function to add lecture details
        cout << "Enter Lecturer Name: ";
        cin >> lecturer_name;
        cout << "Enter Subject Name: ";
        cin >> subject_name;
        cout << "Enter Course Name: ";
        cin >> course_name;
    }
    void display_lecture_details() { //function to display lecture details
        cout << "Lecturer Name: " << lecturer_name<< endl;
        cout << "Subject Name: " << subject_name<< endl;
        cout << "Course Name: " << course_name<< endl;
    }
    int getcount(){ //function to  get final count
        return total_lectures++;
    }
};
int main()
{
    //int size = 5;
    Lecture_details ld[5];
    for(int i=0;i<5;i++){
        cout<<"\n ---------- Enter details for Lecture "<< i + 1 <<" ------------\n";
        ld[i].add_lecture_details();
    }
    cout<<"\n ------------ Lecture Details ------------- \n";
    for(int i=0;i<5;i++){
        cout << "\nLecture " << i + 1 << ":\n";
        ld[i].display_lecture_details();
    }
    cout<<"\nTotal Lectures : "<< ld[0].getcount() <<endl;
    return 0;
}
