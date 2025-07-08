#include<stdio.h>
#include<string.h>
int main()
{
    int choice,len,c;
    char s[50],str2[50],rev_str[50];
do{
    printf("\n\n");
    printf("Main Menu \n");
    printf("        1.String Length\n");
    printf("        2.String Copy\n");
    printf("        3.String Concatenation\n");
    printf("        4.String Reverse\n");
    printf("        5.String Palindrome\n");
    printf("        6.Frequency of Character in s string \n");
    printf("        7.Find number of vowels and consonants \n");
    printf("        8.Find number of blank spaces and digits\n");
    printf("\n");
    printf("Please Enter your choice: ");
    scanf("%d",&choice);
    printf("\n");
    switch(choice)
    {
    case 1:
        printf("Please Enter the String: ");
        scanf("%s",&s);
        len=strlen(s);
        printf("        ------Length of String is : %d\n ",len);
        break;
    case 2:
        printf("Please Enter the source String: ");
        scanf("%s",&s);
        strcpy(str2,s);
        printf("        ------Copied string: %s\n", str2);
        break;
    case 3:
        printf("Please Enter first String: ");
        scanf("%s",&s);
        printf("Please Enter second String: ");
        scanf("%s",&str2);
        strcat(str2,s);
        printf("        ------Concatenated string: %s\n",str2);
        break;
    case 4:
        printf("Please Enter the String: ");
        scanf("%s",&s);
        strrev(s);
        printf("        ------Reversed string: %s\n",s);
        break;
    case 5:
        printf("Please Enter the String: ");
        scanf("%s",&s);
        int is_palindrome = 1;
        len=strlen(s);
        for(int i=0;i<len/2;i++)//loop starts from i=0 to middle of string so len/2.
            {
                if(s[i] != s[len-1-i])//s[i] for character start & s[len-1-i] for character end
                {
                    is_palindrome = 0;
                }
            }
            if (is_palindrome)
                {
                    printf("        ------\"%s\" is a palindrome string.\n", s);//for 0 this is printed
                } else {
                    printf("        ------\"%s\" is not a palindrome string.\n", s);//for 1 this is printed
                }
        break;
    case 6:
        int count=0;
        char ch;
        printf("Please Enter the String: ");
        scanf("%s",&s);
        int len = strlen(s);
        printf("\nEnter the character to find its frequency: ");
        scanf(" %c",&ch);
        for(int i=0;i<len;i++)
        {
            if(s[i] == ch)
            {
                count++;  // if match found, increase count
            }
        }
        printf("\n      ------The frequency of character '%c' is: %d\n",ch,count);
        break;
    case 7:
        int vowels=0,consonants=0;
        printf("Please Enter the String: ");
        scanf(" %[^\n]",&s);
        for(int i=0;s[i]!='\0';i++)
        {
            if(s[i]=='a' || s[i]=='e' || s[i]=='i' || s[i]=='o' || s[i]=='u' ||
               s[i]=='A' || s[i]=='E' || s[i]=='I' || s[i]=='O' || s[i]=='U')
            {
                vowels++;
            }
            else if ((s[i]>='A' && s[i]<='Z') || (s[i]>='a' &&s[i]<='z'))
            {
                consonants++;
            }

        }
        printf("\n      ------Vowels in the entered string is : %d\n",vowels);
        printf("\n      ------Consonants in the entered string is : %d",consonants);
        break;
    case 8:
        int digits=0,spaces=0;
        printf("Please Enter the String: ");
        scanf(" %[^\n]",&s);
        for(int i=0;s[i]!='\0';i++)
        {
            if(s[i]>='0' && s[i]<='9')
            {
                digits++;
            }
            else if (s[i]==' ')
            {
                spaces++;
            }

        }
        printf("\n      ------Digits in the entered string is : %d\n",digits);
        printf("\n      ------Blank Spaces in the entered string is : %d",spaces);
        break;
    default:
        printf("\nInvalid choice. Please try again.\n");
        break;

    }
    printf("\n\nDo you want to continue (Press 9 to continue) ");
    scanf("%d",&c);
  }
  while(c==9);
}
