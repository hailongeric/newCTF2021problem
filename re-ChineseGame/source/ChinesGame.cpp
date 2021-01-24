#include <iostream>
#include <stdlib.h>
#include <cstring>
#include <time.h>

/*

0010001101100011001000110110011100100111011000110010001101100111001000110110001100100111011001110010011101100011001001110110011100100011011000110010011101100111001001110110001100100011011001110010001101100011001000110110011100100111011000110010011101100111001000110110001100100011011001110010011101100011001000110110011100100011011000110010001101100111001001110110001100100111011001110010001101100011001001110110011100100111011000110010001101100111001000110110001100100111011001110010011101100011001001110110011100100011011000110010001101100111001001110110001100100011011001110010001101100011001000110110011100100111011000110010011101100111001000110110001100100111011001110010011101100011001000110110011100100011011000110010001101100111001001110110001100100111011001110010001101100011001000110110011100100111011000110010001101100111001000110110001100100
*/

using namespace std;

int table[] = {1, 3, 1, 2, 1, 5, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 7, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 5, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 6, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 5, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 9, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 5, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 6, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 5, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 7, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 5, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 6, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 5, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 8, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 5, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 6, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 5, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 7, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 5, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 6, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 5, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 10, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 5, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 6, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 5, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 7, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 5, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 6, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 5, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 8, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 5, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 6, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 5, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 7, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 5, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 6, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 5, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 9, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 5, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 6, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 5, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 7, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 5, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 6, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 5, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 8, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 5, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 6, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 5, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 7, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 5, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 6, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 5, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1};

struct circle
{
       int data;
       circle *next;
       circle(int d, circle *n) : data(d), next(n) {}
};

class Ring
{
public:
       Ring(int n) : nRingNum(n)
       {
              circle *temp = new circle(rand() % 100 + 101, NULL);
              head = temp;
              circle *temp2 = new circle(rand() % 100, NULL);
              temp->next = temp2;
              temp = temp2;
              for (int i = 0; i < 8; i++)
              {
                     temp2 = new circle(rand() % 100 + 101, NULL);
                     temp->next = temp2;
                     temp = temp2;
              }
       }

       void UpRing(int n);

       void DownRing(int n);
       void show();

       int totalCnt();

       bool isSucceed();

private:
       circle *head;
       int nRingNum;
       static int s_nCnt;
};

int Ring::s_nCnt = 0;

void Ring::UpRing(int n)
{
       ++s_nCnt;
       if (n > 10 || n < 1)
       {
              return;
       }
       int num = 10 - n;
       circle *temp = head;

       for (int i = 0; i < num; i++)
       {
              temp = temp->next;
       }
       circle *temp2 = temp;

       if (temp->data < 100)
       {
              if (n == 1)
              {
                     temp->data = rand() % 100 + 101;
              }
              else
              {
                     temp = temp->next;
                     if (temp->data < 100)
                     {
                            return;
                     }
                     else
                     {
                            temp = temp->next;
                            while (temp)
                            {
                                   if (temp->data > 100)
                                   {
                                          return;
                                   }
                                   temp = temp->next;
                            }
                     }
              }
       }
       temp2->data = rand() % 100 + 101;
}

void Ring::DownRing(int n)
{
       ++s_nCnt;
       if (n > 10 || n < 1)
       {
              return;
       }
       int num = 10 - n;
       circle *temp = head;

       for (int i = 0; i < num; i++)
       {
              temp = temp->next;
       }
       circle *temp2 = temp;

       if (temp->data > 100)
       {
              if (n == 1)
              {
                     temp->data = rand() % 100;
              }
              else
              {
                     temp = temp->next;
                     if (temp->data < 100)
                     {
                            return;
                     }
                     else
                     {
                            temp = temp->next;
                            while (temp)
                            {
                                   if (temp->data > 100)
                                   {
                                          return;
                                   }
                                   temp = temp->next;
                            }
                     }
              }
       }
       temp2->data = rand() % 100;
}

int Ring::totalCnt()
{
       return s_nCnt;
}

bool Ring::isSucceed()
{
       circle *temp = head;
       while (temp != NULL)
       {
              if (temp->data > 100)
              {
                     return false;
              }
              temp = temp->next;
       }
       return true;
}

int main()
{
       Ring ring(10);
       int i = 0;
       string s;
       cin >> s;
       int l = s.size();
       for (i = 0; i < l; i++)
       {
              switch (s[i])
              {
              case '1':
                     ring.UpRing(table[i]);
                     break;
              case '0':
                     ring.DownRing(table[i]);
                     break;
              default:
                     goto ext;
              }
              if (ring.totalCnt() > 855)
              {
                     break;
              }
       }
ext:
       if (ring.isSucceed())
       {
              system("cat flag");
       }
       return 0;
}
